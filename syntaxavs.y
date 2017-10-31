%{
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
extern int yylex();
extern int yyparse();
extern FILE *yyin;
extern int line_no;
void yyerror(const char *s);
%}
%union {
	int num;
	char *var;
	char *sfval;
}
%token <num> INT
%token <var> ID
%token <sfval> FUNCID
%token FUNC
%token ENDL
%token ARITHOP
%token RELOP
%token END
%token EITHER
%token OR
%token LOOP
%token NOTOP
%token FUNC_PAR
%token OUTPUT
%token INPUT
%token STRING
%token START

%%
stmt:
	START endline statementlist END endline
	;
statementlist:
	statementlist statement
	| statement
	;
statement:
	asst
	| conditional
	| loop
	| function
	| ip
	| opu
	;
opu:
	OUTPUT FUNC_PAR STRING FUNC_PAR endline
	;
ip:
	ID '=' INPUT FUNC_PAR STRING FUNC_PAR endline
	;	
function:
	FUNC FUNCID '(' ID ')' FUNC_PAR endline statementlist FUNC_PAR endline
	;
loop:
	LOOP '(' relationexp ')' FUNC_PAR endline statementlist FUNC_PAR endline
	;
conditional:
	EITHER '(' relationexp ')'FUNC_PAR endline statementlist FUNC_PAR endline		
	| OR FUNC_PAR endline statementlist FUNC_PAR endline	
	;

asst:
	ID '=' relationexp endline
	;
relationexp:
	relationexp RELOP arithexp
	| arithexp
	;
arithexp:
	arithexp ARITHOP term
	| term
	;
term:
	'(' relationexp ')'
	| INT 
	| ID
	| STRING
	;
endline: 
	endline ENDL
	| ENDL
	;
%%
int main() {
	yyin=fopen("check.avs","r");
	do {
		yyparse();
	} while (!feof(yyin));
	printf("correct syntax\n");
	
}

void yyerror(const char *s) {
	printf("error on line %d\n", line_no);
	exit(-1);
}

