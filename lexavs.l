%{
#include "parser.tab.h"
#define YY_DECL extern int yylex()
int line_no = 1;
%}

%%
[ \t]          			;
(==|<=|>=|<|>)			{return RELOP;}
[=\(\)]				{return yytext[0];}
[\+\-\*\/]			{return ARITHOP;}
[0-9]+				{yylval.num = atoi(yytext); return INT;}
func				{return FUNC;}
DISPLAY   			{return OUTPUT;}           
READ      			{return INPUT;}
START	 			{return START;}
END    				{return END;} 			  		
[a-z0-9_]*	  		{yylval.var = strdup(yytext); return ID;}
\n				{line_no++; return ENDL;}
EITHER				{return EITHER;}				
OR				{return OR;}
REPEAT_TILL			{return LOOP;}
"[["|"]]"			{return FUNC_PAR;}		
[A-Z][A-Z]*                     {yylval.sfval = strdup(yytext);return FUNCID;}
['].*[']			{return STRING;}
.				{return yytext[0];}
%%
/*
int yywrap()
{
	return 1;
}*/
