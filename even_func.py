def func(x):
    return sorted([i for i in x if i%2 == 0])

x = []
n = int(input("Enter size of list: "))
while(n!=0):
    x.append(int(input("Enter number: ")))
    n-=1
print(func(x))