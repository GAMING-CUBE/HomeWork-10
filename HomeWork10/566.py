num_rows = input()

mult = set()
char_set = {}


for char in num_rows:
   mult.add(char)
   char_set[char] = char_set.get(char, 0) + 1

print("Repeated symbols")
for char in sorted(mult):
   count = char_set[char]
   if count > 1:
       print(f"{char}: {count} count")