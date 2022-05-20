# Josephy

Functionality to simulate variations of the Josephus problem.

## Tutorial

This tutorial will explain how to use `josephy` to model the Josephus Problem and potential variations. Background information for the Josephus problem can be found here: <https://en.wikipedia.org/wiki/Josephus_problem> 

For this problem, we denote the number of people participating by $n$, and the 'step' by $k$.

To start, we will import the `josephy` library and run the simulation for $n$ = 43, $k$ = 2:

```python
>>> import josephy
>>> no_of_survivors = 1
>>> show_eliminations = False
>>> no_of_players = 43
>>> chosen_rule = 'standard'
>>> k = 2
>>> print(josephy.simulate(no_of_players, chosen_rule, k, no_of_survivors, show_eliminations))
23

```
We can run simulations for different values of $n$:

```python
>>> list = [josephy.simulate(x, chosen_rule, k, no_of_survivors, show_eliminations) for x in range(1,10)]
>>> print(list)
[1, 1, 3, 1, 3, 5, 7, 1, 3]

```

## How to guides
### How to find and select a rule
In order to find a rule that is currently coded into the software, we can use the `display_rules` function:
```python
>>> print(josephy.display_rules())
['cubes', 'fibonacci', 'squares', 'standard']

```
In order to select one of these rules, we just set the variable `chosen_rule` to one before we run a simulation:
```python
>>> chosen_rule = 'fibonacci'

```
### How to run a simulation
In order to run a simulation under certain paramters, we first choose each parameter and then call the function `simulate`:
```python
>>> no_of_players = 15
>>> chosen_rule = 'standard'
>>> k = 3
>>> josephy.simulate(no_of_players, chosen_rule, k, no_of_survivors, show_eliminations)
5

```
Where no_of_players is a natural number,
chosen_rule is a function listed in the Rules class and 
k is a natural number.


### How to add a rule
We can expand upon the Josephus library by adding new rules into the `Rules` class, we can do this simply by writing a new function in the class which takes two arguments: k and iteration, and computes an integer output from these.
## Explanation
### Brief overview of circular lists
The Josephus problem works where players are sat in a circle, however, python lists have finite length and searching for an item with an index that is outside the range of indexes does not work, we can resolve this with the code: 
```python
>>> group = [1,2,3]
>>> idx = 4
>>> idx = idx%(len(group))
>>> print(idx)
1

```
This reduces any index that was to be put into the code to one within the range.

### Mathematical solution for k = 2
For k = 2, the Josephus problem can be solved mathematically without simulation or recursion, this is done by calculating $2\times(n - 2^{\lfloor log{_2}(n)\rfloor})+1$.
We can do this using the `josephus_math` function, for example: $n$ = 43.

```python
>>> print(josephy.josephus_math(43))
23

```
This shows that for $n$ = 43, the survivor is whoever sits in the ${23}^{rd}$ position.
### The "Turks and Christians" variation of the problem
One variant of the problem is a medieval variation involving Turks and Christians, this problem is different as the number of survivors is not necessarily equal to 1, we can change this with this code:
```python
>>> no_of_players = 30
>>> no_of_survivors = 15
>>> chosen_rule = 'standard'
>>> k = 9
>>> print(josephy.simulate(no_of_players, chosen_rule, k, no_of_survivors, show_eliminations))
[1, 2, 3, 4, 10, 11, 13, 14, 15, 17, 20, 21, 25, 28, 29]

```

## Reference
### List of functionality
The following functions are written in `Josephy`:
- `display_rules`
- `simulate`
- `josephus_math`
### Bibliography
The wikipedia page for the Josephus problem gives a good overview: <https://en.wikipedia.org/wiki/Josephus_problem>

The following text is also recommended for further understanding:

>Peter Schumer. "The Josephus Problem: Once More around"



### Testing the software

To test the code:

```
$ python test_josephy.py
```

To test the documentation:

```
$ python -m doctest README.md
```