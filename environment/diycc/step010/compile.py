import inspect
import ply.yacc as yacc
from lex import tokens
from codegen import codegen 

precedence = (
   ('left','OPTASU','OPHIKU'),
   ('left','OPKAKE'),
)

## p_top(p)
## eBNF の 定義 top の定義
## p_ が prefix として付く。
## 仮引数は 前段からわたってく構造体p[0] と eBNF の定義 p[1]~
def p_top(p):
    '''
    teigi : kansuuteigi
    '''
    ## 定義は RETURN というトークン、 NUMBER というトークン、　SEMI というトークン
    ## これらの並びとする
    p[0] = [p[1]]

def p_kansuuteigi(p):
    '''
    kansuuteigi : TYPE SYMBOL KAKKO KOKKA LBRACE bunlist RBRACE
    '''
    p[0] = ['func',p[1],p[2],p[6]]

def p_bunlist(p):
    '''
    bunlist : bun
            | bunlist bun
    '''
    if (len(p) == 2):
        p[0] = [p[1]]
    else:
        tmp = p[1]
        tmp.append(p[2])
        p[0] = tmp

def p_bun_return(p):
    '''
    bun : RETURN expression SEMI
    '''
    p[0] = [p[1],p[2]]

def p_bun_sengen(p):
    '''
    bun : TYPE SYMBOL SEMI
    '''
    p[0] = ['SENGEN',p[1],p[2]]

def p_expression(p):
    '''
    expression : NUMBER
               | expression OPTASU expression
               | expression OPHIKU expression
               | expression OPKAKE expression
    '''
    if (len(p) == 2):
        p[0] = ['NUM',p[1]]
    else:
        p[0] = [p[2],p[1],p[3]]

# syntax error
def p_error(p):
    print ('Syntax error %s' % p)

parser = yacc.yacc()

if __name__ == '__main__':  
    s = '''
    int main(){
        int x;
        int y;
        return 3+2*3;
    }
    '''
    result = parser.parse(s)
    print ("==AST==")
    print (result)
    codegen( result , 'out.s')

    