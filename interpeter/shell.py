from lexer import Lexer
from parse import Parser

while True:
    text = input("ShadowScript> ")

    tokenizer = Lexer(text)
    tokens = tokenizer.tokenize()

    parser = Parser(tokens)
    tree = parser.parse()

    print(tree)