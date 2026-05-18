# 1

def safe_int(s):
    try:
        int(s)
    except Exception as e:
        print(None)

print(safe_int(5))

# 2

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("not valid")

print(safe_divide(1, 0))

# 3

def get_value(d, key):
    try:
        d[key]
    except KeyError:
        return"missing"   
        
print(get_value({"abc": "ABC"} ,"abc"))

# 4

def parse_ints(values):
    num = []
    for value in values:
        try:
            num.append(int(value))
        except ValueError, TypeError:
            continue
    return num

# 5

def set_age(age):
    if age < 0 or age > 150:
        raise ValueError
    else:
        return age

# 6

def retry(func, n):
    for i in range(n):
        try:
            return func()
        except Exception as e:
            if i == n - 1: 
                raise e

# 7
def count_errors(funcs):
    count = 0
    for func in funcs:
        try:
            func()
        except Exception:
            count += 1
    return count


