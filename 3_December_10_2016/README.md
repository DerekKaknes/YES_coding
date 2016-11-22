# Lesson 3 - Intro to Classes and Review of Functions
Welcome back to **_YES Coding!_**  After a break for Thanksgiving and some brain
dissection, I'm looking forward to getting back into some Python!  In the last
two lessons, we have covered `strings` and `functions`, as well as some basic python
syntax.  You may feel a little bit rusty on those topics after the two week
absence, but don't worry - today will be part review and part new material.  Our
focus today is on the concept of [Object-Oriented
Programming](https://en.wikipedia.org/wiki/Object-oriented_programming).
Object-oriented programming is a big concept, but we are going to get our feet
wet with the initial concepts of `classes` and `objects`.
## Beginner - Introduction to Python Classes
Your objectives today are as follows:

1. Read through this introduction and work through (in discussion with others)
the coding problems that are presented;
2. Complete the codecademy course linked to at the end of this section;
3. Attempt as many of the coding challengs in `beginner_classes.py` as you feel
comfortable with.

### Introduction to Classes and OOP
Last lesson, we built some fuctions that could be useful in the future, like
`cube` and `one_good_turn`, and we also learned how to load those function
using `from ____ import ____`.  Ordering and combining several functions into a
single set of commands is one way to organize your code (often called
**Functional Programming**), but a different - and very common - way of
organizing your code is through **Objects**.  In Python, we create `objects`
from `classes`.  A `class` is pretty simple - it is a group of abilities or
attributes that are shared by a type of object.  It is most easily demonstrated
through examples:

### The Difference Between a Class and an Object
My first car was a Toyota Avalon.  My car is one of thousands (maybe
millions) of Toyota Avalons that exist in the world, but each of them shares
common traits and abilities: they are the same size, have the same number
wheels, can drive forward and backward, can reach the same top speed at the
same acceleration, etc.  Thus, my car is an `object` of the
Toyota Avalon `class`.  There might be millions of `objects` (millions of
individual Toyota Avalon cars), but they are all of the same `class` of Toyota
Avalon.

In a sports video game (like FIFA or Madden or NBA2K), there is usually an
option to create a player.  If you choose to create a player, they will often
give you the ability to adjust and customize specific attributes like the
player's height, weight, hairstyle, uniform style, etc.  Each player you create
is an `object` of the Player  `class`.  You can create hundreds of objects,
but they are all of the single Player class.

#### Quiz: Differentiating Classes and objects
For each question, decide whether the blank should be `object` or `class` and
discuss why with your neighbor.

1. Kevin Durant is an ______ of the `BasketPlayer` ______.
2. Tom Brady is an ______ of the `FootballPlayer` _______.
3. The Honda Civic is a _________; the Honda Civics that I see on the streets
are ________.
4. The `SportsUtilityVehicle` (or SUV) is a _________.
5. My mom's SUV is an ________.
6. I am an ________ of the `HumanBeing` __________.
7. Come up with your own and share it with your neighber.

### `attributes` = Characteristics
Let's return to our example of creating a player in Madden (you can think of a
different game if you are not an NFL fan).  Every time we create a player, we
are "initializing" an object of the `FootballPlayer` class.  But what does that
mean?  What characteristics and abilities does a `FootballPlayer` have?  Well, to
start they probably need to have a `name`.  In coding, we would say that the
`FootballPlayer` class has an `attribute` called "name".  The `FootballPlayer`
may have many more `attributes` related to physical appearance: `height`,
`weight`, `hairstyle`, `eye_color`, `skin_color`, and on and on.  

In python, we would define the `FootballPlayer` class and its associated
`attributes` like this:
```python
class FootballPlayer:
  def __init__(self, name, height, weight):
    self.name = name
    self.height = height
    self.weight = weight
```
Woah, there's a lot going on there!  Let's take a look line by line:
```python
class FootballPlayer:
```
This line defines the new class called 'FootballPlayer'.  It is similar to the
`def function_name():` notation that we used to define functions.
```python
  def __init__(self, name, height, weight):
```
Now, this line looks a little crazy - but it's actually just another function that uses
the `def function_name(inputs):` notation.  However, there are a couple unique
things about this line.  First, the `__init__` function (short for "initialize")
is a special function that the `FootballPlayer` class uses to "initialize" (aka
create) new objects (aka to create new players).  Second, you probably notice
that it is surrounded by `__`, that is because python
does not want you to accidentally overwrite this function, so it puts two
underscores (`__`) before and after it as a kind of warning for us.  Lastly, you should also
notice that the first input to `__init__` is `self`.  What is `self`?  `self`
is literally the new object referencing itself.  Don't worry too much about it right
now, but you will see `self` A LOT in Python. It may feel strange at first, but
you will gain comfort with what it means over time.
```python
    self.name = name
    self.height = height
    self.weight = weight
```
These lines defines what `attributes` each object of the class has and gives
each a value.  So for our
`FootballPlayer` class, we want to create and assign values for `name`,
`height`, and `weight`.  Notice that we reference each `attribute` through the
`self.<attribute_name>` notation.  This just tells the object (the player) that
these attributes are referencing itself, and not some other `FootballPlayer`.

---

Finally, let's take a look at how we might use our new `FootballPlayer` class to
create new football players.
```python
tom_brady = FootballPlayer('Tom Brady', 6.33, 225)
rob_gronkowski = FootballPlayer('Rob Gronkowski', 6.50, 265)
joe_montana = FootballPlayer("Joe Montana", 6.16, 205)

print "Player named " + tom_brady.name + " is " + tome_brady.height + "feet tall and weighs " + tom_brady.weight + " pounds"
# Player named Tom Brady is 6.33 feet tall and weighs 225 pounds
```


### `methods` = Abilities
In addition to having common `attributes`, classes will often times often have
common abilities.  For example, a `FootballPlayer` might have an ability called
`run` or `tackle`.  In python, we call these abilities `methods`.  `methods` are
simply functions that are defined within a class.  Defining methods is very
similar to defining functions, except that the first input is (usually) `self`.
```python
class FootballPlayer:
  def __init__(self, name, height, weight):
    self.name = name
    self.height = height
    self.weight = weight

  def run(self):
    # This is a method called 'run'
    print self.name + "is running!"

  def tackle(self, target):
    # This method takes an input of 'target' to identify who to tackle
    print self.name " is tackling " + target + "!"
```
Every object of a class has access to its `methods` and can call those methods
using `<object_name>.<method_name>()` notation.  Let's look at an example from
`FootballPlayer`:
```python
richard_sherman = FootballPlayer("Richard Sherman", 6.10, 230)
richard_sherman.run()
# Richard Sherman is running!
richard_sherman.tackle("Tom Brady")
# Richard Sherman is tackling Tom Brady!
```
#### Quiz: More Methods

1. With your neighbors, discuss and come up with a couple more methods that the
`FootbalPlayer` class might have.  
2. Other than cars and athletes, can you think of another object that you might
represent as a class?  What would be some of its attributes and methods?
3. What would be some of the attributes and methods that the `YESStudent` class
might have?

### Codecademy - Python Classes
Now that you have an idea of classes, go over to [codecademy](https://www.codecademy.com/courses/python-intermediate-en-WL8e4/0/1) to practice a
little more with classes.
### Coding Challenges - `beginner_classes.py`
If you finish the codecademy section, then take a look at `beginner_classes.py`
for some additional work with classes.
## Advanced - Common Design Patterns: Dependency Injection

