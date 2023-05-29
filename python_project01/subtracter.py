
def sub(a,b):
    if type(a) not in [float,int]:
        raise TypeError('a is not a number')
    if type(b) not in [float,int]:
        raise TypeError('b is not a number')
    
    diff = a-b

    if diff>=0:
        return "POSITIVE"
    else: 
        return "NEGATIVE"
    


if __name__ == '__main__':
    print(sub(1,2))