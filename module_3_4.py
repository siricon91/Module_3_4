def single_root_words(root_word, *other_words):
    same_words = []
    for word in other_words:
        if root_word.startswith(word) or word.startswith(root_word):
            same_words.append(word)
    return same_words


result1 = single_root_words('Камча', 'Камчатка', 'Камчадал', 'Камчатский', 'Камбала')
result2 = single_root_words('Лес', 'Лесничий', 'Лесополоса', 'Лиса', 'Леска')

print(result1)
print(result2)
