def walk( tree , f):
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

def codegen( tree , filename ):
    with open(filename, mode='w') as f:

        ## １個目は関数の定義とする
        teigi1 = tree[0]

        ##
        print('===codegen step1===')
        print(teigi1)
        rettype  = teigi1.items[0]    #戻り値の型 int
        funcname = teigi1.items[1]    #関数名 main

        exp = []
        returnexp = list( filter( lambda item: item.label != 'SENGEN' , teigi1.items[2] ) )
        print(returnexp)
        exp = returnexp[0].items[0]
        # exp      = teigi1[3][2][1] #文
        print(exp)

        print('===codegen step2===')
        print('funcname: '+funcname)

        #asm の先頭
        f.write(r'   .text' + "\n")

        #関数ヘッダ
        f.write(r'   .globl	'+ funcname + "\n")
        f.write(r'   .type	'+ funcname + ', @function' + "\n")
        f.write(funcname + ":\n")
        f.write(r'   endbr64' + "\n")
        f.write(r'   pushq %rbp' + "\n")
        f.write(r'   movq %rsp, %rbp' + "\n")

        #式を歩く
        walk(exp,f)
        f.write(r'   pop	%rax'+ "\n")

        #関数フッダ
        f.write(r'   popq	%rbp'+ "\n")
        f.write(r'   ret'+ "\n")
        f.write(r'   .size '+funcname+', .-'+ funcname +"\n")

