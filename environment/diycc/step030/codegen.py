fm = {}
fc = 0
label_count = 0

def walk( tree , f):
    print("!!entering walk!!")
    print(tree)
    if (tree.label == 'NUM'):
        f.write('   pushq $'+tree.items[0]+ "\n")
    elif (tree.label == 'VAR'):
        f.write(r'   pushq -'+str(fm[tree.items[0]])+r'(%rbp)'+"\n")
    elif (tree.label == '+'):
        walk(tree.items[0],f)
        walk(tree.items[1],f)
        f.write(r'   pop %rdi' + "\n")
        f.write(r'   pop %rax' + "\n")
        f.write(r'   add %rdi,%rax' + "\n")
        f.write(r'   pushq %rax' + "\n")
    elif (tree.label == '-'):
        walk(tree.items[0],f)
        walk(tree.items[1],f)
        f.write(r'   pop %rdi' + "\n")
        f.write(r'   pop %rax' + "\n")
        f.write(r'   sub %rdi,%rax' + "\n")
        f.write(r'   pushq %rax' + "\n")
    elif (tree.label == '*'):
        walk(tree.items[0],f)
        walk(tree.items[1],f)
        f.write(r'   pop %rdi' + "\n")
        f.write(r'   pop %rax' + "\n")
        f.write(r'   imul %rdi,%rax' + "\n")
        f.write(r'   pushq %rax' + "\n")
    # elif (tree.label == '/'):
    #     walk(tree.items[0],f)
    #     walk(tree.items[1],f)
    #     f.write(r'   pop %rdi' + "\n")
    #     f.write(r'   pop %rax' + "\n")
    #     f.write(r'   sub %rdi,%rax' + "\n")
    #     f.write(r'   pushq %rax' + "\n")
    elif (tree.label == 'DAINYU'):
        walk(tree.items[1],f)
        print(fm)
        f.write(r'   pop	%rax'+ "\n")
        f.write(r'   mov	%rax, -'+str(fm[tree.items[0]])+r'(%rbp)'+"\n")
    elif (tree.label == 'func'):
        returntype = tree.items[0]  # 戻り値の型
        funcname   = tree.items[1]  # 関数名
        f.write(r'   .globl	'+ funcname + "\n")
        f.write(r'   .type	'+ funcname + ', @function' + "\n")
        f.write(funcname + ":\n")
        f.write(r'   endbr64' + "\n")
        f.write(r'   pushq %rbp' + "\n")
        f.write(r'   movq %rsp, %rbp' + "\n")
        # ローカル変数のサイズ分スタックをずらす
        f.write(r'   subq $'+str(fc*8)+r',%rsp'+"\n")    # sizeof(int)を 8 とする。アライメント調整が面倒なので
        # 引数をスタックへコピーする
        regsmap = ('rdi','rsi','rdx','rcx','r8','r9')
        for idx in range(len(tree.items[2])):
            regname = regsmap[idx]
            address = (fc - idx) * 8
            f.write(r'   movq %'+ regname +',-'+ str(address) +'(%rbp)' + "\n")

        for item in tree.items[3]:
            walk(item,f)
        f.write(r'   .size '+funcname+', .-'+ funcname +"\n")
    #elif (tree.label == 'SENGEN'):
        # sengen
    elif (tree.label == 'return'):
        walk(tree.items[0],f)
        f.write(r'   pop	%rax'+ "\n")
        f.write(r'   leave'+ "\n")
        f.write(r'   ret'+ "\n")
    elif (tree.label == 'FUNCCALL'):
        for param in reversed(tree.items[1]):
            walk(param,f)
        regsmap = ('rdi','rsi','rdx','rcx','r8','r9')
        for idx in range(len(tree.items[1])):
            f.write(r' pop %' + regsmap[idx] + "\n")
        f.write(r'   call	'+tree.items[0] + "\n")
        f.write(r'   push	%rax'+"\n")
    elif (tree.label == 'EXPRESSION'):
        walk(tree.items[0],f)
    elif (tree.label == 'IF'):
        global label_count
        this_label_count = label_count
        label_count = label_count+1

        left_exp = tree.items[0][0] # 左辺
        right_exp = tree.items[0][2] # 右辺
        compare   = tree.items[0][1] # 比較 ==
        walk(left_exp,f)
        walk(right_exp,f)
        if (compare == '=='):
            f.write(r'   pop %rdi' + "\n")
            f.write(r'   pop %rax' + "\n")
            f.write(r'   cmp %rdi,%rax' + "\n")
            f.write(r'   jne .IFEND_'+str(this_label_count)+"\n")
            for item in tree.items[1]:
                walk(item,f)
            f.write(r'.IFEND_'+str(this_label_count)+':'+"\n")

def calcframesize( tree ):
    '''
        sizeof(int)の数
    '''
    return len(list( filter( lambda item: item.label == 'SENGEN' , tree ) ))

def createframemap( tree , params ):
    map = {}
    vars = list( filter( lambda item: item.label == 'SENGEN' , tree ) )
    size = len(vars) * 8 + len(params) * 8
    for param in params:
        map[param[1]] = size
        size -= 8
    for sen in vars:
        map[sen.items[1]] = size
        size -= 8
    return map

def codegen( tree , filename ):
    with open(filename, mode='w') as f:


        #asm の先頭
        f.write(r'   .text' + "\n")

        for teigi in tree:
            ##
            print('===codegen step1===')
            print(teigi)
            rettype  = teigi.items[0]    #戻り値の型 int
            funcname = teigi.items[1]    #関数名 main
            params   = teigi.items[2]    #引数

            global fc
            global fm
            fc = len(params)             #引数の個数
            fc = fc + calcframesize( teigi.items[3] )   # sizeof(int)の数
            fm = createframemap( teigi.items[3] , params ) 

            print( 'calcframesize :' + str(fc) )
            print( fm )

            print('===codegen step2===')
            print('funcname: '+funcname)

            walk(teigi,f)
