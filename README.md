# Uncommon Python Bug: ZeroDivisionError in Edge Case

This repository demonstrates a common error in Python: the ZeroDivisionError. While seemingly basic, these types of errors can be insidious, especially when dealing with complex mathematical or data processing operations. The provided example showcases the error and demonstrates the appropriate resolution.

## Bug Description
The Python function `function_with_uncommon_bug` attempts to perform a division by zero when the input `x` is 0. This results in a `ZeroDivisionError`. 

## Solution
The solution is to add explicit error handling using a `try-except` block or by including a check to prevent division by zero before the operation.