'''
stereo_disparity.py | Robin Forestier | 04.05.2021
Affichage de la profondeur en nuance de gris.
depthai Gen2 version : 2.0.0.0+abbc96a13c7af12762bd2cab17d7360105b2d350
'''

import cv2
import depthai as dai
import numpy as np

pipeline = dai.Pipeline()

depth = pipeline.createStereoDepth()

camR = pipeline.createMonoCamera()
camR.setBoardSocket(dai.CameraBoardSocket.RIGHT)
camR.setResolution(dai.MonoCameraProperties.SensorResolution.THE_400_P) #THE_800_P | THE_720_P

camL = pipeline.createMonoCamera()
camL.setBoardSocket(dai.CameraBoardSocket.LEFT)
camL.setResolution(dai.MonoCameraProperties.SensorResolution.THE_400_P) #THE_800_P | THE_720_P

xoutR = pipeline.createXLinkOut()
xoutR.setStreamName("right")
camR.out.link(depth.right)

xoutL = pipeline.createXLinkOut()
xoutL.setStreamName("left")
#send img left to host
camL.out.link(xoutL.input)
#send img left to depth
camL.out.link(depth.left)

xoutS = pipeline.createXLinkOut()
xoutS.setStreamName("stereo")
depth.depth.link(xoutS.input)

# Pipeline is defined, now we can connect to the device
with dai.Device(pipeline, usb2Mode=True) as device:
    # Start pipeline
    device.startPipeline()

    # Output queue will be used to get the rgb frames from the output defined above
    stereoimg = device.getOutputQueue(name="stereo", maxSize=4, blocking=False)
    qL = device.getOutputQueue(name="left", maxSize=4, blocking=False)
    while True:        
        stereoget = stereoimg.get()  # blocking call, will wait until a new data has arrived
        imgL = qL.get()
        img = stereoget.getCvFrame()
        img = img.astype(np.uint8)
        # Retrieve 'bgr' (opencv format) frame
        cv2.imshow("stereo", img)
        cv2.imshow("left", imgL.getCvFrame())
        
        #lecture des touches de clavier
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        elif key == ord('p'):
            cv2.imwrite("stereo01.png",stereoget.getCvFrame())
            cv2.imwrite("cam01.png",imgL.getCvFrame())
        
#destroy all windows
cv2.destroyAllWindows()
