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
        print(self.cache)
        if key in self.data:
            self.cache.remove(key)
            self.cache.insert(0, key)
            return self.data[key]
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """

        if key in self.data:
            self.data[key] = value
            self.cache.remove(key)
            self.cache.insert(0, key)
        else:
            # 删除字典数据
            self.data[key] = value
            if len(self.cache) >= self.capacity:
                need_del = self.cache[-1]
                del(self.cache[-1])
                del(self.data[need_del])
            self.cache.insert(0, key)


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
