'''
stereo_cam | Robin Forestier | 27.04.2021
Affichage des images prise par les deux caméra latéral (OAK-D) en noir et blanc
'''

import cv2
import depthai as dai

pipeline = dai.Pipeline()

camR = pipeline.createMonoCamera()
camR.setBoardSocket(dai.CameraBoardSocket.RIGHT)
camR.setResolution(dai.MonoCameraProperties.SensorResolution.THE_400_P) #THE_800_P | THE_720_P

camL = pipeline.createMonoCamera()
camL.setBoardSocket(dai.CameraBoardSocket.LEFT)
camL.setResolution(dai.MonoCameraProperties.SensorResolution.THE_400_P) #THE_800_P | THE_720_P


xoutR = pipeline.createXLinkOut()
xoutR.setStreamName("right")
camR.out.link(xoutR.input)

xoutL = pipeline.createXLinkOut()
xoutL.setStreamName("left")
camL.out.link(xoutL.input)

# Pipeline is defined, now we can connect to the device
with dai.Device(pipeline, usb2Mode=True) as device:
    # Start pipeline
    device.startPipeline()

    # Output queue will be used to get the rgb frames from the output defined above
    qR = device.getOutputQueue(name="right", maxSize=4, blocking=False)
    qL = device.getOutputQueue(name="left", maxSize=4, blocking=False)
    
    while True:        
        inR = qR.get()  # blocking call, will wait until a new data has arrived
        inL = qL.get()
        # Retrieve 'bgr' (opencv format) frame
        cv2.imshow("right", inR.getCvFrame())
        cv2.imshow("left", inL.getCvFrame())
        if cv2.waitKey(1) == ord('q'):
            break

#destroy all windows
cv2.destroyAllWindows()
