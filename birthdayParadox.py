# Exercise 3: The Birthday Paradox

import random

# Step 1: Generate a list of random birthdays
def generateBirthdays(n):
    birthdays = []
    for i in range(n):
        birthdays.append(random.randint(1,366))
    return birthdays

# Step 2: Check for duplicates in a list using list functions
def duplicateDetector(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                return True
    return False

# Step 3: Single trial
def singleTrial(n):
    birthdays = generateBirthdays(n)
    has_duplicate = duplicateDetector(birthdays)

    # Bonus: Count how many birthdays fall on each day
    day_counts = [0] * 366
    for day in birthdays:
        day_counts[day - 1] += 1

    duplicate_days = []
    for day in range(366):
        count = day_counts[day]
        if count > 1:
            duplicate_days.append((day + 1, count))

    return has_duplicate, birthdays, duplicate_days

# Step 4: Put it all together
def birthdayParadox(m, n):
    duplicates_count = 0
    for _ in range(m):
        has_duplicate, birthdays, duplicate_days = singleTrial(n)
        if has_duplicate:
            duplicates_count += 1

            for day, count in duplicate_days:
                print(f"There were {count} birthdays on day {day}")

    if n == 23:
        theoretical = 50
    elif n == 70:
        theoretical = 99.9
    else:
        theoretical = 0

    actual = round(((duplicates_count / m) * 100),2)
    print(f"Percentage of trials with duplicate birthdays: {actual}% compared to the theoretical {theoretical}%")


# Example
birthdayParadox(10000, 23)
