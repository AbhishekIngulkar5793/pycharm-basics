"""
# programming approacch

print('Helllloooo')

k = [1,2,3,4]
print(k)
print(k.count(1))
#---------------------------------

# PEP Standards : Python Enhanced Proposal 8
x = 100
y=100 # it is not as pep standards pep8
# read a blog on pep 8 which includes the rules about how to write a code as per standard
-------------------------------------


# INDENTATION : It is a space used by a functional block
# to decide a scope of that block

# when we are writing a function we need indentation
def addition():
    print(100+200)
---------------------------------------------------------------

# flow control blocks
#1. selective or conditional statements
# BASED ON CONDITION WILL PERFORM FURTHER OPERATION
if <condition>:
    perform task
=======================

# example
# syntax: if condition:
# if condition is true then the control will go inside the loop/block
# but if the condition is false then the control will not enter inside the loop/block
if 10 > 2:
    # operations to be performed
    print('10 is greater than 2')
---------------------------------------------------

if else
    if elif else
    if elif elif else
    if elif elif elif # elif ladder
    if elif elif elif else
if #NESTED if else
    if
    else
else

2. Iterative statements
3. transfer statements
============================================

# pin = 1234
pin = int(input('Enter your pin:'))
if pin == 1234:
    print('Perform transaction')
# if condition is resulting false then control will go to else block
else:
    print('you have entered wrong pin, please try again')
"""
# we will use if : when we want to test a single condition
# we will use if else: when we want to test two conditions
# what is the difference between if and else??
# if is condition based whereas else is condition less
# if is the entry point , but else is exit point
# else follows if , but if never follows else
==============================================
