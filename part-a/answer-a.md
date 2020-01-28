## Part a

### Describe what the code in `z3-test.py` is doing in a paragraph or two.

The code in z3-test.py is checking to see if the condition described in the input (ie [And(Not(a), b, x > 0, x < 100, x < y)] and [And(Not(a), b, x > 0, x < 100, x < y), y < 1]) can be satisfied by some some values of x,y,a,b.

Let's consider the first input, [And(Not(a), b, x > 0, x < 100, x < y)]. We want to know if there's some x < y where 0 < x < 100. Similarly, we want to look at booleans for a,b to see if we can satisfy not(a) and b. All of these conditions must be true, and the program tells us that indeed if you let x = 99, y = 100, b = True, and a = False, all of the conditions are satisfied (hence it prints out "sat" and the case where it works).

Consider now the other case, where the input is [And(Not(a), b, x > 0, x < 100, x < y), y < 1]. Since there's no value of x such that 0 < x < y < 1, there's no way to satisfy the input, so it outputs "unsat".