def main():
    currenttime = input('What time is it? ')
    hour = convert(currenttime)
    if 7 <= hour <= 8:
        print('breakfast time')
    elif 12 <= hour <= 13:
        print('lunch time')
    if 18 <= hour <= 19:
        print('dinner time')

def convert(time):
    time = time.strip().replace(':', ' ').replace('a.m.', '')
    if 'p.m.' in time:
        time = time.replace('p.m.', '')
        hours, mins = time.split()
        return float(hours)+12 + float(mins)/60
    else:
        hours, mins = time.split()
        return float(hours)+float(mins)/60

if __name__ == "__main__":
    main()
