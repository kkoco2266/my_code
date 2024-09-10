months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

while True:
    try:
        dat = input("Date: ").strip()
        if dat[0].isalpha() and dat.find(",") == -1:
            raise ValueError
        elif dat[0].isalpha() and dat.find("/") != -1:
            raise ValueError
        date = dat.replace("/", " ").replace(",", "")
        mon, day, year = date.split()
        day = int(day)
        year = int(year)
        if not 0 < day <= 31:
            raise ValueError
        if mon in months:
            mon = months.index(mon) + 1
            break
        else:
            mon = int(mon)
            if not 0 < mon <= 12:
                raise ValueError
            else:
                break
    except ValueError:
        pass

print(f"{year:04}-{mon:02}-{day:02}")
