'''
aruco_dist.py | Robin Forestier | 18.05.2021
depthai Gen2 version : 2.3.0.0
opencv version : 4.5.1
'''

import cv2
import depthai as dai
import numpy as np
import time

stepSize = 0.01

ARUCO_DICT = {
    "DICT_4X4_50":cv2.aruco.DICT_4X4_50,
    "DICT_4X4_100":cv2.aruco.DICT_4X4_100,
    "DICT_4X4_250":cv2.aruco.DICT_4X4_250,
    "DICT_4X4_1000":cv2.aruco.DICT_4X4_1000,
    "DICT_5X5_50":cv2.aruco.DICT_5X5_50,
    "DICT_5X5_100":cv2.aruco.DICT_5X5_100,
    "DICT_5X5_250":cv2.aruco.DICT_5X5_250,
    "DICT_5X5_1000":cv2.aruco.DICT_5X5_1000,
    "DICT_6X6_50":cv2.aruco.DICT_6X6_50,
    "DICT_6X6_100":cv2.aruco.DICT_6X6_100,
    "DICT_6X6_250":cv2.aruco.DICT_6X6_250,
    "DICT_6X6_1000":cv2.aruco.DICT_6X6_1000,
    "DICT_7X7_50":cv2.aruco.DICT_7X7_50,
    "DICT_7X7_100":cv2.aruco.DICT_7X7_100,
    "DICT_7X7_250":cv2.aruco.DICT_7X7_250,
    "DICT_7X7_1000":cv2.aruco.DICT_7X7_1000,
    "DICT_ARUCO_ORIGINAL":cv2.aruco.DICT_ARUCO_ORIGINAL,
    "DICT_APRILTAG_16h5":cv2.aruco.DICT_APRILTAG_16h5,
    "DICT_APRILTAG_25h9":cv2.aruco.DICT_APRILTAG_25h9,
    "DICT_APRILTAG_36h10":cv2.aruco.DICT_APRILTAG_36h10,
    "DICT_APRILTAG_36h11":cv2.aruco.DICT_APRILTAG_36h11
    }

arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_4X4_100)
arucoParams = cv2.aruco.DetectorParameters_create()

def getDist():
    depthFrame = inDepth.getFrame()
        
    depthFrameColor = cv2.normalize(depthFrame, None, 255, 0, cv2.NORM_INF, cv2.CV_8UC1)
    depthFrameColor = cv2.equalizeHist(depthFrameColor)
    #depthFrameColor = cv2.applyColorMap(depthFrameColor, cv2.COLORMAP_BONE)

    spatialData = inDepthAvg.getSpatialLocations()
    for depthData in spatialData:
        roi = depthData.config.roi
        roi = roi.denormalize(width=depthFrameColor.shape[1], height=depthFrameColor.shape[0])

        xmin = int(roi.topLeft().x)
        ymin = int(roi.topLeft().y)
        xmax = int(roi.bottomRight().x)
        ymax = int(roi.bottomRight().y)
            
        fontType = cv2.FONT_HERSHEY_TRIPLEX
        cv2.rectangle(depthFrameColor, (xmin, ymin), (xmax, ymax), color, cv2.FONT_HERSHEY_SCRIPT_SIMPLEX)
        cv2.putText(depthFrameColor, f"Z: {int(depthData.spatialCoordinates.z)/10} cm", (xmin + 10, ymin + 60), fontType, 1, color)
    
    z = int(depthData.spatialCoordinates.z)/10
    
    cv2.imshow("yo",depthFrameColor)
    
    return z, depthFrameColor



# Start defining a pipeline
pipeline = dai.Pipeline()

# Define a source - two mono (grayscale) cameras
camRgb = pipeline.createColorCamera()
monoLeft = pipeline.createMonoCamera()
monoRight = pipeline.createMonoCamera()
stereo = pipeline.createStereoDepth()
spatialLocationCalculator = pipeline.createSpatialLocationCalculator()

xoutRgb = pipeline.createXLinkOut()
xoutDepth = pipeline.createXLinkOut()
xoutSpatialData = pipeline.createXLinkOut()
xinSpatialCalcConfig = pipeline.createXLinkIn()

xoutR = pipeline.createXLinkOut()
xoutR.setStreamName("right")

xoutRgb.setStreamName("rgb")
xoutDepth.setStreamName("depth")
xoutSpatialData.setStreamName("spatialData")
xinSpatialCalcConfig.setStreamName("spatialCalcConfig")

#ColorCamera
camRgb.setBoardSocket(dai.CameraBoardSocket.RGB)
camRgb.setPreviewSize(640, 400)
camRgb.setInterleaved(False)
camRgb.setColorOrder(dai.ColorCameraProperties.ColorOrder.RGB)

# MonoCamera
monoLeft.setResolution(dai.MonoCameraProperties.SensorResolution.THE_400_P)
monoLeft.setBoardSocket(dai.CameraBoardSocket.LEFT)
monoRight.setResolution(dai.MonoCameraProperties.SensorResolution.THE_400_P)
monoRight.setBoardSocket(dai.CameraBoardSocket.RIGHT)

lrcheck = False
subpixel = False

# StereoDepth
stereo.setConfidenceThreshold(255)
#stereo.setDepthAlign(camRgb.getBoardSocket)

stereo.setLeftRightCheck(lrcheck)
stereo.setSubpixel(subpixel)

camRgb.preview.link(xoutRgb.input)
monoRight.out.link(xoutR.input)

monoLeft.out.link(stereo.left)
monoRight.out.link(stereo.right)

spatialLocationCalculator.passthroughDepth.link(xoutDepth.input)
stereo.depth.link(spatialLocationCalculator.inputDepth)

topLeft = dai.Point2f((320/640), (320/640))
bottomRight = dai.Point2f((200/400), (200/400))

spatialLocationCalculator.setWaitForConfigInput(False)
config = dai.SpatialLocationCalculatorConfigData()
#400mm to 10'000mm
config.depthThresholds.lowerThreshold = 400
config.depthThresholds.upperThreshold = 10000
config.roi = dai.Rect(topLeft, bottomRight)
spatialLocationCalculator.initialConfig.addROI(config)
spatialLocationCalculator.out.link(xoutSpatialData.input)
xinSpatialCalcConfig.out.link(spatialLocationCalculator.inputConfig)


#control
control_in = pipeline.createXLinkIn()
control_in.setStreamName('control')
control_in.out.link(monoRight.inputControl)
control_in.out.link(monoLeft.inputControl)

# Connect and start the pipeline
with dai.Device(pipeline) as device:
    device.startPipeline()    
    
    # Output queue will be used to get the depth frames from the outputs defined above
    imgRgb = device.getOutputQueue(name="right", maxSize=4, blocking=False)
    
    depthQueue = device.getOutputQueue(name="depth", maxSize=4, blocking=False)
    spatialCalcQueue = device.getOutputQueue(name="spatialData", maxSize=4, blocking=False)
    spatialCalcConfigInQueue = device.getInputQueue("spatialCalcConfig")

    controlQueue = device.getInputQueue('control')
    
    ctrl = dai.CameraControl()
    ctrl.AntiBandingMode.MAINS_50_HZ
    controlQueue.send(ctrl)

    color = (0, 0, 0)
    startTime = time.monotonic()
    counter = 0
    fps = 0
    
    while True:
        newConfig = False
        
        img = imgRgb.get()
        img = img.getCvFrame()
        
        counter+=1
        current_time = time.monotonic()
        if (current_time - startTime) > 1 :
            fps = counter / (current_time - startTime)
            counter = 0
            startTime = current_time
        
        inDepth = depthQueue.get() # Blocking call, will wait until a new data has arrived
        inDepthAvg = spatialCalcQueue.get() # Blocking call, will wait until a new data has arrived
        
        (corners, ids, rejected) = cv2.aruco.detectMarkers(img, arucoDict, parameters=arucoParams)
        
        if len(corners) > 0:
            ids = ids.flatten()
        
            for (markerCorner, markerID) in zip(corners, ids):
                corners = markerCorner.reshape((4,2))
                (atopLeft, atopRight, abottomRight, abottomLeft) = corners
            
                atopRight = (int(atopRight[0]), int(atopRight[1]))
                abottomRight = (int(abottomRight[0]), int(abottomRight[1]))
                abottomLeft = (int(abottomLeft[0]), int(abottomLeft[1]))
                atopLeft = (int(atopLeft[0]), int(atopLeft[1]))
            
                cv2.line(img, atopLeft, atopRight, (255,125,255),2)
                cv2.line(img, atopRight, abottomRight, (255,125,255),2)
                cv2.line(img, abottomRight, abottomLeft, (255,125,255),2)
                cv2.line(img, atopLeft, abottomLeft, (255,125,255),2)
            
            
                cv2.putText(img, str(markerID),
                        (atopLeft[0], atopLeft[1] - 15), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (0,255,0),2)
            
                topLeft.x = atopLeft[0]/640
                topLeft.y = atopLeft[1]/400
                bottomRight.x = abottomRight[0]/640
                bottomRight.y = abottomRight[1]/400
            
                config.roi = dai.Rect(topLeft, bottomRight)
                cfg = dai.SpatialLocationCalculatorConfig()
                cfg.addROI(config)
                spatialCalcConfigInQueue.send(cfg)
                
                z, depthFrameColor = getDist()
                
                cv2.putText(img, str(z) + " cm",
                        (abottomRight[0], abottomRight[1] + 15), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (0,255,0),2)
        
        
                bleded = cv2.addWeighted(img, 0.6, depthFrameColor, 0.4, 0)
                cv2.imshow("bl", bleded)
                
        cv2.putText(img, "fps: {:.2f}".format(fps), (2, img.shape[0] - 4), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255,0,0))
        cv2.imshow("rgb", img)

        
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

#destroy all windows
cv2.destroyAllWindows()