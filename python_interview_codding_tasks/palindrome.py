# madam
# racecar
# A man, a plan, a canal: Panama

input = 'A man, a plan, a canal: Panama'
s = ''.join(c for c in input if c.isalnum()).lower()
print(s)
print(s == s[::-1])