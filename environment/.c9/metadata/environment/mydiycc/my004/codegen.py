{"filter":false,"title":"codegen.py","tooltip":"/mydiycc/my004/codegen.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":23,"column":0},"action":"insert","lines":["def codegen( tree , filename ):","    with open(filename, mode='w') as f:","        header = '''","            .text","            .globl\tmain","            .type\tmain, @function","        main:","            endbr64","            pushq\t%rbp","            movq\t%rsp, %rbp","        '''","","        footer = '''","            popq\t%rbp","            ret","        \t.size\tmain, .-main","        '''","","        retval = tree[1]","        f.write(header)","        f.write('   movl\t$'+ retval +', %eax')","        f.write(footer)","",""],"id":1}]]},"ace":{"folds":[],"scrolltop":192,"scrollleft":0,"selection":{"start":{"row":12,"column":20},"end":{"row":12,"column":20},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":10,"state":"start","mode":"ace/mode/python"}},"timestamp":1693536890640,"hash":"5d1e2bdc0a561e070e51d19ecc2ac07789880083"}