import ply.lex as lex

tokens = ( 
    'NUMBER',
)

t_NUMBER = r'\d+'

#タブ区切りと空白を無視
t_ignore = ' \t'

#エラー時に表示
def t_error(t):
    print("Error '%s'" % t.value[0])
    t.lexer.skip(1)

#改行時の約束
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    
lexer = lex.lex(debug=0)

if __name__ == '__main__':
    data = '''
    100
    '''
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)