a = "abc,abc,bac,aca"

word = a.split(',')

word_a = sorted(set(word))
result = ','.join(word_a)

print(result)
