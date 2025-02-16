text="Hello, welcome to the world of python programming"
len_of_text=len(text)

print(f"length of string is: {len_of_text}")

upper=text.upper()
print(f"Uppercase version of the string: {upper}")

lower=text.lower()
print(f"lowercase version of the string : {lower}")

sub="python"
is_present=sub in text

print(f"id {sub} present in the original string ? {is_present}")

words=text.split()

print(f"List of words: {words}")
