import ply.lex as lex

tokens = ( 
    'NUMBER',   #数値
    'RETURN',   #return
    'SEMI',     #セミコロン
    'OPTASU',   #+
    'OPHIKU',   #-
    'OPKAKE',   #*
    #'OPWARU',   #\
    'SYMBOL',   #文字
    'LBRACE',   #{
    'RBRACE',   #}
    'KAKKO',    #(
    'KOKKA',    #)
    
    'TYPE'      #型
    
)

t_NUMBER = r'\d+'

#t_RETURN = 'return'

t_SEMI = ';'

t_OPTASU = r'\+'

t_OPHIKU = r'\-'

t_OPKAKE = r'\*'

#t_OPWARU = r'\/'

t_LBRACE = r'\{'

t_RBRACE = r'\}'

t_KAKKO = r'\('

t_KOKKA = r'\)'

def t_SYMBOL(t):
    r'[a-zA-Z_][0-9a-zA-Z_]*'
    if t.value == 'return':
        t.type = 'RETURN'
    if t.value == 'int':
        t.type = 'TYPE'
    return t


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
    int main(){
        int x;
        int y;
        return 3+2*3;
    }
    '''
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)