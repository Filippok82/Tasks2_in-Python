# Задача 22 Напишите программу, которая принимает текст и выводит два слова: наиболее часто встречающееся и самое длинное.


import collections

text = 'lorem ipsum ooggodolor sit amet amet amet'
words = text.split()
count = collections.Counter(words)
most_common, occurrences = count.most_common()[0]

longest = max(words, key=len)

print(most_common, longest)