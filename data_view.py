import cv2
import numpy as np

'''
将像素文件读取成图片存入指定文件夹，再分类成训练集和测试集
'''
# 指定存放图片的路径
# path = 'face_images'

# 读取像素数据
# data = np.loadtxt(r'D:\git-test\facial-expression-recognition\dataset\pixels.csv')


# 按行取数据
# for i in range(data.shape[0]):
#     face_array = data[i, :].reshape((48, 48))  # reshape
#     cv2.imwrite(path + '//' + '{}.jpg'.format(i), face_array)  # 写图片


# 将fer2013 数据可视化，然后进行划分
path = 'face_images/fer_img'
data1 = np.loadtxt(r'D:\git-test\facial-expression-recognition\dataset\fer_pixels.csv')
for i in range(data1.shape[0]):
    face_array = data1[i, :].reshape((48, 48))  # reshape
    cv2.imwrite(path + '//' + '{}.jpg'.format(i), face_array)  # 写图片