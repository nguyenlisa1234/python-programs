# Exercise 1: Weighted Averages

def weightedAverage(list1,list2):
    if len(list1) != len(list2):
        print("Each value should have one weight! ")
    elif len(list1) == len(list2):
        total = 0
        for i in range(len(list1)):
            total += list1[i]*list2[i] 
        return total
weightedAverage([50,40,45],[0.2,0.3,0.5])