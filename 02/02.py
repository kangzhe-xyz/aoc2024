from copy import deepcopy

def task1(lst):
    differences = [lst[i]-lst[i-1] for i in range(1, len(lst))]
    if 0 in differences:
        return False
    posdiff = True if (lst[1] - lst[0]) > 0 else False
    negdiff = True if (lst[1] - lst[0]) < 0 else False
    
    # check magnitude
    for i in differences:
        if i > 3:
            return False
        if i < -3:
            return False
        
    # check sign
    for i in differences:
        if (posdiff and -1 * i > 0) or (negdiff and -1 * i < 0):
            return False
    return True

def task2(lst):
    if task1(lst):
        return True
    else:
        for i in range(len(lst)):
            modlist = deepcopy(lst)
            modlist.pop(i)
            if task1(modlist):
                return True
            else: 
                continue
    return False
                
f = open("input", "r")
task1sol = 0
task2sol = 0
for i in f:
    lst = [int(a) for a in i.split()]
    task1sol += task1(lst)
    task2sol += task2(lst)
    
print(f"Task 1: {task1sol}, Task 2: {task2sol}")
    