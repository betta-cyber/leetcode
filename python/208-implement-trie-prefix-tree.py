#!/usr/bin/env python
# encoding: utf-8

class Trie(object):
    def __init__(self):
        self.root = {}


    def insert(self, word):
        p = self.root
        for c in word:
            if c not in p:
                p[c] = {}
            p = p[c]
        p['#'] = True


    def search(self, word):
        node = self.find(word)
        return node is not None and '#' in node


    def startsWith(self, prefix):
        return self.find(prefix) is not None


    def find(self, prefix):
        p = self.root
        for c in prefix:
            if c not in p: return None
            p = p[c]
        return p



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
