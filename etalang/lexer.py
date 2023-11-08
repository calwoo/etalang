import ply.lex as lex


# reserved words
reserved = {
    "int": "INTTYPE",
    "bool": "BOOLTYPE",
}

# token types
tokens = [
    "ID",
    "INTEGER",
    "STRING",
    "PLUS",
    "EQUAL",
    "COLON",
    "COMMA",
    "LPAREN",
    "RPAREN",
    "LSQBRACKET",
    "RSQBRACKET",
    "LBRACE",
    "RBRACE",
] + list(reserved.values())

# regular expression rules
t_INTEGER = r'0|-?[1-9]([0-9])*'
# t_STRING = r'\"\\.\"'
t_STRING = r'\"(\\.|[^"\\])*\"'

t_PLUS = r'\+'
t_EQUAL = r'\='
t_COLON = r'\:'
t_COMMA = r'\,'

t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LSQBRACKET = r'\['
t_RSQBRACKET = r'\]'
t_LBRACE = r'\{'
t_RBRACE = r'\}'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, "ID")
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print(f"illegal character {t.value[0]}")
    t.lexer.skip(1)

# lexer class
lexer = lex.lex()
