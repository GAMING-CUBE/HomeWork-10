words = input().lower().split()
multiplier = {}

for h in words:
   multiplier[h] = multiplier.get(h, 0) + 1
print(multiplier)

