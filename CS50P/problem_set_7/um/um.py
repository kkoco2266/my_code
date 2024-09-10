import re
import sys

def main():
    print(count(input("Text: ")))

def count(s):
    mat = re.findall(r"\bum\b" , s , flags = re.IGNORECASE)
    return len(mat)

if __name__ == "__main__":
    main()
