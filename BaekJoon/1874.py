numbers=[i+1 for i in reversed(range(int(input())))]
stacked=[]

while(numbers or stacked): 
    n=int(input())
    if numbers and n > numbers[-1]:
        diff=n-numbers[-1]+1
        for i in range(diff):
            stacked.append(numbers.pop())
            print('+')
        stacked.pop()
        print('-')
    elif stacked and stacked[-1] >= n:
        diff=stacked[-1]-n+1
        for i in range(diff):
            stacked.pop()
            print('-')
    else:
        print('NO')
        exit()

