{"filter":false,"title":"codegen.py","tooltip":"/mydiycc/my019/codegen.py","undoManager":{"mark":45,"position":45,"stack":[[{"start":{"row":0,"column":0},"end":{"row":148,"column":0},"action":"insert","lines":["fm = {}","fc = 0","","def walk( tree , f):","    print(\"!!entering walk!!\")","    print(tree)","    if (tree.label == 'NUM'):","        f.write('   pushq $'+tree.items[0]+ \"\\n\")","    elif (tree.label == 'VAR'):","        f.write(r'   pushq -'+str(fm[tree.items[0]])+r'(%rbp)'+\"\\n\")","    elif (tree.label == '+'):","        walk(tree.items[0],f)","        walk(tree.items[1],f)","        f.write(r'   pop %rdi' + \"\\n\")","        f.write(r'   pop %rax' + \"\\n\")","        f.write(r'   add %rdi,%rax' + \"\\n\")","        f.write(r'   pushq %rax' + \"\\n\")","    elif (tree.label == '-'):","        walk(tree.items[0],f)","        walk(tree.items[1],f)","        f.write(r'   pop %rdi' + \"\\n\")","        f.write(r'   pop %rax' + \"\\n\")","        f.write(r'   sub %rdi,%rax' + \"\\n\")","        f.write(r'   pushq %rax' + \"\\n\")","    elif (tree.label == '*'):","        walk(tree.items[0],f)","        walk(tree.items[1],f)","        f.write(r'   pop %rdi' + \"\\n\")","        f.write(r'   pop %rax' + \"\\n\")","        f.write(r'   imul %rdi,%rax' + \"\\n\")","        f.write(r'   pushq %rax' + \"\\n\")","    elif (tree.label == '/'):","        walk(tree.items[0],f)","        walk(tree.items[1],f)","        f.write(r'   pop %rdi' + \"\\n\")","        f.write(r'   pop %rax' + \"\\n\")","        f.write(r'   sub %rdi,%rax' + \"\\n\")","        f.write(r'   pushq %rax' + \"\\n\")","    elif (tree.label == 'DAINYU'):","        walk(tree.items[1],f)","        print(fm)","        f.write(r'   pop\t%rax'+ \"\\n\")","        f.write(r'   mov\t%rax, -'+str(fm[tree.items[0]])+r'(%rbp)'+\"\\n\")","    elif (tree.label == 'func'):","        returntype = tree.items[0]  # 戻り値の型","        funcname   = tree.items[1]  # 関数名","        f.write(r'   .globl\t'+ funcname + \"\\n\")","        f.write(r'   .type\t'+ funcname + ', @function' + \"\\n\")","        f.write(funcname + \":\\n\")","        f.write(r'   endbr64' + \"\\n\")","        f.write(r'   pushq %rbp' + \"\\n\")","        f.write(r'   movq %rsp, %rbp' + \"\\n\")","        # ローカル変数のサイズ分スタックをずらす","        f.write(r'   subq $'+str(fc*8)+r',%rsp'+\"\\n\")    # sizeof(int)を 8 とする。アライメント調整が面倒なので","        for item in tree.items[2]:","            walk(item,f)","        f.write(r'   .size '+funcname+', .-'+ funcname +\"\\n\")","    #elif (tree.label == 'SENGEN'):","        # sengen","    elif (tree.label == 'return'):","        walk(tree.items[0],f)","        f.write(r'   pop\t%rax'+ \"\\n\")","        f.write(r'   leave'+ \"\\n\")","        f.write(r'   ret'+ \"\\n\")","    ","","def calcframesize( tree ):","    '''","        sizeof(int)の数","    '''","    return len(list( filter( lambda item: item.label == 'SENGEN' , tree ) ))","def createframemap( tree ):","    map = {}","    vars = list( filter( lambda item: item.label == 'SENGEN' , tree ) )","    size = len(vars) * 8","    for sen in vars:","        map[sen.items[1]] = size","        size -= 8","    return map","","def codegen( tree , filename ):","    with open(filename, mode='w') as f:","","        ## １個目は関数の定義とする","        teigi1 = tree[0]","","        ##","        print('===codegen step1===')","        print(teigi1)","        rettype  = teigi1.items[0]    #戻り値の型 int","        funcname = teigi1.items[1]    #関数名 main","","        global fc","        global fm","        fc = calcframesize( teigi1.items[2] )   # sizeof(int)の数","        fm = createframemap( teigi1.items[2] ) ","","        print( 'calcframesize :' + str(fc) )","        print( fm )","        ","        # returnexp = list( filter( lambda item: item.label != 'SENGEN' , teigi1.items[2] ) )","        # print(returnexp)","        # dainyu_list = []","        # dainyu_list.append(returnexp[0])","        # dainyu_list.append(returnexp[1])","        # exp = returnexp[2].items[0]","        # exp      = teigi1[3][2][1] #文","        # print(\"exp:\")","        # print(exp)","        # print(\"dainyu_list:\")","        # print(dainyu_list)","","        ","","        print('===codegen step2===')","        print('funcname: '+funcname)","","        #asm の先頭","        f.write(r'   .text' + \"\\n\")","","        walk(teigi1,f)","","        #関数ヘッダ","        # f.write(r'   .globl\t'+ funcname + \"\\n\")","        # f.write(r'   .type\t'+ funcname + ', @function' + \"\\n\")","        # f.write(funcname + \":\\n\")","        # f.write(r'   endbr64' + \"\\n\")","        # f.write(r'   pushq %rbp' + \"\\n\")","        # f.write(r'   movq %rsp, %rbp' + \"\\n\")","        # # ローカル変数のサイズ分スタックをずらす","        # f.write(r'   subq $'+str(fc*8)+r',%rsp'+\"\\n\")    # sizeof(int)を 8 とする。アライメント調整が面倒なので","","        #代入のコードを生成する","        # for d in dainyu_list:","        #     walk(d.items[1],f)","        #     f.write(r'   pop\t%rax'+ \"\\n\")","        #     f.write(r'   mov\t%rax, -'+str(fm[d.items[0]])+r'(%rbp)'+\"\\n\")","","        #式を歩く","        # walk(exp,f)","        # f.write(r'   pop\t%rax'+ \"\\n\")","","        #関数フッダ","        # #f.write(r'   popq\t%rbp'+ \"\\n\")    #ローカル変数分スタックをずらしたので Leave で対処","        # f.write(r'   leave'+ \"\\n\")","        # f.write(r'   ret'+ \"\\n\")","        # f.write(r'   .size '+funcname+', .-'+ funcname +\"\\n\")","",""],"id":1}],[{"start":{"row":84,"column":8},"end":{"row":84,"column":9},"action":"insert","lines":["3"],"id":2},{"start":{"row":84,"column":9},"end":{"row":84,"column":10},"action":"insert","lines":["#"]}],[{"start":{"row":84,"column":8},"end":{"row":84,"column":9},"action":"remove","lines":["3"],"id":3}],[{"start":{"row":84,"column":8},"end":{"row":84,"column":9},"action":"remove","lines":["#"],"id":4}],[{"start":{"row":84,"column":8},"end":{"row":84,"column":9},"action":"insert","lines":["#"],"id":8}],[{"start":{"row":84,"column":8},"end":{"row":84,"column":9},"action":"remove","lines":["#"],"id":9}],[{"start":{"row":84,"column":8},"end":{"row":84,"column":9},"action":"insert","lines":["#"],"id":10}],[{"start":{"row":86,"column":10},"end":{"row":86,"column":11},"action":"insert","lines":["a"],"id":11},{"start":{"row":86,"column":11},"end":{"row":86,"column":12},"action":"insert","lines":["s"]},{"start":{"row":86,"column":12},"end":{"row":86,"column":13},"action":"insert","lines":["m"]}],[{"start":{"row":86,"column":13},"end":{"row":86,"column":16},"action":"insert","lines":["の戦闘"],"id":12}],[{"start":{"row":86,"column":14},"end":{"row":86,"column":16},"action":"remove","lines":["戦闘"],"id":13}],[{"start":{"row":86,"column":14},"end":{"row":86,"column":16},"action":"insert","lines":["先頭"],"id":14}],[{"start":{"row":86,"column":16},"end":{"row":87,"column":0},"action":"insert","lines":["",""],"id":15},{"start":{"row":87,"column":0},"end":{"row":87,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":87,"column":8},"end":{"row":87,"column":9},"action":"insert","lines":["f"],"id":16},{"start":{"row":87,"column":9},"end":{"row":87,"column":10},"action":"insert","lines":["."]},{"start":{"row":87,"column":10},"end":{"row":87,"column":11},"action":"insert","lines":["w"]},{"start":{"row":87,"column":11},"end":{"row":87,"column":12},"action":"insert","lines":["r"]}],[{"start":{"row":87,"column":12},"end":{"row":87,"column":13},"action":"insert","lines":["i"],"id":17},{"start":{"row":87,"column":13},"end":{"row":87,"column":14},"action":"insert","lines":["t"]},{"start":{"row":87,"column":14},"end":{"row":87,"column":15},"action":"insert","lines":["e"]}],[{"start":{"row":87,"column":15},"end":{"row":87,"column":17},"action":"insert","lines":["()"],"id":18}],[{"start":{"row":87,"column":16},"end":{"row":87,"column":17},"action":"insert","lines":["r"],"id":19}],[{"start":{"row":87,"column":17},"end":{"row":87,"column":19},"action":"insert","lines":["''"],"id":20}],[{"start":{"row":87,"column":18},"end":{"row":87,"column":19},"action":"insert","lines":[" "],"id":21},{"start":{"row":87,"column":19},"end":{"row":87,"column":20},"action":"insert","lines":[" "]}],[{"start":{"row":87,"column":20},"end":{"row":87,"column":21},"action":"insert","lines":["."],"id":22},{"start":{"row":87,"column":21},"end":{"row":87,"column":22},"action":"insert","lines":["y"]}],[{"start":{"row":87,"column":21},"end":{"row":87,"column":22},"action":"remove","lines":["y"],"id":23}],[{"start":{"row":87,"column":21},"end":{"row":87,"column":22},"action":"insert","lines":["t"],"id":24},{"start":{"row":87,"column":22},"end":{"row":87,"column":23},"action":"insert","lines":["e"]},{"start":{"row":87,"column":23},"end":{"row":87,"column":24},"action":"insert","lines":["x"]},{"start":{"row":87,"column":24},"end":{"row":87,"column":25},"action":"insert","lines":["t"]}],[{"start":{"row":87,"column":26},"end":{"row":87,"column":27},"action":"insert","lines":[" "],"id":25},{"start":{"row":87,"column":27},"end":{"row":87,"column":28},"action":"insert","lines":["+"]}],[{"start":{"row":87,"column":28},"end":{"row":87,"column":29},"action":"insert","lines":[" "],"id":26}],[{"start":{"row":87,"column":29},"end":{"row":87,"column":31},"action":"insert","lines":["\"\""],"id":27}],[{"start":{"row":87,"column":30},"end":{"row":87,"column":31},"action":"insert","lines":["\\"],"id":28},{"start":{"row":87,"column":31},"end":{"row":87,"column":32},"action":"insert","lines":["n"]}],[{"start":{"row":87,"column":34},"end":{"row":88,"column":0},"action":"insert","lines":["",""],"id":29},{"start":{"row":88,"column":0},"end":{"row":88,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":88,"column":8},"end":{"row":89,"column":0},"action":"insert","lines":["",""],"id":30},{"start":{"row":89,"column":0},"end":{"row":89,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":89,"column":8},"end":{"row":89,"column":9},"action":"insert","lines":["f"],"id":31},{"start":{"row":89,"column":9},"end":{"row":89,"column":10},"action":"insert","lines":["o"]},{"start":{"row":89,"column":10},"end":{"row":89,"column":11},"action":"insert","lines":["r"]}],[{"start":{"row":89,"column":11},"end":{"row":89,"column":12},"action":"insert","lines":[" "],"id":32},{"start":{"row":89,"column":12},"end":{"row":89,"column":13},"action":"insert","lines":["t"]},{"start":{"row":89,"column":13},"end":{"row":89,"column":14},"action":"insert","lines":["e"]},{"start":{"row":89,"column":14},"end":{"row":89,"column":15},"action":"insert","lines":["i"]}],[{"start":{"row":89,"column":15},"end":{"row":89,"column":16},"action":"insert","lines":["g"],"id":33},{"start":{"row":89,"column":16},"end":{"row":89,"column":17},"action":"insert","lines":["i"]}],[{"start":{"row":89,"column":17},"end":{"row":89,"column":18},"action":"insert","lines":[" "],"id":34},{"start":{"row":89,"column":18},"end":{"row":89,"column":19},"action":"insert","lines":["i"]},{"start":{"row":89,"column":19},"end":{"row":89,"column":20},"action":"insert","lines":["n"]}],[{"start":{"row":89,"column":20},"end":{"row":89,"column":21},"action":"insert","lines":[" "],"id":35},{"start":{"row":89,"column":21},"end":{"row":89,"column":22},"action":"insert","lines":["t"]},{"start":{"row":89,"column":22},"end":{"row":89,"column":23},"action":"insert","lines":["r"]},{"start":{"row":89,"column":23},"end":{"row":89,"column":24},"action":"insert","lines":["e"]},{"start":{"row":89,"column":24},"end":{"row":89,"column":25},"action":"insert","lines":["e"]}],[{"start":{"row":89,"column":25},"end":{"row":89,"column":26},"action":"insert","lines":[":"],"id":36}],[{"start":{"row":90,"column":0},"end":{"row":90,"column":4},"action":"insert","lines":["    "],"id":37},{"start":{"row":91,"column":0},"end":{"row":91,"column":4},"action":"insert","lines":["    "]},{"start":{"row":92,"column":0},"end":{"row":92,"column":4},"action":"insert","lines":["    "]},{"start":{"row":93,"column":0},"end":{"row":93,"column":4},"action":"insert","lines":["    "]},{"start":{"row":94,"column":0},"end":{"row":94,"column":4},"action":"insert","lines":["    "]},{"start":{"row":95,"column":0},"end":{"row":95,"column":4},"action":"insert","lines":["    "]},{"start":{"row":96,"column":0},"end":{"row":96,"column":4},"action":"insert","lines":["    "]},{"start":{"row":97,"column":0},"end":{"row":97,"column":4},"action":"insert","lines":["    "]},{"start":{"row":98,"column":0},"end":{"row":98,"column":4},"action":"insert","lines":["    "]},{"start":{"row":99,"column":0},"end":{"row":99,"column":4},"action":"insert","lines":["    "]},{"start":{"row":100,"column":0},"end":{"row":100,"column":4},"action":"insert","lines":["    "]},{"start":{"row":101,"column":0},"end":{"row":101,"column":4},"action":"insert","lines":["    "]},{"start":{"row":102,"column":0},"end":{"row":102,"column":4},"action":"insert","lines":["    "]},{"start":{"row":103,"column":0},"end":{"row":103,"column":4},"action":"insert","lines":["    "]},{"start":{"row":104,"column":0},"end":{"row":104,"column":4},"action":"insert","lines":["    "]},{"start":{"row":105,"column":0},"end":{"row":105,"column":4},"action":"insert","lines":["    "]},{"start":{"row":106,"column":0},"end":{"row":106,"column":4},"action":"insert","lines":["    "]},{"start":{"row":107,"column":0},"end":{"row":107,"column":4},"action":"insert","lines":["    "]},{"start":{"row":108,"column":0},"end":{"row":108,"column":4},"action":"insert","lines":["    "]},{"start":{"row":109,"column":0},"end":{"row":109,"column":4},"action":"insert","lines":["    "]},{"start":{"row":110,"column":0},"end":{"row":110,"column":4},"action":"insert","lines":["    "]},{"start":{"row":111,"column":0},"end":{"row":111,"column":4},"action":"insert","lines":["    "]},{"start":{"row":112,"column":0},"end":{"row":112,"column":4},"action":"insert","lines":["    "]},{"start":{"row":113,"column":0},"end":{"row":113,"column":4},"action":"insert","lines":["    "]},{"start":{"row":114,"column":0},"end":{"row":114,"column":4},"action":"insert","lines":["    "]},{"start":{"row":115,"column":0},"end":{"row":115,"column":4},"action":"insert","lines":["    "]},{"start":{"row":116,"column":0},"end":{"row":116,"column":4},"action":"insert","lines":["    "]},{"start":{"row":117,"column":0},"end":{"row":117,"column":4},"action":"insert","lines":["    "]},{"start":{"row":118,"column":0},"end":{"row":118,"column":4},"action":"insert","lines":["    "]},{"start":{"row":119,"column":0},"end":{"row":119,"column":4},"action":"insert","lines":["    "]},{"start":{"row":120,"column":0},"end":{"row":120,"column":4},"action":"insert","lines":["    "]},{"start":{"row":121,"column":0},"end":{"row":121,"column":4},"action":"insert","lines":["    "]},{"start":{"row":122,"column":0},"end":{"row":122,"column":4},"action":"insert","lines":["    "]},{"start":{"row":123,"column":0},"end":{"row":123,"column":4},"action":"insert","lines":["    "]},{"start":{"row":124,"column":0},"end":{"row":124,"column":4},"action":"insert","lines":["    "]},{"start":{"row":125,"column":0},"end":{"row":125,"column":4},"action":"insert","lines":["    "]},{"start":{"row":126,"column":0},"end":{"row":126,"column":4},"action":"insert","lines":["    "]},{"start":{"row":127,"column":0},"end":{"row":127,"column":4},"action":"insert","lines":["    "]},{"start":{"row":128,"column":0},"end":{"row":128,"column":4},"action":"insert","lines":["    "]},{"start":{"row":129,"column":0},"end":{"row":129,"column":4},"action":"insert","lines":["    "]},{"start":{"row":130,"column":0},"end":{"row":130,"column":4},"action":"insert","lines":["    "]},{"start":{"row":131,"column":0},"end":{"row":131,"column":4},"action":"insert","lines":["    "]},{"start":{"row":132,"column":0},"end":{"row":132,"column":4},"action":"insert","lines":["    "]},{"start":{"row":133,"column":0},"end":{"row":133,"column":4},"action":"insert","lines":["    "]},{"start":{"row":134,"column":0},"end":{"row":134,"column":4},"action":"insert","lines":["    "]},{"start":{"row":135,"column":0},"end":{"row":135,"column":4},"action":"insert","lines":["    "]},{"start":{"row":136,"column":0},"end":{"row":136,"column":4},"action":"insert","lines":["    "]},{"start":{"row":137,"column":0},"end":{"row":137,"column":4},"action":"insert","lines":["    "]},{"start":{"row":138,"column":0},"end":{"row":138,"column":4},"action":"insert","lines":["    "]},{"start":{"row":139,"column":0},"end":{"row":139,"column":4},"action":"insert","lines":["    "]},{"start":{"row":140,"column":0},"end":{"row":140,"column":4},"action":"insert","lines":["    "]},{"start":{"row":141,"column":0},"end":{"row":141,"column":4},"action":"insert","lines":["    "]},{"start":{"row":142,"column":0},"end":{"row":142,"column":4},"action":"insert","lines":["    "]},{"start":{"row":143,"column":0},"end":{"row":143,"column":4},"action":"insert","lines":["    "]},{"start":{"row":144,"column":0},"end":{"row":144,"column":4},"action":"insert","lines":["    "]},{"start":{"row":145,"column":0},"end":{"row":145,"column":4},"action":"insert","lines":["    "]},{"start":{"row":146,"column":0},"end":{"row":146,"column":4},"action":"insert","lines":["    "]},{"start":{"row":147,"column":0},"end":{"row":147,"column":4},"action":"insert","lines":["    "]},{"start":{"row":148,"column":0},"end":{"row":148,"column":4},"action":"insert","lines":["    "]},{"start":{"row":149,"column":0},"end":{"row":149,"column":4},"action":"insert","lines":["    "]},{"start":{"row":150,"column":0},"end":{"row":150,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":91,"column":12},"end":{"row":91,"column":13},"action":"insert","lines":["#"],"id":39}],[{"start":{"row":92,"column":28},"end":{"row":92,"column":29},"action":"remove","lines":["1"],"id":40}],[{"start":{"row":93,"column":27},"end":{"row":93,"column":28},"action":"remove","lines":["i"],"id":41}],[{"start":{"row":93,"column":27},"end":{"row":93,"column":28},"action":"insert","lines":["i"],"id":42}],[{"start":{"row":93,"column":28},"end":{"row":93,"column":29},"action":"remove","lines":["1"],"id":43}],[{"start":{"row":91,"column":24},"end":{"row":91,"column":25},"action":"remove","lines":["1"],"id":44}],[{"start":{"row":91,"column":12},"end":{"row":91,"column":13},"action":"remove","lines":["#"],"id":45}],[{"start":{"row":97,"column":37},"end":{"row":97,"column":38},"action":"remove","lines":["1"],"id":46}],[{"start":{"row":97,"column":36},"end":{"row":97,"column":37},"action":"remove","lines":["i"],"id":47}],[{"start":{"row":97,"column":36},"end":{"row":97,"column":37},"action":"insert","lines":["i"],"id":48}],[{"start":{"row":98,"column":38},"end":{"row":98,"column":39},"action":"remove","lines":["1"],"id":49}],[{"start":{"row":123,"column":22},"end":{"row":123,"column":23},"action":"remove","lines":["1"],"id":50}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":0,"column":0},"end":{"row":151,"column":0},"isBackwards":true},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":88,"state":"start","mode":"ace/mode/python"}},"timestamp":1693975663904,"hash":"e44a4d685fbbda260ad649ad675292472ddf869c"}