"""
국어. 영어, 수학점수를 입력받아서 학점을 출력하는 프로그램을 완성하시오.
각 과목 점수는 0 ~ 100 사이이다.
평균에 따라 다음과 같이 학점이 결정된다
90이상은 A학점
80이상은 B학점
70이상은 C학점
60이상은 D학점
50이상은 E학점
그 이하는 F학점
출력되는 결과는 다음과 같다.
### 성적표 ###
********************************
이름 국어 영어 수학 총점 평균 학점
*******************************
홍길동 90 90 92 272 90.6 A
********************************
"""
class Grade(object):
    def __init__(self, name , ko , en , ma):
        self.name = name
        self.ko = ko
        self.en = en
        self.ma = ma

    def execute(self):
        self.answer = self.get_answer()
        self.get_answer()
        self.va = self.get_va()
        self.get_va()
        self.get_grade()
        self.print_grade()

    def get_answer(self):
        ko = self.ko
        en = self.en
        ma = self.ma
        return ko + en + ma

    def get_va(self):
        self.answer = self.get_answer()
        return self.answer/3


    def get_grade(self):
        va = self.get_va()
        grade = ""
        if va >= 90:
            grade = "A 학점"
        elif va >= 80:
            grade = "B 학점"
        elif va >= 70:
            grade = "C 학점"
        elif va >= 60:
            grade = "D 학점"
        elif va >= 50:
            grade = "E 학점"
        else: grade = "F 학점"
        self.grade = grade

    def print_grade(self):
        grade = self.grade
        name = self.name
        ko = self.ko
        en = self.en
        ma = self.ma
        answer = self.answer
        va = self.va
        title = "### 성적표 ###"
        arster = "*"*30
        ash = "이름 국어 영어 수학 총점 평균 학점"
        she = f" {name} {ko} {en} {ma} {answer} {va}  "
        print(f" {title} \n {arster} \n {ash} \n {she} {grade} \n {arster}  ")

    def main():
        name = input("이름 :")
        ko = int(input("국어 :"))
        en = int(input("영어 :"))
        ma = int(input(" 수학 : "))
        man = Grade(name, ko , en , ma)
        man.execute()
Grade.main()