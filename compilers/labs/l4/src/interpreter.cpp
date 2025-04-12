#include "interpreter.hpp"

#include <cmath>
#include <iostream>
#include <limits>
#include <ranges>
#include <sstream>
#include <unordered_map>
#include <variant>
#include <vector>

std::vector<std::unordered_map<string, Value>> scopes = {{}};

void enterScope() { scopes.push_back({}); }

void exitScope() {
  if (scopes.size() > 1) scopes.pop_back();
}

Value getVar(const string &name) {
  for (auto &scope : std::views::reverse(scopes)) {
    if (scope.count(name)) return scope[name];
  }
  std::cerr << "Error: Undefined variable " << name << std::endl;
  return UndefinedType();
}

void createVar(const string &name, Value value) { scopes.back()[name] = value; }

void setVar(const string &name, Value value) {
  for (auto &scope : std::views::reverse(scopes)) {
    if (scope.count(name)) {
      scope[name] = value;
      return;
    }
  }
  std::cerr << "Error: Undefined variable " << name << std::endl;
}

double toNumber(const Value &v) {
  if (auto p = std::get_if<double>(&v)) return *p;
  if (auto p = std::get_if<bool>(&v)) return *p ? 1.0 : 0.0;
  if (auto p = std::get_if<std::string>(&v)) {
    try {
      size_t pos;
      double num = std::stod(*p, &pos);
      if (pos == p->size()) return num;
    } catch (...) {
    }
    return std::numeric_limits<double>::quiet_NaN();
  }
  return std::numeric_limits<double>::quiet_NaN();
}

std::string toString(const Value &v) {
  if (auto p = std::get_if<double>(&v)) {
    if (std::isnan(*p)) return "NaN";
    if (std::isinf(*p)) return (*p > 0) ? "Infinity" : "-Infinity";
    std::stringstream ss;
    ss << *p;
    std::string s = ss.str();
    if (s.find('.') != std::string::npos) {
      s.erase(s.find_last_not_of('0') + 1, std::string::npos);
      if (s.back() == '.') s.pop_back();
    }
    return s;
  }
  if (auto p = std::get_if<bool>(&v)) return *p ? "true" : "false";
  if (auto p = std::get_if<std::string>(&v)) return *p;
  return "undefined";
}

bool isTruthy(const Value &val) {
  if (auto p = std::get_if<bool>(&val)) return *p;
  if (std::holds_alternative<UndefinedType>(val)) return false;
  if (auto p = std::get_if<double>(&val)) {
    double d = *p;
    return d != 0.0 && !std::isnan(d);
  }
  if (auto p = std::get_if<std::string>(&val)) return !p->empty();
  return false;
}

Value numberToValue(double d) {
  if (std::isnan(d) || std::isinf(d)) return d;
  return d;
}

Value VariableNode::evaluate() const { return getVar(name); }

Value BinaryNode::evaluate() const {
  Value leftVal = left->evaluate();
  Value rightVal = right->evaluate();

  if (op == "+") {
    bool leftIsString = std::holds_alternative<std::string>(leftVal);
    bool rightIsString = std::holds_alternative<std::string>(rightVal);
    if (leftIsString || rightIsString) {
      return toString(leftVal) + toString(rightVal);
    } else {
      double l = toNumber(leftVal);
      double r = toNumber(rightVal);
      return numberToValue(l + r);
    }
  }

  if (op == "-" || op == "*" || op == "/") {
    double l = toNumber(leftVal);
    double r = toNumber(rightVal);
    if (op == "-") return numberToValue(l - r);
    if (op == "*") return numberToValue(l * r);
    if (op == "/") return numberToValue(l / r);
  }

  if (op == "==" || op == "!=") {
    bool equal = false;
    // Handle NaN != NaN
    if (std::holds_alternative<double>(leftVal) &&
        std::holds_alternative<double>(rightVal)) {
      double l = std::get<double>(leftVal);
      double r = std::get<double>(rightVal);
      equal = (l == r) && !std::isnan(l) && !std::isnan(r);
    } else {
      equal = (isTruthy(leftVal) == isTruthy(rightVal));
    }
    return op == "==" ? equal : !equal;
  }

  if (op == ">" || op == "<" || op == ">=" || op == "<=") {
    double l = toNumber(leftVal);
    double r = toNumber(rightVal);
    if (op == ">") return l > r;
    if (op == "<") return l < r;
    if (op == ">=") return l >= r;
    if (op == "<=") return l <= r;
  }

  if (op == "&&" || op == "||") {
    bool l = isTruthy(leftVal);
    bool r = isTruthy(rightVal);
    return op == "&&" ? (l && r) : (l || r);
  }

  std::cerr << "Error: Invalid operator " << op << std::endl;
  return UndefinedType{};
}

Value UnaryNode::evaluate() const {
  Value result = right->evaluate();
  if (op == "-") {
    double num = toNumber(result);
    return numberToValue(-num);
  } else if (op == "!") {
    return !isTruthy(result);
  }
  std::cerr << "Error: Invalid unary operator " << op << std::endl;
  return UndefinedType{};
}

Value AssignNode::evaluate() const {
  Value result = expression->evaluate();
  setVar(name, result);
  return result;
}

Value LetNode::evaluate() const {
  Value result = expression->evaluate();
  createVar(name, result);
  return result;
}

Value IfNode::evaluate() const {
  if (isTruthy(condition->evaluate())) {
    return thenBlock->evaluate();
  } else if (elseBlock) {
    return elseBlock->evaluate();
  }
  return UndefinedType();
}

Value BlockNode::evaluate() const {
  enterScope();
  for (auto &statement : statements) {
    statement->evaluate();
  }
  exitScope();
  return UndefinedType();
}

Value WhileNode::evaluate() const {
  while (isTruthy(condition->evaluate())) {
    block->evaluate();
  }
  return UndefinedType();
}
Value CallNode::evaluate() const {
  if (functionName == "console.log" && argument) {
    Value result = argument->evaluate();
    std::string output = toString(result);
    std::cout << output << std::endl;
  }
  return UndefinedType{};
}
