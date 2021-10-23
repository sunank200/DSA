"""
public class Node
{
public Node[] Children;
public Node Right;
}
 Each node represents an element of a tree and specifies a list of immediate
children.
 The 'Children' property lists all children (in order) but the 'Right'
property is set to null.
Suppose you are given the root of a fully populated tree (i.e. a Node called
RootNode). Write code to set the 'Right' property so that each node is linked
to its right sibling.


"""


class Node(object):
    def __init__(self, value, children=None, right=None):
        if children:
            self.children = children
        else:
            self.children = []

        self.right = right
        self.value = value

    def show(self, tab=0):
        print("{0} Item {1}".format("\t" * tab, self.value))
        print("{0} Right {1}".format("\t" * tab, self.right))
        for c in self.children:
            c.show(tab + 1)


def setRight(root):
    q = list()
    q.append(root)
    q.append(None)

    while len(q) > 0:
        n = q[0]
        q.remove(n)
        if n != None:
            for item in n.children:
                q.append(item)

            if len(q) > 0:
                if q[0] != None:
                    n.right = q[0]
                else:
                    q.append(None)


root.show(0)
