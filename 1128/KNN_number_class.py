import numpy as np, cv2
import matplotlib.pyplot as plt

def find_histo_position(img, direct):
    project = cv2.reduce(img, direct, cv2.REDUCE_AVG).ravel()
    p0, p1 = -1, -1
    length = project.shape[0]
    for i in range(length):
        if p0 < 0 and project[i] < 250:
            p0 = i
        if p1 < 0 and project[length - i - 1] < 250:
            p1 = length - i - 1
    return p0, p1

def find_number(part):
    x0, x1 = find_histo_position(part, 0)
    y0, y1 = find_histo_position(part, 1)
    if x0 < 0 or y0 < 0:
        return None  # 빈 데이터 방지
    return part[y0:y1, x0:x1]

def place_middle(number, new_size):
    h, w = number.shape[:2]
    big = max(h, w)
    square = np.full((big, big), 255, np.float32)
    
    dx, dy = np.subtract(big, (w, h)) // 2
    square[dy:dy + h, dx:dx + w] = number
    return cv2.resize(square, new_size).flatten()

train_image = cv2.imread("C:/IMAGEPROCESSING/image1128/train_numbers.png", cv2.IMREAD_GRAYSCALE)
train_image = train_image[5:405, 6:806]

size, K = (40, 40), 15
nclass, nsample = 10, 20
_, train_image = cv2.threshold(train_image, 32, 255, cv2.THRESH_BINARY)

cells = [np.hsplit(row, nsample) for row in np.vsplit(train_image, nclass)]
nums = [find_number(c) for c in np.reshape(cells, (-1, 40, 40)) if find_number(c) is not None]

# 크기가 다른 이미지를 통일
nums = [cv2.resize(n, size) for n in nums if n.shape[0] > 0 and n.shape[1] > 0]
trainData = np.array([place_middle(n, size) for n in nums])
labels = np.array([i for i in range(nclass) for j in range(nsample)], np.float32)

print("cells 형태: ", np.array(cells).shape)
print("nums 형태: ", np.array(nums).shape)
print("trainData 형태", trainData.shape)
print("labels 형태", labels.shape)

knn = cv2.ml.KNearest_create()
knn.train(trainData, cv2.ml.ROW_SAMPLE, labels)

rows, cols = 10, 20
plt.figure(figsize=(10, 10))
for i in range(min(rows * cols, len(nums))):  # 200 이하로 제한
    test_img = nums[i]
    data = place_middle(test_img, size)
    data = data.reshape(1, -1)
    
    _, [[resp]], _, _ = knn.findNearest(data, K)
    plt.subplot(rows, cols, i + 1), plt.axis('off'), plt.imshow(test_img, cmap='gray')
    plt.title("resp: " + str(int(resp)))
plt.tight_layout(), plt.show()
