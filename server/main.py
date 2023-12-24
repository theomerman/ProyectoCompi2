# from controllers.compiler import *
import controllers.compiler.parser as parser


parser.parser.parse(
    '''
create data base test;
use tesdt;
'''
)
