# ruby_lexer.py
import ply.lex as lex

# Definir estados del lexer
states = (
    ('comment', 'exclusive'),
)

# Palabras reservadas de Ruby
reserved = {
    "alias":   "ALIAS",
    "and":     "AND",
    "break":   "BREAK",
    "case":    "CASE",
    "class":   "CLASS",
    "def":     "DEF",
    "defined?":"DEFINED",
    "do":      "DO",
    "else":    "ELSE",
    "elsif":   "ELSIF",
    "end":     "END",
    "ensure":  "ENSURE",
    "false":   "FALSE",
    "true":    "TRUE",
    "for":     "FOR",
    "if":      "IF",
    "in":      "IN",
    "module":  "MODULE",
    "next":    "NEXT",
    "nil":     "NIL",
    "not":     "NOT",
    "or":      "OR",
    "redo":    "REDO",
    "rescue":  "RESCUE",
    "retry":   "RETRY",
    "return":  "RETURN",
    "self":    "SELF",
    "super":   "SUPER",
    "then":    "THEN",
    "undef":   "UNDEF",
    "unless":  "UNLESS",
    "until":   "UNTIL",
    "when":    "WHEN",
    "while":   "WHILE",
    "yield":   "YIELD",
    "_FILE_":  "_FILE_",
    "_LINE_":  "_LINE_",
    "gets": "GETS",
}

tokens = (
    # literales
    'NUMBER',
    'STRING',
    'ID',

    # operadores aritméticos
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'MOD',
    'EXP',

    # operadores relacionales
    'IGUAL',
    'MAYORQ',
    'MENORQ',
    'MAYORIG',
    'MENORIG',
    'DIFERENTE',

    # delimitadores
    'LPAR',
    'RPAR',
    'LCOR',
    'RCOR',
    'LKEY',
    'RKEY',
    'PTO',
    'COMA',
    'SEMICOLON',

    # operadores lógicos
    'AND',
    'OR',
    'NOT',
    'AND_OP',
    'OR_OP',
    'NOT_OP',

    #asignacion
    'ASIG',
    'MASIG',

    # otros
    'NEWLINE',
    'LEXICAL_ERROR',
) + tuple(reserved.values())

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# ===== Operadores (orden importante: primero los más largos) =====

t_EXP       = r'\*\*'
t_MAYORIG   = r'>='
t_MENORIG   = r'<='
t_DIFERENTE = r'!='

t_PLUS      = r'\+'
t_MINUS     = r'-'
t_TIMES     = r'\*'
t_DIVIDE    = r'/'
t_MOD       = r'%'
t_IGUAL     = r'=='
t_MAYORQ    = r'>'
t_MENORQ    = r'<'

t_LPAR      = r'\('
t_RPAR      = r'\)'
t_LCOR      = r'\['
t_RCOR      = r'\]'
t_LKEY      = r'\{'
t_RKEY      = r'\}'
t_PTO       = r'\.'
t_COMA      = r','
t_SEMICOLON = r';'

t_AND_OP      = r'&&'
t_OR_OP        = r'\|\|'
t_NOT_OP     = r'!'

t_MASIG = r'\+='
t_ASIG = r'='

# ===== Tokens complejos =====

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    if '.' in t.value:
        t.value = float(t.value)
    else:
        t.value = int(t.value)
    return t

def t_STRING(t):
    r'(\"([^\\\n]|(\\.))*\"|\'([^\\\n]|(\\.))*\')'
    t.value = t.value[1:-1]  # quitar comillas
    return t

def t_ID(t):
    r'[A-Za-z_][A-Za-z0-9_]*\??'
    if t.value in reserved:
        t.type = reserved[t.value]
    return t

def t_COMMENT(t):
    r'\#.*'
    pass

# ===== Comentarios multilínea: =begin ... =end =====

def t_MLCOMMENT_START(t):
    r'\s*=begin'
    t.lexer.begin('comment')

# Dentro del estado 'comment' ignoramos todo hasta '=end'

def t_comment_end(t):
    r'=end'
    t.lexer.begin('INITIAL')

def t_comment_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_comment_ignore = ' \t'

def t_comment_any(t):
    r'.'
    pass


def t_comment_error(t):
    t.lexer.skip(1)


def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t

def t_error(t):
    mensaje = f"Caracter ilegal '{t.value[0]}' en la línea {t.lineno}"
    t.lexer.errors.append((t.lineno, t.value[0], mensaje))
    t.type = 'LEXICAL_ERROR'
    t.value = t.value[0]
    t.lexer.skip(1)
    return t

def construir_lexer():
    lexer = lex.lex()
    lexer.errors = []
    return lexer