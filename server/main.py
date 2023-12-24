# from controllers.compiler import *
import controllers.compiler.parser as parser


parser.parser.parse(
    '''
create data base test2;
use test;

CREATE TABLE tbestado (
idestado int PRIMARY KEY,
estado nvarchar(50) NOT NULL);
'''
)
