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

        retval = tree[1]
        f.write(header)
        f.write('   movl	$'+ retval +', %eax')
        f.write(footer)

