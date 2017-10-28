syntaxavs.tab.c syntaxavs.tab.h: syntaxavs.y
	bison -d syntaxavs.y

lex.yy.c: lexavs.l syntaxavs.tab.h
	flex lexavs.l

out: lex.yy.c syntaxavs.tab.c syntaxavs.tab.h
	gcc syntaxavs.tab.c lex.yy.c -lfl -o out
