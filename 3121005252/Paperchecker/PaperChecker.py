
import sys
from Vector import Vector
from Catcher import Catcher
#需查重文件
filenames = [ 'orig.txt', 'orig_0.8_add.txt','orig_0.8_del.txt','orig_0.8_dis_1.txt','orig_0.8_dis_10.txt','orig_0.8_dis_15.txt']
#固定参数
k = 5
d = 100000

#初始化摘要数组并赋值
catchers = [0 for i in filenames]
for i in range(len(filenames)):
    with open(filenames[i], 'r', encoding='utf-8') as f:
        text = f.read()
        catchers[i] = Catcher(text, k, d)
        
#输出结果
for i in range(len(filenames)):
    if i!=0:
        print(f"{filenames[0]}与{filenames[i]}相似度为:{catchers[0].similarTo(catchers[i])}")