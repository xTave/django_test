class Node:
    def __init__(self, length_to_terminal, index):
        self.length_to_terminal = length_to_terminal
        self.index = index
        self.incident = dict()
        self.prev_letter = ""

    def connect(self, other_node, letter):
        self.incident[letter] = other_node
        other_node.prev = self
        other_node.prev_letter = letter

    def __str__(self):
        def qwe(x):
            x = str(x)
            return "0" * (3 - len(x)) + x

        if self.index == "x":
            return "A(xxх,хxx)"
        return "A({},{})".format(qwe(self.length_to_terminal), qwe(self.index))


class Automaton:
    def __init__(self, n, alphabet):
        self.n = n
        self.alphabet = alphabet
        self.states = []

    def create(self):
        self.states.append([Node(self.n, 0)])
        for i in range(self.n // 2):
            a = []
            for j in range(len(self.states[-1])):
                node = self[-1, j]
                for q in range(len(self.alphabet)):
                    other_node = Node(node.length_to_terminal - 1, len(self.alphabet) * node.index + q)
                    a.append(other_node)
                    node.connect(other_node, self.alphabet[q])
            self.states.append(a)
        for i in range(self.n // 2):
            a = []
            for j in range(len(self.states[-1]) // len(self.alphabet)):
                node = Node(self.n // 2 - i - 1, j)
                for q in range(len(self.alphabet)):
                    other_node = self[-1, len(self.alphabet) * j + q]
                    prev_node = self[other_node.length_to_terminal, len(self.alphabet) * j + q]
                    other_node.connect(node, prev_node.prev_letter)
                a.append(node)
            self.states.append(a)

    def __getitem__(self, item):
        return self.states[item[0]][item[1]]

    def __str__(self):
        s = ""
        a = []
        for i in range(self.n + 1):
            b = self.states[i]
            q = []
            for j in b:
                q.append(j)
                for l in self.alphabet:
                    try:
                        q.append(j.incident[l])
                    except:
                        q.append(Node("x", "x"))
            a.append(q)
        for j in range(len(self.alphabet) + 1):
            if j != 0:
                s += self.alphabet[j - 1] + " "
            else:
                s += "/ "
            for i in a:
                for cur in i[j::len(self.alphabet) + 1]:
                    s += str(cur) + " "
                s += "| "
            s += "\n"
            if j == 0:
                for i in self.states:
                    s += "-" * (2 + len(i) * 11)
                s += "-\n"
        return s

a = Automaton(8, "abcde")
a.create()
print(a)
