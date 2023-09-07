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

        exp = tree[1]
        
        f.write(header)
        walk(exp,f)
        f.write(r'   pop	%rax'+ "\n")
        f.write(footer)

