"""
功能：通过keras中预训练好的vgg模型提取特征
日期：2020/12/25
"""
import numpy as np
from numpy import linalg as la
from keras.applications.vgg16 import VGG16
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input


class VGGNet:
    def __init__(self):
        self.input_shape = (224, 224, 3)
        self.weight = 'imagenet'    # 选择权重
        self.pooling = 'max'    # 最大池化
        self.model = VGG16(weights=self.weight, input_shape=(self.input_shape[0], self.input_shape[1], self.input_shape[2]), pooling=self.pooling, include_top=False)
        # print(self.model.summary())

    '''
    使用训练好的VGG16模型来提取特征，输出归一化的特征向量
    '''
    def extract_feat(self, img_path):
        img = image.load_img(img_path, target_size=(self.input_shape[0], self.input_shape[1]))
        img = image.img_to_array(img)
        img = np.expand_dims(img, axis=0)
        img = preprocess_input(img)
        feat = self.model.predict(img)     # 输出为最后一个最大池化层  512
        # print('feat', feat)
        norm_feat = feat[0]/la.norm(feat[0])    # 相当于归一化
        # print('norm_feat', norm_feat)
        return norm_feat


if __name__ == '__main__':
    model = VGGNet()
    print(model.extract_feat(r'D:\working_fold\软件课程设计\ruanjiankeshe\database\all_souls_000001.jpg'))
