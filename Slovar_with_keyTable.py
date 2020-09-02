original_text, key_text, text_to_code, text_to_decode= input(), input(), input(), input()

# Вариант со словарём
slovar = dict(zip(original_text, key_text))
slovar_reverse = dict(zip(key_text, original_text))
print(*[slovar.get(i) for i in text_to_code], sep='')
print(*[slovar_reverse.get(i) for i in text_to_decode], sep='')

# Можно без словаря
print(''.join(key_text[original_text.index(i)] for i in text_to_code))
print(''.join(original_text[key_text.index(i)] for i in text_to_decode))

# С помощью функции translate
print(text_to_code.translate(str.maketrans(original_text, key_text)))
print(text_to_decode.translate(str.maketrans(original_text, key_text)))