'''
central_cam.py | Robin Forestier | 27.04.2021
Réglage de la caméra central OAK-D
depthai Gen2 version : 2.0.0.0+abbc96a13c7af12762bd2cab17d7360105b2d350
'''

import cv2
import depthai as dai

def clamp(num, v0, v1):
    return max(v0, min(num, v1))

# Start defining a pipeline
pipeline = dai.Pipeline()

# Define a source - color camera
camRgb = pipeline.createColorCamera()
camRgb.setPreviewSize(640, 480)

# Create output
xoutRgb = pipeline.createXLinkOut()
xoutRgb.setStreamName("rgb")
camRgb.preview.link(xoutRgb.input)

controlIn = pipeline.createXLinkIn()
controlIn.setStreamName('control')

# Pipeline is defined, now we can connect to the device
with dai.Device(pipeline, usb2Mode=True) as device:
    # Start pipeline
    device.startPipeline()

    qControl = device.getInputQueue('control')

    lensPos = 150
    lensMin = 0
    lensMax = 255
    
    # Output queue will be used to get the rgb frames from the output defined above
    qRgb = device.getOutputQueue(name="rgb", maxSize=4, blocking=False)
    
    while True:        
        inRgb = qRgb.get()  # blocking call, will wait until a new data has arrived
        # Retrieve 'bgr' (opencv format) frame
        cv2.imshow("bgr", inRgb.getCvFrame())
        
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        elif key == ord('t'):
            print("Autofocus trigger (and disable continuous)")
            ctrl = dai.CameraControl()
            ctrl.setAutoFocusMode(dai.CameraControl.AutoFocusMode.AUTO)
            ctrl.setAutoFocusTrigger()
            qControl.send(ctrl)
        elif key == ord('f'):
            print("Autofocus enable, continuous")
            ctrl = dai.CameraControl()
            ctrl.setAutoFocusMode(dai.CameraControl.AutoFocusMode.CONTINUOUS_VIDEO)
            qControl.send(ctrl)
        elif key in [ord(','), ord('.')]:
            if key == ord(','): lensPos -= 3
            if key == ord('.'): lensPos += 3
            lensPos = clamp(lensPos, lensMin, lensMax)
            print("Setting manual focus, lens position:", lensPos)
            ctrl = dai.CameraControl()
            ctrl.setManualFocus(lensPos)
            qControl.send(ctrl)

#destroy all windows
cv2.destroyAllWindows()