{"filter":false,"title":"lex.py","tooltip":"/mydiycc/my017/lex.py","undoManager":{"mark":7,"position":7,"stack":[[{"start":{"row":0,"column":0},"end":{"row":85,"column":18},"action":"insert","lines":["import ply.lex as lex","","tokens = ( ","    'NUMBER',   #数値","    'RETURN',   #return","    'SEMI',     #セミコロン","    'OPTASU',   #+","    'OPHIKU',   #-","    'OPKAKE',   #*","    #'OPWARU',  #\\","    'SYMBOL',   #文字","    'LBRACE',   #{","    'RBRACE',   #}","    'KAKKO',    #(","    'KOKKA',    #)","    'EQUALS',   #代入=","    ","    'TYPE',      #型","    ",")","","t_NUMBER = r'\\d+'","","#t_RETURN = 'return'","","t_SEMI = ';'","","t_OPTASU = r'\\+'","","t_OPHIKU = r'\\-'","","t_OPKAKE = r'\\*'","","#t_OPWARU = r'\\/'","","t_LBRACE = r'\\{'","","t_RBRACE = r'\\}'","","t_KAKKO = r'\\('","","t_KOKKA = r'\\)'","","t_EQUALS = r'='","","def t_SYMBOL(t):","    r'[a-zA-Z_][0-9a-zA-Z_]*'","    if t.value == 'return':","        t.type = 'RETURN'","    if t.value == 'int':","        t.type = 'TYPE'","    return t","","","#タブ区切りと空白を無視","t_ignore = ' \\t'","","","#エラー時に表示","def t_error(t):","    print(\"Error '%s'\" % t.value[0])","    t.lexer.skip(1)","","#改行時の約束","def t_newline(t):","    r'\\n+'","    t.lexer.lineno += len(t.value)","    ","lexer = lex.lex(debug=0)","","if __name__ == '__main__':","    data = '''","    int main(){","        int x;","        int y;","        x=10;","        y=20;","        return 3+2*3;","    }","    '''","    lexer.input(data)","    while True:","        tok = lexer.token()","        if not tok:","            break","        print(tok)"],"id":1}],[{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":2}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":1},"action":"insert","lines":["#"],"id":3}],[{"start":{"row":2,"column":1},"end":{"row":2,"column":4},"action":"insert","lines":["トーク"],"id":4},{"start":{"row":2,"column":4},"end":{"row":2,"column":5},"action":"insert","lines":["ン"]}],[{"start":{"row":2,"column":5},"end":{"row":2,"column":8},"action":"insert","lines":["の定義"],"id":5}],[{"start":{"row":21,"column":0},"end":{"row":22,"column":0},"action":"insert","lines":["",""],"id":6}],[{"start":{"row":22,"column":0},"end":{"row":25,"column":0},"action":"insert","lines":["## トークンのパターン","## tokens にある 'NUMBER' の prefix に t_ を付けたものを定義する","## r'\\d+' は r'' はraw文字列を意味する。 \\d+ は 正規表現で \\d(数字) の +(1個以上の繰り返し)",""],"id":7}],[{"start":{"row":24,"column":63},"end":{"row":25,"column":0},"action":"remove","lines":["",""],"id":8}]]},"ace":{"folds":[],"scrolltop":1102.5000000000002,"scrollleft":0,"selection":{"start":{"row":4,"column":19},"end":{"row":4,"column":19},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":72,"state":"start","mode":"ace/mode/python"}},"timestamp":1693964925907,"hash":"bfff5056f8efe24e79d0529ef8573a7d3cee1732"}