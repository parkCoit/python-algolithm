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
유관순 90 90 92 272 90.6 A
이순신 90 90 92 272 90.6 A
********************************
"""
class Grades(object):
    def __init__(self, name , ko , en , ma):
        self.name = name
        self.ko = ko
        self.en = en
        self.ma = ma
        self.total = ko + en + ma
        self.va = self.total / 3

    def get_grade(self):
        va = self.va
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
        return grade

    def print_grade(self):
        print(f" {self.name} {self.ko} {self.en} {self.ko} {self.total} {self.va} {self.get_grade()} ")

    @staticmethod
    def new_grade():
        name = input("이름 :")
        ko = int(input("국어 :"))
        en = int(input("영어 :"))
        ma = int(input(" 수학 : "))
        return Grades(name, ko, en, ma) # Grades() < 생성자에 값을 직접 입력할 수 있음

    @staticmethod
    def print_menu():
        print(" 1. 성적 등록 ")
        print(" 2. 성적 결과 ")
        print(" 3. 성적 삭제 ")
        print( " 4. 종료 " )
        menu = input(" 선택 : ")
        return int(menu)

    @staticmethod
    def get_grades(ls):
        for i in ls :
            i.print_grade()
    
    @staticmethod
    def main():
        ls = []
        while True :
            menu = Grades.print_menu()
            if menu == 1 :
                print(" ### 성적등록 ### ")
                ls.append(Grades.new_grade())
            elif menu == 2 :
                print("### 성적표 ###" )
                print("*"*30)
                print("이름 국어 영어 수학 총점 평균 학점")
                Grades.get_grades(ls)
                print("*"*30)
            elif menu == 3 :
                print(" ### 성적 삭제 ### ")
            elif menu == 4 :
                print(" ### 종료 ### ")
                break



Grades.main()