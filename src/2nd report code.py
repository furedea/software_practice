class Student:
    __slots__ = ["name", "scores"]

    def __init__(self, name: str, scores: list[int]) -> None:
        self.name = name
        self.scores = scores

    @property
    def total(self) -> int:
        return sum(self.scores)

    @property
    def average(self) -> float:
        return self.total / len(self.scores)


def find_best_student_report(students: list[Student]) -> Student:
    return max(students, key=lambda x: x.total)


if __name__ == "__main__":
    students = [
        Student("Alice", [85, 90, 78]),
        Student("Bob", [92, 88, 84]),
        Student("Charlie", [70, 75, 80]),
        Student("David", [95, 85, 90]),
    ]
    for student in students:
        print(f"Student: {student.name}, Total: {student.total}, Average: {student.average}")
    top_student = find_best_student_report(students)
    print(f"Best student: {top_student.name} with total score: {top_student.total}")
