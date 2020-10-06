import math

int1 = 27
longInt1 = 3000000000000L
float1 = 9.9
string1 = "python"
boolean1 = True

print type(int1)
print type(longInt1)
print type(float1)
print type(string1)
print type(boolean1)

boolean2 = False

print boolean1 and boolean2
print boolean1 or boolean2
print not boolean2

int2 = 73
int3 = 45
float2 = 2.6
float3 = 0.3

print int2 / int3
print float(int2) / float(int3)
print int(float2)
print int(boolean1)

print int1 > int2
print int1 < int2
print int1 >= int2
print int1 <= int2
print int1 != int2
print int1 == int2

boolean1 = int2 == int3

print int1 + int2
print int1 - int2
print int1 * int2
print int1 / int2
print int1 % int2
print int1 ** int2

print math.sqrt(int1)

answer = raw_input("What is your name?")
print "Hello ", answer

longString1 = '''This is a very long string of text \
that goes on and on'''
print longString1

longString2 = 'Still a "string"'
print longString2

longString3 = 'He said \'Hi, how are you?\'\n'
longString4 = "Hello"
print longString3
print longString4
