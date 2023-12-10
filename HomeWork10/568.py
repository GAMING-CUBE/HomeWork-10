num_rows = map(int, input().split())

numbers = set()

for el in num_rows:
   if el in numbers:
       print("Yes")
   else:
       print("No")
       numbers.add(el)
