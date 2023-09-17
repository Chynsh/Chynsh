import sys
from Vector import Vector
class Catcher:
    def __init__(self, text, k, d):#计算论文的摘要向量
        tmp = [0 for i in range(d)]
        for i in range(len(text) - k):
            kgram = text[i:i+k]
            tmp[hash(kgram) % d] += 1
        vector = Vector(tmp)
        self.catcher = vector.direction()
    def __str__(self):
        return str(self.catcher)
    def similarTo(self, other):#比较余弦相似度
        return self.catcher.dot(other.catcher)
