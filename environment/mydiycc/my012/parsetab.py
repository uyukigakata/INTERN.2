
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftOPTASUOPHIKUleftOPKAKEKAKKO KOKKA LBRACE NUMBER OPHIKU OPKAKE OPTASU RBRACE RETURN SEMI SYMBOL TYPE\n    teigi : kansuuteigi\n    \n    kansuuteigi : TYPE SYMBOL KAKKO KOKKA LBRACE bunlist RBRACE\n    \n    bunlist : bun\n            | bunlist bun\n    \n    bun : RETURN expression SEMI\n    \n    bun : TYPE SYMBOL SEMI\n    \n    expression : NUMBER\n               | expression OPTASU expression\n               | expression OPHIKU expression\n               | expression OPKAKE expression\n    '
    
_lr_action_items = {'TYPE':([0,7,9,10,14,17,18,],[3,8,8,-3,-4,-6,-5,]),'$end':([1,2,13,],[0,-1,-2,]),'SYMBOL':([3,8,],[4,12,]),'KAKKO':([4,],[5,]),'KOKKA':([5,],[6,]),'LBRACE':([6,],[7,]),'RETURN':([7,9,10,14,17,18,],[11,11,-3,-4,-6,-5,]),'RBRACE':([9,10,14,17,18,],[13,-3,-4,-6,-5,]),'NUMBER':([11,19,20,21,],[16,16,16,16,]),'SEMI':([12,15,16,22,23,24,],[17,18,-7,-8,-9,-10,]),'OPTASU':([15,16,22,23,24,],[19,-7,-8,-9,-10,]),'OPHIKU':([15,16,22,23,24,],[20,-7,-8,-9,-10,]),'OPKAKE':([15,16,22,23,24,],[21,-7,21,21,-10,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'teigi':([0,],[1,]),'kansuuteigi':([0,],[2,]),'bunlist':([7,],[9,]),'bun':([7,9,],[10,14,]),'expression':([11,19,20,21,],[15,22,23,24,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> teigi","S'",1,None,None,None),
  ('teigi -> kansuuteigi','teigi',1,'p_top','compile.py',17),
  ('kansuuteigi -> TYPE SYMBOL KAKKO KOKKA LBRACE bunlist RBRACE','kansuuteigi',7,'p_kansuuteigi','compile.py',24),
  ('bunlist -> bun','bunlist',1,'p_bunlist','compile.py',31),
  ('bunlist -> bunlist bun','bunlist',2,'p_bunlist','compile.py',32),
  ('bun -> RETURN expression SEMI','bun',3,'p_bun_return','compile.py',43),
  ('bun -> TYPE SYMBOL SEMI','bun',3,'p_bun_sengen','compile.py',50),
  ('expression -> NUMBER','expression',1,'p_expression','compile.py',57),
  ('expression -> expression OPTASU expression','expression',3,'p_expression','compile.py',58),
  ('expression -> expression OPHIKU expression','expression',3,'p_expression','compile.py',59),
  ('expression -> expression OPKAKE expression','expression',3,'p_expression','compile.py',60),
]
