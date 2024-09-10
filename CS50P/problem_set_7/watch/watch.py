import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    if mat := re.search(r'src="https?://(?:www.)?youtube.com/embed/(.+)"' , s) :
        return f"https://youtu.be/{mat.group(1)}"

if __name__ == "__main__":
    main()
