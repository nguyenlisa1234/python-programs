# Exercise 3: Duplicate Detector V2
# White Python
# Oct. 25, 2023


def duplicateDetectorV2(n):
    birthdays = n
    frequency = len(birthdays)
    birthdaySet = set(birthdays)
    frequencySet = len(birthdaySet)
    if frequency != frequencySet:
        return True 
    else:
        return False 

# --------------- original solution below

def duplicateDetector(n):
    birthdayFreq = []
    duplst = []
    for birthday in n:
        if birthday not in birthdayFreq:
            birthdayFreq.append(birthday)
        else:
            duplst.append(birthday) 

    if birthday in duplst:
        return True
    else:
        return False