#Сәпи Аяжан
#лаборатория5
#Бағдарламалау секцияларына қатысатын әртүрлі топтағы студенттерді таныстыруды сұрайтын бағдарламаны жазыңыз. Тізімді сыныптардың өсу реті бойынша сұрыптау қажет. Фамилиялар мен сыныптардың тізімін басып шығарыңыз. 
#Описание класса Student
class Student:
    def __init__(stud):
        stud.fio = ""
        stud.cls = ""
    def __init__(stud, fio):
        stud.fio = fio
        stud.cls = ""
    def __init__(stud, fio, cls):
        stud.fio = fio
        stud.cls = cls
    def __str__(stud):
        return "ФИО: "+ stud.fio +" Класс: "+ stud.cls
#Пустой список учащихся, который будет наполняться
studentList = []
#Форма для пользователя с инструкциями запросов
while True:
    print("+ - Добавить учащегося\nl - Вывести список учащихся\ns - Вывести отсортированный список учащихся\nq - Выход")
    cmd = input()
#Обработка команд
    if cmd == "+":
        print("ФИО:")
        fio = input()
        print("Класс")
        cls = input()
        st = Student(fio, cls)
        studentList.append(st)
#Вывод списка без сортировки
    elif cmd == "l":
        print("------Список учащихся------")
        for student in studentList:
            print(student)
            print("------")

#Вывод сортированного списка
    elif cmd == "s":
        sortedList = studentList
        sortedList.sort(key = lambda x: x.cls)
        print("------Список учащихся------")
        for student in sortedList:
            print(student)
            print("------")
    elif cmd == "q":
        break