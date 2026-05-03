# MINI COMPILER – Academic Project

**6th Semester | Compiler Design Lab**

---

## 📌 Project Overview

This project is a **Mini Compiler implemented in Python** that demonstrates the major phases of compiler design. It processes input source code step-by-step through lexical analysis, syntax analysis, semantic analysis, intermediate code generation, optimization, and final code generation.

This project is designed for **learning and academic purposes** to understand how compilers work internally.

---

## 📁 Project Structure

```
mini_compiler/
│
├── main.py        # Menu-driven entry point
├── lexer.py       # Phase 1: Lexical Analysis
├── parser.py      # Phase 2: Syntax Analysis
├── semantic.py    # Phase 3: Semantic Analysis + Symbol Table
├── intermediate.py# Phase 4: Intermediate Code Generation
├── optimizer.py   # Phase 5: Code Optimization
├── codegen.py     # Phase 6: Target Code Generation
```

---

## ▶️ How to Run

```bash
cd mini_compiler
python main.py
```

---

## ⚙️ Compiler Phases Implemented

### 1. Lexical Analysis (lexer.py)

* Uses Python `re` module for tokenization
* Identifies:

  * Keywords (`int`, `print`)
  * Identifiers
  * Numbers
  * Operators
  * Symbols
* Ignores whitespace automatically
* Reports invalid tokens

---

### 2. Syntax Analysis (parser.py)

* Checks whether statements follow valid syntax
* Supports:

  * Declaration (`int x = 10`)
  * Assignment (`x = x + 5`)
  * Print (`print(x)`)
* Reports syntax errors

---

### 3. Semantic Analysis (semantic.py)

* Maintains a **symbol table (dictionary)**
* Performs:

  * Variable declaration checking
  * Duplicate declaration detection
  * Undeclared variable detection
  * Expression evaluation using `eval()`
* Updates and stores variable values

---

### 4. Intermediate Code Generation (intermediate.py)

* Generates intermediate representation
* Uses temporary variables
* Example:

```
a = b + c
t1 = b + c
a = t1
```

---

### 5. Code Optimization (optimizer.py)

* Improves intermediate code
* Performs:

  * Constant folding
* Example:

```
2 + 3 → 5
```

---

### 6. Target Code Generation (codegen.py)

* Converts intermediate code into simple low-level instructions
* Example instructions:

  * MOV
  * ADD
  * SUB
  * MUL
  * DIV

---

## 🧪 Sample Input

```
int x = 10
x = x + 5
print(x)
```

---

## 📤 Sample Output

```
x declared successfully
x updated successfully
Value of x = 15
```

---

## 🧠 Concepts Covered

* Compiler Design Phases
* Lexical Analysis using Regular Expressions
* Syntax Validation
* Semantic Analysis and Symbol Table
* Expression Evaluation
* Intermediate Code Representation
* Code Optimization
* Code Generation

---

# MINI COMPILER – Academic Project

**6th Semester | Compiler Design Lab**

---

## 📌 Project Overview

This project is a **Mini Compiler implemented in Python** that demonstrates the major phases of compiler design. It processes input source code step-by-step through lexical analysis, syntax analysis, semantic analysis, intermediate code generation, optimization, and final code generation.

This project is designed for **learning and academic purposes** to understand how compilers work internally.

---

## 📁 Project Structure

```id="uld876"
mini_compiler/
│
├── main.py        # Menu-driven entry point
├── lexer.py       # Phase 1: Lexical Analysis
├── parser.py      # Phase 2: Syntax Analysis
├── semantic.py    # Phase 3: Semantic Analysis + Symbol Table
├── intermediate.py# Phase 4: Intermediate Code Generation
├── optimizer.py   # Phase 5: Code Optimization
├── codegen.py     # Phase 6: Target Code Generation
```

---

## ▶️ How to Run

```bash
cd mini_compiler
python main.py
```

---

## ⚙️ Compiler Phases Implemented

### 1. Lexical Analysis (lexer.py)

* Uses Python `re` module for tokenization
* Identifies:

  * Keywords (`int`, `print`)
  * Identifiers
  * Numbers
  * Operators
  * Symbols
* Ignores whitespace automatically
* Reports invalid tokens

---

### 2. Syntax Analysis (parser.py)

* Checks whether statements follow valid syntax
* Supports:

  * Declaration (`int x = 10`)
  * Assignment (`x = x + 5`)
  * Print (`print(x)`)
* Reports syntax errors

---

### 3. Semantic Analysis (semantic.py)

* Maintains a **symbol table (dictionary)**
* Performs:

  * Variable declaration checking
  * Duplicate declaration detection
  * Undeclared variable detection
  * Expression evaluation using `eval()`
* Updates and stores variable values

---

### 4. Intermediate Code Generation (intermediate.py)

* Generates intermediate representation
* Uses temporary variables
* Example:

```id="yvez0q"
a = b + c
t1 = b + c
a = t1
```

---

### 5. Code Optimization (optimizer.py)

* Improves intermediate code
* Performs:

  * Constant folding
* Example:

```id="4za8m3"
2 + 3 → 5
```

---

### 6. Target Code Generation (codegen.py)

* Converts intermediate code into simple low-level instructions
* Example instructions:

  * MOV
  * ADD
  * SUB
  * MUL
  * DIV

---

## 🧪 Sample Input

```id="qcdy14"
int x = 10
x = x + 5
print(x)
```

---

## 📤 Sample Output

```id="xbk9lh"
x declared successfully
x updated successfully
Value of x = 15
```

---

## 🧠 Concepts Covered

* Compiler Design Phases
* Lexical Analysis using Regular Expressions
* Syntax Validation
* Semantic Analysis and Symbol Table
* Expression Evaluation
* Intermediate Code Representation
* Code Optimization
* Code Generation

---
