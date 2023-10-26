def LeapYear(year):
    if year % 4 == 0 and year % 100 != 0:
        return f"Did someone say leap frog? Cause {year} is a leap year!"
    elif year % 100 == 0:
        if year % 400 == 0:
            return f"Did someone say leap frog? Cause {year} is a leap year!"
        else:
            return f"Keep those frogs away! Cause {year} is not a leap year!"
    else:
        return f"Keep those frogs away! Cause {year} is not a leap year!"

year = int(input("Enter year for Leap fr- I mean Leap Year check: "))
print(LeapYear(year))
