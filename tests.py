from parser_ import parser

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

    func void test_func(x : int, y : float) [
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


def test_parser():
    # parser.parse(test_01)
    # parser.parse(test_02)
    parser.parse(test_03)


if __name__ == "__main__":
    test_parser()