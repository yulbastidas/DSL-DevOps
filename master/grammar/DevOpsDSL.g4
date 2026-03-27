grammar DevOpsDSL;

program: statement* EOF;

statement
    : nodeCommand
    | groupCommand
    | deployCommand
    | parallelBlock
    ;

nodeCommand
    : ID '.' 'run' '(' STRING ')'
    ;

groupCommand
    : ID '.' 'update' '(' ')'
    ;

deployCommand
    : 'deploy' ID 'to' ID
    ;

parallelBlock
    : 'parallel' '{' statement+ '}'
    ;

ID: [a-zA-Z_][a-zA-Z0-9_]*;
STRING: '"' .*? '"';
WS: [ \t\r\n]+ -> skip;
