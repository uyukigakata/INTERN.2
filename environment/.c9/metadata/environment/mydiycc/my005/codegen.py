{"filter":false,"title":"codegen.py","tooltip":"/mydiycc/my005/codegen.py","undoManager":{"mark":3,"position":3,"stack":[[{"start":{"row":0,"column":0},"end":{"row":43,"column":0},"action":"insert","lines":["ef walk( tree , f):","    if (tree[0] == 'NUM'):","        f.write('   pushq $'+tree[1]+ \"\\n\")","    elif (tree[0] == '+'):","        walk(tree[1],f)","        walk(tree[2],f)","        f.write(r'   pop %rdi' + \"\\n\")","        f.write(r'   pop %rax' + \"\\n\")","        f.write(r'   add %rdi,%rax' + \"\\n\")","        f.write(r'   pushq %rax' + \"\\n\")","    elif (tree[0] == '-'):","        walk(tree[1],f)","        walk(tree[2],f)","        f.write(r'   pop %rdi' + \"\\n\")","        f.write(r'   pop %rax' + \"\\n\")","        f.write(r'   sub %rdi,%rax' + \"\\n\")","        f.write(r'   pushq %rax' + \"\\n\")","","def codegen( tree , filename ):","    with open(filename, mode='w') as f:","        header = '''","            .text","            .globl\tmain","            .type\tmain, @function","        main:","            endbr64","            pushq\t%rbp","            movq\t%rsp, %rbp","        '''","","        footer = '''","            popq\t%rbp","            ret","        \t.size\tmain, .-main","        '''","","        exp = tree[1]","        ","        f.write(header)","        walk(exp,f)","        f.write(r'   pop\t%rax'+ \"\\n\")","        f.write(footer)","",""],"id":1}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"insert","lines":["s"],"id":2}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"remove","lines":["s"],"id":3}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"insert","lines":["d"],"id":4}]]},"ace":{"folds":[],"scrolltop":492,"scrollleft":0,"selection":{"start":{"row":1,"column":13},"end":{"row":1,"column":13},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":31,"state":"qstring3","mode":"ace/mode/python"}},"timestamp":1693542665047,"hash":"8ee29d57ee7c69026d8b0d43481172c1f41d0aad"}