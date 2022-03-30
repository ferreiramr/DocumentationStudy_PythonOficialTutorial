#%%
######### COMMENTS

# this is the first comment
spam = 1 # and this is the second commnet
     # ... and now a third!
text = "# This is nota a comment because it's inside quotes."


#%%
######### NUMBERS

# %%
2 + 2
# %%
50 - 5*6
# %%
(50 - 5*6) / 4
# %%
8 / 5 # division always returns a floating point number
# %%
17/3 # classic division returns a float
# %%
17 // 3 # floor division discars the fraction part
# %%
17 % 3 # the % operator returns the remainder of the division
# %%
5 * 3 + 2 # floored quotient * divisor + remainder
# %%
5 ** 2 # squared
# %%
2 ** 7 # 2 to the power 7
# %%
width = 20
height = 5 * 9
width * height
# %%
n # try to access an undefined variable
# %%
4 * 3.75 - 1
# %%
tax = 12.5 / 100
# %%
price = 100.5
# %%
price * tax
# %%
12.5625
# %%
price + _
# %%
round(_, 2)
# %%
########## STRINGS
# %%
'spam eggs'     # single quotes
# %%
'doesn\'t'      # user \' to escape the single quote...
# %%
'"Yes," they said.'
# %%
"\"Yes,\" they said."
# %%
'"Isn\'t," they said.'
# %%
'"Isn\'t," they said.'
# %%
print('"Isn\'t," they said.')
# %%
s = 'First line.\nSecond line.' # \n means newline
# %%
s # without print(), \n is included in the output
# %%
print(s) # with print(), \n produces a new line
# %%
print('C:\some\name') # here \n means newline!
# %%
print(r'C:\some\name') # note the r before the quote
# %%
print("""\
Usage: thingy [OPTIONS]
-h                                      Display this usage message
-H hostname                             Hostname to connect to
""")
# %%
# 3 times 'un', followed by 'ium'
3 * 'un' + 'ium'
# %%
'Py' 'thon'
# %%
text = ('Put several strings within parentheses '
        'to have them joined together.')
text
# %%
prefix = 'Py'
#%%
# prefix 'thon' # can't concatenate a variable and a string literal
# %%
prefix + 'thon'
# %%
word = 'Python'
# %%
word[0] # character in position 0
# %%
word[5] # character in position 5
# %%
word[-1] # last character
# %%
word[-2] # second-last character
# %%
word[-6]
# %%
word[0:2] # characters from position 0 (included) to 2 (excluded)
# %%
word[2:5] # characters from position 2 (included) to 5 (excluded)
# %%
word[:2] # character from the beginning to position 2 (excluded)
# %%
word[4:] # characters from position 4 (included) to the end
# %%
word[-2:] # characters from the second-last (included) to the end
# %%
word[:2] + word[2:]
# %%
word[:4] + word[4:]
# %%
word[42] # the word only has 6 characters
# %%
word[4:42]
# %%
word[42:]
# %%
word[0] = 'J'
# %%
word[2:] = 'py'
# %%
'J' + word[1:]
# %%
word[:2] + 'py'
# %%
s = 'supercalifragilisticexpialidocious'
# %%
########## LISTS
# %%
