# -*- coding: utf-8 -*-


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = []
        self.data = {}
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """

        # 更新数据，把刚用过的拉到最前面
        try:
            self.cache.remove(key)
            self.cache.append(key)
        except Exception:
            pass

        return self.data[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """

        self.cache.insert(0, key)

        # 删除字典数据
        if len(self.cache) > self.capacity:
            need_del = self.cache[-1]
            del(self.cache[-1])
            del(self.data[need_del])
        self.data[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

cache = LRUCache(2)

cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))
cache.put(3, 3)
print(cache.get(2))
cache.put(4, 4)
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))
