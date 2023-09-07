   .text
   .globl	main
   .type	main, @function
main:
   endbr64
   pushq %rbp
   movq %rsp, %rbp
   subq $16,%rsp
   pushq $3
   pushq $2
   pushq $3
   pop %rdi
   pop %rax
   imul %rdi,%rax
   pushq %rax
   pop %rdi
   pop %rax
   add %rdi,%rax
   pushq %rax
   pop	%rax
   leave
   ret
   .size main, .-main
