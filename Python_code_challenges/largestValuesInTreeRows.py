
""" largetValuesInTreeRows -- 30min
You have a binary tree t. Your task is to find the largest value in each 
row of this tree. In a tree, a row is a set of nodes that have equal depth. 
For example, a row with depth 0 is a tree root, a row with depth 1 is 
composed of the root's children, etc.

Return an array in which the first element is the largest value in the 
row with depth 0, the second element is the largest value in the row with 
depth 1, the third element is the largest element in the row with depth 2, 
etc.

Example

For

t = {
    "value": -1,
    "left": {
        "value": 5,
        "left": null,
        "right": null
    },
    "right": {
        "value": 7,
        "left": null,
        "right": {
            "value": 1,
            "left": null,
            "right": null
        }
    }
}
the output should be largestValuesInTreeRows(t) = [-1, 7, 1].

The tree in the example looks like this:

    -1
   / \
  5   7
       \
        1
In the row with depth 0, there is only one vertex - the root with value -1;
In the row with depth 1, there are two vertices with values 5 and 7, so 
the largest value here is 7;
In the row with depth 2, there is only one vertex with value 1.
Input/Output

[execution time limit] 4 seconds (py3)

[input] tree.integer t

A binary tree of integers.

Guaranteed constraints:
0 ≤ tree size ≤ 5 · 104,
-1000 ≤ node value ≤ 1000.

[output] array.integer

An array of the largest values in each row of t.
"""

# Definition for binary tree:
class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

def largestValuesInTreeRows(t):
    results, tree = [], [t]
    while any(tree): 
        results.append(max(node.value for node in tree))
        tempHolder = []
        for node in tree:
            for child in (node.left, node.right):
                if child: tempHolder.append(child)
        tree = tempHolder
    return results

# create tree for testing
t = Tree(1)
t.left = Tree(2)
t.right = Tree(4)
t.left.right = Tree(3)
t.right.left = Tree(5)

print(largestValuesInTreeRows(t)) # [1, 4, 5]


