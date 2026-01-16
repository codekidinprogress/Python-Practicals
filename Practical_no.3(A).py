import string
a = "The quick brown fox jumps over the lazy dog"
b = set(string.ascii_lowercase)
s = set(a.lower())
result= b <=s
print(result)
