from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    title = "Welcome to Python Variable Types"
    return render_template("home.html", title=title)

@app.route("/text-sequence-type")
def text_sequence_type():
    title = "Text Sequence Type — str"
    examples = [
        {
            "description": "Textual data in Python is handled with str objects, or strings. Strings are immutable sequences of Unicode code points.",
            "code": "type('hello')",
            "output": "<class 'str'>"
        },
        {
            "description": "String literals can be written in single quotes, double quotes, or triple quotes.",
            "code": "'single quotes', \"double quotes\", '''triple quotes'''",
            "output": "'single quotes', \"double quotes\", '''triple quotes'''"
        },
        {
            "description": "Triple quoted strings may span multiple lines, and all associated whitespace will be included in the string literal.",
            "code": "'''This is a \\nmultiline string'''",
            "output": "'This is a \nmultiline string'"
        },
        {
            "description": "String literals that are part of a single expression and have only whitespace between them are implicitly concatenated.",
            "code": "(\"spam \" \"eggs\")",
            "output": "'spam eggs'"
        },
        {
            "description": "The `r` prefix disables most escape sequence processing, creating raw string literals.",
            "code": "r'C:\\\\path\\\\to\\\\file'",
            "output": "'C:\\\\path\\\\to\\\\file'"
        },
        {
            "description": "Strings may also be created from other objects using the str constructor.",
            "code": "str(123)",
            "output": "'123'"
        },
        {
            "description": "Indexing a string produces strings of length 1. For example:",
            "code": "s = 'hello'; s[0]",
            "output": "'h'"
        },
        {
            "description": "For a non-empty string, slicing a single character is equivalent to indexing.",
            "code": "s = 'hello'; s[0:1]",
            "output": "'h'"
        },
        {
            "description": "The `u` prefix is permitted on string literals for compatibility with Python 2, but it has no effect.",
            "code": "u'hello'",
            "output": "'hello'"
        },
        {
            "description": "Passing a bytes object to str() without encoding or errors arguments returns the informal string representation.",
            "code": "str(b'Zoot!')",
            "output": "\"b'Zoot!'\""
        },
        {
            "description": "The `str` constructor can create strings from bytes with encoding and error handling.",
            "code": "str(b'Zoot!', encoding='utf-8', errors='strict')",
            "output": "'Zoot!'"
        }
    ]
    return render_template("index.html", title=title, examples=examples)

@app.route("/string-methods")
def string_methods():
    title = "String Methods"
    examples = [
        {
            "description": "The `capitalize()` method returns a copy of the string with its first character capitalized and the rest lowercased.",
            "code": "'hello world'.capitalize()",
            "output": "'Hello world'"
        },
        {
            "description": "The `casefold()` method returns a casefolded copy of the string, useful for caseless matching.",
            "code": "'ß'.casefold()",
            "output": "'ss'"
        },
        {
            "description": "The `center()` method centers the string in a string of length `width`, padded with the specified `fillchar`.",
            "code": "'hello'.center(10, '-')",
            "output": "'--hello---'"
        },
        {
            "description": "The `count()` method returns the number of non-overlapping occurrences of a substring.",
            "code": "'hello world'.count('o')",
            "output": "2"
        },
        {
            "description": "The `encode()` method encodes the string to bytes using the specified encoding.",
            "code": "'hello'.encode('utf-8')",
            "output": "b'hello'"
        },
        {
            "description": "The `endswith()` method returns `True` if the string ends with the specified suffix.",
            "code": "'hello world'.endswith('world')",
            "output": "True"
        },
        {
            "description": "The `expandtabs()` method replaces all tab characters with spaces.",
            "code": "'01\\t012\\t0123'.expandtabs(4)",
            "output": "'01  012 0123'"
        },
        {
            "description": "The `find()` method returns the lowest index where the substring is found, or `-1` if not found.",
            "code": "'hello world'.find('world')",
            "output": "6"
        },
        {
            "description": "The `isalpha()` method returns `True` if all characters in the string are alphabetic.",
            "code": "'hello'.isalpha()",
            "output": "True"
        },
        {
            "description": "The `isdigit()` method returns `True` if all characters in the string are digits.",
            "code": "'12345'.isdigit()",
            "output": "True"
        },
        {
            "description": "The `islower()` method returns `True` if all cased characters in the string are lowercase.",
            "code": "'hello'.islower()",
            "output": "True"
        },
        {
            "description": "The `isspace()` method returns `True` if the string contains only whitespace characters.",
            "code": "'   '.isspace()",
            "output": "True"
        },
        {
            "description": "The `istitle()` method returns `True` if the string is titlecased.",
            "code": "'Hello World'.istitle()",
            "output": "True"
        },
        {
            "description": "The `isupper()` method returns `True` if all cased characters in the string are uppercase.",
            "code": "'HELLO'.isupper()",
            "output": "True"
        },
        {
            "description": "The `join()` method concatenates the elements of an iterable with the string as a separator.",
            "code": "'-'.join(['a', 'b', 'c'])",
            "output": "'a-b-c'"
        },
        {
            "description": "The `lower()` method returns a copy of the string with all characters converted to lowercase.",
            "code": "'HELLO'.lower()",
            "output": "'hello'"
        },
        {
            "description": "The `lstrip()` method removes leading characters from the string.",
            "code": "'   hello'.lstrip()",
            "output": "'hello'"
        },
        {
            "description": "The `partition()` method splits the string at the first occurrence of the separator.",
            "code": "'hello world'.partition(' ')",
            "output": "('hello', ' ', 'world')"
        },
        {
            "description": "The `replace()` method replaces occurrences of a substring with another substring.",
            "code": "'hello world'.replace('world', 'Python')",
            "output": "'hello Python'"
        },
        {
            "description": "The `rfind()` method returns the highest index where the substring is found, or `-1` if not found.",
            "code": "'hello world'.rfind('o')",
            "output": "7"
        },
        {
            "description": "The `split()` method splits the string into a list of substrings based on a delimiter.",
            "code": "'a,b,c'.split(',')",
            "output": "['a', 'b', 'c']"
        },
        {
            "description": "The `startswith()` method returns `True` if the string starts with the specified prefix.",
            "code": "'hello world'.startswith('hello')",
            "output": "True"
        },
        {
            "description": "The `strip()` method removes leading and trailing characters from the string.",
            "code": "'   hello   '.strip()",
            "output": "'hello'"
        },
        {
            "description": "The `swapcase()` method returns a copy of the string with uppercase characters converted to lowercase and vice versa.",
            "code": "'Hello World'.swapcase()",
            "output": "'hELLO wORLD'"
        },
        {
            "description": "The `title()` method returns a titlecased version of the string.",
            "code": "'hello world'.title()",
            "output": "'Hello World'"
        },
        {
            "description": "The `upper()` method returns a copy of the string with all characters converted to uppercase.",
            "code": "'hello'.upper()",
            "output": "'HELLO'"
        },
        {
            "description": "The `zfill()` method pads the string with zeros on the left to fill the specified width.",
            "code": "'42'.zfill(5)",
            "output": "'00042'"
        }
    ]
    return render_template("index.html", title=title, examples=examples)

@app.route("/f-strings")
def f_strings():
    title = "F-Strings"
    examples = [
        {
            "description": "F-strings provide a way to embed expressions inside string literals, using curly braces.",
            "code": "name = 'World'; f'Hello, {name}!'",
            "output": "'Hello, World!'"
        },
        {
            "description": "F-strings can include expressions directly.",
            "code": "f'{2 + 2}'",
            "output": "'4'"
        },
        {
            "description": "F-strings support debugging by including the expression text and its value using the `=` sign.",
            "code": "name = 'Alice'; f'{name=}'",
            "output": "'name=Alice'"
        },
        {
            "description": "F-strings support formatting with nested fields.",
            "code": "value = 12.34567; f'result: {value:.2f}'",
            "output": "'result: 12.35'"
        },
        {
            "description": "F-strings support date formatting using the `datetime` module.",
            "code": "from datetime import datetime; today = datetime(2025, 4, 7); f'{today:%B %d, %Y}'",
            "output": "'April 07, 2025'"
        },
        {
            "description": "F-strings support integer formatting with prefixes.",
            "code": "number = 1024; f'{number:#0x}'",
            "output": "'0x400'"
        },
        {
            "description": "F-strings preserve whitespace around expressions when using the `=` sign.",
            "code": "foo = 'bar'; f'{ foo = }'",
            "output": "' foo = bar'"
        },
        {
            "description": "F-strings allow using `repr()` for debugging with `!r`.",
            "code": "line = \"The mill's closed\"; f'{line = !r}'",
            "output": "'line = \"The mill\\'s closed\"'"
        },
        {
            "description": "F-strings allow backslashes inside replacement fields.",
            "code": "a = ['a', 'b', 'c']; f'List a contains:\\n{\\n.join(a)}'",
            "output": "'List a contains:\\na\\nb\\nc'"
        },
        {
            "description": "F-strings support reusing the same quoting type inside replacement fields.",
            "code": "a = {'x': 2}; f'abc {a[\"x\"]} def'",
            "output": "'abc 2 def'"
        }
    ]
    return render_template("index.html", title=title, examples=examples)

@app.route("/format-string-syntax")
def format_string_syntax():
    title = "Format String Syntax"
    examples = [
        {
            "description": "The `format()` method allows you to format strings using placeholders.",
            "code": "'Hello, {}!'.format('World')",
            "output": "'Hello, World!'"
        },
        {
            "description": "You can use positional arguments in the `format()` method.",
            "code": "'{1} {0}'.format('World', 'Hello')",
            "output": "'Hello World'"
        },
        {
            "description": "You can use named arguments in the `format()` method.",
            "code": "'My quest is {name}'.format(name='finding the Holy Grail')",
            "output": "'My quest is finding the Holy Grail'"
        },
        {
            "description": "You can access object attributes using the `format()` method.",
            "code": "class Obj: weight = 42; 'Weight in tons {0.weight}'.format(Obj)",
            "output": "'Weight in tons 42'"
        },
        {
            "description": "You can access dictionary elements using the `format()` method.",
            "code": "players = ['Arthur', 'Lancelot']; 'Units destroyed: {players[0]}'.format(players=players)",
            "output": "'Units destroyed: Arthur'"
        },
        {
            "description": "The `!s` conversion flag calls `str()` on the value before formatting.",
            "code": "'Harold's a clever {0!s}'.format('knight')",
            "output": "'Harold's a clever knight'"
        },
        {
            "description": "The `!r` conversion flag calls `repr()` on the value before formatting.",
            "code": "'Bring out the holy {name!r}'.format(name='Grail')",
            "output": "'Bring out the holy 'Grail''"
        },
        {
            "description": "The `!a` conversion flag calls `ascii()` on the value before formatting.",
            "code": "'More {!a}'.format('café')",
            "output": "'More caf\\xe9'"
        },
        {
            "description": "You can specify field width, alignment, and padding using the `format()` method.",
            "code": "'{:>10}'.format('test')",
            "output": "'      test'"
        },
        {
            "description": "You can specify decimal precision using the `format()` method.",
            "code": "'{:.2f}'.format(3.14159)",
            "output": "'3.14'"
        },
        {
            "description": "You can use nested replacement fields in the `format()` method.",
            "code": "width = 10; '{:{width}}'.format('test', width=width)",
            "output": "'      test'"
        }
    ]
    return render_template("index.html", title=title, examples=examples)

@app.route("/print-style-formatting")
def print_style_formatting():
    title = "Print-F Style String Formatting"
    examples = [
        {
            "description": "The `%` operator can be used for string formatting.",
            "code": "'Hello, %s!' % 'World'",
            "output": "'Hello, World!'"
        },
        {
            "description": "You can format numbers using `%`.",
            "code": "'%d + %d = %d' % (2, 3, 5)",
            "output": "'2 + 3 = 5'"
        },
        {
            "description": "You can use dictionaries for mapping keys in the format string.",
            "code": "'%(language)s has %(number)03d quote types.' % {'language': 'Python', 'number': 2}",
            "output": "'Python has 002 quote types.'"
        },
        {
            "description": "The `#` flag adds alternate forms for octal and hexadecimal values.",
            "code": "'Octal: %#o, Hex: %#x' % (10, 255)",
            "output": "'Octal: 0o12, Hex: 0xff'"
        },
        {
            "description": "The `0` flag pads numeric values with zeros.",
            "code": "'%05d' % 42",
            "output": "'00042'"
        },
        {
            "description": "The `-` flag left-aligns the result.",
            "code": "'%-10s' % 'left'",
            "output": "'left      '"
        },
        {
            "description": "The `+` flag adds a sign character to numeric values.",
            "code": "'%+d' % 42",
            "output": "'+42'"
        },
        {
            "description": "The `.` precision specifies the number of digits after the decimal point for floating-point numbers.",
            "code": "'%.2f' % 3.14159",
            "output": "'3.14'"
        },
        {
            "description": "The `%` character can be escaped by using `%%`.",
            "code": "'Discount: 50%% off!'",
            "output": "'Discount: 50% off!'"
        }
    ]
    return render_template("print_style_formatting.html", title=title, examples=examples)

@app.route("/python-variable-types")
def python_variable_types():
    title = "Python Variable Types"
    examples = [
        # Numbers Section
        {
            "section": "Numbers",
            "description": "Basic arithmetic operations.",
            "code": "2 + 2\n50 - 5 * 6\n(50 - 5 * 6) / 4\n8 / 5",
            "output": "4\n20\n5.0\n1.6"
        },
        {
            "section": "Numbers",
            "description": "Floor division and modulus.",
            "code": "17 / 3\n17 // 3\n17 % 3\n5 * 3 + 2",
            "output": "5.666666666666667\n5\n2\n17"
        },
        {
            "section": "Numbers",
            "description": "Exponentiation.",
            "code": "5 ** 2\n2 ** 7",
            "output": "25\n128"
        },
        {
            "section": "Numbers",
            "description": "Variable assignment and usage.",
            "code": "width = 20\nheight = 5 * 9\nwidth * height",
            "output": "900"
        },
        {
            "section": "Numbers",
            "description": "Floating-point operations.",
            "code": "4 * 3.75 - 1",
            "output": "14.0"
        },
        {
            "section": "Numbers",
            "description": "Using the `_` variable for the last result.",
            "code": "tax = 12.5 / 100\nprice = 100.50\nprice * tax\nprice + _\nround(_, 2)",
            "output": "12.5625\n113.0625\n113.06"
        },
        # Text Section
        {
            "section": "Text",
            "description": "String literals with single and double quotes.",
            "code": "'spam eggs'\n\"Paris rabbit got your back :)! Yay!\"",
            "output": "'spam eggs'\n'Paris rabbit got your back :)! Yay!'"
        },
        {
            "section": "Text",
            "description": "Escaping quotes in strings.",
            "code": "'doesn\\'t'\n\"doesn't\"\n'\"Yes,\" they said.'\n\"\\\"Yes,\\\" they said.\"",
            "output": "\"doesn't\"\n\"doesn't\"\n'\"Yes,\" they said.'\n'\"Yes,\" they said.'"
        },
        {
            "section": "Text",
            "description": "Using raw strings to avoid escape sequences.",
            "code": "print('C:\\\\some\\\\name')\nprint(r'C:\\\\some\\\\name')",
            "output": "C:\\some\\name\nC:\\some\\name"
        },
        {
            "section": "Text",
            "description": "String concatenation and repetition.",
            "code": "3 * 'un' + 'ium'\n'Py' 'thon'",
            "output": "'unununium'\n'Python'"
        },
        {
            "section": "Text",
            "description": "String slicing.",
            "code": "word = 'Python'\nword[0:2]\nword[2:5]\nword[:2]\nword[4:]\nword[-2:]",
            "output": "'Py'\n'tho'\n'Py'\n'on'\n'on'"
        },
        {
            "section": "Text",
            "description": "String immutability.",
            "code": "word = 'Python'\n'J' + word[1:]\nword[:2] + 'py'",
            "output": "'Jython'\n'Pypy'"
        },
        {
            "section": "Text",
            "description": "Getting the length of a string.",
            "code": "s = 'supercalifragilisticexpialidocious'\nlen(s)",
            "output": "34"
        },
        # Lists Section
        {
            "section": "Lists",
            "description": "Create a list of squares.",
            "code": "squares = [1, 4, 9, 16, 25]\nprint(squares)",
            "output": "[1, 4, 9, 16, 25]"
        },
        {
            "section": "Lists",
            "description": "Indexing a list.",
            "code": "squares = [1, 4, 9, 16, 25]\nprint(squares[0])\nprint(squares[-1])",
            "output": "1\n25"
        },
        {
            "section": "Lists",
            "description": "Slicing a list.",
            "code": "squares = [1, 4, 9, 16, 25]\nprint(squares[-3:])",
            "output": "[9, 16, 25]"
        },
        {
            "section": "Lists",
            "description": "Concatenating lists.",
            "code": "squares = [1, 4, 9, 16, 25]\nprint(squares + [36, 49, 64, 81, 100])",
            "output": "[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]"
        },
        {
            "section": "Lists",
            "description": "Modifying a list.",
            "code": "cubes = [1, 8, 27, 65, 125]\ncubes[3] = 64\nprint(cubes)",
            "output": "[1, 8, 27, 64, 125]"
        },
        {
            "section": "Lists",
            "description": "Appending to a list.",
            "code": "cubes = [1, 8, 27, 64, 125]\ncubes.append(216)\ncubes.append(7 ** 3)\nprint(cubes)",
            "output": "[1, 8, 27, 64, 125, 216, 343]"
        },
        {
            "section": "Lists",
            "description": "List assignment does not copy data.",
            "code": "rgb = ['Red', 'Green', 'Blue']\nrgba = rgb\nrgba.append('Alph')\nprint(rgb)",
            "output": "['Red', 'Green', 'Blue', 'Alph']"
        },
        {
            "section": "Lists",
            "description": "Slicing creates a shallow copy.",
            "code": "rgba = ['Red', 'Green', 'Blue', 'Alph']\ncorrect_rgba = rgba[:]\ncorrect_rgba[-1] = 'Alpha'\nprint(correct_rgba)\nprint(rgba)",
            "output": "['Red', 'Green', 'Blue', 'Alpha']\n['Red', 'Green', 'Blue', 'Alph']"
        },
        {
            "section": "Lists",
            "description": "Assignment to slices.",
            "code": "letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']\nletters[2:5] = ['C', 'D', 'E']\nprint(letters)\nletters[2:5] = []\nprint(letters)\nletters[:] = []\nprint(letters)",
            "output": "['a', 'b', 'C', 'D', 'E', 'f', 'g']\n['a', 'b', 'f', 'g']\n[]"
        },
        {
            "section": "Lists",
            "description": "Using len() with lists.",
            "code": "letters = ['a', 'b', 'c', 'd']\nprint(len(letters))",
            "output": "4"
        },
        {
            "section": "Lists",
            "description": "Nesting lists.",
            "code": "a = ['a', 'b', 'c']\nn = [1, 2, 3]\nx = [a, n]\nprint(x)\nprint(x[0])\nprint(x[0][1])",
            "output": "[['a', 'b', 'c'], [1, 2, 3]]\n['a', 'b', 'c']\n'b'"
        }
    ]
    return render_template("index.html", title=title, examples=examples)

if __name__ == "__main__":
    app.run(debug=True)