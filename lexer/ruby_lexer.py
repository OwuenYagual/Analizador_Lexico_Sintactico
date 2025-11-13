import ply.lex as lex

reserved = {
            "alias":"ALIAS",
            "and": "AND",
            "break": "BREAK",
            "case": "CASE",
            "class": "CLASS",
            "def": "DEF",
            "defined?": "DEFINED?",
            "do": "DO",
            "else": "ELSE",
            "elsif":"ELSIF",
            "end":"END",
            "ensure":"ENSURE",
            "false":"FALSE",
            "true":"TRUE",
            "for":"FOR",
            "if":"PUTS",
            "in":"PUTS",
            "module":"PUTS",
            "next":"PUTS",
            "nil":"PUTS",
            "not":"PUTS",
            "or":"PUTS",
            "redo":"PUTS",
            "rescue":"PUTS",
            "retry":"PUTS",
            "return":"PUTS",
            "self":"PUTS",
            "super":"PUTS",
            "then":"PUTS",
            "undef":"PUTS",
            "unless":"PUTS",
            "until":"PUTS",
            "when":"PUTS",
            "while":"PUTS",
            "yield":"PUTS",
            "_FILE_":"PUTS",
            "_LINE_":"PUTS",
}



tokens = (
   'NUMBER',
   'PLUS',
   'MINUS',
   'TIMES',
   'DIVIDE',
    'MOD',
    'EXP',
    'IGUAL',
    'MAYORQ',
    'MENORQ',
    'MAYORIG',
    'MENORIG',
    'DIFERENTE',
    'LPAR',
    'RPAR',
    'LCOR',
    'RCOR',
    'LKEY',
    'RKEY',
    'PTO',
    'COMA',
    'SEMICOLON',
    'AND',
    'OR',
    'NOT'
    

)+ tuple(reserved.values())



t_PLUS     = r'\+'
t_MINUS    = r'-'
t_TIMES    = r'\*'
t_DIVIDE   = r'/'
t_MOD      = r'%'
t_EXP      = r'\*\*'
t_IGUAL = r'=='
t_MAYORQ = r'>'
t_MENORQ = r'<'
t_MAYORIG = r'>='
t_MENORIG = r'<='
t_DIFERENTE = r'!='
t_LPAR  = r'\('
t_RPAR  = r'\)'
t_LCOR  = r'\['
t_RCOR  = r'\]'
t_LKEY  = r'\{'
t_RKEY  = r'\}'
t_PTO = r'\.'
t_COMA = r','
t_SEMICOLON = r';'
t_AND   = r'&&'
t_OR    = r'\|\|'
t_NOT   = r'!'