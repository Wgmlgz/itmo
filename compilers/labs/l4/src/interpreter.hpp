#ifndef interpreter_HPP
#define interpreter_HPP

#include <string>
#include <variant>
#include <vector>

using string = std::string;

struct UndefinedType {};

using Value = std::variant<double, bool, string, UndefinedType>;

class Node {
 public:
  virtual ~Node() = default;
  virtual Value evaluate() const = 0;
};

class BoolNode : public Node {
 public:
  bool value;
  BoolNode(bool val) : value(val) {}
  Value evaluate() const override { return value; }
};

class NumberNode : public Node {
 public:
  double value;
  NumberNode(double val) : value(val) {}
  Value evaluate() const override { return value; }
};

class UndefinedNode : public Node {
 public:
  UndefinedNode() {}
  Value evaluate() const override { return UndefinedType(); }
};

class StringNode : public Node {
 public:
  string value;
  StringNode(string val) : value(val) {}
  Value evaluate() const override { return value; }
};

class VariableNode : public Node {
 public:
  string name;
  VariableNode(const string &n) : name(n) {}
  Value evaluate() const override;
};

class BinaryNode : public Node {
 public:
  string op;
  Node *left;
  Node *right;

  BinaryNode(const string &o, Node *l, Node *r) : op(o), left(l), right(r) {}

  Value evaluate() const override;
};

class UnaryNode : public Node {
 public:
  string op;
  Node *right;

  UnaryNode(const string &o, Node *r) : op(o), right(r) {}

  Value evaluate() const override;
};

class AssignNode : public Node {
 public:
  string name;
  Node *expression;
  AssignNode(const string &n, Node *expr) : name(n), expression(expr) {}
  Value evaluate() const override;
};

class LetNode : public Node {
 public:
  string name;
  Node *expression;
  LetNode(const string &n, Node *expr) : name(n), expression(expr) {}
  Value evaluate() const override;
};

class IfNode : public Node {
 public:
  Node *condition;
  Node *thenBlock;
  Node *elseBlock;
  IfNode(Node *cond, Node *thenB, Node *elseB = nullptr)
      : condition(cond), thenBlock(thenB), elseBlock(elseB) {}
  Value evaluate() const override;
};

class BlockNode : public Node {
 public:
  std::vector<Node *> statements;
  void addStatement(Node *statement) { statements.push_back(statement); }
  Value evaluate() const override;
};

class WhileNode : public Node {
 public:
  Node *condition;
  Node *block;
  WhileNode(Node *cond, Node *blk) : condition(cond), block(blk) {}
  Value evaluate() const override;
};

class CallNode : public Node {
  string functionName;
  Node *argument;

 public:
  CallNode(const std::string &name, Node *arg)
      : functionName(name), argument(arg) {}

  Value evaluate() const override;
};

#endif  // interpreter_HPP