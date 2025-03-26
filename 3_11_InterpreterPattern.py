
'''
Interpreter Pattern
- The Interpreter Pattern is implemented by defining a grammar for interpreting a language and providing an interpreter to parse the grammar.
- The Interpreter Pattern is used when you want to interpret a language or need to parse complex expressions.'''


class AbstractExpression():
    "All Terminal and Non-Terminal expressions will implement an `interpret` method"
    @staticmethod
    def interpret():
        """
        The `interpret` method gets called recursively for each
        AbstractExpression
        """

class Number(AbstractExpression):
    "Terminal Expression"

    def __init__(self, value):
        self.value = int(value)

    def interpret(self):
        return self.value

    def __repr__(self):
        return str(self.value)

class Add(AbstractExpression):
    "Non-Terminal Expression."

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() + self.right.interpret()

    def __repr__(self):
        return f"({self.left} Add {self.right})"

class Subtract(AbstractExpression):
    "Non-Terminal Expression"

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() - self.right.interpret()

    def __repr__(self):
        return f"({self.left} Subtract {self.right})"

# The Client
# The sentence complies with a simple grammar of
# Number -> Operator -> Number -> etc,
SENTENCE = "5 + 4 - 3 + 7 - 2"
print(SENTENCE)

# Split the sentence into individual expressions that will be added to
# an Abstract Syntax Tree (AST) as Terminal and Non-Terminal expressions
TOKENS = SENTENCE.split(" ")
print(TOKENS)

# Manually Creating an Abstract Syntax Tree from the tokens
AST: list[AbstractExpression] = []
# AST = []  # Python 3.8 or earlier
AST.append(Add(Number(TOKENS[0]), Number(TOKENS[2])))  # 5 + 4
AST.append(Subtract(AST[0], Number(TOKENS[4])))        # ^ - 3
AST.append(Add(AST[1], Number(TOKENS[6])))             # ^ + 7
AST.append(Subtract(AST[2], Number(TOKENS[8])))        # ^ - 2

# Use the final AST row as the root node.
AST_ROOT = AST.pop()

# Interpret recursively through the full AST starting from the root.
print(AST_ROOT.interpret())

# Print out a representation of the AST_ROOT
print(AST_ROOT)


''' 
    How It Works:

Tokenization:
The input string is split into tokens representing numbers and operators.

AST Construction:
The tokens are used to manually construct an Abstract Syntax Tree (AST) with terminal and non-terminal expressions.

Recursive Interpretation:
The interpret method is called on the root of the AST.
This method recursively evaluates the tree by calling interpret on the left and right subtrees.

Result:
The final result of the expression is returned by the root's interpret method.

    Use Cases:
Parsing and evaluating mathematical expressions.
Compilers and interpreters for programming languages.
Rule engines and configuration file parsers.
Query languages (e.g., SQL, XPath).
This implementation provides a clean and extensible way to interpret expressions in a custom language or grammar.'''