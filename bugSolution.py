def function_with_uncommon_bug(x):
    try:
        if x == 0:
            return 1 / x
        else:
            return x + 1
    except ZeroDivisionError:
        return float('inf')  # Or another appropriate response

result = function_with_uncommon_bug(0)
print(result) # Output: inf