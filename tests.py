from x_parser import parser
from x_lexer import lexer

# Test cases

test_01 = """
    program test;

    var x : int;

    main {
        x = 2; print(x);
    }
    end
"""

test_02 = """
    program test;

    var x : int;
        y : float;
    
    main {
        x = 2; y = 3.5; print(x); print(y);
    }
    end
"""

test_03 = """
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
"""


def test_lexer():
    lexer.input(test_03)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)


def test_parser():
    parser.parse(test_03)


if __name__ == "__main__":
    # test_lexer()
    test_parser()