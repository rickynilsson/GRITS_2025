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

1. Open the same file `simple_funcs.py` that you created in exercise 1.
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
Now we will test Copilot's understanding of **code efficiency** and its ability to suggest **refactoring**. As an example for this we will write a function to **find the first non-repeated character in a string**.

You will first intentionally write a less efficient, brute-force solution (using nested loops) and then prompt Copilot to suggest a more efficient one (using a dictionary/hash map).

**Goal:** Write a function that finds and returns the first character in a string that appears only once.

1. Open the same file `simple_funcs.py` that you created in exercise 1.
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


## Exercise 5: Debugging
In this exercise we demonstrate GitHub Copilot's ability to **find and fix bugs** is by introducing a subtle, common logical error into a simple Python function that should pass basic tests but fail in a specific edge case. You will use the `/fix` command in the Inline Chat.

**Goal:** Create a function intended to return the median element of a sorted list, but with a subtle off-by-one error when handling even-length lists. Then, ask Copilot to fix it.

1. Open the same file `simple_funcs.py` that you created in exercise 1.
2. Define a function that calculates the median, *intentionally introducing a bug* for even-length lists. This code will successfully return the correct index for odd-length lists but will be slightly off for even-length ones.
```
def find_median(data):
    # A function to find the median value in a sorted list.
    # This function has a bug when the list has an even number of elements.
    n = len(data)
    if n % 2 == 1:
        # Correct for odd lists
        return data[n // 2]
    else:
        # BUG: This returns the element at n/2, but for an even list (e.g., len 4), 
        # the median should be the average of indices 1 and 2. 
        # This logic only returns the element at index 2.
        # It should ideally return the average of the two middle elements.
        mid = n // 2
        return data[mid]
```
3. Run a quick test to show the incorrect output:
```
GRITS_2025/ » python
Python 3.11.7 (main, Dec 15 2023, 12:09:04) [Clang 14.0.6 ] on darwin
Type "help", "copyright", "credits" or "license" for more information.
Cmd click to launch VS Code Native REPL
>>> from simple_funcs import find_median
>>> # Expected correct output: (20 + 30) / 2 = 25.0
>>> sorted_list = [10, 20, 30, 40]
>>> print(f"Median: {find_median(sorted_list)}") # Output will be 30 (Incorrect)
```
4. Use Copilot's **Inline Chat** to fix the code:
   + Select the entire function block (all lines from `def find_median(data):` to `return `data[mid]`).
   + Open the Inline Chat feature (usually by pressing **Ctrl+I** or **Cmd+I**).
   + Enter the specialized debug command: */fix*
   + Copilot should analyze the context and the flawed logic for the else block (even-length lists). It will recognize that the median for an even list requires the average of the two middle elements. The suggested fix will involve returning the average of `data[mid - 1]` and `data[mid]`:
```
# Copilot's suggested fix will appear here, which may look like this:
def find_median(data):
    n = len(data)
    if n % 2 == 1:
        return data[n // 2]
    else:
        mid = n // 2
        # FIX: Return the average of the two middle elements
        return (data[mid - 1] + data[mid]) / 2
```
5. Review the corrected $O(1)$ logic and press **Accept** to apply the bug fix.

This exercise demonstrates Copilot's ability to diagnose a logic error and apply the correct algorithmic fix using the dedicated `/fix` command, showcasing its value beyond simple completions.

## Exercise 6: Commenting and explaining code
Now we will demonstrate GitHub Copilot's `/explain` command by creating a class that performs an abstract task with several interdependent methods and internal state management, all without any docstrings or inline comments.

The complexity comes from using internal attributes (self._state), nested data structures, and a common algorithmic task that isn't immediately obvious from the method names.

**Goal:** Write a Python class that processes a list of transactions, calculates a moving average, and identifies anomalies using a threshold. The code should be fully functional but completely uncommented.

1. Create a file called `processor.py`, copy and paste the code from below and save the file.
```
import collections

class DataProcessor:

    def __init__(self, size):
        self.window = collections.deque(maxlen=size)
        self._state = []
        self._threshold = 1.5

    def ingest(self, value):
        if len(self.window) == self.window.maxlen:
            self._prune()
        self.window.append(value)
        self._process_window()

    def _prune(self):
        self._state.pop(0)

    def _get_avg(self):
        if not self.window:
            return 0
        return sum(self.window) / len(self.window)

    def _process_window(self):
        current_avg = self._get_avg()
        diff = abs(self.window[-1] - current_avg)
        anomaly = diff > self._threshold
        self._state.append((self.window[-1], current_avg, anomaly))
        return anomaly

    def get_anomalies(self):
        return [t for t in self._state if t[2]]

# Example Usage:
processor = DataProcessor(size=3)
data_points = [10, 11, 10, 50, 12, 11]

for point in data_points:
    processor.ingest(point)

print(processor.get_anomalies())
```
2. Select the entire `class DataProcessor:` block, including all methods.
3. Activate Inline Chat.
4. Type the slash command: */explain* and hit Enter.
5. Copilot will provide a comprehensive explanation of the class's purpose and the logic of its methods, even though they lack comments.
6. Expected output: Copilot should identify that the class is implementing a Moving Average Anomaly Detector. It will probably explain:
 + `__init__`: Initializes a `deque` (a fixed-size window for the moving average) and sets the anomaly **threshold**.
 + `ingest`: Manages the window size, adds a new value, and then triggers the processing logic.
 + `_get_avg`: Calculates the simple **moving average** of the current elements in the window.
 + `_process_window`: Calculates the difference between the **latest value** and the **moving average**, determines if it exceeds the `_threshold`, and stores the result in `self._state`.
 + `get_anomalies`: Filters the stored state to return only the points that were flagged as **anomalous**.
7. Open the Copilot Chat, ensure that the file `processor.py` is chosen as context, and ask Copilot to *Add docstrings and comments to clarify what the code does*.
8. Chose to either apply the updated code in the editor or insert into a new file.

The exercise shows Copilot's ability to **reason about the intent and function of uncommented, multi-method class structures** and complex internal state.

## Exercise 7: Build your own basic Python package with the help of Copilot in VS Code
Now that you have all this knowledge about how to use Copilot, use it to create a simple student database with basic functionality for adding, editing, and removing student info. Maybe include unit tests? Maybe documentation? Maybe create a simple web interface to view the database as a table? Your imagination is the only limit!
