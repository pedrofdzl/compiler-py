import sys
from x_parser import parse

if __name__ == "__main__":
    filename = str(sys.argv[1])

    with open(f'tests/{filename}', 'r') as file:
        code = file.read()
        output = parse(code)
        
        with open(f'out/{filename.split(".")[0]}.dk', 'w') as file:
            for value, address in output[0].items():
                file.write(f'{address}𓃱{value}\n')
            file.write('𓃻\n')
            file.write(output[1])