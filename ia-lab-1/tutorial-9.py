import exceptions

class Dog:
    __secret = 2


def main():

    # lists all of the exceptions available inside of python
    """
    for i in dir(exceptions):
        print i
    """

    # create a custom exception
    """
    raise Exception('JustDisagreeable')
    """

    # raises the AttributeError
    """
    puppy = Dog()
    print puppy.__secret
    """

    # raises the IOError
    """
    f = open('student.txt')
    """

    # raises the IndexError
    """
    list0 = [1, 2, 3]
    print list0[4]
    """

    # raises the KeyError
    """
    dict0 = ({'Age' : 21})
    print dict0['Name']
    """

    # raises the NameError
    """
    print monkey
    """

    # raises the TypeError
    """
    print "Tomato" % 5
    """

    # raises the ZeroDivisionError
    """
    zeroDivision = 1 / 0
    """

    # exception handling in python

    """
    try:
        zeroDivision = 1 / 0
    except ZeroDivisionError:
        print "You can't divide by zero"
    """

    try:
        #zeroDivision = notHere / 0
        zeroDivision = 1.0 / 2.0
    except (NameError, ZeroDivisionError), e:
        print "You can't divide by those numbers"
        print e
    else:
        print zeroDivision
    finally:
        print "Done"


if  __name__ == '__main__': main()