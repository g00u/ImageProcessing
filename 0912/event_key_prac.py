import numpy as np
import cv2 as cv

switch_case = {
    ord('a'): "a키 입력", # ord()함수 : unicode 로 변환
    ord('b'): "b키 입력", 
    0x41 : "A키 입력", 
    int('0x42', 16) : "B키 입력",
    2424832: '왼쪽 화살표키 입력', 
    2490368: "윗쪽 화살표키 입력", 
    2555904: "오른쪽 화살표키 입력", 
    2621440: "아래쪽 화살표키 입력"
}

image = np.ones((200, 300), np.float32)
cv.namedWindow('Keyboard Event')
cv.imshow('Keyboard Event', image)

while True:
    key = cv.waitKeyEx(100)
    if key==27: break #esc키 27

    try :
        result = switch_case[key]
        print(result)
    except KeyError:
        result = -1

cv.destroyAllWindows()