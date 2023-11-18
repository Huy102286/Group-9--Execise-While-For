string=input('Enter string:')
revstr=''
for i in string:
    revstr=i+revstr
if string==revstr:
    print('The string is a palindrome')
else:
    print('The string is not a palindrome')