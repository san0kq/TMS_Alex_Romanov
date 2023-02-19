import timeit

new_string = input('Введите предложение из двух слов (разделённые пробелом): ')

word_1, word_2 = new_string.split(' ')

print('!{word_2} ! {word_1}!'.format(word_1=word_1, word_2=word_2))
print(f'!{word_2} ! {word_1}!')

# f-string 5 times faster than .format()
print(timeit.timeit(
    "'!{word_2} ! {word_1}!'.format(word_1=word_1, word_2=word_2)",
    globals=globals()
))
print(timeit.timeit("f'!{word_2} ! {word_1}!'", globals=globals()))
