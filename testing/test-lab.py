def position(sequence, item):
    sum = 0 
    for n in sequence:
        if n != item:
            sum += 1
        else:
            return sum

def test_position_int():
    assert position([1,2,3,4,5,6,7], 5) == 4
    assert position([], 3) == None
    assert position([8, 6, 4, 2], 10) == None

def test_position_str():
    assert position(["bannanna","apples","grapes","raspberry","orange"], "grapes") == 2
    assert position([], "blueberry") == None
    assert position(["bannanna","apples","grapes","raspberry","orange"], "strawberries") == None

test_position_int()
test_position_str()



def fact(x):
    if x <= 0:
        return 1
    return x * fact(x - 1)

def test_fact():
    assert fact(5) == 120
    assert fact(0) == 1
    assert fact(9) == 362880
    assert fact(-2) == 1

test_fact()



def list_of_squares(n):
    if n <= 0:
            print("index out of range")
    else:
        d=dict()
        for i in range(1,n+1):
            d[i]=i*i
        return d

def test_list_of_squares():
    assert list_of_squares(3) == {1: 1, 2: 4, 3: 9}
    assert list_of_squares(0) == "index out of range"
    assert list_of_squares(-3) == "index out of range"

test_list_of_squares()

