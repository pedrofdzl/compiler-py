import sys

memory = [None for i in range(1000000)]

if __name__ == "__main__":
    filename = str(sys.argv[1])

    with open(f'out/{filename}', 'r') as file:
        quadruples = file.read()