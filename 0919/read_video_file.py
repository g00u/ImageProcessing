import cv2 as cv
from Common.utils import put_string

capture = cv.VideoCapture("C:/Users/grace/Downloads/video_file.avi")
if not capture.isOpened():
    raise Exception('동영상 파일 개방 안됨')

frame_rate = capture.get(cv.CAP_PROP_FPS)
delay = int(1000/frame_rate)
frame_cnt = 0

while True:
    ret, frame = capture.read()
    if not ret or cv.waitKey(delay) >= 0: break

    blue, green, red = cv.split(frame)
    frame_cnt += 1

    if 100 <= frame_cnt < 200: 
        cv.add(blue, 100, blue)
    elif 200 <= frame_cnt < 300:
        cv.add(green, 100, green)
    elif 300 <= frame_cnt < 400:
        cv.add(red, 100, red)

    frame = cv.merge([blue, green, red])
    put_string(frame, 'frame_cnt: ', (20, 30), frame_cnt)
    cv.imshow('Read Video File', frame)

capture.release()