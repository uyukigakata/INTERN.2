
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftOPTASUOPHIKUleftOPKAKEEQUALS KAKKO KOKKA LBRACE NUMBER OPHIKU OPKAKE OPTASU RBRACE RETURN SEMI SYMBOL TYPE\n    teigi : kansuuteigi\n          | teigi kansuuteigi\n    \n    kansuuteigi : TYPE SYMBOL KAKKO KOKKA LBRACE bunlist RBRACE\n    \n    kansuuteigi : TYPE SYMBOL KAKKO TYPE SYMBOL KOKKA LBRACE bunlist RBRACE\n    \n    bunlist : bun\n            | bunlist bun\n    \n    bun : RETURN expression SEMI\n    \n    bun : TYPE SYMBOL SEMI\n    \n    bun : SYMBOL EQUALS expression SEMI\n    \n    bun : expression SEMI\n    \n    expression : NUMBER\n               | expression OPTASU expression\n               | expression OPHIKU expression\n               | expression OPKAKE expression\n    \n    expression : SYMBOL\n    \n    expression : SYMBOL KAKKO KOKKA\n    \n    expression : SYMBOL KAKKO expression KOKKA\n    '
    
_lr_action_items = {'TYPE':([0,1,2,4,6,10,14,15,19,23,24,27,31,32,36,40,41,],[3,3,-1,-2,7,12,12,-5,12,-3,-6,-10,12,-8,-7,-4,-9,]),'$end':([1,2,4,23,40,],[0,-1,-2,-3,-4,]),'SYMBOL':([3,7,10,12,14,15,16,19,21,22,24,27,28,29,30,31,32,36,41,],[5,9,13,20,13,-5,26,13,26,26,-6,-10,26,26,26,13,-8,-7,-9,]),'KAKKO':([5,13,26,],[6,22,22,]),'KOKKA':([6,9,18,22,26,34,35,37,38,39,42,],[8,11,-11,34,-15,-16,42,-12,-13,-14,-17,]),'LBRACE':([8,11,],[10,19,]),'RETURN':([10,14,15,19,24,27,31,32,36,41,],[16,16,-5,16,-6,-10,16,-8,-7,-9,]),'NUMBER':([10,14,15,16,19,21,22,24,27,28,29,30,31,32,36,41,],[18,18,-5,18,18,18,18,-6,-10,18,18,18,18,-8,-7,-9,]),'EQUALS':([13,],[21,]),'SEMI':([13,17,18,20,25,26,33,34,37,38,39,42,],[-15,27,-11,32,36,-15,41,-16,-12,-13,-14,-17,]),'OPTASU':([13,17,18,25,26,33,34,35,37,38,39,42,],[-15,28,-11,28,-15,28,-16,28,-12,-13,-14,-17,]),'OPHIKU':([13,17,18,25,26,33,34,35,37,38,39,42,],[-15,29,-11,29,-15,29,-16,29,-12,-13,-14,-17,]),'OPKAKE':([13,17,18,25,26,33,34,35,37,38,39,42,],[-15,30,-11,30,-15,30,-16,30,30,30,-14,-17,]),'RBRACE':([14,15,24,27,31,32,36,41,],[23,-5,-6,-10,40,-8,-7,-9,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'teigi':([0,],[1,]),'kansuuteigi':([0,1,],[2,4,]),'bunlist':([10,19,],[14,31,]),'bun':([10,14,19,31,],[15,24,15,24,]),'expression':([10,14,16,19,21,22,28,29,30,31,],[17,17,25,17,33,35,37,38,39,17,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> teigi","S'",1,None,None,None),
  ('teigi -> kansuuteigi','teigi',1,'p_top','compile.py',19),
  ('teigi -> teigi kansuuteigi','teigi',2,'p_top','compile.py',20),
  ('kansuuteigi -> TYPE SYMBOL KAKKO KOKKA LBRACE bunlist RBRACE','kansuuteigi',7,'p_kansuuteigi','compile.py',33),
  ('kansuuteigi -> TYPE SYMBOL KAKKO TYPE SYMBOL KOKKA LBRACE bunlist RBRACE','kansuuteigi',9,'p_kansuuteigi_1','compile.py',40),
  ('bunlist -> bun','bunlist',1,'p_bunlist','compile.py',47),
  ('bunlist -> bunlist bun','bunlist',2,'p_bunlist','compile.py',48),
  ('bun -> RETURN expression SEMI','bun',3,'p_bun_return','compile.py',59),
  ('bun -> TYPE SYMBOL SEMI','bun',3,'p_bun_sengen','compile.py',66),
  ('bun -> SYMBOL EQUALS expression SEMI','bun',4,'p_bun_dainyu','compile.py',73),
  ('bun -> expression SEMI','bun',2,'p_bun_expression_only','compile.py',79),
  ('expression -> NUMBER','expression',1,'p_expression','compile.py',92),
  ('expression -> expression OPTASU expression','expression',3,'p_expression','compile.py',93),
  ('expression -> expression OPHIKU expression','expression',3,'p_expression','compile.py',94),
  ('expression -> expression OPKAKE expression','expression',3,'p_expression','compile.py',95),
  ('expression -> SYMBOL','expression',1,'p_expression_var','compile.py',106),
  ('expression -> SYMBOL KAKKO KOKKA','expression',3,'p_expression_funccall','compile.py',112),
  ('expression -> SYMBOL KAKKO expression KOKKA','expression',4,'p_expression_funccall_2','compile.py',118),
]