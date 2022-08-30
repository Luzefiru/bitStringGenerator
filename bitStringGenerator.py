def generateBitString(first, second):
    """
    Parameters
    ----------
    first : int/str
        The first bit string - a sequence of 1's or 0's.
    second : int/str
        The second bit string - a sequence of 1's or 0's.
    
    Notes
    -----
    first and second must have equal length in order to do a sucessful bit operation.

    Returns
    -------
    This function returns a bit string,
    which is a result of the bitwise operation on the first & second bit strings.
    
    """
    # int -> str conversion
    first, second = str(first), str(second)

    # length & invalid character checks
    if len(first) != len(second) or len([x for x in first+second if x not in ('1','0')]) > 0:
        return "Cannot create a bit string."
    print('===========================================')

    # asks the user to input a valid bit operation, reprompts if they do not.
    operationList = ['and', 'or', 'xor']
    operation = None
    while operation not in operationList:
        print(f'List of Available Operations: {", ".join([x for x in operationList])}')
        print('===========================================')
        operation = input('What bitwise operation will be executed? ')

    # execution of bit operators based on user input
    bitStringOutput = []
    for i in range(len(first)):
        if operation == 'and':
            bitStringOutput.append(1 if first[i] == '1' and second[i] == '1' else 0)
        if operation == 'or':
            bitStringOutput.append(1 if first[i] == '1' or second[i] == '1' else 0)
        if operation == 'xor':
            bitStringOutput.append(0 if first[i] == '0' and second[i] == '0' else 1 if first[i] == '0' or second[i] == '0' else 0)
    
    # returns the bit string built by the bit operation with the function parameters as input
    return ''.join([str(x) for x in bitStringOutput])
        
def __main__():
    # asks user to input the bit strings to be used for the bit operation
    first = input('Input the first bit string: ')
    second = input('Input the second bit string: ')
    # prints the result
    print(f'===========================================\nResult:\n{generateBitString(first, second)}')

__main__()