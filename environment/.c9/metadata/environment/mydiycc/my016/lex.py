{"filter":false,"title":"lex.py","tooltip":"/mydiycc/my016/lex.py","undoManager":{"mark":3,"position":3,"stack":[[{"start":{"row":0,"column":0},"end":{"row":85,"column":18},"action":"insert","lines":["import ply.lex as lex","","tokens = ( ","    'NUMBER',   #数値","    'RETURN',   #return","    'SEMI',     #セミコロン","    'OPTASU',   #+","    'OPHIKU',   #-","    'OPKAKE',   #*","    #'OPWARU',  #\\","    'SYMBOL',   #文字","    'LBRACE',   #{","    'RBRACE',   #}","    'KAKKO',    #(","    'KOKKA',    #)","    'EQUALS',   #代入=","    ","    'TYPE',      #型","    ",")","","t_NUMBER = r'\\d+'","","#t_RETURN = 'return'","","t_SEMI = ';'","","t_OPTASU = r'\\+'","","t_OPHIKU = r'\\-'","","t_OPKAKE = r'\\*'","","#t_OPWARU = r'\\/'","","t_LBRACE = r'\\{'","","t_RBRACE = r'\\}'","","t_KAKKO = r'\\('","","t_KOKKA = r'\\)'","","t_EQUALS = r'='","","def t_SYMBOL(t):","    r'[a-zA-Z_][0-9a-zA-Z_]*'","    if t.value == 'return':","        t.type = 'RETURN'","    if t.value == 'int':","        t.type = 'TYPE'","    return t","","","#タブ区切りと空白を無視","t_ignore = ' \\t'","","","#エラー時に表示","def t_error(t):","    print(\"Error '%s'\" % t.value[0])","    t.lexer.skip(1)","","#改行時の約束","def t_newline(t):","    r'\\n+'","    t.lexer.lineno += len(t.value)","    ","lexer = lex.lex(debug=0)","","if __name__ == '__main__':","    data = '''","    int main(){","        int x;","        int y;","        x=10;","        y=20;","        return 3+2*3;","    }","    '''","    lexer.input(data)","    while True:","        tok = lexer.token()","        if not tok:","            break","        print(tok)"],"id":1}],[{"start":{"row":50,"column":23},"end":{"row":51,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":51,"column":0},"end":{"row":51,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":51,"column":4},"end":{"row":51,"column":8},"action":"remove","lines":["    "],"id":3}],[{"start":{"row":51,"column":0},"end":{"row":51,"column":4},"action":"remove","lines":["    "],"id":4},{"start":{"row":50,"column":23},"end":{"row":51,"column":0},"action":"remove","lines":["",""]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":4,"column":23},"end":{"row":4,"column":23},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1693964210920,"hash":"a49a038741a699ca6d82cf8fc33080d5c87c4124"}