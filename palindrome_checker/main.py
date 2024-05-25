def remove_non_alphanumeric_chars(string):
  return ''.join([i for i in string if i.isalnum()])

def number_of_unique_chars(string):
  return len(set(string))

def is_palindrome(string):
  return string == string[::-1]

with open('./input.txt', 'r') as f:
  lines = f.readlines()
  for i in lines:
    string = remove_non_alphanumeric_chars(i.lower())
    if is_palindrome(string):
      print(f"YES, {number_of_unique_chars(string)}")
    else: 
      print("NO, -1")