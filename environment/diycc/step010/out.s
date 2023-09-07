  .text
  .globl	main
  .type	main, @function
main:
  endbr64
  pushq %rbp
  movq %rsp, %rbp
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
   popq	%rbp
   ret
   .size main, .-main
