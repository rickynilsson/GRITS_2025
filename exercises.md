# GRITS 2025 Workshop session 2: AI-assisted coding with Copilot in VS Code

## Exercise 1: Simple code completion example 1
A basic coding exercise to demonstrate GitHub Copilot's simple code completion in VS Code is creating a **factorial function** in Python.

**Goal:** Write a function that calculates the factorial of a non-negative integer.

1. Create a file named `simple_funcs.py`.
2. Write a clear comment in natural language describing the function's purpose. This gives Copilot context.
```
# Function to calculate the factorial of a given number using a loop
```
3. Start the function definition directly below your comment.
```
def factorial(n):
```
4. As soon as you type the function signature and press Enter (or open the curly brace in JavaScript), GitHub Copilot will likely suggest the *entire* function body, including initialization, the loop, and the return statement, in greyed-out text (ghost text).
   **Accept the suggestion** by pressing the **Tab** key.


## Exercise 2: Simple code completion example 2
A similar basic Python exercise that demonstrates GitHub Copilot's simple code completion is creating a function to **reverse a string**.

**Goal:** Write a Python function that takes a string and returns the string with its characters in reverse order.

1. Open the same file `simple_funcs.py` that you just created in exercise 1.
2. On the first line, write a clear, descriptive comment.
```
# Write a function that reverses a string
```
3. On the next line, start defining the function, including a descriptive name and parameter.
```
def reverse_string(text):
```
4. As soon as you press Enter after the colon (:), Copilot will likely suggest the entire function body, which often includes the most idiomatic Python solution (using slicing).
   Press the **Tab** key to **accept** the suggested code completion.


Copilot has the ability to interpret a simple natural language prompt (in the comment and/or function signature) and immediately provide a multi-line, syntactically correct code block for a common task, showcasing its most basic form of code completion.

In the VS Code terminal, start a Python interpreter and try out your functions!
```
GRITS_2025/ » python
Python 3.11.7 (main, Dec 15 2023, 12:09:04) [Clang 14.0.6 ] on darwin
Type "help", "copyright", "credits" or "license" for more information.
Cmd click to launch VS Code Native REPL
>>> from simple_funcs import factorial, reverse_string
>>> factorial(14)
87178291200
>>> reverse_string('hello world')
'dlrow olleh'
```


## Exercise 3: Slightly more complex code completion
A slightly more advanced Python exercise that still relies heavily on simple code completion is creating a function to **check if a word is an anagram of another word**.
This task is more advanced because the solution requires multiple lines and a specific logic (sorting or character counting), which Copilot is very good at inferring.

**Goal:** Write a function that takes two strings and returns `True` if one is an anagram of the other (meaning they contain the same characters with the same frequency, ignoring case/spaces), and `False` otherwise.

1. Open the same file `simple_funcs.py` that you just created in exercise 1.
2. Write a comment that clearly outlines the function's purpose and the required inputs.
```
# Write a function that takes two strings and checks if they are anagrams.
# The function should ignore spaces and case.
```
3. Begin defining the function.
```
def is_anagram(str1, str2):
```
4. As soon as you press Enter after the colon (:), Copilot will use the context of the comment and the function signature to suggest the complete, multi-step solution.
   The suggested completion will likely involve cleaning the strings (removing spaces and converting to lowercase) and then sorting them for comparison, which is a common and efficient way to solve this problem.
   Press the **Tab** key to **accept** the suggested code completion.

This code is slightly more complex because it involves multiple, distinct steps inside the function body (`.replace()`, `.lower()`, and `sorted()`), demonstrating Copilot's ability to generate a small algorithm, not just a single-line result.


## Exercise 4: Code efficiency and refactoring
Now we will test Copilot's understanding of **code efficiency** and its ability to suggest **refactoring**. A great example for this is a function to **find the first non-repeated character in a string**.

You will intentionally write a less efficient, brute-force solution (using nested loops) and then prompt Copilot to suggest a more efficient one (using a dictionary/hash map).

**Goal:** Write a function that finds and returns the first character in a string that appears only once.
1. Open the same file `simple_funcs.py` that you just created in exercise 1.
2. Intentionally write a function using a nested-loop approach (or a similar brute-force method) that has a time complexity of $O(n^2)$.
```
def find_first_non_repeated_char(text):
    for i in range(len(text)):
        is_repeated = False
        for j in range(len(text)):
            if i != j and text[i] == text[j]:
                is_repeated = True
                break
        if not is_repeated:
            return text[i]
    return None
```
*This code works but is slow for long strings.*

3. Use Copilot's **Inline Chat** to Refactor:
   + Select the entire function block (all lines from `def find_first_non_repeated_char(text):` to `return None`).
   + Open the Inline Chat feature (usually by pressing **Ctrl+I** or **Cmd+I**).
   + Enter the following prompt: *Refactor this function to be more efficient. Use a dictionary or a hash map.*
   + Copilot should analyze the selected code and the prompt, and then suggest a refactored version that uses a single pass to count character frequencies, and a second pass to find the first character with a count of one.
     This is a much more efficient $O(n)$ solution. Review the $O(n)$ solution and press Accept to replace your original, less efficient code.

This exercise demonstrates how Copilot can assist with refactoring based on explicit instructions for algorithmic improvement, moving beyond simple one-line completions.
