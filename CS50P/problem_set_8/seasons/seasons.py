from datetime import date
import inflect, sys
p = inflect.engine()


def main():
    try:
        date_ob = date.fromisoformat(input("Date of Birth: "))
    except ValueError:
        sys.exit("Invalid date")
    time_diff = date.today() - date_ob
    print(day_to_min(time_diff.days).capitalize() + " minutes")

def day_to_min(days):
    mins = days * 24 * 60
    return p.number_to_words(mins, andword="")


if __name__ == "__main__":
    main()
