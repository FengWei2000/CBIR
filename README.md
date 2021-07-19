## 一、环境配置

Python 3.7.6

第三方库：PIL,tkinter,time,xlwt,numpy,keras=2.4.3,TensorFlow=2.3.1,h5py,heapq,math
建议大家直接运行root.py，看缺少哪个库就pip安装哪一个。面向报错修改就可以了。

OS:Windows10

## 二、使用方法

**将5063张图片放入settings中对应路径文件夹。**

1、下载后直接运行root.py即可进入默认的主界面，通过预先生成的索引文件对默认数据库《The Oxford Buildings Dataset》进行检索。

2、通过更改settings.py中的classes，运行one_ap.py即可计算对应样例的ap。

3、通过更改ap.py文件中的rootdir和magins_path再运行ap.py即可运算所有样例的ap并输出在excel文件中。

4、通过在query.py对应位置进行注释和解注释即可选择是否进行特征降维，以及选择检索方法（包括K-D Tree，线性搜索，np.argsort()）。

5、通过更改settings.py中的pic_file_path和h5即可选择自己的图形库和运行index.py生成自己的特征文件。

任何路径都可在settings.py中修改。


百度网盘链接：https://pan.baidu.com/s/1YzFRFTY_bDCXVxICA3r69g 提取码：7oaf
百度网盘里包括图片等运行程序的所有内容，下载解压后即可直接运行root.py文件进入主界面。
