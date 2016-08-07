import random


class Neuron:
    def __init__(self, index):
        self.index = index
        self.value = 0
        self.incidents = list()
        self.weight = dict()

    def connect(self, neutron):
        self.incidents.append(neutron)
        neutron.weight[self.index] = float(str(random.random())[:4])

    def set_value(self, value):
        self.value = value

    def make_signal(self):
        for neutron in self.incidents:
            neutron.react_on_signal(self)

    def react_on_signal(self, neutron):
        self.value += self.weight[neutron.index] * neutron.value

    def __str__(self):
        return "Neutron ({}, {})".format(self.weight, self.value)


class NeuronNetwork:
    def __init__(self, input_neutron_count, hided_neutron_count, output_neutron_count):
        self.input_neutrons = [Neuron(i) for i in range(input_neutron_count)]
        self.hided_neutrons = [Neuron(i) for i in range(hided_neutron_count)]
        self.output_neutrons = [Neuron(i) for i in range(output_neutron_count)]
        for i in self.input_neutrons:
            for j in self.hided_neutrons:
                i.connect(j)
        for i in self.hided_neutrons:
            for j in self.output_neutrons:
                i.connect(j)

    def get_answer(self, array):
        if len(array) != len(self.input_neutrons):
            raise Exception
        for i in range(len(array)):
            self.input_neutrons[i].set_value(array[i])
            self.input_neutrons[i].make_signal()
        for i in self.hided_neutrons:
            i.make_signal()
        max_i = -1
        ans = -1
        for i in range(len(self.output_neutrons)):
            if ans < self.output_neutrons[i].value:
                max_i = i
                ans = self.output_neutrons[i].value
        print(max_i)

    def __str__(self):
        s = "INPUT\n"
        for i in self.input_neutrons:
            s += str(i) + ", "
        s = s[:-2] + "\nHIDED\n"
        for i in self.hided_neutrons:
            s += str(i) + ", "
        s = s[:-2] + "\nOUTPUT\n"
        for i in self.output_neutrons:
            s += str(i) + ", "
        return s[:-2]


n = NeuronNetwork(3, 3, 2)
n.get_answer([0, 1, 0])
print(n)
