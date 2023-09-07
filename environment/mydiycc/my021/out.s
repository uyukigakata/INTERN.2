  .text
   .globl	func
   .type	func, @function
func:
   endbr64
   pushq %rbp
   movq %rsp, %rbp
   subq $0,%rsp
   pushq $10
   pop	%rax
   leave
   ret
   .size func, .-func
   .globl	main
   .type	main, @function
main:
   endbr64
   pushq %rbp
   movq %rsp, %rbp
   subq $16,%rsp
   pushq $10
   pop	%rax
   mov	%rax, -16(%rbp)
   pushq $20
   pop	%rax
   mov	%rax, -8(%rbp)
   call	func
   push   %rax
   pushq -16(%rbp)
   pushq -8(%rbp)
   pop %rdi
   pop %rax
   add %rdi,%rax
   pushq %rax
   pop	%rax
   leave
   ret
   .size main, .-main
