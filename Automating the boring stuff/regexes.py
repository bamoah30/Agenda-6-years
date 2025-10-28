import re
phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

mo = phoneNumberRegex.search('My number is 415-555-4242.')
#To solve the problem of getting an error when no match is found, we guard the call to mo.group() with an if statement
#We do this because the search() method returns None if no match is found and None does not have a group() method
if mo:
	print('Phone number found: ' + mo.group(1))
	print(mo.group(2))
	print(mo.group(0))
	print('Full match: ' + mo.group())
	#The groups() methode returns all the groups of a match in a tuple
	#Thus from the above: print(mo.groups()) should return ('415', '555-4242')
	print('All groups: ' + str(mo.groups()))
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