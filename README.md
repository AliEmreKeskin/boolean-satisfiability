# boolean-satisfiability


Task 1
Some random propositional formula that is 3-SAT is written. Which is given below.
(A ∨ B ∨ C) ∧ (D ∨ B ∨ C) ∧ (A ∨ E ∨ F) ∧ (F ∨ G ∨ H) ∧ (A ∨ B ∨ D)
The formula is written in SMT-LIB2 syntax.
(declare-const A Bool)
(declare-const B Bool)
(declare-const C Bool)
(declare-const D Bool)
(declare-const E Bool)
(declare-const F Bool)
(declare-const G Bool)
(declare-const H Bool)
(assert
(and
(or A B C)
(or D B C)
(or A E F)
(or F G H)
(or A B D)
))
(check-sat)
(get-model)
The formula is saved to a file named “3SAT”. The file is passed to z3 program with given command form command line.
z3 -smt2 3SAT
And the output is:
sat
(
  (define-fun A () Bool
    true)
  (define-fun D () Bool
    false)
  (define-fun G () Bool
    true)
  (define-fun B () Bool
    true)
  (define-fun F () Bool
    false)
  (define-fun E () Bool
    false)
  (define-fun H () Bool
    false)
  (define-fun C () Bool
    false)
)
The output means the formula is satisfiable and the satisfying assignment is A=true, B=true, C=false, D=false, E=false, F=false, G=true, H=false.
Truth Table Generator tool is aldo used to verify that the given assignment returns true.

Task 2
An unrestricted propositional formula is written by using all possible operators.
(((p ∨ q) → (q ∧ r)) ↔ ¬s)
The formula is converted to CNF by hand with listed operations below:
(((p ∨ q) → (q ∧ r)) ↔ ¬s) biconditional elimination
((((p ∨ q) → (q ∧ r)) → ¬s) ∧ (¬s → ((p ∨ q) → (q ∧ r)))) implication elimination
(((¬(p ∨ q) ∨ (q ∧ r)) → ¬s) ∧ (¬s → ((p ∨ q) → (q ∧ r)))) implicaiton elimination
(((¬(p ∨ q) ∨ (q ∧ r)) → ¬s) ∧ (¬s → (¬(p ∨ q) ∨ (q ∧ r)))) implication elimination
((¬(¬(p ∨ q) ∨ (q ∧ r)) ∨ ¬s) ∧ (¬s → (¬(p ∨ q) ∨ (q ∧ r)))) implication elimination
((¬(¬(p ∨ q) ∨ (q ∧ r)) ∨ ¬s) ∧ (¬¬s ∨ (¬(p ∨ q) ∨ (q ∧ r)))) de Morgan
((¬((¬p ∧ ¬q) ∨ (q ∧ r)) ∨ ¬s) ∧ (¬¬s ∨ (¬(p ∨ q) ∨ (q ∧ r)))) de Morgan
((¬((¬p ∧ ¬q) ∨ (q ∧ r)) ∨ ¬s) ∧ (¬¬s ∨ ((¬p ∧ ¬q) ∨ (q ∧ r)))) de Morgan
(((¬(¬p ∧ ¬q) ∧ ¬(q ∧ r)) ∨ ¬s) ∧ (¬¬s ∨ ((¬p ∧ ¬q) ∨ (q ∧ r)))) de Morgan
((((¬¬p ∨ ¬¬q) ∧ ¬(q ∧ r)) ∨ ¬s) ∧ (¬¬s ∨ ((¬p ∧ ¬q) ∨ (q ∧ r)))) de Morgan
((((¬¬p ∨ ¬¬q) ∧ (¬q ∨ ¬r)) ∨ ¬s) ∧ (¬¬s ∨ ((¬p ∧ ¬q) ∨ (q ∧ r)))) double-negation elimination
((((p ∨ q) ∧ (¬q ∨ ¬r)) ∨ ¬s) ∧ (s ∨ ((¬p ∧ ¬q) ∨ (q ∧ r)))) distribute or over and
((((p ∨ q) ∨ ¬s) ∧ ((¬q ∨ ¬r) ∨ ¬s)) ∧ (s ∨ ((¬p ∧ ¬q) ∨ (q ∧ r)))) associativity of or
(((p ∨ q ∨ ¬s) ∧ (¬q ∨ ¬r ∨ ¬s)) ∧ (s ∨ ((¬p ∧ ¬q) ∨ (q ∧ r)))) distribute or over and
(((p ∨ q ∨ ¬s) ∧ (¬q ∨ ¬r ∨ ¬s)) ∧ (s ∨ ((¬p ∨ q) ∧ (¬p ∨ r) ∧ (¬q ∨ q) ∧ (¬q ∨ r)))) distribute or over and
(((p ∨ q ∨ ¬s) ∧ (¬q ∨ ¬r ∨ ¬s)) ∧ ((s ∨ ¬p ∨ q) ∧ (s ∨ ¬p ∨ r) ∧ (s ∨ ¬q ∨ q) ∧ (s ∨ ¬q ∨ r))) associativity of and
((p ∨ q ∨ ¬s) ∧ (¬q ∨ ¬r ∨ ¬s) ∧ (s ∨ ¬p ∨ q) ∧ (s ∨ ¬p ∨ r) ∧ (s ∨ ¬q ∨ q) ∧ (s ∨ ¬q ∨ r))
Since the formula is already 3-SAT no more steps are required. The resulting formula is:
(( p ∨  q ∨ ¬s) ∧
 (¬q ∨ ¬r ∨ ¬s) ∧
 ( s ∨ ¬p ∨  q) ∧
 ( s ∨ ¬p ∨  r) ∧
 ( s ∨ ¬q ∨  q) ∧
 ( s ∨ ¬q ∨  r))
USAT-org
The original unrestricted formula is written in SMT_LIB2 syntax:
(declare-const p Bool)
(declare-const q Bool)
(declare-const r Bool)
(declare-const s Bool)
(assert (iff (implies (or p q) (and q r)) (not s)))
(check-sat)
(get-model)
USAT-converted
The converted 3-SAT formule is written in SMT_LIB2 syntax:
(declare-const p Bool)
(declare-const q Bool)
(declare-const r Bool)
(declare-const s Bool)
(assert
(and
(or p q (not s))
(or (not q) (not r) (not s))
(or s (not p) q)
(or s (not p) r)
(or s (not q) q)
(or s (not q) r)
))
(check-sat)
(get-model)
Equisatisfiability
If the two formula is both satisfiable or both not satisfiable then they are equisatisfiable. [https://en.wikipedia.org/wiki/Equisatisfiability]
USAT-org given to z3 as below:
z3 -smt2 USAT-org
The output for USAT-org:
sat
(
  (define-fun s () Bool
    true)
  (define-fun p () Bool
    true)
  (define-fun q () Bool
    false)
  (define-fun r () Bool
    false)
)
USAT-converted given to z3 as below:
z3 -smt2 USAT-converted
The output for USAT-converted:
sat
(
  (define-fun p () Bool
    false)
  (define-fun q () Bool
    false)
  (define-fun s () Bool
    false)
  (define-fun r () Bool
    false)
)
As the first line is “sat” for both original and converted formula outputs we say that these two formula is equisatisfiable.
Task 3
For the solution of n-queens problem “Automated Reasoning: satisfiability” course on coursera.org was very helpful. [https://www.coursera.org/learn/automated-reasoning-sat] Even for the 4-queen solution the SMT-LIB3 code will be very long to write by hand. So a Pyhton script utilized to generate the file for us. Since the script will include some loops it will be easy to make them parameterized for n number of iterations. At that point lets focus on the n-queens problem.
Some constraints are defined for the solution. The constraints are listed below:
    1. At least one queen on every row:
       Since the problem defines the number of queens and the number of rows as same there has to be at leas one queen on every row. For a single row this can be satifiable with an “or” of if the position has queen for every position on the row. Propositional formula for this constraint can be written as below:
       
       If one row has at least one queen then if we “and” the formula for all these rows this gives as every row has at least one queen and this can be written as below:
       
    2. At most one queen on every row:
       Since a queen can beat another queen on the same row there has to be a single queen on a row. If every row has a queen then they also has to be single on the row. For a single row it means any two position cant have a queen at same time. This can be written as:
       
       To make it a constraint for every row. Write the formula for all rows and “and” them. This can be written as:
       
    3. At least one queen on every column:
       Since the problem defines the number of queens and the number of columns as same there has to be at leas one queen on every column. This is similar to formula for the rows. Just re-aling the indices for columns. This can be written as:
       
    4. At most one queen on every row:
       Similar to row this rule also applies to columns and the folmula can be written as:
       
    5. At most one queen on every diagonal:
       Since the number on diagonals are more than the number of queens there is no constraint on the least number of queens on a diagonal but a queen can beat another queen on the same diagonal so it has to be at most one queen on a diagonal. This rule does not matter for the direction of diagonal ither like “/” or “\”. Two position is diagonal if the sum of indeces are equal or the difference of indices are equal. This can be written as:
       
All these constraint has to be satisfied at the same time so they will be connected with “and” operator.
Python Script
This Python script accepts the number of queens and generates the <n>-queens.smt file thas has a formula written in SMT-LIB2 syntax.

4-Queens
SMT-LIB2 file is created like this:
(declare-fun p (Int Int) Bool)
(assert (and
(or (p 1 1) (p 1 2) (p 1 3) (p 1 4))
(or (p 2 1) (p 2 2) (p 2 3) (p 2 4))
(or (p 3 1) (p 3 2) (p 3 3) (p 3 4))
(or (p 4 1) (p 4 2) (p 4 3) (p 4 4))
(or (not (p 1 1)) (not (p 1 2)))
(or (not (p 1 1)) (not (p 1 3)))
(or (not (p 1 1)) (not (p 1 4)))
(or (not (p 1 2)) (not (p 1 3)))
(or (not (p 1 2)) (not (p 1 4)))
(or (not (p 1 3)) (not (p 1 4)))
(or (not (p 2 1)) (not (p 2 2)))
(or (not (p 2 1)) (not (p 2 3)))
(or (not (p 2 1)) (not (p 2 4)))
(or (not (p 2 2)) (not (p 2 3)))
(or (not (p 2 2)) (not (p 2 4)))
(or (not (p 2 3)) (not (p 2 4)))
(or (not (p 3 1)) (not (p 3 2)))
(or (not (p 3 1)) (not (p 3 3)))
(or (not (p 3 1)) (not (p 3 4)))
(or (not (p 3 2)) (not (p 3 3)))
(or (not (p 3 2)) (not (p 3 4)))
(or (not (p 3 3)) (not (p 3 4)))
(or (not (p 4 1)) (not (p 4 2)))
(or (not (p 4 1)) (not (p 4 3)))
(or (not (p 4 1)) (not (p 4 4)))
(or (not (p 4 2)) (not (p 4 3)))
(or (not (p 4 2)) (not (p 4 4)))
(or (not (p 4 3)) (not (p 4 4)))
(or (p 1 1) (p 2 1) (p 3 1) (p 4 1))
(or (p 1 2) (p 2 2) (p 3 2) (p 4 2))
(or (p 1 3) (p 2 3) (p 3 3) (p 4 3))
(or (p 1 4) (p 2 4) (p 3 4) (p 4 4))
(or (not (p 1 1)) (not (p 2 1)))
(or (not (p 1 1)) (not (p 3 1)))
(or (not (p 1 1)) (not (p 4 1)))
(or (not (p 2 1)) (not (p 3 1)))
(or (not (p 2 1)) (not (p 4 1)))
(or (not (p 3 1)) (not (p 4 1)))
(or (not (p 1 2)) (not (p 2 2)))
(or (not (p 1 2)) (not (p 3 2)))
(or (not (p 1 2)) (not (p 4 2)))
(or (not (p 2 2)) (not (p 3 2)))
(or (not (p 2 2)) (not (p 4 2)))
(or (not (p 3 2)) (not (p 4 2)))
(or (not (p 1 3)) (not (p 2 3)))
(or (not (p 1 3)) (not (p 3 3)))
(or (not (p 1 3)) (not (p 4 3)))
(or (not (p 2 3)) (not (p 3 3)))
(or (not (p 2 3)) (not (p 4 3)))
(or (not (p 3 3)) (not (p 4 3)))
(or (not (p 1 4)) (not (p 2 4)))
(or (not (p 1 4)) (not (p 3 4)))
(or (not (p 1 4)) (not (p 4 4)))
(or (not (p 2 4)) (not (p 3 4)))
(or (not (p 2 4)) (not (p 4 4)))
(or (not (p 3 4)) (not (p 4 4)))
;-------------------------------
(or (not (p 1 1)) (not (p 2 2)))
(or (not (p 1 2)) (not (p 2 1)))
(or (not (p 1 2)) (not (p 2 3)))
(or (not (p 1 3)) (not (p 2 2)))
(or (not (p 1 3)) (not (p 2 4)))
(or (not (p 1 4)) (not (p 2 3)))
(or (not (p 1 1)) (not (p 3 3)))
(or (not (p 1 2)) (not (p 3 4)))
(or (not (p 1 3)) (not (p 3 1)))
(or (not (p 1 4)) (not (p 3 2)))
(or (not (p 1 1)) (not (p 4 4)))
(or (not (p 1 4)) (not (p 4 1)))
(or (not (p 2 1)) (not (p 3 2)))
(or (not (p 2 2)) (not (p 3 1)))
(or (not (p 2 2)) (not (p 3 3)))
(or (not (p 2 3)) (not (p 3 2)))
(or (not (p 2 3)) (not (p 3 4)))
(or (not (p 2 4)) (not (p 3 3)))
(or (not (p 2 1)) (not (p 4 3)))
(or (not (p 2 2)) (not (p 4 4)))
(or (not (p 2 3)) (not (p 4 1)))
(or (not (p 2 4)) (not (p 4 2)))
(or (not (p 3 1)) (not (p 4 2)))
(or (not (p 3 2)) (not (p 4 1)))
(or (not (p 3 2)) (not (p 4 3)))
(or (not (p 3 3)) (not (p 4 2)))
(or (not (p 3 3)) (not (p 4 4)))
(or (not (p 3 4)) (not (p 4 3)))
))
(check-sat)
(get-model)
z3 output is like this:
sat
(
  (define-fun p ((x!0 Int) (x!1 Int)) Bool
    (ite (and (= x!0 1) (= x!1 3)) true
    (ite (and (= x!0 2) (= x!1 1)) true
    (ite (and (= x!0 3) (= x!1 4)) true
    (ite (and (= x!0 4) (= x!1 2)) true
      false)))))
)
n-queens
The to the n-queens is making the loop iterate to the n. The script is written like this so we can generate a formula for any number of queens. Some examples are given in the appendix.
References
Appendix
