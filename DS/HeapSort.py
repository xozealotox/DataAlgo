"""
堆处理海量数据的 topK，分位数 非常合适，优先队列 应用在元素优先级排序，比如本题的频率排序非常合适。与基于比较的排序算法 时间复杂度
O(nlogn) 相比，使用 堆，优先队列 复杂度可以下降到
O(nlogk)，在总体数据规模 n 较大，而维护规模 k 较小时，时间复杂度优化明显。

堆，优先队列 的本质其实就是个完全二叉树，有其下重要性质
ps: 堆 heap[0] 插入一个占位节点，此时堆顶为 index 为 1 的位置，可以更方便的运用位操作。
[1,2,3] -> [0,1,2,3]

父节点 index 为 i
左子节点 index 为 i << 1
右子节点 index 为 i << 1 | 1
大顶堆中每个父节点大于子节点，小顶堆每个父节点小于子节点
优先队列以优先级为堆的排序依据
因为性质 1，2，3，堆可以用数组直接来表示，不需要通过链表建树。
堆，优先队列 有两个重要操作，时间复杂度均是
O(logk)。以小顶锥为例：

上浮 sift up: 向堆尾新加入一个元素，堆规模 +1，依次向上与父节点比较，如小于父节点就交换。
下沉 sift down: 从堆顶取出一个元素（堆规模 -1，用于堆排序）或者更新堆中一个元素（本题），依次向下与子节点比较，如大于子节点就交换。
对于 topk 问题：最大堆求topk小，最小堆求 topk 大。

topk小：构建一个 k 个数的最大堆，当读取的数小于根节点时，替换根节点，重新塑造最大堆
topk大：构建一个 k 个数的最小堆，当读取的数大于根节点时，替换根节点，重新塑造最小堆
这一题的总体思路 总体时间复杂度

O(nlogk)

遍历统计元素出现频率O(n)
前k个数构造 规模为 k+1 的最小堆 minheap，O(k)， 注意 +1 是因为占位节点。
遍历规模k之外的数据，大于堆顶则入堆，下沉维护规模为k的最小堆 minheap.O(nlogk)
(如需按频率输出，对规模为k的堆进行排序)
"""
"""
给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。

输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]

输入: nums = [1], k = 1
输出: [1]
"""


def heapify(tree: list, n: int, i: int):
    """
    使得堆成立
    :param tree: 数组
    :param n: 树中的节点个数
    :param i: 当前节点下标
    :return:
    """
    if i >= n:
        return
    max = i
    lchild = i * 2 + 1
    rchild = i * 2 + 2
    if lchild < n and tree[lchild] > tree[i]:
        max = lchild
    if rchild < n and tree[rchild] > tree[max]:
        max = rchild
    if max != i:
        tree[max], tree[i] = tree[i], tree[max]
        heapify(tree, n, max)


def heapify_big(tree: list, n: int, i: int):
    """
    使得堆成立
    :param tree: 数组
    :param n: 树中的节点个数
    :param i: 当前节点下标
    :return:
    """
    if i >= n:
        return
    max = i
    lchild = i * 2 + 1
    rchild = i * 2 + 2
    if lchild < n and tree[lchild] < tree[i]:
        max = lchild
    if rchild < n and tree[rchild] < tree[max]:
        max = rchild
    if max != i:
        tree[max], tree[i] = tree[i], tree[max]
        heapify(tree, n, max)


def build_heap(tree: list, n: int):
    last_node = n - 1
    parent = (last_node - 1) >> 1
    for i in range(parent, -1, -1):
        heapify_big(tree, n, i)
    return tree


def heap_sort(tree: list, n: int):
    build_heap(tree, n)
    for i in range(n - 1, -1, -1):
        tree[i], tree[0] = tree[0], tree[i]
        heapify_big(tree, i, 0)
    return tree


if __name__ == '__main__':
    tree = [1, 3, 4, 5, 6, 2, 7, 11]
    print(heap_sort(tree, len(tree)))
