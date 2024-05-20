import argparse
from x_parser import parser
from x_lexer import lexer

# Test cases

test_cases = ["""
    program test;

    var x : int;

    main {
        x = 2; print(x);
    }
    end
""","""
    program test;

    var x : int;
        y : float;
    
    main {
        x = 2; y = 3.5; print(x); print(y);
    }
    end
""","""
    program test;

    var x : int;
        y : float;

    void test_func(x : int, y : float) [
        var z : int;
        {
            z = x + 2;
            print(z);
        }
    ];

    main {
        x = 2; y = 3.5; print(x); print(y);
        test_func(x, y);
    }
    end
""","""
    program test;

    var x : int;
        y : float;
        z : int;

    main {
        x = 2;
        z = 3;

        y = (-x + z) * -2.5;
    }
    end
""","""
    program test;

    var a : float;
        b : float;
        c : float;
        d : float;
        e : float;
        f : float;
        g : float;
        h : float;
        j : float;
        k : float;

    main {
        print ('Hello, World!');
        a = b + c * (d - e / f) * h;
        b = e - f;
        do {
            h = j * k + b;
            if (b < h) {
                b = h + j;
                do {
                    print (a + b * c, d - e);
                    b = b - j;
                } while (b >= a + c);
            } else {
                do {
                    a = a + b;
                    print (b - d);
                } while (a - d < c + b);
            };
        } while (a * b - c > d * e / (g + h));
        f = a + b;
    }
    end
"""]

def test_lexer(n):
    lexer.input(test_cases[n])
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)


def test_parser(n):
    parser.parse(test_cases[n])


if __name__ == "__main__":
    argparser = argparse.ArgumentParser(description="Run specific test case.")
    argparser.add_argument("test_number", type=int, help="The test case number to run (1-5).")
    argparser.add_argument("--lexer", action="store_true", help="Run lexer test.")
    argparser.add_argument("--parser", action="store_true", help="Run parser test.")
    args = argparser.parse_args()

    if args.lexer:
        test_lexer(args.test_number - 1)

    if args.parser:
        test_parser(args.test_number - 1)