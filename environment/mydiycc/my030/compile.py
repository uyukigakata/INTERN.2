import inspect
import ply.yacc as yacc
from lex import tokens
from codegen import codegen 
from collections import namedtuple
Node = namedtuple('Node',('label','items'))
#+- < *\
precedence = (
            ('left','OPTASU','OPHIKU'),
            ('left','OPKAKE','OPWARU'),
)

## p_top(p)
## eBNF の 定義 top の定義
## p_ が prefix として付く。
## 仮引数は 前段からわたってく構造体p[0] と eBNF の定義 p[1]~
def p_top(p):
    '''
    teigi : kansuuteigi
          | teigi kansuuteigi
    '''
    ## 定義は RETURN というトークン、 NUMBER というトークン、　SEMI というトークン
    ## これらの並びとする
    if (len(p) == 2):
        p[0] = [p[1]]
    else:
        tmp = p[1]
        tmp.append(p[2])
        p[0] = tmp
        
def p_kansuuteigi(p):
    '''
    kansuuteigi : TYPE SYMBOL KAKKO KOKKA LBRACE bunlist RBRACE
    '''
    #p[0] = ['func',p[1],p[2],p[6]]
    p[0] = Node(label='func',items=[p[1],p[2],[],p[6]])

def p_kansuuteigi_hiki(p):
    '''
    kansuuteigi : TYPE SYMBOL KAKKO TYPE SYMBOL KOKKA LBRACE bunlist RBRACE
    '''
    #p[0] = ['func',p[1],p[2],p[6]]
    p[0] = Node(label='func',items=[p[1],p[2],[[p[4],p[5]]],p[8]])

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
    #p[0] = [p[1],p[2]]
    p[0] = Node(label='return',items=[p[2]])

def p_bun_sengen(p):
    '''
    bun : TYPE SYMBOL SEMI
    '''
    #p[0] = ['SENGEN',p[1],p[2]]
    p[0] = Node(label='SENGEN',items=[p[1],p[2]])
    
def p_bun_dainyu(p):
    '''
    bun : SYMBOL EQUALS expression SEMI
    '''
    p[0] = Node(label='DAINYU', items=[p[1],p[3]])

#def p_bun_if(p):ifを高度に書いた例(codegenがかければ訂正可)
    #'''
    #bun : IF KAKKO expression KOKKA LBRACE bunlist RBRACE
    #'''
    #p[0] = Node(label='IF', items=[p[3]])

def p_bun_if(p):
    '''
    bun : IF KAKKO expression COMPEQ expression KOKKA LBRACE bunlist RBRACE
    '''
    p[0] = Node(label='IF', items=[[p[3],p[4],p[5]],p[8]])

def p_bun_expression_only(p):
    '''
    bun : expression SEMI
    '''
    p[0] = Node(label='EXPRESSION',items=[p[1]])
    
    
#def p_bun_funccall(p):
#    '''
#    bun : SYMBOL KAKKO KOKKA SEMI
#    '''
#    p[0] = Node(label='FUNCCALL', items=[p[1], []])
  
def p_expression(p):
    '''
    expression : NUMBER
               | expression OPTASU expression
               | expression OPHIKU expression
               | expression OPKAKE expression
               | expression OPWARU expression
    '''
    if(len(p) == 2):
        #p[0] = ['NUM', p[1]]
        p[0] = Node(label='NUM',items=[p[1]])
    else:
        #p[0] = [p[2],p[1],p[3]]
        p[0] = Node(label=p[2],items=[p[1],p[3]])
        
def p_expression_var(p):
    '''
    expression : SYMBOL 
    '''
    p[0] = Node(label = 'VAR', items=[p[1]])
    
def p_expression_funccall(p):
    '''
    expression : SYMBOL KAKKO KOKKA
    '''
    p[0] = Node(label='FUNCCALL', items=[p[1],[]])

def p_expression_funcall_hiki(p):
    '''
    expression : SYMBOL KAKKO expression KOKKA
    '''
    p[0] = Node(label='FUNCCALL', items=[p[1],[p[3]]])

#def p_expression_if(p):
    #'''
    #expression : SYMBOL COMPEQ expression 
    #'''
    #p[0] = Node(label='VAR', items=[p[1],p[2],p[3]])
    
# syntax error
def p_error(p):
    print ('Syntax error %s' % p)

parser = yacc.yacc()
#テスト実行
if __name__== '__main__':
    s = '''
    int func( int p ){
        int x;
        int y;
        x = 10;
        y = 30;
        return x+y+p;
    }
    int main(){
        int x;
        int y;
        x = 10;
        if (x == 10){
            y = 20;
        }
        return x+y;
    }
    '''
    result = parser.parse(s)
    print("==AST==")
    print(result)
    codegen(result, 'out.s')