tuple1 = ('iolia', 21, 'Cluj-Napoca', 'Cluj')
print tuple1

tuple2 = tuple('abcd')
print tuple2

print tuple2[0:2]

list1 = ['iolia', 21, 'Cluj-Napoca', 'Cluj']
print list1[0:2]
print list1[-1]

list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print list2[-3:]
print list2[:3]
print list2[1:10:2]

print len(list2)
print min(list2)
print max(list2)

list3 = list('Fred')
print list3

list3[4:] = 'dy'
print list3
print ''.join(list3)

list4 = [1, 2, 3, 4]
list4[1] = 5
print list4
del list4[1]
print list4

list1.append('Romania')
print list1
list1.remove('Romania')
list1.remove(list1[3])
print list1
list1.insert(3, 'Cluj')
print list1

list5 = ['f', 'e', 'c', 'd', 'a', 'b']
list5.sort()
print list5

list6 = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]

print list6[2][1]