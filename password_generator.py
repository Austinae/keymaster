# To include in README.md:
# 
# Command line tool to generate a password
# 
# Example use cases
#
# Generate password with 20 characters, with custom symbols *, $, `, /, =, £ , ',' and ?
# 
# py password_generator.py -l 20 -cs '*$`/=£,?'
# => z`BMSnE/JfpE3$G?vsu
#
# Generate password with 14 characters, no numbers and no symbols
#
# py password_generator.py -l 14 -nn -ns
# => AwwtzcOramhTSy
#
# Which also equates to
#
# py password_generator.py -l 14 --no-numbers --no-symbols
# => bTugbLLAxQwuKN

import argparse
import random

def generate_password(no_uppercase, no_lowercase, no_numbers, no_symbols, custom_symbols, length):
	possible_characters = []
	if not no_uppercase:
		possible_characters += [chr(i) for i in range(ord('A'), ord('Z')+1)]
	if not no_lowercase:
		possible_characters += [chr(i) for i in range(ord('a'), ord('z')+1)]
	if not no_numbers:
		possible_characters += [chr(i) for i in range(ord('0'), ord('9')+1)]
	if custom_symbols is not None:
		possible_characters += [x for x in custom_symbols]
	else:
		if not no_symbols:
			possible_characters += ['*', '^', '!', '@', '#', '$', '?', '/', '[', ']', '+', '_']
	if not possible_characters:
		return "Incorrect parameters, the generated password would be empty, please try again"
	
	password = ''
	for i in range(length):
		password += random.choice(possible_characters)
	return password

parser = argparse.ArgumentParser(prog = 'Password Generator', description = 'What the program does', epilog = 'Thanks for using Password Generator by Wills')
parser.add_argument('-nu', '--no-uppercase', action='store_true', default=False, help='Password will not contain uppercase characters')
parser.add_argument('-nl', '--no-lowercase', action='store_true', default=False, help='Password will not contain lowercase characters')
parser.add_argument('-nn', '--no-numbers', action='store_true', default=False, help='Password will not contain numbers')
parser.add_argument('-ns', '--no-symbols', action='store_true', default=False, help='Password will not contain default symbols *^!@#$?/[]+_]')
parser.add_argument('-cs', '--custom-symbols', type=str, help='Custom set of symbols for your password, takes precedence on default symbols')
parser.add_argument('-l', '--length', type=int, default=8, help='The length of the password')

if __name__ == '__main__':
	args = parser.parse_args()
	password = generate_password(args.no_uppercase, args.no_lowercase, args.no_numbers, args.no_symbols, args.custom_symbols, args.length)
	print(password)

