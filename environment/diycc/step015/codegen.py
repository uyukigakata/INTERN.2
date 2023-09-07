fm = {}
fc = 0

def walk( tree , f):
    print("!!entering walk!!")
    print(tree)
    if (tree.label == 'NUM'):
        f.write('   pushq $'+tree.items[0]+ "\n")
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
        for item in tree.items[2]:
            walk(item,f)
        f.write(r'   .size '+funcname+', .-'+ funcname +"\n")
    #elif (tree.label == 'SENGEN'):
        # sengen
    elif (tree.label == 'return'):
        walk(tree.items[0],f)
        f.write(r'   pop	%rax'+ "\n")
        f.write(r'   leave'+ "\n")
        f.write(r'   ret'+ "\n")
    

def calcframesize( tree ):
    '''
        sizeof(int)の数
    '''
    return len(list( filter( lambda item: item.label == 'SENGEN' , tree ) ))
def createframemap( tree ):
    map = {}
    vars = list( filter( lambda item: item.label == 'SENGEN' , tree ) )
    size = len(vars) * 8
    for sen in vars:
        map[sen.items[1]] = size
        size -= 8
    return map

def codegen( tree , filename ):
    with open(filename, mode='w') as f:

        ## １個目は関数の定義とする
        teigi1 = tree[0]

        ##
        print('===codegen step1===')
        print(teigi1)
        rettype  = teigi1.items[0]    #戻り値の型 int
        funcname = teigi1.items[1]    #関数名 main

        global fc
        global fm
        fc = calcframesize( teigi1.items[2] )   # sizeof(int)の数
        fm = createframemap( teigi1.items[2] ) 

        print( 'calcframesize :' + str(fc) )
        print( fm )
        
        # returnexp = list( filter( lambda item: item.label != 'SENGEN' , teigi1.items[2] ) )
        # print(returnexp)
        # dainyu_list = []
        # dainyu_list.append(returnexp[0])
        # dainyu_list.append(returnexp[1])
        # exp = returnexp[2].items[0]
        # exp      = teigi1[3][2][1] #文
        # print("exp:")
        # print(exp)
        # print("dainyu_list:")
        # print(dainyu_list)

        

        print('===codegen step2===')
        print('funcname: '+funcname)

        #asm の先頭
        f.write(r'   .text' + "\n")

        walk(teigi1,f)

        #関数ヘッダ
        # f.write(r'   .globl	'+ funcname + "\n")
        # f.write(r'   .type	'+ funcname + ', @function' + "\n")
        # f.write(funcname + ":\n")
        # f.write(r'   endbr64' + "\n")
        # f.write(r'   pushq %rbp' + "\n")
        # f.write(r'   movq %rsp, %rbp' + "\n")
        # # ローカル変数のサイズ分スタックをずらす
        # f.write(r'   subq $'+str(fc*8)+r',%rsp'+"\n")    # sizeof(int)を 8 とする。アライメント調整が面倒なので

        #代入のコードを生成する
        # for d in dainyu_list:
        #     walk(d.items[1],f)
        #     f.write(r'   pop	%rax'+ "\n")
        #     f.write(r'   mov	%rax, -'+str(fm[d.items[0]])+r'(%rbp)'+"\n")

        #式を歩く
        # walk(exp,f)
        # f.write(r'   pop	%rax'+ "\n")

        #関数フッダ
        # #f.write(r'   popq	%rbp'+ "\n")    #ローカル変数分スタックをずらしたので Leave で対処
        # f.write(r'   leave'+ "\n")
        # f.write(r'   ret'+ "\n")
        # f.write(r'   .size '+funcname+', .-'+ funcname +"\n")

