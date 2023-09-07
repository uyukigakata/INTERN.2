   .text
   .globl	func
   .type	func, @function
func:
   endbr64
   pushq %rbp
   movq %rsp, %rbp
   subq $24,%rsp
   movq %rdi,-24(%rbp)
   pushq $10
   pop	%rax
   mov	%rax, -16(%rbp)
   pushq $30
   pop	%rax
   mov	%rax, -8(%rbp)
   pushq -16(%rbp)
   pushq -8(%rbp)
   pop %rdi
   pop %rax
   add %rdi,%rax
   pushq %rax
   pushq -24(%rbp)
   pop %rdi
   pop %rax
   add %rdi,%rax
   pushq %rax
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
   pushq -16(%rbp)
   pushq $10
   pop %rdi
   pop %rax
   cmp %rdi,%rax
   jne .IFEND_0
   pushq $20
   pop	%rax
   mov	%rax, -8(%rbp)
.IFEND_0:
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
