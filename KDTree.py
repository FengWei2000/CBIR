"""
K-D Tree
参考资料：https://blog.csdn.net/zhanghao632045/article/details/78447159
         https://blog.csdn.net/silangquan/article/details/41483689
         https://github.com/stefankoegl/kdtree
"""
from __future__ import print_function
import heapq
import math


class KDNode(object):
    """节点"""
    def __init__(self, data=None, left=None, right=None, axis=None,
                 sel_axis=None, dimensions=None):
        """ 节点 """
        self.data = data    # 值.    列表
        self.left = left    # 左叶子节点
        self.right = right  # 右叶子节点
        # sel_axis(axis)在创建当前节点的子节点中将被使用，输入为父节点的axis，输出为子节点的axis
        self.axis = axis
        self.sel_axis = sel_axis
        self.dimensions = dimensions

    def __nonzero__(self):
        return self.data is not None

    __bool__ = __nonzero__

    def dist(self, point):
        """计算当前点和指定点的平方距离"""
        return sum([math.pow(self.data[i] - point[i], 2) for i in range(self.dimensions)])

    def search_knn(self, point, k, dist=None):
        """ 寻找和给定值最近的k个节点，输出为元组(node, distance) """
        if dist is None:
            get_dist = (lambda n: n.dist(point))
        else:
            get_dist = (lambda n: dist(n.data, point))

        results = []
        self.search_node(point, k, results, get_dist)

        return [(node, -d) for d, node in sorted(results, reverse=True)]  # (<KdNode>, distance)     排序后输出

    def search_node(self, point, k, results, get_dist):
        """
        :param point: 给定点
        :param k: 查找数目
        :param results: 结果，类型是列表
        :param get_dist: 计算距离
        """
        if not self:
            return

        nodeDist = get_dist(self)
        item = (-nodeDist, self)
        if len(results) >= k:           # 如果堆满了，就替换掉最远的那个值
            if -nodeDist > results[0][0]:
                heapq.heapreplace(results, item)
        else:           # 堆没满就都加入堆中
            heapq.heappush(results, item)
        # 得到分界面
        split_plane = self.data[self.axis]
        # 指定点和分界面的平方距离
        plane_dist = pow(point[self.axis] - split_plane, 2)

        # 从根节点递归向下访问，若point的axis维小于且分点坐标
        # 则移动到左子节点，否则移动到右子节点
        if point[self.axis] < split_plane:
            if self.left is not None:
                self.left.search_node(point, k, results, get_dist)
        else:
            if self.right is not None:
                self.right.search_node(point, k, results, get_dist)

        # 检查父节点的另一子节点是否存在比当前子节点更近的点
        # 判断另一区域是否与当前最近邻的圆相交
        if -plane_dist > results[0][0] or len(results) < k:
            if point[self.axis] < self.data[self.axis]:
                if self.right is not None:
                    self.right.search_node(point, k, results, get_dist)
            else:
                if self.left is not None:
                    self.left.search_node(point, k, results, get_dist)


def create(point_list=None, dimensions=None, axis=0):
    """ 由列表创建一个K-D Tree """
    sel_axis = (lambda prev_axis: (prev_axis+1) % dimensions)   # 用来计算sel_axis

    if not point_list:
        return KDNode(sel_axis=sel_axis, axis=axis, dimensions=dimensions)

    # 排序，选择中心
    point_list = list(point_list)
    point_list.sort(key=lambda point: point[axis])
    median = len(point_list) // 2

    loc = point_list[median]
    left = create(point_list[:median], dimensions, sel_axis(axis))      # sel_axis表示下一次需要切分的维度
    right = create(point_list[median + 1:], dimensions, sel_axis(axis))
    return KDNode(loc, left, right, axis=axis, sel_axis=sel_axis, dimensions=dimensions)
