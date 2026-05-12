from pathlib import Path

base_path = Path(__file__).parent
file_path = base_path / "pi_digits.txt"

with open(file_path, 'r') as f:
    contents = f.read()
    contents = contents.rstrip()
    lines = contents.splitlines()
    pi_string = ''
    for line in lines:
        pi_string += line.lstrip()


print(f"{pi_string[:52]}...")
print(len(pi_string))