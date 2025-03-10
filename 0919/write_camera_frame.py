import cv2 as cv

capture = cv.VideoCapture(0)
if capture.isOpened() == False:
    raise Exception("카메라 연결 안됨")

fps = 29.97
delay = round(1000/fps)
size = (640, 360)
fourcc = cv.VideoWriter_fourcc(*'DX50')

print('width x height: ', size)
print('VideoWiterfourcc: %s' % fourcc)
print('delay: %2d ms' % delay)
print('fps: %.2f' % fps)

capture.set(cv.CAP_PROP_ZOOM, 1)
capture.set(cv.CAP_PROP_FOCUS, 0)
capture.set(cv.CAP_PROP_FRAME_WIDTH, size[0])
capture.set(cv.CAP_PROP_FRAME_HEIGHT, size[1])

writer = cv.VideoWriter('C:/Users/SWK/Desktop/digitalImageProcessing/images/video_file_2.avi', fourcc, fps, size)
# writer = cv.VideoWriter('/Users/kwakseungwoo/Desktop/digitalImageProcessing/images/video_file.avi', fourcc, fps, size)
if writer.isOpened() == False:
    raise Exception('동영상 파일 개방 안됨')

while True:
    ret, frame = capture.read()
    if not ret: break
    if cv.waitKey(delay) >= 0: break

    writer.write(frame)
    cv.imshow('View Frame from Camera', frame)
    cv.waitKey(0)
    
writer.release()
capture.release()
cv.destroyAllWindows()