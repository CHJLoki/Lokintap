def sumStartToEnd(start,end):
    sum = 0
    for n in range(start,end+1):
        sum = sum + n
    return sum
print(sumStartToEnd(1,100))
