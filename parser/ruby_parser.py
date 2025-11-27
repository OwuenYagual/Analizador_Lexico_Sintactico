# parser/ruby_parser.py
# Analizador sintáctico PLY (YACC) para Ruby – AVANCE 2

import ply.yacc as yacc
from lexer.ruby_lexer import construir_lexer

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

    # operadores lógicos
    'AND',
    'OR',
    'NOT',

    # asignaciones
    'ASIG',
    'MASIG',

    # delimitadores
    'LPAR',
    'RPAR',
    'LCOR',
    'RCOR',
    'COMA',

    # otros
    'NEWLINE',
    'RETURN',


    # reservadas usadas en la gramática
    'IF',
    'THEN',
    'END',
    'WHILE',
    'DO',
    'DEF',
    'CLASS',
    'TRUE',
    'FALSE',
    'NIL',
    'GETS',   # gets como palabra reservada
)

# ============================================================
# PRECEDENCIA
# ============================================================

precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'IGUAL', 'DIFERENTE', 'MAYORQ', 'MENORQ', 'MAYORIG', 'MENORIG'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'MOD'),
    ('right', 'EXP'),
    ('right', 'NOT'),
)

# ============================================================
# REGLA INICIAL
# ============================================================

def p_program(p):
    'program : statement_list'
    p[0] = ("program", p[1])

def p_statement_list_multiple(p):
    'statement_list : statement_list statement'
    p[0] = p[1] + [p[2]]

def p_statement_list_single(p):
    'statement_list : statement'
    p[0] = [p[1]]

# ============================================================
# REGLAS BASE PARA STATEMENTS
# ============================================================

def p_statement(p):
    '''statement : print_stmt
                 | input_stmt
                 | assign_stmt
                 | if_stmt
                 | while_stmt
                 | func_def
                 | class_def
                 | data_structure_stmt'''
    p[0] = p[1]

def p_return_stmt(p):
    'statement : RETURN expr'
    p[0] = ("return", p[2])

# ============================================================
# ===================== INTEGRANTE 1 ==========================
# Owuen Yagual
# ============================================================

# ---------- IMPRESIÓN (puts expr) ----------
def p_print_stmt(p):
    '''print_stmt : ID expr'''
    # puts expr
    if p[1] == "puts":
        p[0] = ("print", p[2])
    else:
        p[0] = ("call", p[1], [p[2]])

# ---------- INPUT (x = gets) ----------
def p_input_stmt(p):
    'input_stmt : ID ASIG GETS'
    p[0] = ("input", p[1])

# ---------- ASIGNACIONES ----------
def p_assign_stmt(p):
    '''assign_stmt : ID ASIG expr
                   | ID MASIG expr'''
    p[0] = ("assign", p[2], p[1], p[3])


# ============================================================
# ERRORES
# ============================================================

parser_errors = []

def p_error(p):
    if p:
        msg = f"Error sintáctico cerca de '{p.value}' en la línea {p.lineno}"
    else:
        msg = "Error sintáctico: fin de entrada inesperado"
    parser_errors.append(msg)

# ============================================================
# CONSTRUCTOR DEL PARSER
# ============================================================

def construir_parser():
    global parser_errors
    parser_errors = []
    parser = yacc.yacc()
    return parser, parser_errors

# ============================================================
# ===================== INTEGRANTE 2 ==========================
# Andres Pino G.
# ============================================================

def p_expr_binop(p):
    '''expr : expr PLUS expr
            | expr MINUS expr
            | expr TIMES expr
            | expr DIVIDE expr
            | expr MOD expr
            | expr EXP expr
            | expr IGUAL expr
            | expr DIFERENTE expr
            | expr MAYORQ expr
            | expr MENORQ expr
            | expr MAYORIG expr
            | expr MENORIG expr
            | expr AND expr
            | expr OR expr'''
    p[0] = ("binop", p[2], p[1], p[3])

def p_expr_group(p):
    'expr : LPAR expr RPAR'
    p[0] = p[2]

def p_expr_unary_not(p):
    'expr : NOT expr'
    p[0] = ("not", p[2])

def p_expr_literal(p):
    '''expr : NUMBER
            | STRING
            | TRUE
            | FALSE
            | NIL'''
    p[0] = ("lit", p[1])

def p_expr_var(p):
    'expr : ID'
    p[0] = ("var", p[1])

# ---------- IF ----------
def p_if_stmt(p):
    '''if_stmt : IF expr THEN statement_list END
               | IF expr statement_list END'''
    if len(p) == 6:
        p[0] = ("if", p[2], p[4])
    else:
        p[0] = ("if", p[2], p[3])

# ---------- WHILE ----------
def p_while_stmt(p):
    '''while_stmt : WHILE expr DO statement_list END
                  | WHILE expr statement_list END'''
    if len(p) == 6:
        p[0] = ("while", p[2], p[4])
    else:
        p[0] = ("while", p[2], p[3])

def p_statement_list_newline(p):
    'statement_list : statement_list NEWLINE'
    p[0] = p[1]
# ============================================================
# ===================== INTEGRANTE 3 ==========================
# Joaquin Guerra Aviles
# ============================================================

# ---------- ARRAYS ----------
def p_data_structure_array(p):
    'data_structure_stmt : ID ASIG LCOR expr_list RCOR'
    p[0] = ("assign_array", p[1], p[4])

def p_expr_list_multiple(p):
    'expr_list : expr_list COMA expr'
    p[0] = p[1] + [p[3]]

def p_expr_list_single(p):
    'expr_list : expr'
    p[0] = [p[1]]

# ---------- FUNCIONES ----------
def p_func_def(p):
    'func_def : DEF ID param_list_opt NEWLINE statement_list END'
    p[0] = ("func_def", p[2], p[3], p[5])

def p_param_list_opt_empty(p):
    'param_list_opt : '
    p[0] = []

def p_param_list_opt(p):
    'param_list_opt : LPAR param_list RPAR'
    p[0] = p[2]

def p_param_list_multi(p):
    'param_list : param_list COMA ID'
    p[0] = p[1] + [p[3]]

def p_param_list_single(p):
    'param_list : ID'
    p[0] = [p[1]]

# ---------- CLASES ----------
def p_class_def(p):
    'class_def : CLASS ID NEWLINE class_body END'
    p[0] = ("class_def", p[2], p[4])

def p_class_body(p):
    'class_body : statement_list'
    p[0] = p[1]