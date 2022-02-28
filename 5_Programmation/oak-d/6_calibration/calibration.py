'''
calibration.py | Robin Forestier | 04.05.2021
Calibration de la caméra OAK-D
depthai Gen2 version : 2.0.0.0+abbc96a13c7af12762bd2cab17d7360105b2d350
'''

import cv2
import depthai as dai
import numpy as np

x = 0

pipeline = dai.Pipeline()

#Depth
depth = pipeline.createStereoDepth()
#seuille de confiance
depth.setConfidenceThreshold(200)
depth.setOutputDepth(False)
# Options: MEDIAN_OFF, KERNEL_3x3, KERNEL_5x5, KERNEL_7x7 (default)
median = dai.StereoDepthProperties.MedianFilter.KERNEL_7x7 # For depth filtering
depth.setMedianFilter(median)


camR = pipeline.createMonoCamera()
camR.setBoardSocket(dai.CameraBoardSocket.RIGHT)
camR.setResolution(dai.MonoCameraProperties.SensorResolution.THE_400_P) #THE_800_P | THE_720_P

camL = pipeline.createMonoCamera()
camL.setBoardSocket(dai.CameraBoardSocket.LEFT)
camL.setResolution(dai.MonoCameraProperties.SensorResolution.THE_400_P) #THE_800_P | THE_720_P


xoutR = pipeline.createXLinkOut()
xoutR.setStreamName("right")

camR.out.link(xoutR.input)

camR.out.link(depth.right)

xoutL = pipeline.createXLinkOut()
xoutL.setStreamName("left")
#send img left to host
camL.out.link(xoutL.input)
#send img left to depth
camL.out.link(depth.left)

xoutS = pipeline.createXLinkOut()
xoutS.setStreamName("stereo")
depth.disparity.link(xoutS.input)

# Pipeline is defined, now we can connect to the device
with dai.Device(pipeline, usb2Mode=True) as device:
    # Start pipeline
    device.startPipeline()

    # Output queue will be used to get the rgb frames from the output defined above
    stereoimg = device.getOutputQueue(name="stereo", maxSize=4, blocking=False)
    qL = device.getOutputQueue(name="left", maxSize=4, blocking=False)
    qR = device.getOutputQueue(name="right", maxSize=4, blocking=False)
    while True:        
        imgL = qL.get()
        imgR = qR.get()
        '''
        inDepth = stereoimg.get()  # blocking call, will wait until a new data has arrived
        
        frame = inDepth.getFrame()
        frame1 = frame.copy()
        cv2.imshow("nb",frame1)
        # 255 / 95 ~= 2.5 (disparity = 95) 
        frame = (frame*2.5).astype(np.uint8)
        frame = cv2.applyColorMap(frame, cv2.COLORMAP_JET)
        # cv2.COLORMAP_HSV | cv2.COLORMAP_HOT | cv2.COLORMAP_BONE
        
        cv2.imshow("stereo", frame)
        '''
        frameL = imgL.getCvFrame()
        frameR = imgR.getCvFrame()
        
        cv2.imshow("left", frameL)
        cv2.imshow("right", frameR)
        
        #lecture des touches de clavier
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        elif key == ord('p'):
            cv2.imwrite("right/right_{}.png".format(x),frameL)
            cv2.imwrite("left/left_{}.png".format(x),frameR)
            x = x + 1
            #cv2.imwrite("cam03.png",imgL.getCvFrame())
        
#destroy all windows
cv2.destroyAllWindows()