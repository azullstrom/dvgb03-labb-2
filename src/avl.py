#!/usr/bin/env python3

import sys
import bst
import logging

log = logging.getLogger(__name__)

class AVL(bst.BST):
    def __init__(self, value=None):
        '''
        Initializes an empty tree if `value` is None, else a root with the
        specified `value` and two empty children.
        '''
        self.set_value(value)
        if not self.is_empty():
            self.cons(AVL(), AVL())

    def add(self, v):
        '''
        Calling super class add function and balancing the tree afterwards.
        '''
        super().add(v)
        return self.balance()

    def delete(self, v):
        '''
        Calling super class delete function and balancing the tree afterwards.
        '''
        super().delete(v)
        return self.balance()

    def bf(self):
        '''
        Returns the balance of the tree. Negative number if right subtree is higher
        and vice versa.
        '''
        return self.lc().height() - self.rc().height()

    def balance(self):
        '''
        AVL-balances around the node rooted at `self`.  In other words, this
        method applies one of the following if necessary: slr, srr, dlr, drr.
        '''
        if self.bf() == -2:  # Right heavy
            if self.rc().bf() >= 1:  # Inner heavy
                return self.dlr()
            else:  # Outer heavy
                return self.slr()
        elif self.bf() == 2:  # Left heavy
            if self.lc().bf() <= -1:
                return self.drr()
            else:
                return self.srr()
        return self

    def slr(self):
        '''
        Performs a single-left rotate around the node rooted at `self`.
        '''
        node = self.rc()
        self.set_rc(node.lc())
        node.set_lc(self)
        return node

    def srr(self):
        '''
        Performs a single-right rotate around the node rooted at `self`.
        '''
        node = self.lc()
        self.set_lc(node.rc())
        node.set_rc(self)
        return node

    def dlr(self):
        '''
        Performs a double-left rotate around the node rooted at `self`.
        '''
        self.set_rc(self.rc().srr())
        return self.slr()

    def drr(self):
        '''
        Performs a double-right rotate around the node rooted at `self`.
        '''
        self.set_lc(self.lc().slr())
        return self.srr()

if __name__ == "__main__":
    log.critical("module contains no main module")
    sys.exit(1)
