# Lesson 2 - Working with Functions
Today we are going to learn about functions and how they are used in
programming.  You may be familiar with functions from math - y=f(x) ... - and,
if you are, programmed functions are very similar.  In general, a function is
defined as a set of actions that takes one or more inputs and returns one or
more outputs.
## Beginners - Functions
In python, functions are defined using:
 ```python
def name_of_function(input):
   # Do stuff
   return output
``` 
In this example, we are defining - the "def" - a new function that is called
`name_of_function`, and that function takes a input value called `input` and
returns an output value called `output`.  That is pretty abstract, so let's look
at an example from last week:
```python
def greet(name):
  print "Hello " + name + "!"
  return None
```
What do you think this function will do?  If you remember from last week, this
function, called `greet`, takes a `name` as an input, then prints out "Hello
<name>!" to the screen.  Notice that the function returns `None`, which is a way
of saying that it doesn't return any value.  Compare that to a function that
does return a value:
```python
def add_two_numbers(x, y):
  sum = x + y
  return sum
```
This function, called `add_two_numbers`, takes in two numbers, `x` and `y`, and
returns the sum of those numbers.  Thus, if we called the function we would
expect the following:
```python
add_two_numbers(2, 3)
# 5
add_two_numbers(100, 50)
# 150
```
In today's lesson, we are going to work through the [codecademy course on python
functions](https://www.codecademy.com/courses/python-beginner-c7VZg/0/1?curriculum_id=4f89dab3d788890003000096).
After we have completed that course (should take ~30 minutes), we will move on to today's coding challenge.  
In today's challenge, we are going to build a series of functions that compute
mathematical and logical functions.  You can find the starter code in
`beginner_functions.py`.

## Expert - Object Oriented Design: Working with Classes
Based on your level of experience, you may or may not be familiar with Classes.
We will have a series of challenges and design patterns that utilize classes and
objects.  Take a look at the [codecademy course on python classes](https://www.codecademy.com/courses/python-intermediate-en-WL8e4/0/1?curriculum_id=4f89dab3d788890003000096).
If you are comfortable with this content, then you can advance to the code
challenges with classes and inheritance.
