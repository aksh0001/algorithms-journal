"""
Test module for AVL Trees + benchmark against BSTs

@author a.k
"""
import random
import time

from matplotlib import pyplot as plt

from data_structures.trees.AVLTree import AVLTree
from data_structures.trees.BinarySearchTree import BST
from questions.trees_graphs.IsBST import validate_bst


def test_left_left():
    ll = [24, 20, 26, 15, 22]
    t1 = AVLTree.burst_insert(ll)
    assert validate_bst(t1.root), 'ERROR!'
    # pretty_print_tree(t1.root)
    t1.insert(14)
    assert validate_bst(t1.root), 'ERROR!'
    # pretty_print_tree(t1.root)

    ll = [13, 10, 15, 5, 11, 16, 4, 8]
    t1 = AVLTree.burst_insert(ll)
    assert validate_bst(t1.root), 'ERROR!'
    # pretty_print_tree(t1.root)
    t1.insert(3)
    assert validate_bst(t1.root), 'ERROR!'
    # pretty_print_tree(t1.root)

    print('PASSED LEFT-LEFT')


def test_right_right():
    rr = [23, 20, 26, 25, 28, 24, 34]
    t1 = AVLTree.burst_insert(rr)
    assert validate_bst(t1.root), 'ERROR!'
    # pretty_print_tree(t1.root)

    rr = [20, 10, 30, 8, 25, 40, 50]
    t1 = AVLTree.burst_insert(rr)
    assert validate_bst(t1.root), 'ERROR!'
    # pretty_print_tree(t1.root)
    t1.insert(60)
    assert validate_bst(t1.root), 'ERROR!'
    # pretty_print_tree(t1.root)

    print('PASSED RIGHT-RIGHT')


def test_left_right():
    lr = [24, 20, 26, 14, 22]
    t1 = AVLTree.burst_insert(lr)
    assert validate_bst(t1.root), 'ERROR!'
    # pretty_print_tree(t1.root)
    t1.insert(21)
    # pretty_print_tree(t1.root)
    assert validate_bst(t1.root), 'ERROR!'

    print('PASSED LEFT-RIGHT')


def test_right_left():
    rl = [23, 20, 26, 25, 28]
    t1 = AVLTree.burst_insert(rl)
    assert validate_bst(t1.root), 'ERROR!'
    # pretty_print_tree(t1.root)
    t1.insert(24)
    # pretty_print_tree(t1.root)
    assert validate_bst(t1.root), 'ERROR!'

    print('PASSED LEFT-RIGHT')


def test_correctness():
    # CORRECTNESS TEST
    try:
        test_left_left()
        test_right_right()
        test_left_right()
        test_right_left()
        print('> PASSED CORRECTNESS TEST')
    except Exception:
        print('ERROR!')


def test_performance():
    x = [i for i in range(10000, 100001, 10000)]
    y1, y2 = [0] * 10, [0] * 10
    bst, avl = BST(), AVLTree()
    # Benchmark BST with random input
    for i in range(10000, 100001, 10000):
        t1 = time.time()
        for _ in range(i):
            bst.insert(random.randint(-50, 50))
        y1[(i - 10000) // 10000] = time.time() - t1
    # Benchmark AVL with random input
    for i in range(10000, 100001, 10000):
        t1 = time.time()
        for _ in range(i):
            avl.insert(random.randint(-50, 50))
        y2[(i - 10000) // 10000] = time.time() - t1
    plt.plot(x, y2, marker='', color='blue', linewidth=2, label='AVL')
    plt.plot(x, y1, marker='', color='olive', linewidth=2, linestyle='dashed', label="BST")
    plt.xlabel('input size')
    plt.ylabel('insert time')
    plt.title('Input size vs Insertion time for AVL and BST (Random input)')
    plt.legend()
    plt.savefig('./benchmarks/avl_bst_benchmark-random.png')
    plt.clf()

    y1, y2 = [0] * 10, [0] * 10
    bst, avl = BST(), AVLTree()
    # Benchmark BST with slight sorted skew input
    for i in range(10000, 100001, 10000):
        t1 = time.time()
        for j in range(i):
            bst.insert(random.randint(i + j, 50 * (i + j)))
        y1[(i - 10000) // 10000] = time.time() - t1
    # Benchmark AVL with slight sorted skew input
    for i in range(10000, 100001, 10000):
        t1 = time.time()
        for j in range(i):
            avl.insert(random.randint(i + j, 50 * (i + j)))
        y2[(i - 10000) // 10000] = time.time() - t1
    plt.plot(x, y2, marker='', color='black', linewidth=1, label='AVL')
    plt.plot(x, y1, marker='', color='gold', linewidth=1, linestyle='dashed', label="BST")
    plt.xlabel('input size')
    plt.ylabel('insert time')
    plt.title('Input size vs Insertion time for AVL and BST (Slight sorted skew)')
    plt.legend()
    plt.savefig('./benchmarks/avl_bst_benchmark-sorted.png')
    plt.clf()

    y1, y2, x = [0] * 10, [0] * 10, [i for i in range(10000, 100001, 10000)]
    bst, avl = BST(), AVLTree()
    # Benchmark BST and AVL get() with random input
    for i in range(10000, 100001, 10000):
        values = []
        for j in range(i):
            rand_num = random.randint(-100, 200)
            bst.insert(rand_num)
            avl.insert(rand_num)
            values.append(rand_num)
        random.shuffle(values)
        # benchmark bst
        t1 = time.time()
        for val in values:
            bst.get(val)
        y1[(i - 10000) // 10000] = time.time() - t1
        # benchmark avl
        t2 = time.time()
        for val in values:
            avl.get(val)
        y2[(i - 10000) // 10000] = time.time() - t2
    plt.plot(x, y2, marker='', color='black', linewidth=1, label='AVL')
    plt.plot(x, y1, marker='', color='gold', linewidth=1, linestyle='dashed', label="BST")
    plt.xlabel('input size')
    plt.ylabel('retrieval time')
    plt.title('Input size vs Retrieval time for AVL and BST (Random input)')
    plt.legend()
    plt.savefig('./benchmarks/avl_bst_benchmark-retrieval.png')
    plt.clf()

    y1, y2, x = [0] * 10, [0] * 10, [i for i in range(10000, 100001, 10000)]
    bst, avl = BST(), AVLTree()
    # Benchmark BST and AVL get() with skewed input
    for i in range(10000, 100001, 10000):
        values = []
        for j in range(i):
            rand_num = random.randint(i + j, 50 * (i + j))
            bst.insert(rand_num)
            avl.insert(rand_num)
            values.append(rand_num)
        random.shuffle(values)
        # benchmark bst
        t1 = time.time()
        for val in values:
            bst.get(val)
        y1[(i - 10000) // 10000] = time.time() - t1
        # benchmark avl
        t2 = time.time()
        for val in values:
            avl.get(val)
        y2[(i - 10000) // 10000] = time.time() - t2
    plt.plot(x, y2, marker='', color='black', linewidth=1, label='AVL')
    plt.plot(x, y1, marker='', color='gold', linewidth=1, linestyle='dashed', label="BST")
    plt.xlabel('input size')
    plt.ylabel('retrieval time')
    plt.title('Input size vs Retrieval time for AVL and BST (Slightly sorted skew input)')
    plt.legend()
    plt.savefig('./benchmarks/avl_bst_benchmark-retrieval-sorted.png')
    plt.clf()


if __name__ == '__main__':
    test_correctness()
    test_performance()
