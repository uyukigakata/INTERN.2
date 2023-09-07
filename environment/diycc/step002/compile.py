import inspect
import ply.yacc as yacc
from lex import tokens

## p_top(p)
## eBNF の 定義 top の定義
## p_ が prefix として付く。
## 仮引数は 前段からわたってく構造体p[0] と eBNF の定義 p[1]~
def p_top(p):
    '''
    teigi : RETURN NUMBER SEMI
    '''
    ## 定義は RETURN というトークン、 NUMBER というトークン、　SEMI というトークン
    ## これらの並びとする
    p[0] = [p[1],p[2],p[3]]


# syntax error
def p_error(p):
    print ('Syntax error %s' % p)

parser = yacc.yacc()

if __name__ == '__main__':  
    s = '''
    return 3;
    '''
    result = parser.parse(s)
    print ("==AST==")
    print (result)

    