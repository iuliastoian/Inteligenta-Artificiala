list1 = [4, 5, 6]

string1 = "Random string"

print 4 in list1
print 3 in list1

print "String" in string1

x = 1

while x <= 30:
    #print x
    print x,
    x += 1

print '\n'

list2 = [0, 1, 2]
list3 = ['serotonin', 'dopamine', 'oxytocin']
list4 = [27, 70, 99]

for i in list2:
    print '%s is %d' % (list3[i], list4[i])

list5 = [1, 2, 3, 4, 5]

for i in list5:
    print i,

print '\n'

for i in range(1, 31):
    print i,

print '\n'

list5 = range(1, 31)

for i in list5:
    print i,

print '\n'

for i in list5:
    if (i % 2 == 0):
        continue
    elif i == 25:
        break
    else:
        print i,