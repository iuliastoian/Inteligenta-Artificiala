import math

dict1 = ({"Age" : 21, "Height" : "1.72 m", "Weight" : "67 kg"})

print dict1
print dict1.get("Height")
print dict1.items()
print dict1.values()

dict1.pop("Height")
print dict1

name = 'iolia'
age = 21.25
sex = 'f'
kids = 0
married = False

print 'My name is ' + name
print '%s is %.2f years old' % (name, age)
print 'Sex: %c' % (sex)
print 'She has %d kids and said it\'s %s that she is married' % (kids, married)

print '%.15f' % (math.pi)
print '%.20f' % (math.pi)
print '%20.15f' % (math.pi)
print '%-25.15f is the value of pi' % (math.pi)

#precisionPi = int(raw_input("How precise should pi be: "))
#print 'pi = %.*f' % (precisionPi, math.pi)

string1 = 'Here is a long string that I will be messing with'
print string1[1:20:2]

print string1.find("string")
print string1.count('e')
print string1.count('e', 4)
print string1.count('e', 4, 20)

copyStr1 = tuple(string1)
print copyStr1
#copyStr2 = ''.join(copyStr1)
#print copyStr2

print ', '.join(copyStr1)

print string1.lower()
print string1.upper()

print string1.replace('long', 'small')

print string1.split(' ')

randWs = '                       Random white space      '
print randWs.strip()