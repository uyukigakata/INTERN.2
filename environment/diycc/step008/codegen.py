def walk( tree , f):
    if (tree[0] == 'NUM'):
        f.write('   pushq $'+tree[1]+ "\n")
    elif (tree[0] == '+'):
        walk(tree[1],f)
        walk(tree[2],f)
        f.write(r'   pop %rdi' + "\n")
        f.write(r'   pop %rax' + "\n")
        f.write(r'   add %rdi,%rax' + "\n")
        f.write(r'   pushq %rax' + "\n")
    elif (tree[0] == '-'):
        walk(tree[1],f)
        walk(tree[2],f)
        f.write(r'   pop %rdi' + "\n")
        f.write(r'   pop %rax' + "\n")
        f.write(r'   sub %rdi,%rax' + "\n")
        f.write(r'   pushq %rax' + "\n")
    elif (tree[0] == '*'):
        walk(tree[1],f)
        walk(tree[2],f)
        f.write(r'   pop %rdi' + "\n")
        f.write(r'   pop %rax' + "\n")
        f.write(r'   imul %rdi,%rax' + "\n")
        f.write(r'   pushq %rax' + "\n")
    # elif (tree[0] == '/'):
    #     walk(tree[1],f)
    #     walk(tree[2],f)
    #     f.write(r'   pop %rdi' + "\n")
    #     f.write(r'   pop %rax' + "\n")
    #     f.write(r'   sub %rdi,%rax' + "\n")
    #     f.write(r'   pushq %rax' + "\n")

def codegen( tree , filename ):
    with open(filename, mode='w') as f:
        header = '''
            .text
            .globl	main
            .type	main, @function
        main:
            endbr64
            pushq	%rbp
            movq	%rsp, %rbp
        '''

        footer = '''
            popq	%rbp
            ret
        	.size	main, .-main
        '''

        ## １個目は関数の定義とする
        teigi1 = tree[0]

        ##
        print('===codegen step1===')
        print(teigi1)
        rettype  = teigi1[1]    #戻り値の型 int
        funcname = teigi1[2]    #関数名 main
        exp      = teigi1[3][1] #文
        print(exp)

        print('===codegen step2===')
        print('funcname: '+funcname)

        #asm の先頭
        f.write(r'  .text' + "\n")

        #関数ヘッダ
        f.write(r'  .globl	'+ funcname + "\n")
        f.write(r'  .type	'+ funcname + ', @function' + "\n")
        f.write(funcname + ":\n")
        f.write(r'  endbr64' + "\n")
        f.write(r'  pushq %rbp' + "\n")
        f.write(r'  movq %rsp, %rbp' + "\n")

        #式を歩く
        walk(exp,f)
        f.write(r'   pop	%rax'+ "\n")

        #関数フッダ
        f.write(r'   popq	%rbp'+ "\n")
        f.write(r'   ret'+ "\n")
        f.write(r'   .size '+funcname+', .-'+ funcname +"\n")

