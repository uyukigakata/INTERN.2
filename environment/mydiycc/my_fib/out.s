   .text
   .globl	fib
   .type	fib, @function
fib:
   endbr64
   pushq %rbp
   movq %rsp, %rbp
   subq $8,%rsp
   movq %rdi,-8(%rbp)
   pushq -8(%rbp)
   pushq $0
   pop %rdi
   pop %rax
   cmp %rdi,%rax
   jne .IFEND_0
   pushq $0
   pop	%rax
   leave
   ret
.IFEND_0:
   pushq -8(%rbp)
   pushq $1
   pop %rdi
   pop %rax
   cmp %rdi,%rax
   jne .IFEND_1
   pushq $1
   pop	%rax
   leave
   ret
.IFEND_1:
   pushq -8(%rbp)
   pushq $1
   pop %rdi
   pop %rax
   sub %rdi,%rax
   pushq %rax
 pop %rdi
   call	fib
   push	%rax
   pushq -8(%rbp)
   pushq $2
   pop %rdi
   pop %rax
   sub %rdi,%rax
   pushq %rax
 pop %rdi
   call	fib
   push	%rax
   pop %rdi
   pop %rax
   add %rdi,%rax
   pushq %rax
   pop	%rax
   leave
   ret
   .size fib, .-fib
   .globl	main
   .type	main, @function
main:
   endbr64
   pushq %rbp
   movq %rsp, %rbp
   subq $16,%rsp
   pushq $1
   pop	%rax
