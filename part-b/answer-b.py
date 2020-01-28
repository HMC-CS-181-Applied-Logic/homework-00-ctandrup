from propositional_logic import *

A = BoolVar('A')
B = BoolVar('B')
C = BoolVar('C')

# write code using A, B, and C, along with 
# the classes from propositional_logic.py
# and the .format() mathod to output the
# following expression:

# (((A => B) & (B => C)) => (A => C))

# the innermost formulas
f1 = Implies(A,B)
f2 = Implies(B,C)
f3 = Implies(A,C)

# combining ((A => B) & (B => C))
f4 = And(f1,f2)

# final formula
f5 = Implies(f4,f3)
print(f5)
print(f5.format())
print()