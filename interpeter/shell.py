from lexer import Lexer
from parse import Parser
from interpreter import Interpreter

while True:
    text = input("ShadowScript> ")

    tokenizer = Lexer(text)
    tokens = tokenizer.tokenize()

    parser = Parser(tokens)
    tree = parser.parse()

    interpreter = Interpreter(tree)
    result = interpreter.interpret()

    print(result)