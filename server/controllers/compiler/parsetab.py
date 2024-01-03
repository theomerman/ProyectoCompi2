
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDEleftANDAND_WORDleftORleftEQUALDIFFERENTGREATERLESSGREATER_EQUALLESS_EQUALrightUMINUSADD ALTER AND AND_WORD AT BASE CAST COLUMN COMMA COMPARE CONCATENA CONTAR CREATE DATA DATE DECIMAL DECIMALES DIFFERENT DIVIDE DROP EQUAL FROM GREATER GREATER_EQUAL HOY ID INSERT INT INTO KEY LESS LESS_EQUAL LPAREN MINUS NOT NOT_EQUAL NOT_SYMBOL NULL NUMBER NVARCHAR OR PERIOD PLUS PRIMARY REFERENCE RPAREN SELECT SEMICOLON STRING SUBSTRAER SUMA TABLE TIMES USE VALUES WHEREinit : statement init\n            | statement\n            statement : create_database\n                | use_database\n                | create_table\n                | insert_into\n                | alter_table\n                | select_total\n                create_database : CREATE DATA BASE ID SEMICOLONuse_database : USE ID SEMICOLON\n    create_table : CREATE TABLE ID LPAREN columns RPAREN SEMICOLON\n\n    \n    columns : columns COMMA column\n            | column\n    \n    column : ID type attributes\n    \n    type : INT\n         | DATE\n         | NVARCHAR LPAREN NUMBER RPAREN\n         | DECIMAL\n    \n    attributes : attributes attribute\n               | attribute\n               | empty\n    \n    attribute : PRIMARY KEY\n              | REFERENCE ID LPAREN ID RPAREN\n              | NOT NULL\n    \n    insert_into : INSERT INTO ID LPAREN ids RPAREN VALUES LPAREN primitives RPAREN SEMICOLON\n    \n    ids : ids COMMA ID\n        | ID\n    \n    primitives  : primitives COMMA primitive\n                | primitive\n    \n    primitive   : NUMBER\n                | DECIMALES\n                | STRING\n    \n    alter_table : ALTER TABLE ID ADD COLUMN ID type SEMICOLON\n                | ALTER TABLE ID DROP COLUMN ID SEMICOLON\n    \n    select_total : SELECT select_columns from_statement SEMICOLON\n    \n    select_columns  : select_columns COMMA select_column\n                    | select_column\n    \n    select_column   : concatena\n                    | substraer\n                    | hoy\n                    | contar\n                    | suma\n                    | parameters_two\n                    | TIMES\n    \n    from_statement  : FROM ids where_statement\n                    | empty\n    \n    where_statement : WHERE expression\n                    | empty\n    \n    expression : expression PLUS expression\n                | expression MINUS expression\n                | expression TIMES expression\n                | expression DIVIDE expression\n\n                | expression EQUAL expression\n                | expression DIFFERENT expression\n                | expression GREATER expression\n                | expression LESS expression\n                | expression GREATER_EQUAL expression\n                | expression LESS_EQUAL expression\n\n                | expression AND expression\n                | expression AND_WORD expression\n                | expression OR expression\n                | expression NOT_SYMBOL expression\n    expression : MINUS expression %prec UMINUS\n    expression  : LPAREN expression RPAREN\n                | NUMBER\n                | DECIMALES\n                | STRING\n\n    \n    expression  : ID PERIOD ID\n                | ID\n    \n    concatena : CONCATENA LPAREN concatena_parameters RPAREN\n    \n    concatena_parameters    : concatena_parameters COMMA parameters_one\n                            | parameters_one\n    \n    parameters_one  : STRING\n                    | ID PERIOD ID\n                    | ID\n    \n    substraer : SUBSTRAER LPAREN parameters_one COMMA NUMBER COMMA NUMBER RPAREN\n    \n    hoy : HOY LPAREN RPAREN\n    \n    contar : CONTAR LPAREN contar_parameters RPAREN\n    \n    contar_parameters   : TIMES\n                        | ID PERIOD ID\n                        | ID \n    \n    suma : SUMA LPAREN parameters_two RPAREN\n\n    \n    parameters_two  : ID PERIOD ID\n                    | ID\n    empty :'
    
_lr_action_items = {'CREATE':([0,2,3,4,5,6,7,8,37,55,70,117,121,146,176,],[9,9,-3,-4,-5,-6,-7,-8,-10,-35,-9,-11,-34,-33,-25,]),'USE':([0,2,3,4,5,6,7,8,37,55,70,117,121,146,176,],[10,10,-3,-4,-5,-6,-7,-8,-10,-35,-9,-11,-34,-33,-25,]),'INSERT':([0,2,3,4,5,6,7,8,37,55,70,117,121,146,176,],[11,11,-3,-4,-5,-6,-7,-8,-10,-35,-9,-11,-34,-33,-25,]),'ALTER':([0,2,3,4,5,6,7,8,37,55,70,117,121,146,176,],[12,12,-3,-4,-5,-6,-7,-8,-10,-35,-9,-11,-34,-33,-25,]),'SELECT':([0,2,3,4,5,6,7,8,37,55,70,117,121,146,176,],[13,13,-3,-4,-5,-6,-7,-8,-10,-35,-9,-11,-34,-33,-25,]),'$end':([1,2,3,4,5,6,7,8,14,37,55,70,117,121,146,176,],[0,-2,-3,-4,-5,-6,-7,-8,-1,-10,-35,-9,-11,-34,-33,-25,]),'DATA':([9,],[15,]),'TABLE':([9,12,],[16,19,]),'ID':([10,13,16,18,19,35,41,42,44,45,47,48,49,51,52,75,76,78,79,82,83,86,94,100,101,114,122,123,124,125,126,127,128,129,130,131,132,133,134,135,138,164,],[17,34,36,38,39,50,34,58,62,62,67,34,69,71,58,96,97,98,105,62,107,109,71,105,105,142,105,105,105,105,105,105,105,105,105,105,105,105,105,105,162,172,]),'INTO':([11,],[18,]),'TIMES':([13,41,47,99,102,103,104,105,136,137,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,],[28,28,66,124,-65,-66,-67,-69,-63,124,124,124,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,124,-64,-68,]),'CONCATENA':([13,41,],[29,29,]),'SUBSTRAER':([13,41,],[30,30,]),'HOY':([13,41,],[31,31,]),'CONTAR':([13,41,],[32,32,]),'SUMA':([13,41,],[33,33,]),'BASE':([15,],[35,]),'SEMICOLON':([17,20,21,22,23,24,25,26,27,28,34,40,43,50,56,57,58,64,69,77,80,81,85,87,89,90,92,93,97,98,99,102,103,104,105,120,136,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,165,171,173,],[37,-85,-37,-38,-39,-40,-41,-42,-43,-44,-84,55,-46,70,-36,-85,-27,-77,-83,-45,-48,-70,-78,-82,-15,-16,-18,117,121,-26,-47,-65,-66,-67,-69,146,-63,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-64,-68,-17,-76,176,]),'COMMA':([20,21,22,23,24,25,26,27,28,34,56,57,58,59,60,61,62,63,64,69,72,73,74,81,85,87,88,89,90,92,98,106,107,108,110,111,112,118,140,141,143,165,166,167,168,169,170,171,175,177,],[41,-37,-38,-39,-40,-41,-42,-43,-44,-84,-36,78,-27,82,-72,-73,-75,84,-77,-83,94,-13,78,-70,-78,-82,-85,-15,-16,-18,-26,-71,-74,139,-14,-20,-21,-12,-19,-22,-24,-17,174,-29,-30,-31,-32,-76,-23,-28,]),'FROM':([20,21,22,23,24,25,26,27,28,34,56,64,69,81,85,87,171,],[42,-37,-38,-39,-40,-41,-42,-43,-44,-84,-36,-77,-83,-70,-78,-82,-76,]),'LPAREN':([29,30,31,32,33,36,38,79,91,100,101,119,122,123,124,125,126,127,128,129,130,131,132,133,134,135,142,],[44,45,46,47,48,51,52,101,116,101,101,145,101,101,101,101,101,101,101,101,101,101,101,101,101,101,164,]),'PERIOD':([34,62,67,105,],[49,83,86,138,]),'RPAREN':([34,46,58,59,60,61,62,65,66,67,68,69,72,73,74,88,89,90,92,98,102,103,104,105,106,107,109,110,111,112,118,136,137,140,141,143,144,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,165,166,167,168,169,170,172,175,177,],[-84,64,-27,81,-72,-73,-75,85,-79,-81,87,-83,93,-13,95,-85,-15,-16,-18,-26,-65,-66,-67,-69,-71,-74,-80,-14,-20,-21,-12,-63,161,-19,-22,-24,165,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-64,-68,171,-17,173,-29,-30,-31,-32,175,-23,-28,]),'ADD':([39,],[53,]),'DROP':([39,],[54,]),'STRING':([44,45,79,82,100,101,122,123,124,125,126,127,128,129,130,131,132,133,134,135,145,174,],[61,61,104,61,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,170,170,]),'COLUMN':([53,54,],[75,76,]),'WHERE':([57,58,98,],[79,-27,-26,]),'INT':([71,96,],[89,89,]),'DATE':([71,96,],[90,90,]),'NVARCHAR':([71,96,],[91,91,]),'DECIMAL':([71,96,],[92,92,]),'MINUS':([79,99,100,101,102,103,104,105,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,],[100,123,100,100,-65,-66,-67,-69,100,100,100,100,100,100,100,100,100,100,100,100,100,100,-63,123,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,123,-64,-68,]),'NUMBER':([79,84,100,101,116,122,123,124,125,126,127,128,129,130,131,132,133,134,135,139,145,174,],[102,108,102,102,144,102,102,102,102,102,102,102,102,102,102,102,102,102,102,163,168,168,]),'DECIMALES':([79,100,101,122,123,124,125,126,127,128,129,130,131,132,133,134,135,145,174,],[103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,169,169,]),'PRIMARY':([88,89,90,92,110,111,112,140,141,143,165,175,],[113,-15,-16,-18,113,-20,-21,-19,-22,-24,-17,-23,]),'REFERENCE':([88,89,90,92,110,111,112,140,141,143,165,175,],[114,-15,-16,-18,114,-20,-21,-19,-22,-24,-17,-23,]),'NOT':([88,89,90,92,110,111,112,140,141,143,165,175,],[115,-15,-16,-18,115,-20,-21,-19,-22,-24,-17,-23,]),'VALUES':([95,],[119,]),'PLUS':([99,102,103,104,105,136,137,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,],[122,-65,-66,-67,-69,-63,122,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,122,-64,-68,]),'DIVIDE':([99,102,103,104,105,136,137,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,],[125,-65,-66,-67,-69,-63,125,125,125,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,125,-64,-68,]),'EQUAL':([99,102,103,104,105,136,137,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,],[126,-65,-66,-67,-69,-63,126,126,126,126,126,-53,-54,-55,-56,-57,-58,126,126,126,126,-64,-68,]),'DIFFERENT':([99,102,103,104,105,136,137,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,],[127,-65,-66,-67,-69,-63,127,127,127,127,127,-53,-54,-55,-56,-57,-58,127,127,127,127,-64,-68,]),'GREATER':([99,102,103,104,105,136,137,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,],[128,-65,-66,-67,-69,-63,128,128,128,128,128,-53,-54,-55,-56,-57,-58,128,128,128,128,-64,-68,]),'LESS':([99,102,103,104,105,136,137,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,],[129,-65,-66,-67,-69,-63,129,129,129,129,129,-53,-54,-55,-56,-57,-58,129,129,129,129,-64,-68,]),'GREATER_EQUAL':([99,102,103,104,105,136,137,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,],[130,-65,-66,-67,-69,-63,130,130,130,130,130,-53,-54,-55,-56,-57,-58,130,130,130,130,-64,-68,]),'LESS_EQUAL':([99,102,103,104,105,136,137,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,],[131,-65,-66,-67,-69,-63,131,131,131,131,131,-53,-54,-55,-56,-57,-58,131,131,131,131,-64,-68,]),'AND':([99,102,103,104,105,136,137,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,],[132,-65,-66,-67,-69,-63,132,132,132,132,132,-53,-54,-55,-56,-57,-58,-59,-60,-61,132,-64,-68,]),'AND_WORD':([99,102,103,104,105,136,137,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,],[133,-65,-66,-67,-69,-63,133,133,133,133,133,-53,-54,-55,-56,-57,-58,-59,-60,-61,133,-64,-68,]),'OR':([99,102,103,104,105,136,137,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,],[134,-65,-66,-67,-69,-63,134,134,134,134,134,-53,-54,-55,-56,-57,-58,134,134,-61,134,-64,-68,]),'NOT_SYMBOL':([99,102,103,104,105,136,137,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,],[135,-65,-66,-67,-69,-63,135,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,135,-64,-68,]),'KEY':([113,],[141,]),'NULL':([115,],[143,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,2,],[1,14,]),'statement':([0,2,],[2,2,]),'create_database':([0,2,],[3,3,]),'use_database':([0,2,],[4,4,]),'create_table':([0,2,],[5,5,]),'insert_into':([0,2,],[6,6,]),'alter_table':([0,2,],[7,7,]),'select_total':([0,2,],[8,8,]),'select_columns':([13,],[20,]),'select_column':([13,41,],[21,56,]),'concatena':([13,41,],[22,22,]),'substraer':([13,41,],[23,23,]),'hoy':([13,41,],[24,24,]),'contar':([13,41,],[25,25,]),'suma':([13,41,],[26,26,]),'parameters_two':([13,41,48,],[27,27,68,]),'from_statement':([20,],[40,]),'empty':([20,57,88,],[43,80,112,]),'ids':([42,52,],[57,74,]),'concatena_parameters':([44,],[59,]),'parameters_one':([44,45,82,],[60,63,106,]),'contar_parameters':([47,],[65,]),'columns':([51,],[72,]),'column':([51,94,],[73,118,]),'where_statement':([57,],[77,]),'type':([71,96,],[88,120,]),'expression':([79,100,101,122,123,124,125,126,127,128,129,130,131,132,133,134,135,],[99,136,137,147,148,149,150,151,152,153,154,155,156,157,158,159,160,]),'attributes':([88,],[110,]),'attribute':([88,110,],[111,140,]),'primitives':([145,],[166,]),'primitive':([145,174,],[167,177,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> statement init','init',2,'p_init','parser.py',22),
  ('init -> statement','init',1,'p_init','parser.py',23),
  ('statement -> create_database','statement',1,'p_statement','parser.py',28),
  ('statement -> use_database','statement',1,'p_statement','parser.py',29),
  ('statement -> create_table','statement',1,'p_statement','parser.py',30),
  ('statement -> insert_into','statement',1,'p_statement','parser.py',31),
  ('statement -> alter_table','statement',1,'p_statement','parser.py',32),
  ('statement -> select_total','statement',1,'p_statement','parser.py',33),
  ('create_database -> CREATE DATA BASE ID SEMICOLON','create_database',5,'p_create_database','parser.py',38),
  ('use_database -> USE ID SEMICOLON','use_database',3,'p_use_database','parser.py',50),
  ('create_table -> CREATE TABLE ID LPAREN columns RPAREN SEMICOLON','create_table',7,'p_create_table','parser.py',62),
  ('columns -> columns COMMA column','columns',3,'p_columns','parser.py',74),
  ('columns -> column','columns',1,'p_columns','parser.py',75),
  ('column -> ID type attributes','column',3,'p_column','parser.py',85),
  ('type -> INT','type',1,'p_type','parser.py',105),
  ('type -> DATE','type',1,'p_type','parser.py',106),
  ('type -> NVARCHAR LPAREN NUMBER RPAREN','type',4,'p_type','parser.py',107),
  ('type -> DECIMAL','type',1,'p_type','parser.py',108),
  ('attributes -> attributes attribute','attributes',2,'p_attributes','parser.py',121),
  ('attributes -> attribute','attributes',1,'p_attributes','parser.py',122),
  ('attributes -> empty','attributes',1,'p_attributes','parser.py',123),
  ('attribute -> PRIMARY KEY','attribute',2,'p_attribute','parser.py',146),
  ('attribute -> REFERENCE ID LPAREN ID RPAREN','attribute',5,'p_attribute','parser.py',147),
  ('attribute -> NOT NULL','attribute',2,'p_attribute','parser.py',148),
  ('insert_into -> INSERT INTO ID LPAREN ids RPAREN VALUES LPAREN primitives RPAREN SEMICOLON','insert_into',11,'p_insert_into','parser.py',159),
  ('ids -> ids COMMA ID','ids',3,'p_ids','parser.py',169),
  ('ids -> ID','ids',1,'p_ids','parser.py',170),
  ('primitives -> primitives COMMA primitive','primitives',3,'p_primitives','parser.py',178),
  ('primitives -> primitive','primitives',1,'p_primitives','parser.py',179),
  ('primitive -> NUMBER','primitive',1,'p_primitive','parser.py',187),
  ('primitive -> DECIMALES','primitive',1,'p_primitive','parser.py',188),
  ('primitive -> STRING','primitive',1,'p_primitive','parser.py',189),
  ('alter_table -> ALTER TABLE ID ADD COLUMN ID type SEMICOLON','alter_table',8,'p_alter_table','parser.py',196),
  ('alter_table -> ALTER TABLE ID DROP COLUMN ID SEMICOLON','alter_table',7,'p_alter_table','parser.py',197),
  ('select_total -> SELECT select_columns from_statement SEMICOLON','select_total',4,'p_select_total','parser.py',219),
  ('select_columns -> select_columns COMMA select_column','select_columns',3,'p_select_columns','parser.py',230),
  ('select_columns -> select_column','select_columns',1,'p_select_columns','parser.py',231),
  ('select_column -> concatena','select_column',1,'p_select_column','parser.py',240),
  ('select_column -> substraer','select_column',1,'p_select_column','parser.py',241),
  ('select_column -> hoy','select_column',1,'p_select_column','parser.py',242),
  ('select_column -> contar','select_column',1,'p_select_column','parser.py',243),
  ('select_column -> suma','select_column',1,'p_select_column','parser.py',244),
  ('select_column -> parameters_two','select_column',1,'p_select_column','parser.py',245),
  ('select_column -> TIMES','select_column',1,'p_select_column','parser.py',246),
  ('from_statement -> FROM ids where_statement','from_statement',3,'p_from_statement','parser.py',252),
  ('from_statement -> empty','from_statement',1,'p_from_statement','parser.py',253),
  ('where_statement -> WHERE expression','where_statement',2,'p_where_statement','parser.py',266),
  ('where_statement -> empty','where_statement',1,'p_where_statement','parser.py',267),
  ('expression -> expression PLUS expression','expression',3,'p_expression','parser.py',277),
  ('expression -> expression MINUS expression','expression',3,'p_expression','parser.py',278),
  ('expression -> expression TIMES expression','expression',3,'p_expression','parser.py',279),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression','parser.py',280),
  ('expression -> expression EQUAL expression','expression',3,'p_expression','parser.py',282),
  ('expression -> expression DIFFERENT expression','expression',3,'p_expression','parser.py',283),
  ('expression -> expression GREATER expression','expression',3,'p_expression','parser.py',284),
  ('expression -> expression LESS expression','expression',3,'p_expression','parser.py',285),
  ('expression -> expression GREATER_EQUAL expression','expression',3,'p_expression','parser.py',286),
  ('expression -> expression LESS_EQUAL expression','expression',3,'p_expression','parser.py',287),
  ('expression -> expression AND expression','expression',3,'p_expression','parser.py',289),
  ('expression -> expression AND_WORD expression','expression',3,'p_expression','parser.py',290),
  ('expression -> expression OR expression','expression',3,'p_expression','parser.py',291),
  ('expression -> expression NOT_SYMBOL expression','expression',3,'p_expression','parser.py',292),
  ('expression -> MINUS expression','expression',2,'p_uminus_expression','parser.py',299),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_primitives','parser.py',305),
  ('expression -> NUMBER','expression',1,'p_expression_primitives','parser.py',306),
  ('expression -> DECIMALES','expression',1,'p_expression_primitives','parser.py',307),
  ('expression -> STRING','expression',1,'p_expression_primitives','parser.py',308),
  ('expression -> ID PERIOD ID','expression',3,'p_expresion_primitives2','parser.py',318),
  ('expression -> ID','expression',1,'p_expresion_primitives2','parser.py',319),
  ('concatena -> CONCATENA LPAREN concatena_parameters RPAREN','concatena',4,'p_concatena','parser.py',336),
  ('concatena_parameters -> concatena_parameters COMMA parameters_one','concatena_parameters',3,'p_concatena_param','parser.py',342),
  ('concatena_parameters -> parameters_one','concatena_parameters',1,'p_concatena_param','parser.py',343),
  ('parameters_one -> STRING','parameters_one',1,'p_parameters_one','parser.py',352),
  ('parameters_one -> ID PERIOD ID','parameters_one',3,'p_parameters_one','parser.py',353),
  ('parameters_one -> ID','parameters_one',1,'p_parameters_one','parser.py',354),
  ('substraer -> SUBSTRAER LPAREN parameters_one COMMA NUMBER COMMA NUMBER RPAREN','substraer',8,'p_substraer','parser.py',364),
  ('hoy -> HOY LPAREN RPAREN','hoy',3,'p_hoy','parser.py',371),
  ('contar -> CONTAR LPAREN contar_parameters RPAREN','contar',4,'p_contar','parser.py',378),
  ('contar_parameters -> TIMES','contar_parameters',1,'p_contar_param','parser.py',384),
  ('contar_parameters -> ID PERIOD ID','contar_parameters',3,'p_contar_param','parser.py',385),
  ('contar_parameters -> ID','contar_parameters',1,'p_contar_param','parser.py',386),
  ('suma -> SUMA LPAREN parameters_two RPAREN','suma',4,'p_suma','parser.py',393),
  ('parameters_two -> ID PERIOD ID','parameters_two',3,'p_parameters_two','parser.py',399),
  ('parameters_two -> ID','parameters_two',1,'p_parameters_two','parser.py',400),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',418),
]
