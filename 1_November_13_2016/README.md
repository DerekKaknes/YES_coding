# Lesson 1 - Strings and Traffic Lights
Today we are going to take our first dive into programming with Python.  Some
folks may already be familiar with the Python programming language, while most
of you will not be.  As such, we have three separate coding challenges ranging
in difficulty - I suggest that you pair up with a fellow student who is similar
in coding proficiency and work together to complete your challenges.

##Beginners - Working with Strings
As an intro to programming in python, we are going to start by introducing the
different data types and structures used most frequently.  Most of these types
can be found under the documentation for [Built-In
Types](https://docs.python.org/2/library/stdtypes.html).  The first of those
types will be [Strings
(`str`)](https://docs.python.org/2/library/stdtypes.html#string-methods), 
which you can think of as sequences of characters (both letters, numbers and
special characters). Read through the documentation and methods for Strings and
then try and complete the first two lessons of
[Codecademy's](https://www.codecademy.com/learn/python) online python
tutorial.  Once you have completed those lessons - or if you feel up for it
beforehand - try downloading the starter code from this repo (ask Derek if you
have questions) and try to code up a working solution!

##Intermediate - Advanced Strings and Regular Expressions (regex)
One of the most common - and potentially most frustrating - tasks in programming
is to search through a string or list of strings in order to find and/or replace
certain values.  A great resource to start or brush up on regex rules is
[Codecademy's](https://www.codecademy.com/courses/python-intermediate-en-HJJev/0/1)
online python course for using regex.  Try to complete the exmaples in this
short course and then test your knowledge on the challenges found under
`intermediate_regex.py`.  If you have questions, you can always refer to the
[`regex` documentation](https://docs.python.org/2/library/re.html).

##Expert - Computer Vision: Traffic Light Challenge
For our first project, we are going to look into using Computer Vision to aid in
a (for now) theoretical robot's decision making.  In this challenge, you are
tasked with developing a program that will process an image from your computer's
webcam and make a decision on whether the color in the image is (predominately)
red, yellow or green.  Based on that determination, your program should inform
your robot to either Stop!, Slow Down!, or Go!, respectively.  

You can find starter code under `expert_traffic_light.py`, which will repeatedly
capture images from your computers webcam and pass them to your processing
function, which is called `determine_light_color`.  Currently, that function
will always return a valu of `'red'`; your job is to write code that will
analyze the RGB image in order to make a determination as to what color is
actually present.

For guidance, you may want to start by reading about RBG images and how they are
stored as arrays of pixel values.  You may also want to famliarize yourself a
little bit with python's `numpy` package and `numpy.array` data structure, which 
we are using to store and analyze our images.  For this project, you should not
need to use any particularly complex data analytics algorithms; however, I would
encourage you to read more about the tools that company's like Google, Nvidia, Tesla and
Uber are using in developing their own autonomous vehicles.



