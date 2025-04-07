import datetime
import decimal

# Text Sequence Type — str
print("Text Sequence Type — str Examples:")
print(type('hello'))  # Example 1

single_quotes = 'single quotes'
double_quotes = "double quotes"
triple_quotes = '''triple quotes'''
print(single_quotes)  # Example 2
print(double_quotes)
print(triple_quotes)

multiline_string = '''This is a 
multiline string'''
print(multiline_string)  # Example 3

concatenated_string = ("spam " "eggs")
print(concatenated_string)  # Example 4

raw_string = r'C:\\path\\to\\file'
print(raw_string)  # Example 5

converted_string = str(123)
print(converted_string)  # Example 6

s = 'hello'
print(s[0])  # Example 7
print(s[0:1])  # Example 8

unicode_string = u'hello'
print(unicode_string)  # Example 9

bytes_to_string = str(b'Zoot!')
print(bytes_to_string)  # Example 10

bytes_with_encoding = str(b'Zoot!', encoding='utf-8', errors='strict')
print(bytes_with_encoding)  # Example 11

print("-" * 50)

# String Methods
print("String Methods Examples:")
print('hello world'.capitalize())  # Example 1
print('ß'.casefold())  # Example 2
print('hello'.center(10, '-'))  # Example 3
print('hello world'.count('o'))  # Example 4
print('hello'.encode('utf-8'))  # Example 5
print('hello world'.endswith('world'))  # Example 6
print('01\t012\t0123'.expandtabs(4))  # Example 7
print('hello world'.find('world'))  # Example 8
print('hello'.isalpha())  # Example 9
print('12345'.isdigit())  # Example 10
print('hello'.islower())  # Example 11
print('   '.isspace())  # Example 12
print('Hello World'.istitle())  # Example 13
print('HELLO'.isupper())  # Example 14
print('-'.join(['a', 'b', 'c']))  # Example 15
print('HELLO'.lower())  # Example 16
print('   hello'.lstrip())  # Example 17
print('hello world'.partition(' '))  # Example 18
print('hello world'.replace('world', 'Python'))  # Example 19
print('hello world'.rfind('o'))  # Example 20
print('a,b,c'.split(','))  # Example 21
print('hello world'.startswith('hello'))  # Example 22
print('   hello   '.strip())  # Example 23
print('Hello World'.swapcase())  # Example 24
print('hello world'.title())  # Example 25
print('hello'.upper())  # Example 26
print('42'.zfill(5))  # Example 27

print("-" * 50)

# F-Strings
print("F-Strings Examples:")
name = 'World'
print(f'Hello, {name}!')  # Example 1

print(f'{2 + 2}')  # Example 2

name = 'Alice'
print(f'{name=}')  # Example 3

value = 12.34567
print(f'result: {value:.2f}')  # Example 4

today = datetime.datetime(2025, 4, 7)
print(f'{today:%B %d, %Y}')  # Example 5

number = 1024
print(f'{number:#0x}')  # Example 6

foo = 'bar'
print(f'{ foo = }')  # Example 7

line = "The mill's closed"
print(f'{line = !r}')  # Example 8


a = ['a', 'b', 'c']
print(f'List a contains:\n{"\n".join(a)}')  # Example 10

a = {'x': 2}
print(f'abc {a["x"]} def')  # Example 11

print("-" * 50)

# Format String Syntax
print("Format String Syntax Examples:")
print('Hello, {}!'.format('World'))  # Example 1
print('{1} {0}'.format('World', 'Hello'))  # Example 2
print('My quest is {name}'.format(name='finding the Holy Grail'))  # Example 3

class Obj:
    weight = 42

print('Weight in tons {0.weight}'.format(Obj))  # Example 4

players = ['Arthur', 'Lancelot']
print('Units destroyed: {players[0]}'.format(players=players))  # Example 5

print('Harold\'s a clever {0!s}'.format('knight'))  # Example 6
print('Bring out the holy {name!r}'.format(name='Grail'))  # Example 7
print('More {!a}'.format('café'))  # Example 8
print('{:>10}'.format('test'))  # Example 9
print('{:.2f}'.format(3.14159))  # Example 10

width = 10
print('{:{width}}'.format('test', width=width))  # Example 11

print("-" * 50)

# Print-F Style String Formatting
print("Print-F Style String Formatting Examples:")
print('Hello, %s!' % 'World')  # Example 1
print('%d + %d = %d' % (2, 3, 5))  # Example 2
print('%(language)s has %(number)03d quote types.' % {'language': 'Python', 'number': 2})  # Example 3
print('Octal: %#o, Hex: %#x' % (10, 255))  # Example 4
print('%05d' % 42)  # Example 5
print('%-10s' % 'left')  # Example 6
print('%+d' % 42)  # Example 7
print('%.2f' % 3.14159)  # Example 8
print('Discount: 50%% off!')  # Example 9

print("-" * 50)