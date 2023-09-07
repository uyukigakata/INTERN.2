
            .text
            .globl	main
            .type	main, @function
        main:
            endbr64
            pushq	%rbp
            movq	%rsp, %rbp
           movl	$8, %eax
            popq	%rbp
            ret
        	.size	main, .-main
        