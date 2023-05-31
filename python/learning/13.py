num = str(input("Enter the number:"))
t1=len(num)
for item in range(0,t1,1):
    if num[item] == '1':
        print('One ')
    elif num[item] == '2':
        print("two ")
    elif num[item] == '3':
        print("three ")
    elif num[item] == '4':
        print("four ")
    elif num[item] == '5':
        print("five ")
    elif num[item] == '6':
        print("six ")
    elif num[item] == '7':
        print("seven ")
    elif num[item] == '8':
        print("eight ")
    elif num[item] == '9':
        print("nine ")
    elif num[item] == '0':
        print("zero ")
    else:
        break
