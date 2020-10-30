from removingkeys import removekeys as rk

randomdict = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4, 
    'e': 5,
    'f': 6,
    'g': 7,
}

randomlist = ['b', 'd' , 'e']


if __name__ == "__main__":
    print(rk(randomdict , randomlist))