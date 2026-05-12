from pathlib import Path

base_path = Path(__file__).parent
file_path = base_path / "pi_digits.txt"

with open(file_path, 'r') as f:
   contents = f.read()
   contents = contents.rstrip()
   #print(contents)
   lines = contents.splitlines()
   for line in lines:
      print(line)
pi_string = ''
for line in lines:
   pi_string += line
print(pi_string)
print(len(pi_string))
