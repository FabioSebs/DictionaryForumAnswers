from values import findvalue as fv

randomdict = {
    'a': 1,
    'b': 0,
    'c': 1,
    'd': 0, 
    'e': 2,
    'f': 2,
    'g': 3,
}

value = 0

if __name__ == "__main__":
    print(fv(randomdict, value))