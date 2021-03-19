"""
计算ap
"""
from settings import gt_path
from settings import classes


def main():
    ranked_list = load_list('rank_list.txt')
    good_ls = load_list(gt_path + '\\' + classes+'_good.txt')
    ok_ls = load_list(gt_path + '\\' + classes + '_ok.txt')
    junk_ls = load_list(gt_path + '\\' + classes + '_junk.txt')

    pos_ls = good_ls + ok_ls

    compute_ap(pos_ls, junk_ls, ranked_list)


def compute_ap(pos, amb, ranked_list):
    ap = 0
    for j in range(10):
        for i in range(j+1):
            if ranked_list[i] in amb:
                continue
            elif ranked_list[i] in pos:
                ap += 1
        print('top', j+1, ':', ap*100/(j+1), sep='')
        ap = 0


def load_list(path):
    with open(path, 'r') as f:
        data = f.readlines()

    return data


if __name__ == '__main__':
    main()
