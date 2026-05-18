from deep_translator import GoogleTranslator

text = input("翻訳したい文章: ")

translated = GoogleTranslator(
    source='ja',
    target='cs'
).translate(text)

print("\n翻訳結果:")
print(translated)