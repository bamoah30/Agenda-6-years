import re
phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

mo = phoneNumberRegex.search('My number is 415-555-4242.')
#To solve the problem of getting an error when no match is found, we guard the call to mo.group() with an if statement
#We do this because the search() method returns None if no match is found and None does not have a group() method
if mo:
	print('Phone number found: ' + mo.group(1)) #Output: Phone number found: 415
	print(mo.group(2)) #Output: 555-4242
	print(mo.group(0)) #Output: 415-555-4242
	print('Full match: ' + mo.group()) #Output: Full match: 415-555-4242
	#The groups() methode returns all the groups of a match in a tuple
	#Thus from the above: print(mo.groups()) should return ('415', '555-4242')
	print('All groups: ' + str(mo.groups())) #Output: All groups: ('415', '555-4242')
else:
	print('No phone number found.')
	
'''
Matching Multiple Groups with the pipe | Operator
The  | operator is called a pipe or alternation. It is used to match one of many possible groups.
It returns the first occurence of a match.
An illustration is shown below
'''
heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
if mo1:
	print(mo1.group())  #prints 'Batman' because it is the first match
else:
	print(None)
mo2 = heroRegex.search('Tina Fey and Batman.')
if mo2:
	print(mo2.group())  #prints 'Tina Fey' because it is the first match
else:
	print(None)

'''
You can also use the pipe operator to match one of several patterns with some intial commonality.
The below code demonstrate this concept
'''
# Example 1: Using capturing groups - () captures part of the match
print('\nExample 1: Capturing groups')
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')  # parentheses create a capture group
mo = batRegex.search('Batmobile lost a wheel')
if mo:
    print(mo.group())      # prints 'Batmobile' - full match
    print(mo.group(0))     # same as mo.group() - full match
    print(mo.group(1))     # prints 'mobile' - only the captured part inside ()
    print(mo.groups())     # prints ('mobile',) - all captured groups as tuple

# Example 2: Using non-capturing groups - (?:...) doesn't capture
print('\nExample 2: Non-capturing groups')
batRegex2 = re.compile(r'Bat(?:man|mobile|copter|bat)')  # (?:) means "don't capture this group"
mo2 = batRegex2.search('Batmobile lost a wheel')
if mo2:
    print(mo2.group())     # prints 'Batmobile'
    # print(mo2.group(1))  # This would raise an error - no groups were captured
    print(mo2.groups())    # prints () - empty tuple, no captures

# Example 3: Using named capturing groups - (?P<name>...)
print('\nExample 3: Named capturing groups')
batRegex3 = re.compile(r'Bat(?P<vehicle>man|mobile|copter|bat)')  # Give the group a name
mo3 = batRegex3.search('Batmobile lost a wheel')
if mo3:
    print(mo3.group())            # prints 'Batmobile'
    print(mo3.group('vehicle'))   # prints 'mobile' - access by group name
    print(mo3.groups())           # prints ('mobile',)   - all captured groups as tuple


#Wednesday, October 29, 2025
'''The ? Question Mark: Optional Matching
The question mark indicates that the group preceding it is optional.
So, it matches zero or one occurrence of the preceding group.
Example Usage:
'''

batRegex = re.compile(r'Bat(wo)?man') 
mo1 = batRegex.search('The Adventures of Batman')
mo2 = batRegex.search('The Adventures of Batwoman')

if mo1:
	print(mo1.group())  # prints 'Batman'
if mo2:
	print(mo2.group())  # prints 'Batwoman'

'''However, the question mark can be used to signify the non-greedy matching when used after other quantifiers 
like *, +, or {}.
Note that by default, these quantifiers are greedy, meaning they match as many characters as possible.
To make them non-greedy, you add a question mark ? after the quantifier
For eexample:'''
greedyHaRegex = re.compile(r'(Ha){3,5}')  #The {3,5} quantifier means "match between 3 and 5 occurrences of 'Ha'".
mo1 = greedyHaRegex.search('HaHaHaHaHa')

nongreedyHaRegex = re.compile(r'(Ha){3,5}?') #This wiil output Ha that appears three times.
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')

if mo1:
	print(mo1.group())  # prints 'HaHaHaHaHa' - greedy match
else:
	print('No match for mo1')
if mo2:
	print(mo2.group())  # prints 'HaHaHa' - non-greedy match
else:
	print('No match for mo2')



'''To match zero or more occurrences, use the asterisk * character.
For example:
'''
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
mo2 = batRegex.search('The Adventures of Batwoman')
mo3 = batRegex.search('The Adventures of Batwowowowoman')
if mo1:
	print(mo1.group())  # prints 'Batman'
if mo2:
	print(mo2.group())  # prints 'Batwoman'
if mo3:
	print(mo3.group())  # prints 'Batwowowowoman'

'''
To match one or more occurrences, use the plus + character.
For example:
'''
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
mo2 = batRegex.search('The Adventures of Batwowowowoman')
mo3 = batRegex.search('The Adventures of Batman')
if mo1:
	print(mo1.group())  # prints 'Batwoman'
else:
	print('No match for mo1') #To see the effect when no match is found

if mo2:
	print(mo2.group())  # prints 'Batwowowowoman'
else:
	print('No match for mo2') 

if mo3:
	print(mo3.group())  
else:
	print('No match for mo3') #Output: No match for mo3

''' 
The findall() Method
The findall() method returns a list of strings of all matches in the searched text.
If the regex has no groups, the findall() method returns a list of strings.
If the regex has groups, the findall() method returns a list of tuples.
For example:
'''

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')) # prints ['415-555-9999', '212-555-0000']

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') # has groups
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')) # prints [('415', '555-9999'), ('212', '555-0000')]

'''
Shorthand Character Classes
A character class is a set of characters inside square brackets [] that you wish to match.
For regular expressions, there are several shorthand character classes that can be used to simplify patterns.
\d  -  Any numeric digit from 0 to 9. Equivalent to [0-9].
\D  -  Any character that is not a numeric digit from 0 to 9. Equivalent to [^0-9].
\s  -  Any whitespace character (space, tab, newline, etc.). Equivalent to [ \t\n\r\f\v].
\S  -  Any character that is not a whitespace character. Equivalent to [^ \t\n\r\f\v].
\w  -  Any alphanumeric character (letters, digits, and underscore). Equivalent to [a-zA-Z0-9_].
\W  -  Any character that is not an alphanumeric character. Equivalent to [^a-zA-Z0-9_].
For example:
'''
xmasRegex = re.compile(r'\d+\s\w+') # matches one or more digits (\d+), followed by a whitespace character (\s),
# followed by one or more alphanumeric characters (\w+)

print(xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, ' \
'		6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')) 
# prints ['12 drummers', '11 pipers', '10 lords', '9 ladies', '8 maids', '7 swans', 
# 		'6 geese', '5 rings', '4 birds', '3 hens', '2 doves', '1 partridge']


'''
Making Your Own Character Classes
You can create your own character classes by placing the characters you want to match inside square brackets [].
For negaitve character classes, you can place a caret ^ at the start of the character class.
For example:
'''
vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')) # prints ['o', 'o', 'o', 'e', 'a', 'a', 'o', 'O', 'O']


consonantRegex = re.compile(r'[^aeiouAEIOU]')
print(consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')) 
# prints ['R', 'b', 'c', 'p', ' ', 't', 's', ' ', 
#			'b', 'b', 'y', ' ', 'f', 'd', '.', ' 
#        ', 'B', 'B', 'Y', ' ', 'F', 'D', '.']
#The caret ^ at the start of the character class negates it, so it matches any character that is not a vowel.

'''The caret  used outside a []  matcheds the character at the start of a string or pattern.
For example:'''
beginsWithHello = re.compile(r'^Hello')
mo1 = beginsWithHello.search('Hello world!')
mo2 = beginsWithHello.search('He said Hello.')
if mo1:
	print(mo1.group())  # prints 'Hello'
else:
	print('No match for mo1')


if mo2:
	print(mo2.group())
else:
	print('No match for mo2')  # prints 'No match for mo2'

'''The dollar sign $ is used to match the end of a string or pattern.
For example:
'''
endsWithNumber = re.compile(r'\d$')
mo1 = endsWithNumber.search('Your number is 42')
mo2 = endsWithNumber.search('Your number is forty two.')
if mo1:
	print(mo1.group())  # prints '2'	
else:
	print('No match for mo1')
if mo2:
	print(mo2.group())
else:
	print('No match for mo2')  # prints 'No match for mo2'

'''You can use both the caret ^ and dollar sign $ together to match an entire string.
For example:
'''
wholeStringIsNum = re.compile(r'^\d+$')
print(wholeStringIsNum.search('1234567890'))  # prints a match object
print(wholeStringIsNum.search('12345xyz67890'))  # prints None
print(wholeStringIsNum.search('12345 67890'))  # prints None


'''
The match() Method, search() method , and the fullmatch() Method:
The match() method checks for a match only at the beginning of the string.
The search() method checks for a match anywhere in the string.
The fullmatch() method checks for a match that spans the entire string.
'''

'''The Wildcard Character . (Dot)
The dot . character in a regular expression matches any character except a newline.
For example:
'''
atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat.')) # prints ['cat', 'hat', 'sat', 'lat', 'mat']
#Note the ommission of 'f' in 'flat' because the dot matches only one character.


'''The dot-star .* uses the dot character followed by the star quantifier.
The .* matches zero or more occurrences of any character except a newline.
For example:
'''
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)') # The .* will match any characters between 'First Name: ' and ' Last Name: '
#and between 'Last Name: ' and the end of the string.
mo = nameRegex.search('First Name: Al Last Name: Sweigart') #Searching for the pattern in the given string
if mo:
	print(mo.group(0))  # prints 'First Name: Al Last Name: Sweigart'
	print('First name: ' + mo.group(1))  # prints 'First name: Al'
	print('Last name: ' + mo.group(2))   # prints 'Last name: Sweigart'
else:
	print('No match found.')

'''Greedy and Non-Greedy Dot-
By default, the .* is greedy, meaning it matches as many characters as possible.
To make it non-greedy, you can use .*? instead.
For example:
'''
nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
if mo:
	print(mo.group())  # prints '<To serve man>'
else:
	print('No match found.')

greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
if mo:
	print(mo.group()) #prints <To serve man> for dinner.>
else:
	print("No Match Found")

'''Matching Newlines with the Dot Character.
The Dot Character does not match newline element.
To make it recognise the newline element, pass  re.DOTALL
as the second argument in  re.compile.
For example:
'''
noNewlineRegex = re.compile('.*')
mo1 = noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')
if mo1:
	print(mo1.group()) #prints 'Serve the public trust.'
else:
	print("No match found")

newlineRegex = re.compile('.*', re.DOTALL)
mo1 = newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')
if mo1:
	print(mo1.group()) #Print :'Serve the public trust.
							#	Protect the innocent.
							#	Uphold the law.'
else:
	print("No Match found")

'''Case Insensitivity of Regexes:
Regexes are case sensitive. To make them inssensitive, we pass re.I or re.IGNORECASE
For example: These codes are have different results
regex1 = re.compile('RoboCop')
regex2 = re.compile('ROBOCOP')
regex3 = re.compile('robOcop')
regex4 = re.compile('RobocOp')
To make the regex insensitive:
'''
robocop = re.compile(r'robocop', re.I)
mo1 = robocop.search('RoboCop is part man, part machine, all cop.')
mo2 = robocop.search('ROBOCOP protects the innocent.')
mo3 = robocop.search('Al, why does your programming book talk about robocop so much?')
if mo1:
	print(mo1.group()) #prints RoboCop
else:
	print("No Match for mo1") 

if mo2:
	print(mo2.group()) #prints ROBOCOP
else:
	print("No Match found for mo2")

if mo3:
	print(mo3.group()) #prints robocop
else:
	print("No match found for mo3")

'''The sub() method:
This replaces the searched pattern with a new one.
For example:
'''
namesRegex = re.compile(r'Agent \w+')
mo1 =namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
print(mo1) #prints 'CENSORED gave the secret documents to CENSORED.'



# October 30, 2025
#Files handling