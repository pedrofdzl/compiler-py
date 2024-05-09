from parser_ import parser

# Test the parser
data = """
    program test;

    var x : int;

    main {
        x = 2; print(x);
    }
    end
"""

parser.parse(data)