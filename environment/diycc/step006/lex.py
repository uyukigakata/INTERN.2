import ply.lex as lex

##トークンの定義
tokens = (
    'NUMBER',

    'OPTASU',
    'OPHIKU',

    'OPKAKE',

    'SEMI',
    'RETURN'
)

## トークンのパターン
## tokens にある 'NUMBER' の prefix に t_ を付けたものを定義する
## r'\d+' は r'' はraw文字列を意味する。 \d+ は 正規表現で \d(数字) の +(1個以上の繰り返し)
t_NUMBER = r'\d+'

t_OPTASU = r'\+'
t_OPHIKU = r'\-'

t_OPKAKE = r'\*'
#t_OPWARU = r'\/'

t_SEMI   = ';'
t_RETURN = 'return'

## space と \t は igonore(無視)
t_ignore = ' \t'

## お約束的
## エラー発生時に呼ばれる
def t_error(t):
    print("Error '%s'" % t.value[0])
    t.lexer.skip(1)

## お約束的
## 改行の時
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

lexer = lex.lex(debug=0)

if __name__ == '__main__':  
    # ここからテスト
    data = '''
    return 49+5;
    '''
    lexer.input(data)    
    while True:
        tok = lexer.token()
        if not tok:  
            # これ以上トークンはない
            break
        # トークンを出力
        print(tok)
