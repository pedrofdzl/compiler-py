import sys
from x_parser import parse

if __name__ == "__main__":
    filename = str(sys.argv[1])

    with open(f'tests/{filename}', 'r') as file:
        code = file.read()
        output = parse(code)
        
        with open(f'out/{filename.split(".")[0]}.dk', 'w') as file:
            for _, table in output[0].items():
                for t, c in table.items():
                    if type(c) == dict:
                        file.write('𓅭\n')
                        file.write(f'{t}\n')
                        for t2, c2 in c.items():
                            file.write(f'{t2}𓃱{c2}\n')
                    else:
                        file.write(f'{t}𓃱{c}\n')
            file.write('𓃻\n')
            for value, address in output[1].items():
                file.write(f'{address}𓃱{value}\n')
            file.write('𓃻\n')
            file.write(output[2])