def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    s = s.strip()
    if test2(s) and test1(s) and test3(s) and test4(s):
        return True
    else:
        return False

def test1(s):
    if s[0].isalpha() and s[1].isalpha():
        return True
    else:
        return False

def test2(s):
    if 2<= len(s) <=6:
        return True
    else:
        return False

def test3(s):
    for i in range(len(s)-1):
        if s[i].isnumeric() and s[i+1].isalpha():
            return False
    for i in range(len(s)):
        if s[i].isnumeric() and s[i] == '0' and s[i-1].isalpha():
            return False
    return True

def test4(s):
    for i in s:
        if not i.isalnum():
            return False
    return True

main()
