'''
spacial_location.py | Robin Forestier | 17.05.2021
depthai Gen2 version : 2.3.0.0
opencv version : 4.5.1
'''

import cv2
import depthai as dai
import numpy as np

stepSize = 0.01
moy = np.zeros(50)
i = 0
moyenne = False

# Start defining a pipeline
pipeline = dai.Pipeline()

# Define a source - two mono (grayscale) cameras
monoLeft = pipeline.createMonoCamera()
monoRight = pipeline.createMonoCamera()
stereo = pipeline.createStereoDepth()
spatialLocationCalculator = pipeline.createSpatialLocationCalculator()

xoutLeft = pipeline.createXLinkOut()

xoutDepth = pipeline.createXLinkOut()
xoutSpatialData = pipeline.createXLinkOut()
xinSpatialCalcConfig = pipeline.createXLinkIn()

xoutLeft.setStreamName("left")
monoRight.out.link(xoutLeft.input)

xoutDepth.setStreamName("depth")
xoutSpatialData.setStreamName("spatialData")
xinSpatialCalcConfig.setStreamName("spatialCalcConfig")

# MonoCamera
monoLeft.setResolution(dai.MonoCameraProperties.SensorResolution.THE_400_P)
monoLeft.setBoardSocket(dai.CameraBoardSocket.LEFT)
monoRight.setResolution(dai.MonoCameraProperties.SensorResolution.THE_400_P)
monoRight.setBoardSocket(dai.CameraBoardSocket.RIGHT)

lrcheck = False
subpixel = False

# StereoDepth
stereo.setConfidenceThreshold(255)

stereo.setLeftRightCheck(lrcheck)
stereo.setSubpixel(subpixel)

monoLeft.out.link(stereo.left)
monoRight.out.link(stereo.right)

spatialLocationCalculator.passthroughDepth.link(xoutDepth.input)
stereo.depth.link(spatialLocationCalculator.inputDepth)

topLeft = dai.Point2f(0.59, 0.59)
bottomRight = dai.Point2f(0.6, 0.6)

spatialLocationCalculator.setWaitForConfigInput(False)
config = dai.SpatialLocationCalculatorConfigData()
#100mm to 10'000mm
config.depthThresholds.lowerThreshold = 100
config.depthThresholds.upperThreshold = 10000
config.roi = dai.Rect(topLeft, bottomRight)
spatialLocationCalculator.initialConfig.addROI(config)
spatialLocationCalculator.out.link(xoutSpatialData.input)
xinSpatialCalcConfig.out.link(spatialLocationCalculator.inputConfig)


# Connect and start the pipeline
with dai.Device(pipeline) as device:
    

    # Output queue will be used to get the depth frames from the outputs defined above
    imgL = device.getOutputQueue(name="left", maxSize=4, blocking=False)
    
    depthQueue = device.getOutputQueue(name="depth", maxSize=4, blocking=False)
    spatialCalcQueue = device.getOutputQueue(name="spatialData", maxSize=4, blocking=False)
    spatialCalcConfigInQueue = device.getInputQueue("spatialCalcConfig")

    color = (0, 0, 0)

    #print("Use WASD keys to move ROI!")
    

    while True:
        img = imgL.get()
        img = img.getCvFrame()
        
        inDepth = depthQueue.get() # Blocking call, will wait until a new data has arrived
        inDepthAvg = spatialCalcQueue.get() # Blocking call, will wait until a new data has arrived

        depthFrame = inDepth.getFrame()
        depthFrameColor = cv2.normalize(depthFrame, None, 255, 0, cv2.NORM_INF, cv2.CV_8UC1)
        depthFrameColor = cv2.equalizeHist(depthFrameColor)
        depthFrameColor = cv2.applyColorMap(depthFrameColor, cv2.COLORMAP_JET)

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
            
            cv2.rectangle(img, (xmin, ymin), (xmax, ymax), color, cv2.FONT_HERSHEY_SCRIPT_SIMPLEX)
            cv2.putText(img, f"Z: {int(depthData.spatialCoordinates.z)/10} cm", (xmin + 10, ymin + 60), fontType, 1, color)
            
        cv2.imshow("depth", depthFrameColor)
        cv2.imshow("left", img)

        newConfig = False
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        elif key == ord('m'):
            cv2.imwrite('mesure_nb_{}_cm.png'.format(int(depthData.spatialCoordinates.z)/10),img)
            print("save : mesure_nb_{}_cm.png".format(int(depthData.spatialCoordinates.z)/10))
        elif key == ord('n'):
            moyenne = True
        elif key == ord('w'):
            if topLeft.y - stepSize >= 0:
                topLeft.y -= stepSize
                bottomRight.y -= stepSize
                newConfig = True
        elif key == ord('a'):
            if topLeft.x - stepSize >= 0:
                topLeft.x -= stepSize
                bottomRight.x -= stepSize
                newConfig = True
        elif key == ord('s'):
            if bottomRight.y + stepSize <= 1:
                topLeft.y += stepSize
                bottomRight.y += stepSize
                newConfig = True
        elif key == ord('d'):
            if bottomRight.x + stepSize <= 1:
                topLeft.x += stepSize
                bottomRight.x += stepSize
                newConfig = True

        if newConfig:
            config.roi = dai.Rect(topLeft, bottomRight)
            cfg = dai.SpatialLocationCalculatorConfig()
            cfg.addROI(config)
            spatialCalcConfigInQueue.send(cfg)

        if moyenne:
            if i == 50:
                print("moyenne : ",np.mean(moy))
                
                cv2.imwrite('Mesures_img/mesure_nb_{:.1f}_cm.png'.format(np.mean(moy)),img)
                print("save : mesure_nb_{:.1f}_cm.png".format(np.mean(moy)))
                cv2.imwrite('Mesures_img/mesure_depth_{:.1f}_cm.png'.format(np.mean(moy)),depthFrameColor)
                print("save : mesure_depth_{:.1f}_cm.png".format(np.mean(moy)))
                
                i = 0
                moyenne = False
                moy = np.zeros(50)
            else:
                moy[i] = int(depthData.spatialCoordinates.z)/10
                i += 1

#destroy all windows
cv2.destroyAllWindows()
