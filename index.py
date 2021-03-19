"""
创建索引文件，存储在h5中
"""
import os
import h5py
import numpy as np
from extract_feature import VGGNet
from settings import pic_file_path
from settings import h5


def creat_h5(path, output=os.getcwd() + h5):
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
        try:
            norm_feat = model.extract_feat(img_path)
            img_name = os.path.split(img_path)[1]
            feats.append(norm_feat)
            names.append(img_name)
            print("extracting feature from image No. {} , {} images in total".format(i+1, len(img_list)))
        except Exception as e:
            print('出错了！', img_path)
            print(e)

    feats = np.array(feats)

    print("--------------------------------------------------")
    print("               正在写入特征提取结果              ...")
    print("--------------------------------------------------")

    h5f = h5py.File(output, 'w')
    h5f.create_dataset('dataset_1', data=feats)
    h5f.create_dataset('dataset_2', data=np.string_(names))
    h5f.close()

    return output


def get_imlist(path):
    return [os.path.join(path, f) for f in os.listdir(path) if (f.endswith('.jpg') or f.endswith('.png'))]


if __name__ == '__main__':
    creat_h5(pic_file_path)
