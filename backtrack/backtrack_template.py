"""
Here are a few notes about the above pseudocode.

Overall, the enumeration of candidates is done in two levels:
 1). at the first level, the function is implemented as recursion. At each
 occurrence of recursion, the function is one step further to the final
 solution.

 2). as the second level, within the recursion, we have an iteration that
 allows us to explore all the candidates that are of the same progress to the
  final solution.

The backtracking should happen at the level of the iteration within the
recursion.

Unlike brute-force search, in backtracking algorithms we are often able to
determine if a partial solution candidate is worth exploring further (i.e.
is_valid(next_candidate)), which allows us to prune the search zones. This is
also known as the constraint, e.g. the attacking zone of queen in N-queen game.

There are two symmetric functions that allow us to mark the decision
 (place(candidate)) and revert the decision (remove(candidate)).
In the next sections, we show some concrete examples and explain how to apply
the above pseudocode template.
"""
def backtrack(candidate):
    if find_solution(candidate):
        output(candidate)
        return

    # iterate all possible candidates.
    for next_candidate in list_of_candidates:
        if is_valid(next_candidate):
            # try this partial candidate solution
            place(next_candidate)
            # given the candidate, explore further.
            backtrack(next_candidate)
            # backtrack
            remove(next_candidate)