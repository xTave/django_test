class Student:
    def __init__(self, name, group, number, scores):
        self.name = name
        self.group = group
        self.id = number
        self.scores = scores

    def __str__(self):
        return "{}({}, id = {})".format(self.name, self.group, self.id)


class StudentsRepository:
    def __init__(self):
        self.students = []
        self.changes = []

    def add_new_student(self, student_info):
        self.students.append(Student(*student_info))

    def get_student_by_id(self, student_id):
        for i in self.students:
            if i.id == student_id:
                return i
        raise Exception

    def try_to_change_student(self, student_id, new_scores):
        student = self.get_student_by_id(student_id)
        if sum(student.scores) != sum(new_scores):
            student.scores = new_scores
            self.changes.append(student)

    def get_report(self):
        if len(self.changes):
            for i in self.changes:
                print("{} изменился".format(i))
        else:
            print("Никто не изменился :(")