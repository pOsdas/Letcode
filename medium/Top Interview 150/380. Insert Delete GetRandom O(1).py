import random


class RandomizedSet(object):

    def __init__(self):
        self.data = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.data:
            return False
        else:
            self.data.append(val)

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.data:
            return False
        else:
            self.data.remove(val)

    def getRandom(self):
        """
        :rtype: int
        """
        if len(self.data) == 0 or not self.data:
            return 0
        else:
            return random.choice(self.data)

    # def getlist(self):
    #     print(self.data)
