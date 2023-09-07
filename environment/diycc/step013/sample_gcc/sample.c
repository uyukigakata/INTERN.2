int foo(){
	int x =0;
	int y =1;
    return x+y;
}
int main(){
	int x =0;
	int y =1;
	foo();
    return x+y;
}
/*
gcc -S sample.c 

 -fno-asynchronous-unwind-tables 
gcc  -fno-asynchronous-unwind-tables  -S sample.c 


	.text
	.globl	main
	.type	main, @function
main:
	endbr64
	pushq	%rbp
	movq	%rsp, %rbp
	movl	$3, %eax
	popq	%rbp
	ret
	.size	main, .-main
	.ident	"GCC: (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0"
	.section	.note.GNU-stack,"",@progbits
	.section	.note.gnu.property,"a"
	.align 8
	.long	 1f - 0f
	.long	 4f - 1f
	.long	 5
0:
	.string	 "GNU"
1:
	.align 8
	.long	 0xc0000002
	.long	 3f - 2f
2:
	.long	 0x3
3:
	.align 8
4:



*/