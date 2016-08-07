class CodeLine:
    def __init__(self, text: str):
        self.text = text
        self.words = self.text.split(" ")

    def is_class_line(self):
        return self.words[0] == "class"

    def is_func_line(self):
        return self.words[0] == 'def'

    def is_return_line(self):
        return "return" in self.text

    def is_from_line(self):
        return len(self.words) > 3 and self.words[0] == "from" and self.words[2] == "import"


def read_code(code : str):
    def replace(s):
        for (old, new) in r:
            s = s.replace(old, new)
        return s
    a = []
    r = []
    splited_code = code.split("\n")
    cur = None
    for i in range(len(splited_code)):
        if splited_code[i] != "":
            line = CodeLine(replace(splited_code[i]))
            if line.is_from_line():
                r.append((line.words[3], line.words[1] + "." + line.words[3]))
            if line.is_class_line():
                cur = Class(line.words[1][:-1])
                a.append(cur)
            elif line.is_func_line():
                cur = Func(line.text)
                a.append(cur)
            elif cur is not None:
                if isinstance(cur, Class) and CodeLine(line.text[4:]).is_func_line():
                    cur.funcs.append(Func(line.text[4:], True))
                if isinstance(cur, Func) and CodeLine(line.text[4:]).is_return_line() and cur.return_type == "None":
                    cur.return_type = "object"
    for i in a:
        print(i)
        print()


class Func:
    def __init__(self, name: str, in_class=False):
        self.name = name[4:-1]
        if "->" in self.name:
            a = self.name.find("->")
            self.return_type = self.name[a + 2:].replace(" ", "")
            self.name = self.name[:a].replace(" ", "")
        else:
            self.return_type = "None"
        args = self.name[self.name.find("(") + 1:self.name.find(")")]
        self.args = []
        self.name = self.name[:self.name.find("(")]
        args = args.replace(" ", "").split(",")
        for i in range(len(args)):
            if i == 0 and in_class:
                continue
            elif ":" in args[i]:
                self.args.append(args[i].split(":"))
            else:
                if "**" in args[i]:
                    self.args.append((args[i], "dict"))
                elif "*" in args[i]:
                    self.args.append((args[i], "list"))
                else:
                    self.args.append((args[i], "object"))

    def __str__(self):
        s = "def {}(".format(self.name)
        for i in self.args:
            s += i[0].replace(" ", "") + " : " + i[1] + ", "
        if self.args:
            s = s[:-2]
        if self.return_type is None:
            s += ") -> None"
        else:
            s += ") -> {}".format(self.return_type)
        return s


class Class:
    def __init__(self, name: str):
        if "(" in name:
            self.father_class = name[name.find("(") + 1:-1]
            self.name = name[:name.find("(")]
        else:
            self.father_class = "object"
            self.name = name
        self.funcs = []

    def __str__(self):
        s = "Class {}({}):".format(self.name, self.father_class)
        if not len(self.funcs):
            s += " Empty Class"
        for i in self.funcs:
            s += "\n\t" + str(i)
        return s


def read_file(filename):
    with open(filename, mode="r") as o:
        return o.read()

read_code(read_file("qwe.py"))