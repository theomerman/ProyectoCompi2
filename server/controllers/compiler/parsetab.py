
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADD ALTER AND AT BASE COLUMN COMMA COMPARE CREATE DATA DATE DECIMAL DECIMALES DIFFERENT DIVIDE EQUAL FROM GREATER GREATER_EQUAL ID INSERT INT INTO KEY LESS LESS_EQUAL LPAREN MINUS NOT NOT_EQUAL NOT_SYMBOL NULL NUMBER NVARCHAR OR PERIOD PLUS PRIMARY REFERENCE RPAREN SELECT SEMICOLOM STRING TABLE TIMES USE VALUES WHEREinit : statement init\n            | statement\n            statement : create_database\n                | use_database\n                | create_table\n                \n                create_database : CREATE DATA BASE ID SEMICOLOMuse_database : USE ID SEMICOLOM\n    create_table : CREATE TABLE ID LPAREN columns RPAREN SEMICOLOM\n    \n    columns : columns COMMA column\n            | column\n    \n    column : ID type attributes\n    \n    type : INT\n         | DATE\n         | NVARCHAR LPAREN NUMBER RPAREN\n         | DECIMAL\n    \n    attributes : attributes attribute\n               | attribute\n               | empty\n    \n    attribute : PRIMARY KEY\n              | REFERENCE ID LPAREN ID RPAREN\n              | NOT NULL\n    empty :'
    
_lr_action_items = {'CREATE':([0,2,3,4,5,14,17,35,],[6,6,-3,-4,-5,-7,-6,-8,]),'USE':([0,2,3,4,5,14,17,35,],[7,7,-3,-4,-5,-7,-6,-8,]),'$end':([1,2,3,4,5,8,14,17,35,],[0,-2,-3,-4,-5,-1,-7,-6,-8,]),'DATA':([6,],[9,]),'TABLE':([6,],[10,]),'ID':([7,10,12,16,27,32,42,],[11,13,15,18,18,39,44,]),'BASE':([9,],[12,]),'SEMICOLOM':([11,15,26,],[14,17,35,]),'LPAREN':([13,24,39,],[16,34,42,]),'INT':([18,],[22,]),'DATE':([18,],[23,]),'NVARCHAR':([18,],[24,]),'DECIMAL':([18,],[25,]),'RPAREN':([19,20,21,22,23,25,28,29,30,36,37,38,40,41,43,44,45,],[26,-10,-22,-12,-13,-15,-11,-17,-18,-9,-16,-19,-21,43,-14,45,-20,]),'COMMA':([19,20,21,22,23,25,28,29,30,36,37,38,40,43,45,],[27,-10,-22,-12,-13,-15,-11,-17,-18,-9,-16,-19,-21,-14,-20,]),'PRIMARY':([21,22,23,25,28,29,30,37,38,40,43,45,],[31,-12,-13,-15,31,-17,-18,-16,-19,-21,-14,-20,]),'REFERENCE':([21,22,23,25,28,29,30,37,38,40,43,45,],[32,-12,-13,-15,32,-17,-18,-16,-19,-21,-14,-20,]),'NOT':([21,22,23,25,28,29,30,37,38,40,43,45,],[33,-12,-13,-15,33,-17,-18,-16,-19,-21,-14,-20,]),'KEY':([31,],[38,]),'NULL':([33,],[40,]),'NUMBER':([34,],[41,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,2,],[1,8,]),'statement':([0,2,],[2,2,]),'create_database':([0,2,],[3,3,]),'use_database':([0,2,],[4,4,]),'create_table':([0,2,],[5,5,]),'columns':([16,],[19,]),'column':([16,27,],[20,36,]),'type':([18,],[21,]),'attributes':([21,],[28,]),'attribute':([21,28,],[29,37,]),'empty':([21,],[30,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> statement init','init',2,'p_init','parser.py',14),
  ('init -> statement','init',1,'p_init','parser.py',15),
  ('statement -> create_database','statement',1,'p_statement','parser.py',20),
  ('statement -> use_database','statement',1,'p_statement','parser.py',21),
  ('statement -> create_table','statement',1,'p_statement','parser.py',22),
  ('create_database -> CREATE DATA BASE ID SEMICOLOM','create_database',5,'p_create_database','parser.py',30),
  ('use_database -> USE ID SEMICOLOM','use_database',3,'p_use_database','parser.py',39),
  ('create_table -> CREATE TABLE ID LPAREN columns RPAREN SEMICOLOM','create_table',7,'p_create_table','parser.py',47),
  ('columns -> columns COMMA column','columns',3,'p_columns','parser.py',54),
  ('columns -> column','columns',1,'p_columns','parser.py',55),
  ('column -> ID type attributes','column',3,'p_column','parser.py',65),
  ('type -> INT','type',1,'p_type','parser.py',85),
  ('type -> DATE','type',1,'p_type','parser.py',86),
  ('type -> NVARCHAR LPAREN NUMBER RPAREN','type',4,'p_type','parser.py',87),
  ('type -> DECIMAL','type',1,'p_type','parser.py',88),
  ('attributes -> attributes attribute','attributes',2,'p_attributes','parser.py',101),
  ('attributes -> attribute','attributes',1,'p_attributes','parser.py',102),
  ('attributes -> empty','attributes',1,'p_attributes','parser.py',103),
  ('attribute -> PRIMARY KEY','attribute',2,'p_attribute','parser.py',126),
  ('attribute -> REFERENCE ID LPAREN ID RPAREN','attribute',5,'p_attribute','parser.py',127),
  ('attribute -> NOT NULL','attribute',2,'p_attribute','parser.py',128),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',140),
]
