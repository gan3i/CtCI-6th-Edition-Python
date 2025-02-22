from collections import deque

from chapter_04.binary_search_tree import BinarySearchTree


def find_bst_sequences(bst):
    if not bst.root:
        return []
    return helper(bst.root)


def helper(node):
    if not node:
        return [deque()]

    right_sequences = helper(node.right)
    left_sequences = helper(node.left)
    sequences = []
    for right in right_sequences:
        for left in left_sequences:
            sequences = weave(left, right, deque([node.key]), sequences)
    return sequences


def weave(first, second, prefix, results):
    if len(first) == 0 or len(second) == 0:
        result = prefix.copy()
        result.extend(first)
        result.extend(second)
        results.append(result)
        return results
    head = first.popleft()
    prefix.append(head)
    results = weave(first, second, prefix, results)
    first.appendleft(head)
    prefix.pop()
    head = second.popleft()
    prefix.append(head)
    results = weave(first, second, prefix, results)
    prefix.pop()
    second.appendleft(head)
    return results


def test_find_bst_sequences():
    bst = BinarySearchTree()
    bst.insert(2)
    bst.insert(1)
    bst.insert(3)
    sequences = find_bst_sequences(bst)
    assert deque([2, 1, 3]) in sequences
    assert deque([2, 3, 1]) in sequences
    assert len(sequences) == 2


def example():
    bst = BinarySearchTree()
    bst.insert(20)
    bst.insert(9)
    bst.insert(25)
    bst.insert(5)
    bst.insert(12)
    # bst.insert(11);
    # bst.insert(14);

    sequences = find_bst_sequences(bst)
    print(sequences)


if __name__ == "__main__":
    example()
