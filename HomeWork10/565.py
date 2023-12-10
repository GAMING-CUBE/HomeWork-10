num_rows = int(input())

words = set()
word_counter = {}

for i in range(num_rows):
   words_input = input().split()
   words.update(words_input)
   for w in words_input:
       word_counter[w] = word_counter.get(w, 0) + 1

max_count = max(word_counter.values())
most_words = { word for word, count in word_counter.items() if count == max_count}

print(sorted(most_words)[0])