"""
匹配图片
有3中搜索方法，分别为K-D树，冒泡排序，np.argsort()。使用时注释掉另外两种即可，其中除K-D树外两种方法均可选择是否进行PCA特征降维。
"""
from extract_feature import VGGNet
import os
import h5py
from settings import pic_file_path
import time
import KDTree
import numpy as np
from sklearn.decomposition import PCA


def query_picture(pic, nums=10, database=pic_file_path, index=os.getcwd() + r'\featureCNN1.h5'):
    """
    :param pic: 要查询的图片
    :param nums: 想要匹配的数量
    :param database: 图片库路径
    :param index: h5文件路径
    :return: 查询所得文件路径列表
    """
    h5f = h5py.File(index, 'r')
    feats = h5f['dataset_1'][:]
    # print(feats)
    imgNames = h5f['dataset_2'][:]
    # print(imgNames)
    h5f.close()
    fe_ls = [list(feat.reshape(512)) for feat in feats]
    im_ls = [imgNmae for imgNmae in imgNames]

    model = VGGNet()        # 初始化VGG16模型

    queryVec = model.extract_feat(pic)  # 提取要搜索的图片的特征

    # # 特征降维
    # queryVec_ls = list(queryVec.reshape(512))
    # fe_ls.append(queryVec_ls)
    # pca = PCA(n_components=0.9)
    # fe_ls = list(pca.fit_transform(fe_ls))
    # queryVec = fe_ls.pop()
    # feats = np.array(fe_ls)
    # #

    # # 使用K-D Tree
    # kd_tree = KDTree.create(fe_ls, len(fe_ls[0]))
    # start = time.perf_counter()
    # nearest_points = kd_tree.search_knn(queryVec, nums)
    # end = time.perf_counter()
    # imlist = [database + '\\' + str(im_ls[fe_ls.index(index[0].data)], 'utf-8') for index in nearest_points]
    # #

    # # 使用冒泡排序线性搜索
    # start = time.perf_counter()
    # scores = np.dot(queryVec, feats.T)  # T转置,类似numpy.transpose         矩阵的点积
    # scores2 = list(scores.copy())
    # for k in range(len(scores)):
    #     for j in range(0, len(scores)-k-1):
    #         if scores[j] < scores[j+1]:
    #             scores[j], scores[j+1] = scores[j+1], scores[j]
    # rank_ID = [scores2.index(s) for s in scores]
    # end = time.perf_counter()
    # imlist = [database + '\\' + str(imgNames[index], 'utf-8') for i, index in enumerate(rank_ID[0:nums])]
    # #

    # # 使用np.argsort()进行线性搜索
    start = time.perf_counter()
    scores = np.dot(queryVec, feats.T)  # T转置,类似numpy.transpose         矩阵的点积
    rank_ID = np.argsort(scores)[::-1]
    end = time.perf_counter()
    imlist = [database + '\\' + str(imgNames[index], 'utf-8') for i, index in enumerate(rank_ID[0:nums])]
    # #

    print("top {} images in order are: {}".format(nums, imlist))
    print('time', (end-start)/len(imlist))

    with open('rank_list.txt', 'w') as f:
        for im in imlist:
            f.write(im.split('\\')[-1][:-4] + '\n')

    return imlist


if __name__ == '__main__':
    query_picture(r'D:\working_fold\software\oxbuild_images\bodleian_000132.jpg')
