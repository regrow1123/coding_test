cardN, target = list(map(int, input().split(' ')))
cards = list(map(int, input().split(' ')))

optimal=0
for i in range(cardN):
    for j in range(i+1, cardN):
        for k in range(j+1, cardN):
            result = cards[i] + cards[j] + cards[k]
            if result > target:
                continue
            
            optimal = max(optimal, result)

print(optimal)

