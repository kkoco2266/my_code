import re
import sys

def main():
    print(convert(input("Hours: ")))


def convert(s):
    if mat := re.search(r"^((?:[1-9]|1[0-2])(?::[0-5][0-9])? (?:AM|PM)) to ((?:[0-9]|1[0-2])(?::[0-5][0-9])? (?:AM|PM))$" , s):
        start = mat.group(1)
        fin = mat.group(2)
        times = []
        for i in [start, fin]:
            time, merdm = i.split()
            if len(time.split(':')) == 2 :
                hr, mins = time.split(':')
                hr = int(hr)
                mins = int(mins)
                times.append(hrmins_24(hr, mins, merdm))
            else:
                times.append(hr_24(int(time), merdm))
        return times[0] + ' to ' + times[1]
    else:
        raise ValueError

def hrmins_24(hr, mins, merdm):
    if hr == 12 and merdm == 'AM':
        return f"00:{mins:02}"
    elif hr == 12 and merdm == 'PM':
        return f"12:{mins:02}"
    elif merdm == 'AM':
        return f"{hr:02}:{mins:02}"
    elif merdm == 'PM':
        return f"{hr+12:02}:{mins:02}"

def hr_24(hr, merdm):
    if hr == 12 and merdm == 'AM':
        return f"00:00"
    elif hr == 12 and merdm == 'PM':
        return f"12:00"
    elif merdm == 'AM':
        return f"{hr:02}:00"
    elif merdm == 'PM':
        return f"{hr+12:02}:00"


if __name__ == "__main__":
    main()
