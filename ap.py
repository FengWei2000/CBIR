"""
计算ap
"""
from settings import gt_path, pic_file_path
import os
from query import query_picture
import xlwt


def compute_one_ap(classes):
    ranked_list = load_list('rank_list.txt')
    good_ls = load_list(gt_path + '\\' + classes+'good.txt')
    ok_ls = load_list(gt_path + '\\' + classes + 'ok.txt')
    junk_ls = load_list(gt_path + '\\' + classes + 'junk.txt')

    pos_ls = good_ls + ok_ls

    return compute_ap(pos_ls, junk_ls, ranked_list)


def compute_ap(pos, amb, ranked_list):
    ap = 0
    ap_ls = []
    for j in range(10):
        for i in range(j+1):
            if ranked_list[i] in amb:
                continue
            elif ranked_list[i] in pos:
                ap += 1
        ap_ls.append(ap*100/(j+1))
        print('top', j+1, ':', ap*100/(j+1), sep='')
        ap = 0
    return ap_ls


def load_list(path):
    with open(path, 'r') as f:
        data = f.readlines()
    return data


def main():
    rootdir = gt_path   # gt文件夹路径
    magins_path = pic_file_path      # 图形库文件夹路径
    excelf = xlwt.Workbook()
    sheet1 = excelf.add_sheet(u'sheet1', cell_overwrite_ok=True)
    n = 0
    for dirpath, dirnames, filenames in os.walk(rootdir):
        for filename in filenames:
            if filename.split('.')[0][-5:] == 'query':
                classes = filename.split('.')[0][:-5]
                with open(rootdir + '\\' + filename) as f:
                    pic_name = f.read().split(' ')[0][5:]
                    pic_path = magins_path + '\\' + pic_name + '.jpg'
                    query_picture(pic_path, 10)
                    ap_ls = compute_one_ap(classes)
                    for i in range(len(ap_ls)):
                        sheet1.write(n, i, ap_ls[i])
                n += 1
    excelf.save('ap.xls')


if __name__ == '__main__':
    main()
