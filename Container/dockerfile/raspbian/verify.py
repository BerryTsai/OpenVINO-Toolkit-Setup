import cv2 as cv
# Load the model.
net = cv.dnn_DetectionModel('face-detection-retail-0004.xml',
                            'face-detection-retail-0004.bin')
# Specify target device.
net.setPreferableTarget(cv.dnn.DNN_TARGET_MYRIAD)
# Read an image.
frame = cv.imread('berrytsai.png')
if frame is None:
    raise Exception('Image not found!')
# Perform an inference.
_, confidences, boxes = net.detect(frame, confThreshold=0.5)
# Draw detected faces on the frame.
for confidence, box in zip(list(confidences), boxes):
    cv.rectangle(frame, box, color=(0, 255, 0))
# Save the frame to an image file.
cv.imwrite('out.png', frame)