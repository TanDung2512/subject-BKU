grammar MP;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: mptype 'main' LB RB LP RP EOF ;


mptype: INTTYPE | VOIDTYPE ;

body: funcall SM;

exp: funcall | INTLIT ;

funcall: ID LB exp? RB ;
INTTYPE: 'int' ;
VOIDTYPE: 'void'  ;

ID: [a-zA-Z]+ ;

INTLIT: [0-9]+;

LP: '{';
RP: '}';

fragment A: [aA] ;
fragment B: [bB] ;
fragment C: [cC] ;
fragment D: [dD] ;
fragment E: [eE] ;
fragment F: [fF] ;
fragment G: [gG] ;
fragment H: [hH] ;
fragment I: [iI] ;
fragment J: [jJ] ;
fragment K: [kK] ;
fragment L: [lL] ;
fragment M: [mM] ;
fragment N: [nN] ;
fragment O: [oO] ;
fragment P: [pP] ;
fragment Q: [qQ] ;
fragment R: [rR] ;
fragment S: [sS] ;
fragment T: [tT] ;
fragment U: [uU] ;
fragment V: [vV] ;
fragment W: [wW] ;
fragment X: [xX] ;
fragment Y: [yY] ;
fragment Z: [zZ] ;
fragment LETTER_ID: (A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z) ;

IDENTIFIERS: (LETTER_ID|'_')([0-9]|'_'|LETTER_ID)* ;

//keywords
BREAK: B R E A K;
CONTINUE: C O N T I N U E;
FOR: F O R;
TO : T O;
DOWNTO: D O W N T O;
DO: D O;
IF: I F;
THEN: T H E N;
ELSE: E L S E;
RETURN: R E T U R N;
WHILE: W H I L E;
BEGIN: B E G I N;
END: E N D;
FUNCTION: F U N C T I O N;
PROCEDURE: P R O C E D U R E;
VAR: V A R;
TRUE: T R U E;
FALSE: F A L S E;
ARRAY: A R R A Y;
OF: O F;
REAL: R E A L;
BOOLEAN: B O O L E A N;
INTEGER: I N T E G E R;
STRING: S T R I N G;
NOT: N O T;
AND: A N D;
OR: O R;
DIV: D I V;
MOD: M O D;

//OPERATOR
ADDITION: '+';
MULTIPLICATION: '*';
LOGICAL_NOT:'not';
LOGICAL_OR: 'or';
NOT_EQUAL: '<>';
LESS_THAN: '<';
LESS_THAN_OR_EQUAL: '<=';
INTEGER_DIVISION: 'div';
SUBSTACTION:'-';
DIVISION: '/';
MODULUS: 'mod';
LOGICAL_AND: 'and';
EQUAL: '=';
GREATER_THAN: '>';
GREATER_THAN_OR_EQUAL: '>=';

//separator:
LSB: '[';
RSB: ']';
LB: '(';
RB: ')';
SM: ';';
DD: '..';
CM: ',';
CL: ':';
//Tut_ques_1: Letter[a-z0-9]* ;
//ut_ques_3_b: ('\''[a-z]+'\'')+;

//Literal
INTEGERLIT: [0-9]+ ;
FlOATLIT: ([0-9]+('e'|'E')('-')?[0-9]+)|([0-9]*'.'[0-9]+('e'|'E')('-')?[0-9]+)|([0-9]+'.'[0-9]*)|([0-9]*'.'[0-9]+) ;
BOOLEANLIT: ('true')|('false') ;
//STRINGLIT: '"'([a-zA-Z0-9]|('\b')|('\f')|('\r')|('\n')|('\t')|('\\\\')|('\'')|('\\"')|(' '))*'"'|'"''"' ;
STRINGLIT: '"'('\\t'|'\\\\'|'\\n'|'\\"'|~[\t\r\n\f\b'\\"])*'"' ;
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
fragment ERROR_CHARACTER: [\t\r\n\f\b\\];
//ERROR_STRING: '"'([a-zA-Z0-9 ]|('\b')|('\f')|('\r')|('\n')|('\t')|('\\')|('\'')|('\\"')|ERROR_CHARACTER)*'"';
ERROR_CHAR: .;
//UNCLOSE_STRING: '"'([a-zA-Z0-9 ]|('\b')|('\f')|('\r')|('\n')|('\t')|('\\')|('\'')|('\\"'))*|([a-zA-Z0-9 ]|('\b')|('\f')|('\r')|('\n')|('\t')|('\\')|('\'')|('\\"'))*'"';
ILLEGAL_ESCAPE: .;
