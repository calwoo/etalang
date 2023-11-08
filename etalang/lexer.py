import re
import ply.lex as lex


# reserved words
reserved = {
    "use": "USE",
    "if": "IF",
    "while": "WHILE",
    "else": "ELSE",
    "return": "RETURN",
    "length": "LENGTH",
    "int": "INTTYPE",
    "bool": "BOOLTYPE",
    "true": "TRUE",
    "false": "FALSE",
}

# token types
tokens = [
    "ID",
    "INTEGER",
    "CHARACTER",
    "STRING",
    "PLUS",
    "MINUS",
    "TIMES",
    "DIVIDE",
    "NOTEQUAL",
    "EQUAL",
    "LT",
    "GT",
    "COLON",
    "SEMICOLON",
    "COMMA",
    "LPAREN",
    "RPAREN",
    "LSQBRACKET",
    "RSQBRACKET",
    "LBRACE",
    "RBRACE",
    "ERROR",
] + list(reserved.values())

# regular expression rules
t_INTEGER = r'0|-?[1-9]([0-9])*'

t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_NOTEQUAL = r'\!\='
t_EQUAL = r'\='
t_LT = r'\<'
t_GT = r'\>'
t_COLON = r'\:'
t_SEMICOLON = r'\;'
t_COMMA = r'\,'

t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LSQBRACKET = r'\['
t_RSQBRACKET = r'\]'
t_LBRACE = r'\{'
t_RBRACE = r'\}'

# comments to be discarded
def t_COMMENT(t):
    r'\/\/.*'
    pass

def t_STRING(t):
    r'\"(\\.|[^"\\])*\"'
    t.value = t.value.strip('\"')
    # # rip off all \x{y} -> \xy
    ripped_val = re.sub(r'\\x\{([0-9a-fA-F]+)\}', lambda x: r'\x' + x.group(1), t.value).encode().decode("unicode_escape")
    t.value = repr(ripped_val).strip('\'')
    return t

def t_CHARACTER(t):
    r'\'.?\''
    t.value = t.value.strip('\'')
    if len(t.value) == 0:
        t.type = "ERROR"
        t.value = "empty character literal"
    return t

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
