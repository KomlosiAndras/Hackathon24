#removes every non alphanumeric charcters from a given string
def remove_non_alphanumeric_chars(string):
  return ''.join([i for i in string if i.isalnum()])

#returns the number of unique characters in a given string
def number_of_unique_chars(string):
  return len(set(string))

#returns true if the given string is a palindrome (it is the same forwards and backwards)
def is_palindrome(string):
  return string == string[::-1]

#reading the input file and and checking each line to see if it is a palindrome or not
with open('./input.txt', 'r') as f:
  lines = f.readlines()
  for i in lines:
    string = remove_non_alphanumeric_chars(i.lower())
    if is_palindrome(string):
      print(f"YES, {number_of_unique_chars(string)}")
    else: 
      print("NO, -1")