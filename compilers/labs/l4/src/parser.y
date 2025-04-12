%{
#include <iostream>
#include <unordered_map>
#include <vector>
#include "../src/interpreter.hpp"

void yyerror(const char* s) {
  std::cerr << "Error: " << s << std::endl;
}
int yylex();
Node* root = nullptr;
extern char* yytext;
%}

%union {
  Node *node;
  char* str;
  int num;
}
%token <num> NUMBER
%token <str> IDENTIFIER STRING
%token PLUS MINUS STAR SLASH EOL ASSIGN VAR EQ LT GT LEQ GEQ NEQ AND OR NOT TRUE FALSE UNDEFINED IF ELSE OPEN_PARENTHESES CLOSE_PARENTHESES OPEN_BRACKET CLOSE_BRACKET WHILE
%type <node> program statements statement expression_statement expression precedence16 precedence15 precedence14 precedence10 precedence9 precedence6 precedence5 precedence3 precedence0 if_statement block while_statement arguments
%nonassoc IF ELSE
%%

program:
  statements { root = $1; }
  ;
statements:
  statement statements { 
    $$ = new BlockNode(); 
    dynamic_cast<BlockNode*>($$)->addStatement($1); 
    dynamic_cast<BlockNode*>($$)->addStatement($2); 
  }
  | statement { 
    $$ = new BlockNode(); 
    dynamic_cast<BlockNode*>($$)->addStatement($1); 
  }
  ;
statement:
  expression_statement EOL { $$ = $1; }
  | if_statement { $$ = $1; }
  | while_statement { $$ = $1; }
  | block { $$ = $1; }
  | EOL { $$ = new UndefinedNode(); }
  ;
block:
  OPEN_BRACKET EOL statements CLOSE_BRACKET { $$ = $3; }
  ;
expression_statement:
  expression { $$ = $1; }
  ;
if_statement:
  IF OPEN_PARENTHESES expression CLOSE_PARENTHESES block ELSE block { $$ = new IfNode($3, $5, $7); }
  | IF OPEN_PARENTHESES expression CLOSE_PARENTHESES block { $$ = new IfNode($3, $5, nullptr); }
  ;
while_statement:
  WHILE OPEN_PARENTHESES expression CLOSE_PARENTHESES block { $$ = new WhileNode($3, $5); }
expression:
  precedence16 { $$ = $1; }
  ;
// c++ precedence 16
precedence16:
  IDENTIFIER ASSIGN precedence16 { $$ = new AssignNode($1, $3); }
  | VAR IDENTIFIER ASSIGN precedence16 { $$ = new LetNode($2, $4); }
  | precedence15 { $$ = $1; }
  ;
// c++ precedence 15
precedence15:
  precedence14 OR precedence14 { $$ = new BinaryNode("||", $1, $3); }
  | precedence14 { $$ = $1; }
  ;
// c++ precedence 14
precedence14:
  precedence10 AND precedence10 { $$ = new BinaryNode("&&", $1, $3); }
  | precedence10 { $$ = $1; }
  ;
// c++ precedence 10
precedence10:
  precedence9 EQ precedence9 { $$ = new BinaryNode("==", $1, $3); }
  | precedence9 NEQ precedence9 { $$ = new BinaryNode("!=", $1, $3); }
  | precedence9 { $$ = $1; }
  ;
// c++ precedence 9
precedence9:
  precedence6 LT precedence6 { $$ = new BinaryNode("<", $1, $3); }
  | precedence6 GT precedence6 { $$ = new BinaryNode(">", $1, $3); }
  | precedence6 GEQ precedence6 { $$ = new BinaryNode(">=",$1, $3); }
  | precedence6 LEQ precedence6 { $$ = new BinaryNode("<=",$1, $3); }
  | precedence6 { $$ = $1; }
  ;
// c++ precedence 6
precedence6:
  precedence6 PLUS precedence5 { $$ = new BinaryNode("+", $1, $3); }
  | precedence6 MINUS precedence5 { $$ = new BinaryNode("-", $1, $3); }
  | precedence5 { $$ = $1; }
  ;
// c++ precedence 5
precedence5:
  precedence5 STAR precedence3 { $$ = new BinaryNode("*", $1, $3); }
  | precedence5 SLASH precedence3 { $$ = new BinaryNode("/", $1, $3); }
  | precedence3 { $$ = $1; }
  ;
// c++ precedence 3
precedence3:
  MINUS precedence3 { $$ = new UnaryNode("-", $2); }
  | NOT precedence3 { $$ = new UnaryNode("!", $2); }
  | precedence0 { $$ = $1; }
  ;
arguments:
  /* empty */ { $$ = nullptr; }
  | expression { $$ = $1; }
  ;
// c++ precedence 0
precedence0:
  FALSE { $$ = new BoolNode(false); }
  | TRUE { $$ = new BoolNode(true); }
  | UNDEFINED { $$ = new UndefinedNode(); }
  | NUMBER { $$ = new NumberNode($1); }
  | IDENTIFIER { $$ = new VariableNode($1); }
  | STRING { $$ = new StringNode($1); }
  | OPEN_PARENTHESES expression CLOSE_PARENTHESES { $$ = $2; }
  | IDENTIFIER OPEN_PARENTHESES arguments CLOSE_PARENTHESES { $$ = new CallNode($1, $3); }
  ;
%%

extern FILE * yyin;
int main(int argc, char **argv) {
   if (argc > 1) {
      yyin = fopen(argv[1], "r");
      if (yyin == NULL){
         printf("syntax: %s filename\n", argv[0]);
      }
   }
   if (yyparse() == 0 && root) {
      root->evaluate();
   }
   return 0;
}
