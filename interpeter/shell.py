from lexer import Lexer

while True:
    text = input("ShadowScript> ")
    tokenizer = Lexer(text)
    tokens = tokenizer.tokenize()

    print(tokens)