CC = g++
LEX = flex
BISON = bison
CFLAGS = -std=c++20
INTERPRETER = out/js

.PHONY: run


run: $(INTERPRETER)
	$(INTERPRETER) example.js


$(INTERPRETER): out/lexer.tab.cpp out/parser.tab.cpp src/interpreter.cpp
	$(CC) $(CFLAGS) out/lexer.tab.cpp out/parser.tab.cpp src/interpreter.cpp -o $(INTERPRETER)

out/lexer.tab.cpp: src/lexer.l
	$(LEX) -o out/lexer.tab.cpp src/lexer.l

out/parser.tab.cpp: src/parser.y
	$(BISON) -Wcounterexamples -d -o out/parser.tab.cpp src/parser.y

test: $(INTERPRETER)
	@echo "Running tests...\n"
	@for test in tests/**; do \
		echo "Running $$test..."; \
		$(INTERPRETER) < $$test; \
		echo " "; \
	done

clean:
	rm -f out
	mkdir out
