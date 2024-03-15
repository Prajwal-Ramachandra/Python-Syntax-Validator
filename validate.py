import ply.lex as lex
import ply.yacc as yacc
tokens = (
'FUNCTION',
'IDENTIFIER',
'LPAREN',
'RPAREN',
'LBRACE',
'RBRACE',
'LBRACKET',
'RBRACKET',
'STRING',
'NUMBER',
'COLON',
'COMMA',
'ASSIGN'
)
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMA = r','
t_COLON = r':'
t_STRING = r"'[^']*'"
t_IDENTIFIER = r"[a-zA-Z_][a-zA-Z0-9_]*"
t_NUMBER = r'-?\d+(\.\d+)?'
t_ASSIGN = r'='
def t_FUNCTION(t):
r'def'
return t
t_ignore = ' \t\n'
def t_error(t):
print(f"Illegal character: {t.value[0]}")
t.lexer.skip(1)
lexer = lex.lex()
def p_statement(p):
'''
statement : list
| tuple
| dictionary
| function_declaration
| slice_expression
'''
p[0] = p[1]
# Grammar rules for list constructs
def p_list(p):
'''
list : LBRACKET elements RBRACKET
| LBRACKET RBRACKET
'''
p[0] = p[2]
if len(p) == 3:
p[0] = 'Valid Python list statement'
else:
p[0] = 'Valid Python list statement'
def p_tuple(p):
'''
tuple : LPAREN element COMMA elements RPAREN
| LPAREN RPAREN
| LPAREN element COMMA RPAREN
'''
p[0] = p[2]
if len(p) == 3:
p[0] = 'Valid Python tuple statement'
else:
p[0] = 'Valid Python tuple statement'
def p_elements(p):
'''
elements : element
| elements COMMA element
'''
if len(p) == 2:
p[0] = [p[1]]
else:
p[0] = p[1] + [p[3]]
def p_element(p):
'''
element : STRING
| NUMBER
| IDENTIFIER
| list
| tuple
'''
p[0] = p[1]
def p_dictionary(p):
'''
dictionary : LBRACE RBRACE
| LBRACE eles RBRACE
'''
if len(p) == 3:
p[0] = {}
else:
p[0] = dict(p[2])
if len(p) == 3:
print('Valid Python dictionary statement')
else:
print('Valid Python dictionary statement')
def p_eles(p):
'''
eles : ele
| eles COMMA ele
'''
p[0] = p[1] if len(p) == 2 else p[1].update(p[3]) or p[1]
def p_ele(p):
'''
ele : NUMBER COLON NUMBER
| NUMBER COLON STRING
| NUMBER COLON list
| NUMBER COLON tuple
| NUMBER COLON dictionary
| STRING COLON NUMBER
| STRING COLON STRING
| STRING COLON list
| STRING COLON tuple
| STRING COLON dictionary
| IDENTIFIER COLON STRING
| IDENTIFIER COLON NUMBER
| IDENTIFIER COLON IDENTIFIER
| IDENTIFIER COLON list
| IDENTIFIER COLON tuple
| IDENTIFIER COLON dictionary
| NUMBER COLON IDENTIFIER
| STRING COLON IDENTIFIER
| tuple COLON NUMBER
| tuple COLON STRING
| tuple COLON IDENTIFIER
| tuple COLON list
| tuple COLON tuple
| tuple COLON dictionary
'''
p[0] = {p[1]: p[3]}
def p_function_declaration(p):
'''
function_declaration : FUNCTION IDENTIFIER LPAREN argument_list RPAREN
COLON
| FUNCTION IDENTIFIER LPAREN RPAREN COLON
'''
print("Valid Python function declaration")
def p_argument_list(p):
'''
argument_list : argument
| argument_list COMMA argument
'''
def p_argument(p):
'''
argument : IDENTIFIER
| IDENTIFIER ASSIGN IDENTIFIER
| IDENTIFIER ASSIGN NUMBER
| IDENTIFIER ASSIGN STRING
| IDENTIFIER ASSIGN list
| IDENTIFIER ASSIGN tuple
| IDENTIFIER ASSIGN dictionary
'''
def p_slice_expression(p):
'''
slice_expression : IDENTIFIER LBRACKET NUMBER COLON NUMBER RBRACKET
| IDENTIFIER LBRACKET NUMBER RBRACKET
| STRING LBRACKET NUMBER RBRACKET
| STRING LBRACKET NUMBER COLON NUMBER RBRACKET
'''
p[0] = f'Correct syntax for string slicing: {p[1]}[{p[3]}:{p[5]}]'
# Error handling
def p_error(p):
if p:
print(f"Syntax error at line {p.lineno}, position {p.lexpos}:
Unexpected token '{p.value}'")
else:
print("Syntax error at EOF")
# Build the parser
parser = yacc.yacc()
while True:
input_string = ""
print("Enter your Python statement (type 'done' on a new line to
finish):")
while True:
line = input()
if line.strip() == 'done':
break
input_string += line + "\n"
if input_string.strip():
result = parser.parse(input_string)
print(result)
else:
print("No input provided or empty input, exiting.")
break
