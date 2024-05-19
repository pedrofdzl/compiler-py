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

test_04 = """
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
"""

test_05 = """
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
        a = b + c * (d - e / f) * h;
        b = e - f;
        do {
            h = j * k + b;
            if (b < h) {
                b = h + j;
                do {
                    print (a + b * c, d - e);
                    b = b - j;
                } while (b > a + c);
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
"""

def test_lexer():
    lexer.input(test_03)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)


def test_parser():
    parser.parse(test_05)


if __name__ == "__main__":
    # test_lexer()
    test_parser()