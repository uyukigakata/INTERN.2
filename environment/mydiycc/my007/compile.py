import inspect
import ply.yacc as yacc
from lex import tokens
from codegen import codegen 

#+- < *\
precedence = (
            ('left','OPTASU','OPHIKU'),
            ('left','OPKAKE'),
        )

#定義
def p_top(p):
    '''
    teigi : kansuuteigi
    '''
    
    p[0] = [p[1]]

def p_kansuuteigi(p):
    '''
    kansuuteigi : SYMBOL SYMBOL KAKKO KOKKA LBRACE bunlist RBRACE
    '''
    p[0] = ['func',p[1],p[2],p[6]]

def p_bunlist(p):
    '''
    bunlist : RETURN expression SEMI
    '''
    p[0] = [p[1],p[2],p[3]]

def p_expression(p):
    '''
    expression : NUMBER
               | expression OPTASU expression
               | expression OPHIKU expression
               | expression OPKAKE expression
    '''
    
    if(len(p) == 2):
        p[0] = ['NUM', p[1]]
    else:
        p[0] = [p[2],p[1],p[3]]

# syntax error
def p_error(p):
    print ('Syntax error %s' % p)

parser = yacc.yacc()

#テスト実行
if __name__== '__main__':
    s = '''
    int main(){
        return 3+2*3;
    }
    '''
    result= parser.parse(s)
    print("==AST==")
    print(result)
    #codegen(result, 'out.s')

    