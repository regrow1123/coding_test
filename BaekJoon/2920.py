numbers=list(map(int,input().split(' ')))
#print(numbers)

ascending=True
descending=True
for i in range(1,len(numbers)):
    if numbers[i-1] > numbers[i]:
        ascending=False
    if numbers[i-1] < numbers[i]:
        descending=False

if ascending:
    print('ascending')
elif descending:
    print('descending')
else:
    print('mixed')

