import inspect
import ply.yacc as yacc
from lex import tokens
from codegen import codegen 

def p_top(p):
    '''
    teigi : RETURN expression SEMI
    '''
    
    p[0] = [p[1],p[2],p[3]]

def p_expression(p):
    '''
    expression : NUMBER
               | expression OPTASU NUMBER
               | expression OPHIKU NUMBER
    '''
    
    if(len(p) == 2):
        p[0] = ['NUM', p[1]]
    else:
        p[0] = [p[2],p[1],['NUM',p[3]]]

# syntax error
def p_error(p):
    print ('Syntax error %s' % p)

parser = yacc.yacc()

if __name__== '__main__':
    s = '''
    return 4+3;
    '''
    result= parser.parse(s)
    print("==AST==")
    print(result)
    #codegen(result, 'out.s')
    