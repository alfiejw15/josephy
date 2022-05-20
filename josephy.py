import functools

class Rules():
    """
    This class of objects contains all used rules for the modeller
    """
    def standard(k, iteration):
        """
        This rule is the standard rule for the simulate problem,
        where every kth person is eliminated
        """
        return k

    def squares(k, iteration):
        """
        This rule outputs the ith square number where i is the
        current iteration or 'round' of the problem
        """
        return iteration**2

    def cubes(k, iteration):
        """
        This rule outputs the ith cube number where i is the
        current iteration or 'round' of the problem
        """
        return iteration**3
    
    @functools.lru_cache()
    def fibonacci(k, iteration):
        """
        This rule takes an input n and outputs the nth fibonacci number,
        where fib(0) = 1 , fib(1) = 1 and fib(n) = fib(n-1) + fib(n-2)
        """
        if iteration == 0:
            return 1
        if iteration == 1:
            return 1
        else:
            output = Rules.fibonacci(k, (iteration - 1)) + Rules.fibonacci(k, (iteration - 2))
            return output

def display_rules():
    """
    Displays all rules in the Rules directory
    """
    list_of_rules = ([f for f in dir(Rules) if f.startswith('__') is False])
    return list_of_rules

def simulate(no_of_players, rule, k, no_of_survivors, show_eliminations):
    """
    This function takes three inputs: the group of players, the chosen rule, and k.
    it then runs the simulation under these parameters.
    """
    group  = [i for i in range(1, no_of_players + 1)]
    iteration = 1
    skip = eval('Rules.'+str(rule)+'('+str(k)+','+str(iteration)+')')
    skip -= 1 # this reduces skip by 1 to account for how the index of player n is actually (n - 1)
    idx = skip
    idx = idx%(len(group)) # this uses modular arithmetic to make the list circular
    while len(group) > no_of_survivors:
        iteration += 1
        if show_eliminations == True:
            print(group.pop(idx))
        else:
            group.pop(idx)
        skip = eval('Rules.'+str(rule)+'('+str(k)+','+str(iteration)+')')
        idx = idx + skip - 1
        idx = idx%(len(group))
    if no_of_survivors == 1:
        return (group[0])
    else:
        return group

def josephus_math(no_of_players):
    """
    This function takes a natural number as an input and computes 2l + 1,
    where l is the difference between the input and the biggest power of 2
    that is less than or equal to the input.
    """
    greatest_power = 0
    while 2**(greatest_power + 1) <= no_of_players:
        greatest_power += 1
    l = (no_of_players - 2**greatest_power)
    return 2*l + 1