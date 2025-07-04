# Integer variable
integer_var = 10
# Float variable
float_var = 3.14
# String variable
string_var = "Hello, World!"
# Boolean variable
boolean_var = True

# Perform basic operations

# Integer operations
sum_integers = integer_var + 5
product_integers = integer_var * 2

# Float operations
sum_floats = float_var + 1.86
product_floats = float_var * 2

# String operations
concat_strings = string_var + " How are you?"
repeat_string = string_var * 2

# Boolean operations
boolean_not = not boolean_var
boolean_and = boolean_var and False

# Print results and their types

print(f"Integer variable: {integer_var}, Type: {type(integer_var)}")
print(f"Sum of integers: {sum_integers}, Type: {type(sum_integers)}")
print(f"Product of integers: {product_integers}, Type: {type(product_integers)}")

print(f"Float variable: {float_var}, Type: {type(float_var)}")
print(f"Sum of floats: {sum_floats}, Type: {type(sum_floats)}")
print(f"Product of floats: {product_floats}, Type: {type(product_floats)}")

print(f"String variable: {string_var}, Type: {type(string_var)}")
print(f"Concatenated strings: {concat_strings}, Type: {type(concat_strings)}")
print(f"Repeated string: {repeat_string}, Type: {type(repeat_string)}")

print(f"Boolean variable: {boolean_var}, Type: {type(boolean_var)}")
print(f"Negated boolean: {boolean_not}, Type: {type(boolean_not)}")
print(f"Boolean AND operation: {boolean_and}, Type: {type(boolean_and)}")
