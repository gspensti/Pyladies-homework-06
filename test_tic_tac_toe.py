from Homework_lesson_06 import evaluate, move

def test_evaluate():
    is_x = evaluate("xxx-----------------")
    is_o = evaluate("ooo-----------------")
    is_full = evaluate("xoxoxoxoxoxoxoxoxoxo")
    not_finished = evaluate("xxo-----------------")
    assert is_x == "x" # tests if scenario where x wins is handled correctly
    assert is_o == "o" # tests if scenario where o wins is handled correctly
    assert is_full == "!" # tests if scenario where neither wins (aka board is full) is handled correctly
    assert not_finished == "-"  # tests if handling of ongoing game is handled correctly
    

def test_evaluate_draw(): # tests if both x an o can win  
    tie = evaluate("xxx--------------ooo") # meant to fail since this scenario shouldn't happen anyways
    assert tie == "!" # tells us that we're not yet handling this scenario in the program 

def test_no_input_yet(): 
    nothing = evaluate("--------------------") # handles ongoning game correctly 
    assert nothing == "-"

def test_move():
    x_in_string = move("--------------------", 2, "x") # tests if function updates board correctly (puts char at given position)
    assert x_in_string == "--x-----------------" # should be on position 3 since position number will be subtracted by 1 only in player_move function, not in move function
    
def test_takes_other_characters(): # tests if function allows other characters than x or o as input
    u_in_string = move("--------------------", 2, "u") # test works but this means I need to rewrite the game so that x and o are only chars allowed 
    assert u_in_string == "--u-----------------"

""" What is a Python module and how does it differ from a Python package?

A module is usually a single file containing related ready-to-use functions, variables, classes, etc.  
A package is a collection of related modules. They can also contain sub-packages in them. 

What are side effects and give some examples.
Side effects are undesired effects happeneing when modules are imported.
This happens when a module performs any action beside defining functions, classes, etc. (e.g. it prints, writes, opens, moves a turtle etc). Because python 
runs scripts from top to bottom once they're imported.  
An example would be a custom module with a print statement. When imported, this module will be executed and 
it will print something. If the module is imported again, the print function will not be executed anymore because 
Python uses the already initialized module. 

What are Exceptions and what to do if third-party code that we use throws them?
Excptions are error states that can kill a program. Python has some built in exceptions, organized in hierarchies. 
They kind of tell you more about why your program doesn't work as desired. E.g. ZeroDivisionError tells you 
that your program had to divide something by zero, which is not possible. 

If third-party code throws exceptions we need to look at the error message to get an idea of what the problem is. We could also check the documentation 
of the code or look for the message online. 
Eventually, we want our program to catch and handle the exception. We might need to check our input (are data/parameters correct and within expected ranges?) and/or
we can handle it by useing try/except blocks. 



Using which keywords can you create, throw and catch your new custom Exception?
"raise" + name of exception, creates/throws an exception (doesn't handle it)
"except", catches all exceptions 
"except" + name of exception catches specific type of exception; exceot is used for part of program that 
handles errors 

Give examples of some benefits of testing?
Testing verifies that a program runs correctly, or that errors are handled correctly. It can also help
in finding bugs/non desired behavior that has not been considered yet. """










