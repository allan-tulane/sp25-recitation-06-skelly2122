CMPS 2200 Recitation 06 Answers

Name: Samuel Kelly
Name: Miles Whiteford

Place all written answers from recitation-06.md here for easier grading.

Q2) The work recurrence for fib_recursive(n) is: W(n) = W(n-1) + W(n-2) + O(1)
This is the same recurrence relation as the Fibonacci sequence itself, but with an additional constant factor.
The solution to this recurrence is W(n) = O(φ^n), where φ ≈ 1.618 is the golden ratio.

Q3) The span recurrence for fib_recursive(n) is: S(n) = max(S(n-1), S(n-2)) + O(1) = S(n-1) + O(1) (since S(n-1) > S(n-2))
Solving this, we get S(n) = O(n).

Q4) Looking at the counts list, we can observe that:
The entries increase exponentially as the index increases
Each Fibonacci number F(i) is computed F(n-i+1) times
For example, F(n-1) is computed twice, F(n-2) is computed three times, F(n-3) is computed five times, etc.
This pattern shows the number of times each subproblem is recomputed, demonstrating the exponential inefficiency of the recursive algorithm.

Q6) When computing F(n) using the top-down memoization approach:
Each value F(i) is computed exactly once for 0 ≤ i ≤ n
Once computed, the value is stored in the fibs array and reused
Each fib_top_down(i) is called at most 2 times (e.g., once by its left parent and once by its right parent in the recursion tree). After the first call, the result is cached, so subsequent calls return immediately. The maximum is 2, not dependent on subproblem appearances.
Work: Since each F(i) is computed exactly once and each computation takes constant time (excluding recursive calls), the total work is O(n).

Span: The maximum depth of recursion is n, so the span is O(n).

Q8) In the bottom-up approach:
Each F(i) is computed exactly once
For each F(i) computation, we read F(i-1) and F(i-2), so each F(i) is read at most twice (except F(0) and F(1))
The maximum number of times any F(i) will be read is 2
Work: We perform a constant amount of work for each of the n values, so the work is O(n).

Span: Since we compute the values iteratively in a for loop, the span is also O(n).

