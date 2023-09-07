import inspect
import ply.yacc as yacc
from lex import tokens
from codegen import codegen 

def p_top(p):
    '''
    teigi : RETURN NUMBER SEMI
    '''
    
    p[0] = [p[1],p[2],p[3]]
    

# syntax error
def p_error(p):
    print ('Syntax error %s' % p)

parser = yacc.yacc()

if __name__== '__main__':
    s = '''
    return 8;
    '''
    result= parser.parse(s)
    print("==AST==")
    print(result)
    codegen(result, 'out.s')
    