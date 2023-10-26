# Exercise 3: The Birthday Paradox

# Step 1: Random Birthday Generator
import random
def birthdays(n):
    lst = []
    newlst = []
    for i in range(1,366):
        lst.append(i)
    for day in lst:
        day = random.choice(lst)
        newlst.append(day)
        
    return newlst[:n]

# Step 2: Duplicate Detector in a List
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

# Step 3: Single Trial 
def singleTrial(n):
    size = birthdays(n)
    test = duplicateDetector(size)
    if test == True:
        return True
    elif test == False:
        return False

# Step 4: Solution (putting it all together)
def birthdayParadox(m,n):
    df = 0
    for i in range(1,m):
        trials = singleTrial(i)
        if trials == True:
            df += 1
        else:
            df += 0
    
    if n == 23:
        theoretical = 50
    elif n == 70:
        theoretical = 99.9
    actual = round((((df)/(m))*100),1)
    print(f"The actual percentage of duplicate birthdays was {actual}% compared to the theoretical {theoretical}%")