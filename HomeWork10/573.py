n = 35
multiplier = set()
while True:
   print('Type "q-" to quit ')
   an_input = input("Enter a sentence: ")
   if an_input == "q-":
       break
   for i in an_input.split():
       multiplier.add(i)

print(f"{len(multiplier) }")
