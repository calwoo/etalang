import ply.lex as lex


# token types
tokens = (
    "PLUS",
    "LPAREN",
    "RPAREN",
)

# regular expression rules
t_PLUS = r'\+'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print(f"illegal character {t.value[0]}")
    t.lexer.skip(1)

# lexer class
lexer = lex.lex()
