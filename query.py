"""
匹配图片
"""
from extract_feature import VGGNet
import os
import numpy as np
import h5py

import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def query_picture(pic, nums=10, database=r'D:\working_fold\软件课程设计\vgg\image1', index=os.getcwd() + r'\featureCNN.h5'):
    """
    :param pic: 要查询的图片
    :param nums: 想要匹配的数量
    :param database: 图片库路径
    :param index: h5文件路径
    :return: 查询所得文件路径列表
    """
    h5f = h5py.File(index, 'r')
    feats = h5f['dataset_1'][:]
    print(feats)
    imgNames = h5f['dataset_2'][:]
    print(imgNames)
    h5f.close()

    # init VGGNet16 model
    model = VGGNet()

    # extract query image's feature, compute simlarity score and sort
    queryVec = model.extract_feat(pic)
    scores = np.dot(queryVec, feats.T)  # T转置,类似numpy.transpose         矩阵的点积
    rank_ID = np.argsort(scores)[::-1]
    rank_score = scores[rank_ID]    # 按顺序排列

    imlist = [database + '\\' + str(imgNames[index], 'utf-8') for i, index in enumerate(rank_ID[0:nums])]
    print("top {} images in order are: {}".format(nums, imlist))

    return imlist


if __name__ == '__main__':
    query_picture(r'D:\working_fold\软件课程设计\vgg\image1\1.png')
