
#problem 1 part a
def line_number(from_py, to_txt):
    in_py = open(from_py)
    lines = in_py.read()
    out_txt = open(to_txt, 'w')
    out_txt.write(lines)

    in_py.close()
    out_txt.close()
    print("Done")

#problem 1 part b
def parse_functions(filename):
    """The function reads and parses the Python file.
    Returns a tuple with each being
    element 0 ~ a function name,
    element 1 ~ line number,
    element 2 ~ the code (signature and body) """
    code = ""
    tupples = []
    f = open(filename)
    count = 1
    done = False
    start = False

    for line in f:
        done = False
        # First, remove comments:
        if ('#') in line:
            # split pound comment, keep left as line
            line, comment = line.split('#', 1)

        if ('"""') in line:
            # split quotation comment, keep left as line
            line, comment = line.split('"""', 1)

        if "def" in line:
            start = True
            code += line
            line, name = line.rsplit("def")
            # strip spaces:
            name = name.strip()
            linecount = count
        # Second, find lines with an option=value:

        #if start and line != ['']:
        #    code += line

        if ("return") in line:
            line = line.split("\n")
            code += " " + line[0]
            done = True
            tupple = (name, linecount, code)
            code = ''
            start = False

        if done:
            try:
                tupples.append(tupple)
            except:
                pass

        count += 1
    f.close()
    return tupples


tupples = parse_functions('funs.py')
print(tupples)

line_number('test.py', 'test.py.txt')
