
            .text
            .globl	main
            .type	main, @function
        main:
            endbr64
            pushq	%rbp
            movq	%rsp, %rbp
           pushq $3
   pushq $1
   pop %rdi
   pop %rax
   sub %rdi,%rax
   pushq %rax
   pushq $1
   pop %rdi
   pop %rax
   sub %rdi,%rax
   pushq %rax
   pop	%rax

            popq	%rbp
            ret
        	.size	main, .-main
        