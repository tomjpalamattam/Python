# find maximum
numbers = [3,6,2,8,4,10]
length=len(numbers)
for x in range(1,length,1):
    if numbers[x] > numbers[x-1]:
        max = numbers[x]
print(f"max is {max}")
