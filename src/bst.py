#!/usr/bin/env python3

import bt
import sys
import logging

log = logging.getLogger(__name__)

class BST(bt.BT):
    def __init__(self, value=None):
        '''
        Initializes an empty tree if `value` is None, else a root with the
        specified `value` and two empty children.
        '''
        self.set_value(value)
        if not self.is_empty():
            self.cons(BST(), BST())

    def is_member(self, v):
        '''
        Returns true if the value `v` is a member of the tree.
        '''
        if self.is_empty():
            return False
        if v == self.value():
            return True
        if v < self.value():
            return self.lc().is_member(v)
        else:
            return self.rc().is_member(v)

    def size(self):
        '''
        Returns the number of nodes in the tree.
        '''
        if self.is_empty():
            return 0
        else:
            left = self.lc().height()
            right = self.rc().height()
            return 1 + left + right

    def height(self):
        '''
        Returns the height of the tree.
        '''
        if self.is_empty():
            return 0
        else:
            left = self.lc().height()
            right = self.rc().height()
            return 1 + max(left, right)

    def preorder(self):
        '''
        Returns a list of all members in preorder.
        '''
        if self.is_empty():
            return []
        return [self.value()] + self.lc().preorder() + self.rc().preorder()

    def inorder(self):
        '''
        Returns a list of all members in inorder.
        '''
        if self.is_empty():
            return []
        return self.lc().preorder() + [self.value()] + self.rc().preorder()

    def postorder(self):
        '''
        Returns a list of all members in postorder.
        '''
        if self.is_empty():
            return []
        return self.lc().preorder() + self.rc().preorder() + [self.value()]

    def bfs_order_star(self):
        '''
        Returns a list of all members in breadth-first search* order, which
        means that empty nodes are denoted by "stars" (here the value None).
        '''
        if self.is_empty():
            return []

        bfs_queue = self.get_bfs_star_queue()

        return bfs_queue

    def get_bfs_star_queue(self):
        '''
        Returns a BFS queue with None values included.
        '''
        if self.is_empty():
            return []

        queue = [self]
        bfs_queue = []
        perfect_size = 2**self.height() - 1

        while len(queue) <= perfect_size:
            node = queue.pop(0)
            bfs_queue.append(node.value())
            # New temp node with value None
            temp = BST(0)
            temp.set_value(None)

            queue.append(node.lc()) if not node.lc().is_empty() else queue.append(temp)
            queue.append(node.rc()) if not node.rc().is_empty() else queue.append(temp)

        return bfs_queue

    def add(self, v):
        '''
        Adds the value `v` and returns the new (updated) tree.  If `v` is
        already a member, the same tree is returned without any modification.
        '''
        if self.is_empty():
            self.__init__(value=v)
            return self
        if v < self.value():
            return self.cons(self.lc().add(v), self.rc())
        if v > self.value():
            return self.cons(self.lc(), self.rc().add(v))
        return self
    
    def delete(self, v):
        '''
        Removes the value `v` from the tree and returns the new (updated) tree.
        If `v` is a non-member, the same tree is returned without modification.
        '''
        if not self.is_member(v):
            log.error("Value does not exist")
            return self

        # This recursion will end when the node with v value is found
        if v < self.value():
            return self.cons(self.lc().delete(v), self.rc())
        elif v > self.value():
            return self.cons(self.lc(), self.rc().delete(v))
        else:
            return self.delete_node()

    def delete_node(self):
        if self.lc().is_empty():
            temp = self.rc()
            self.set_value(None)
            return temp
        elif self.rc().is_empty():
            temp = self.lc()
            self.set_value(None)
            return temp
        else:
            if self.lc().height() < self.rc().height():
                node = self.rc().min_value_node()
                self.set_value(node.value())
                self.set_rc(self.rc().delete(node.value()))
            else:
                node = self.lc().max_value_node()
                self.set_value(node.value())
                self.set_lc(self.lc().delete(node.value()))
            return self

    def min_value_node(self):
        '''
        Returns node with minimum value
        '''
        if not self.lc().is_empty():
            return self.lc().min_value_node()
        else:
            return self

    def max_value_node(self):
        '''
        Returns node with maximium value
        '''
        if not self.rc().is_empty():
            return self.rc().max_value_node()
        else:
            return self

if __name__ == "__main__":
    log.critical("module contains no main module")
    sys.exit(1)
