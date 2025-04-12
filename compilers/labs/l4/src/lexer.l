%{
#include "../src/interpreter.hpp"
#include "parser.tab.hpp"
%}

%%
           
[0-9]+           { yylval.num = atoi(yytext); return NUMBER; }
"("              { return OPEN_PARENTHESES; }
")"              { return CLOSE_PARENTHESES; }
"{"              { return OPEN_BRACKET; }
"}"              { return CLOSE_BRACKET; }
"=="             { return EQ; }
"<"              { return LT; }
">"              { return GT; }
"<="             { return LEQ; }
">="             { return GEQ; }
"!="             { return NEQ; }
"&&"             { return AND; }
"+"              { return PLUS; }
"-"              { return MINUS; }
"*"              { return STAR; }
"/"              { return SLASH; }
"||"             { return OR; }
"!"              { return NOT; }
"if"             { return IF; }
"else"           { return ELSE; }
"while"          { return WHILE; }
"let"            { return VAR; }
"true"           { return TRUE; }
"false"          { return FALSE; }
"undefined"      { return UNDEFINED; }
"="              { return ASSIGN; }
\n               { return EOL; }
([ \t])|(\/\/.*) {}

[a-zA-Z_][.a-zA-Z_0-9]* { 
    yylval.str = strdup(yytext); 
    return IDENTIFIER;
}
\"[^\"]*\"  { 
    yylval.str = strdup(yytext + 1);
    yylval.str[strlen(yylval.str) - 1] = '\0';
    return STRING;
    }
.   { return 0; }

%%

int yywrap() {
    return 1;
}
