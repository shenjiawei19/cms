a = [1, 2, 3, 4, 5]
# # d = [tuple([a[i+d] for d in xrange(0,2)]) for i in xrange(0,len(a)-1,2)]
# # print zip(*[iter(a)]*2)
# print [reduce((lambda x,y:x*y),a)]

# class Iters:
#     def __init__(self,value):
#         self.data = value
#     def __getitem__(self, item):
#         print ('get[%s]:'%item,)
#         return self.data[item]
#     def __iter__(self):
#         print ('iter=>',)
#         self.ix = 0
#         return self
#     def next(self):
#         print 'next:',
#         if self.ix == len(self.data):raise StopIteration
#         item = self.data[self.ix]
#         self.ix += 1
#         return item
#     def __contains__(self, item):
#         print 'contains:',
#         return item in self.data
#
# X = Iters([1,2,3,4,5])
# print (3 in X)
#
# for i in X:
#     print i,"|"
#
# print ()
# print ([i**2 for i in X])
#
#
# print X[1]
# print a[1:4]
# print a[slice(1,4,2)]
a = 123
# print repr(a)+1

# class Eee:
#     def __init__(self):
#         self.name = '1'
#     def __call__(self, *args, **kwargs):
#         print "22"
#     def __repr__(self):
#         return self.name
#
# a = Eee()
# print (a)
dl= 'tt'
a =  '''
    tt
'''
print a