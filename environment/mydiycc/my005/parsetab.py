
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'NUMBER OPHIKU OPTASU RETURN SEMI\n    teigi : RETURN expression SEMI\n    \n    expression : NUMBER\n               | expression OPTASU NUMBER\n               | expression OPHIKU NUMBER\n    '
    
_lr_action_items = {'RETURN':([0,],[2,]),'$end':([1,5,],[0,-1,]),'NUMBER':([2,6,7,],[4,8,9,]),'SEMI':([3,4,8,9,],[5,-2,-3,-4,]),'OPTASU':([3,4,8,9,],[6,-2,-3,-4,]),'OPHIKU':([3,4,8,9,],[7,-2,-3,-4,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'teigi':([0,],[1,]),'expression':([2,],[3,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> teigi","S'",1,None,None,None),
  ('teigi -> RETURN expression SEMI','teigi',3,'p_top','compile.py',8),
  ('expression -> NUMBER','expression',1,'p_expression','compile.py',15),
  ('expression -> expression OPTASU NUMBER','expression',3,'p_expression','compile.py',16),
  ('expression -> expression OPHIKU NUMBER','expression',3,'p_expression','compile.py',17),
]