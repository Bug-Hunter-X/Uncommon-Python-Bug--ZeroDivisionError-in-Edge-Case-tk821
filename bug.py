def function_with_uncommon_bug(x):
    if x == 0:
        return 1 / x  # ZeroDivisionError
    else:
        return x + 1

result = function_with_uncommon_bug(0)
print(result)