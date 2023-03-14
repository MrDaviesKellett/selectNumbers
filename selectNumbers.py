# Select even Numbers

# Do not modify this function name or parameters
def selectEven(inList):
    '''Given a list of numbers, return a new list with all of the odd numbers removed'''
    outList = inList
    # fill this function with your logic to solve the challenge

    return outList

def selectOdd(inList):
    '''Given a list of numbers, return a new list with all of the even numbers removed'''
    outList = inList
    return inList

def selectMultiples(inList, multiple):
    '''Given a list of numbers, return a new list containing only multiples of the parameter multiple'''
    outList = inList
    return inList

if __name__ == "__main__":
    assert selectEven([1,2,3,4,5]) == [2,4]
    assert selectOdd([1,2,3,4,5]) == [1,3,5]
    assert selectMultiples([1,2,3,4,5],3) == [3]