from requests import get
from students_repository import StudentsRepository
import time
import re
repository = StudentsRepository()


def get_content(first_time):
    response = get("http://anytask.urgu.org/course/47")
    content = response.content.decode()
    a = re.findall(r"<td>(.*?)</td>", content)
    b = re.findall(r'<td align="center" class="student_(.*?)">', content)
    for i in range(0, len(a), 3):
        number = int(b[(i // 3) * 11])
        scores = re.findall(r'<td align="center" class="student_{}">.*?<span class="label.*?">(.*?)</span>.*?</td>'.format(number), content, re.DOTALL)
        for j in range(len(scores)):
            scores[j] = int(scores[j])
        if first_time:
            student_info = [a[i].replace("&nbsp;", " "), a[i + 1], number, scores]
            repository.add_new_student(student_info)
        else:
            repository.try_to_change_student(number, scores)
    if not first_time:
        repository.get_report()

get_content(True)
print("Программа заработала")
while True:
    time.sleep(60)
    get_content(False)