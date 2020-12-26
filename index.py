"""
创建索引
"""
import os
import h5py
import numpy as np
from extract_feature import VGGNet


def creat_h5(path, output=os.getcwd() + r'\featureCNN.h5'):
    """
    :param path: 图片库路径
    :param output: 生成h5文件路径
    :return: 生成h5文件路径
    """
    img_list = get_imlist(path)
    print('图片列表已读取完毕')

    feats = []
    names = []
    model = VGGNet()

    for i, img_path in enumerate(img_list):
        norm_feat = model.extract_feat(img_path)
        img_name = os.path.split(img_path)[1]
        feats.append(norm_feat)
        names.append(img_name)
        print("extracting feature from image No. {} , {} images in total".format(i+1, len(img_list)))

    feats = np.array(feats)

    print("--------------------------------------------------")
    print("      writing feature extraction results ...")
    print("--------------------------------------------------")

    h5f = h5py.File(output, 'w')
    h5f.create_dataset('dataset_1', data=feats)
    # h5f.create_dataset('dataset_2', data = names)
    h5f.create_dataset('dataset_2', data=np.string_(names))
    h5f.close()

    return output


def get_imlist(path):
    return [os.path.join(path, f) for f in os.listdir(path) if (f.endswith('.jpg') or f.endswith('.png'))]


if __name__ == '__main__':
    creat_h5(r'D:\working_fold\软件课程设计\vgg\image1')

