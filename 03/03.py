import re

def task1(s):
    return 0

def task2(s):
    x = re.findall("mul\((\d+),(\d+)\)|(do\(\)|don\'t\(\))", s) 
    print(x)
    doing = "do()"
    runningsum = 0
    for i in x:
        if doing == "do()":
            try:
                runningsum += int(i[0])*int(i[1])
            except:
                pass
            finally:
                if i[2] == "don't()":
                    doing = i[2]
        elif doing == "don't()":
            if i[2] == "do()":
                doing = i[2]
        
    return runningsum
            
sum = 0
with open("input", "r") as f:
    sum += task2(f.read())
#        for i, j in x:
#            sum += int(i)*int(j)

print(sum)