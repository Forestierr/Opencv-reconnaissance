# OAK-D central cam

## But

Afficher l'image prise par la caméra central (OAK-D) en couleur.

## Code

```python
'''
central_cam.py | Robin Forestier | 27.04.2021
Affichage de la caméra central OAK-D
depthai Gen2 version : 2.0.0.0+abbc96a13c7af12762bd2cab17d7360105b2d350
'''

import cv2
import depthai as dai

# Start defining a pipeline
pipeline = dai.Pipeline()

# Define a source - color camera
camRgb = pipeline.createColorCamera()
camRgb.setPreviewSize(640, 480)

# Create output
xoutRgb = pipeline.createXLinkOut()
xoutRgb.setStreamName("rgb")
camRgb.preview.link(xoutRgb.input)

# Pipeline is defined, now we can connect to the device
with dai.Device(pipeline, usb2Mode=True) as device:
    # Start pipeline
    device.startPipeline()

    # Output queue will be used to get the rgb frames from the output defined above
    qRgb = device.getOutputQueue(name="rgb", maxSize=4, blocking=False)
    
    while True:        
        inRgb = qRgb.get()  # blocking call, will wait until a new data has arrived
        # Retrieve 'bgr' (opencv format) frame
        cv2.imshow("bgr", inRgb.getCvFrame())
        if cv2.waitKey(1) == ord('q'):
            break

#destroy all windows
cv2.destroyAllWindows()

```

<h2> </h2>

<div align="center">
    <i>Robin Forestier</i>
</div>
