
import cv2
import depthai as dai
import numpy as np

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
#camL.out.link(xoutL.input)
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
    qL = device.getOutputQueue(name="right", maxSize=4, blocking=False)
    while True:        
        imgL = qL.get()
        inDepth = stereoimg.get()  # blocking call, will wait until a new data has arrived
        left = imgL.getCvFrame()
        
        frame = inDepth.getFrame()
        frame1 = frame.copy()
        frame2 = frame.copy()
        ret, frame2 = cv2.threshold(frame1, 50, 100, cv2.THRESH_BINARY)
        
        contours, h = cv2.findContours(frame2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
            perimetre = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.01*perimetre,True)
    
            M = cv2.moments(cnt)
            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
            else:
                cx,cy = 0,0
                
            cv2.drawContours(left,[cnt],-1,(0,255,0),2)
        
        ret, frame1 = cv2.threshold(frame1, 50, 15, cv2.THRESH_BINARY_INV)
        ret, frame = cv2.threshold(frame, 20, 15, cv2.THRESH_BINARY)
        
        frame = frame * frame1
        frame += frame2
        # Retrieve 'bgr' (opencv format) frame
        cv2.imshow("stereo", frame)
        cv2.imshow("left", left)
        
        #lecture des touches de clavier
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        elif key == ord('p'):
            cv2.imwrite("stereo_nb_03.png",frame1)
            cv2.imwrite("stereo_color_HOT_03.png",frame)
            cv2.imwrite("cam03.png",imgL.getCvFrame())
        
#destroy all windows
cv2.destroyAllWindows()
