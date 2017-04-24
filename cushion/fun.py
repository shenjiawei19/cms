# -*- coding: utf-8 -*-

def type(typ):
    d = [1,1,0,3,9,10,14,15][typ=='自建' or typ=='所有'and 2 or typ=='奇异' and 3 or typ=='又拍' and 4 or typ=='乐视' and 5 or typ =='金山' and 6 or typ=='蛮蛮云' and 7]
    print d
# cdn_id 1表示视云自建
# cdn_id 0 表示所有
# cdn_id 3 表示奇异
# cdn_id 9 表示又拍
# cdn_id 10 表示乐视
# cdn_id 14 表示金山
# cdn_id 15 表示蛮蛮云
type('蛮蛮云')
#
# [typ=='自建']
# a = '所有' == '自建' and '2' or '所有' == '所有' and '3' or '1'
# a = 3
# b = 4
# d = '自建' == '自建' and a or b
# print a