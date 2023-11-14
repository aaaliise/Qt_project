import sys
import sqlite3

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit, QSpinBox
from PyQt5.QtWidgets import QInputDialog, QColorDialog
from PyQt5.QtGui import QPixmap
from random import choice, randint
from PyQt5.QtWidgets import QMainWindow, QSpinBox

NAME_BD = 'project1.sqlite'
NUMBER_QUES = 1
HELP = 0
MARK = 0
TEXT_VALUE = 0


class Inte(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.li_but = []

    def initUI(self):
        self.setGeometry(100, 100, 800, 500)
        self.setWindowTitle('Образовательная викторина')

        self.pixmap = QPixmap('im.png')
        self.image = QLabel(self)
        self.image.resize(800, 500)
        self.image.move(0, 0)
        self.image.setPixmap(self.pixmap)

        self.text_pres = QLabel(self)
        self.text_pres.move(20, 35)
        self.text_pres.setText('Добро пожаловать на викторину! Здесь вы можете выбрать: '
                               'викторина и далее за вами остаётя выбор предмета или подбадривающие цитаты')

        self.but_quiz = QPushButton('Викторина', self)
        self.but_quiz.resize(150, 25)
        self.but_quiz.move(105, 150)
        self.but_quiz.clicked.connect(self.open_second_form)

        self.but_quote = QPushButton('Игра', self)
        self.but_quote.resize(150, 25)
        self.but_quote.move(505, 150)
        self.but_quote.clicked.connect(self.open_third_form)

        self.but_remark = QPushButton('Ошибки', self)
        self.but_remark.resize(150, 25)
        self.but_remark.move(120, 200)
        self.but_remark.clicked.connect(self.open_remark_form)

        self.col_button = QPushButton(self)
        self.col_button.move(180, 300)
        self.col_button.setText("Изменить цвет кнопок")
        self.col_button.clicked.connect(self.run)

        self.ruls_button = QPushButton(self)
        self.ruls_button.move(500, 300)
        self.ruls_button.setText("Правила")
        self.ruls_button.clicked.connect(self.rules)

        self.marks_button = QPushButton(self)
        self.marks_button.move(325, 450)
        self.marks_button.setText("Количество очков")
        self.marks_button.clicked.connect(self.marks)

        self.opi_button = QPushButton(self)
        self.opi_button.move(55, 420)
        self.opi_button.setText("Мнение")
        self.opi_button.clicked.connect(self.opi)

    def opi(self):
        self.opi_form = OpiForm()
        self.opi_form.show()
        self.hide()

    def marks(self):
        global MARK
        global HELP
        self.marks_button.setText(str(max(0, (MARK - (HELP * 0.5)))))
        MARK = min(0, (MARK - (HELP * 0.5)))
        HELP = 0

    def rules(self):
        self.rules_form = RulesForm()
        self.rules_form.show()
        self.hide()

    def run(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.but_remark.setStyleSheet(
                "background-color: {}".format(color.name()))
            self.but_quote.setStyleSheet(
                "background-color: {}".format(color.name()))
            self.but_quiz.setStyleSheet(
                "background-color: {}".format(color.name()))
            self.ruls_button.setStyleSheet(
                "background-color: {}".format(color.name()))
            self.marks_button.setStyleSheet(
                "background-color: {}".format(color.name()))
            self.opi_button.setStyleSheet(
                "background-color: {}".format(color.name()))

    def open_second_form(self):
        self.second_form = SecondForm()
        self.second_form.show()
        self.hide()

    def open_third_form(self):
        self.play_form = PlayForm()
        self.play_form.show()
        self.hide()

    def open_remark_form(self):
        self.remark_form = RemarkForm()
        self.remark_form.show()
        self.hide()


class SecondForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        global NUMBER_QUES
        NUMBER_QUES = 1
        self.setGeometry(300, 300, 800, 300)
        self.setWindowTitle('Предметы')

        self.lbl1 = QLabel(self)
        self.lbl1.setText('Выберете предмет и начните прохождение викторины')
        self.lbl1.resize(500, 15)
        self.lbl1.move(160, 50)

        self.but_rus = QPushButton('Русский язык', self)
        self.but_rus.resize(100, 25)
        self.but_rus.move(5, 150)
        self.but_rus.clicked.connect(self.cl_rus)

        self.but_mat = QPushButton('Математика', self)
        self.but_mat.resize(100, 25)
        self.but_mat.move(125, 150)
        self.but_mat.clicked.connect(self.cl_mat)

        self.but_bio = QPushButton('Биология', self)
        self.but_bio.resize(100, 25)
        self.but_bio.move(250, 150)
        self.but_bio.clicked.connect(self.cl_bio)

        self.but_ph = QPushButton('Физика', self)
        self.but_ph.resize(100, 25)
        self.but_ph.move(375, 150)
        self.but_ph.clicked.connect(self.cl_ph)

        self.but_his = QPushButton('История', self)
        self.but_his.resize(100, 25)
        self.but_his.move(500, 150)
        self.but_his.clicked.connect(self.cl_his)

        self.but_en = QPushButton('Английский язык', self)
        self.but_en.resize(100, 25)
        self.but_en.move(625, 190)
        self.but_en.clicked.connect(self.cl_en)

        self.but_pe = QPushButton('Физическая культура', self)
        self.but_pe.resize(200, 25)
        self.but_pe.move(5, 190)
        self.but_pe.clicked.connect(self.cl_pe)

        self.but_geo = QPushButton('География', self)
        self.but_geo.resize(100, 25)
        self.but_geo.move(225, 190)
        self.but_geo.clicked.connect(self.cl_geo)

        self.but_lit = QPushButton('Литература', self)
        self.but_lit.resize(100, 25)
        self.but_lit.move(350, 190)
        self.but_lit.clicked.connect(self.cl_lit)

        self.but_ch = QPushButton('Химия', self)
        self.but_ch.resize(100, 25)
        self.but_ch.move(475, 190)
        self.but_ch.clicked.connect(self.cl_ch)

        self.but_back = QPushButton('Вернуться на главную страницу', self)
        self.but_back.resize(200, 25)
        self.but_back.move(500, 90)
        self.but_back.clicked.connect(self.back)

        self.marks_button = QPushButton(self)
        self.marks_button.move(650, 20)
        self.marks_button.setText("Количество очков")
        self.marks_button.clicked.connect(self.marks)

    def marks(self):
        global MARK
        global HELP
        self.marks_button.setText(str(max(0, MARK - (HELP * 0.5))))
        MARK = min(0, (MARK - (HELP * 0.5)))
        HELP = 0

    def back(self):
        self.inte_form = Inte()
        self.inte_form.show()
        self.hide()

    def cl_rus(self):
        self.rus_form = RusForm()
        self.rus_form.show()
        self.hide()

    def cl_mat(self):
        self.mat_form = MatForm()
        self.mat_form.show()
        self.hide()

    def cl_bio(self):
        self.bio_form = BioForm()
        self.bio_form.show()
        self.hide()

    def cl_en(self):
        self.en_form = EnForm()
        self.en_form.show()
        self.hide()

    def cl_ph(self):
        self.ph_form = PhForm()
        self.ph_form.show()
        self.hide()

    def cl_geo(self):
        self.geo_form = GeoForm()
        self.geo_form.show()
        self.hide()

    def cl_his(self):
        self.his_form = HisForm()
        self.his_form.show()
        self.hide()

    def cl_lit(self):
        self.lit_form = LitForm()
        self.lit_form.show()
        self.hide()

    def cl_pe(self):
        self.pe_form = PeForm()
        self.pe_form.show()
        self.hide()

    def cl_ch(self):
        self.ch_form = ChForm()
        self.ch_form.show()
        self.hide()

    def cl_go(self):
        pass


class PlayForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Игра')

        self.text_lab = QLabel(self)
        self.text_lab.move(5, 40)
        self.text_lab.setText('Отдохните тыкая на кнопочки😊😁😃😋)')

        self.but_rus_back = QPushButton('Начать', self)
        self.but_rus_back.resize(200, 25)
        self.but_rus_back.move(5, 100)
        self.but_rus_back.clicked.connect(self.front)

        self.but_rus_back = QPushButton('Вернуться на главную страницу', self)
        self.but_rus_back.resize(200, 25)
        self.but_rus_back.move(100, 160)
        self.but_rus_back.clicked.connect(self.back)

    def back(self):
        self.inte_form = Inte()
        self.inte_form.show()
        self.hide()

    def front(self):
        self.play_form = Play_Form()
        self.play_form.show()


class Play_Form(QMainWindow):
    def __init__(self):
        global TEXT_VALUE
        super().__init__()
        self.setWindowTitle('Игра')
        text = QSpinBox()
        first_number = randint(1, 1000)
        second_number = randint(1, 1000)
        while first_number == second_number:
            second_number = randint(1, 1000)
        if first_number > second_number:
            first_number, second_number = second_number, first_number
        text.setMinimum(first_number)
        text.setMaximum(second_number)
        text.setSingleStep(1)
        self.setCentralWidget(text)


class RulesForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 570, 200)
        self.setWindowTitle('Правила')

        self.rul_pres = QLabel(self)
        self.rul_pres.resize(self.rul_pres.sizeHint())
        self.rul_pres.move(5, 50)

        self.but_rus_back = QPushButton('Вернуться на главную страницу', self)
        self.but_rus_back.resize(200, 25)
        self.but_rus_back.move(100, 160)
        self.but_rus_back.clicked.connect(self.back)

        d = open('rul_proj.txt', mode='r', encoding='utf-8')
        number = 5
        for i in list(d):
            self.rul_pres = QLabel(self)
            self.rul_pres.setText(f'{i.strip()}\n')
            self.rul_pres.resize(self.rul_pres.sizeHint())
            self.rul_pres.move(5, number)
            number += 12

    def back(self):
        self.inte_form = Inte()
        self.inte_form.show()
        self.hide()


class RemarkForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Форма для ошибок')

        self.but_rem = QPushButton('Ошибки', self)
        self.but_rem.resize(150, 25)
        self.but_rem.move(105, 150)
        self.but_rem.clicked.connect(self.cl_rem)

        self.but_rus_back = QPushButton('Вернуться на главную страницу', self)
        self.but_rus_back.resize(200, 25)
        self.but_rus_back.move(80, 80)
        self.but_rus_back.clicked.connect(self.back)

    def cl_rem(self):
        d = {'Русский язык': 'Rusuan', 'Математика': 'Maths', 'Биология': 'Biology',
             'Физика': 'physics', 'История': 'history', 'Английский язык': 'English', 'Физическая культура': 'PE',
             'География': 'Geography', 'Литература': 'Literature', 'Химия': 'Сhemistry'}
        d_id = {'Русский язык': 'id_rus', 'Математика': 'id_mat', 'Биология': 'id_bio',
                'Физика': 'id_ph', 'История': 'id_his', 'Английский язык': 'id_en', 'Физическая культура': 'id_pe',
                'География': 'id_geo', 'Литература': 'id_lit', 'Химия': 'id_ch'}
        dd = {'вопрос': 'que', 'ответ': 'ans'}
        answer, ok_pressed = QInputDialog.getText(self, f'Исправление ошибки',
                                                  'Пожалуйста, введите название предмета в точности со '
                                                  'всеми знаками и необходимыми пробылами,\n'
                                                  'затем введите цифру - номер вопроса или ответа, '
                                                  'в котором содержится ошибка,\n'
                                                  'введите одно из двух: вопрос или ответ,\nи последним, '
                                                  'то каким он должен быть\n'
                                                  'Введите через запятую без пробелов между отдельными частями '
                                                  'данного запроса')

        if ok_pressed:
            print(answer)
            con = sqlite3.connect(NAME_BD)
            cur = con.cursor()

            info = f"UPDATE {d[str((str(answer).split(','))[0])]} " \
                   f"SET {dd[str((str(answer).split(','))[-2])]} " \
                   f"= '{str((str(answer).split(','))[-1])}' " \
                   f"WHERE {d_id[str((str(answer).split(','))[0])]} = {int((str(answer).split(','))[1])}"
            cur.execute(info)
            con.commit()
            con.close()

    def back(self):
        self.inte_form = Inte()
        self.inte_form.show()
        self.hide()


class OpiForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.count_cl_opi = 1

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Оставте ваше мнение об этом приложении для разработчика)')

        self.opi = QLineEdit(self)
        self.opi.resize(self.opi.sizeHint())
        self.opi.move(5, 5)

        self.opi_but = QPushButton(self)
        self.opi_but.move(10, 50)
        self.opi_but.setText("Сохранить")
        self.opi_but.setStyleSheet(
            "background-color: {}".format('red'))
        self.opi_but.clicked.connect(self.opion)

        self.but_back = QPushButton('Вернуться на главную страницу', self)
        self.but_back.resize(200, 25)
        self.but_back.move(10, 100)
        self.but_back.clicked.connect(self.back)

    def opion(self):
        self.opi_but.setStyleSheet(
            "background-color: {}".format('green'))

    def back(self):
        self.inte_form = Inte()
        self.inte_form.show()
        self.hide()


class RusForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('Русский язык')

        self.rus_answer = QLabel(self)
        self.rus_answer.resize(self.rus_answer.sizeHint())
        self.rus_answer.move(5, 50)
        self.rus_answer.setText('')

        self.but_rus_1 = QPushButton('Вопрос', self)
        self.but_rus_1.resize(100, 25)
        self.but_rus_1.move(100, 150)
        self.but_rus_1.clicked.connect(self.run)

        self.but_rus_back = QPushButton('Вернуться к предметам', self)
        self.but_rus_back.resize(150, 25)
        self.but_rus_back.move(100, 80)
        self.but_rus_back.clicked.connect(self.back)

    def run(self):
        global NUMBER_QUES
        global MARK
        if NUMBER_QUES > 20:
            self.rus_answer.setText('Вопросы данной категории закончились')
            self.rus_answer.resize(self.rus_answer.sizeHint())
        else:
            con = sqlite3.connect(NAME_BD)
            cur = con.cursor()
            result = cur.execute("""SELECT que, ans FROM Rusuan
                                WHERE id_rus = ?""", (NUMBER_QUES,)).fetchall()
            quetion, answer = result[0]
            con.close()
            answer1, ok_pressed = QInputDialog.getText(self, f'Вопрос №{NUMBER_QUES}', str(quetion))
            if ok_pressed:
                if str(answer) in str(answer1):
                    MARK += 1
                    self.rus_answer.setText('Правильный ответ +1 балл')
                    self.rus_answer.resize(self.rus_answer.sizeHint())
                else:
                    self.rus_answer.setText(f'Неправильный ответ +0 баллов, Правильный ответ {str(answer)}')
                    self.rus_answer.resize(self.rus_answer.sizeHint())
            NUMBER_QUES += 1

    def back(self):
        self.second_form = SecondForm()
        self.second_form.show()
        self.hide()


class MatForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 800, 300)
        self.setWindowTitle('Математика')

        self.mat_answer = QLabel(self)
        self.mat_answer.resize(self.mat_answer.sizeHint())
        self.mat_answer.move(5, 50)
        self.mat_answer.setText('')

        self.but_mat_1 = QPushButton('Вопрос', self)
        self.but_mat_1.resize(100, 25)
        self.but_mat_1.move(100, 150)
        self.but_mat_1.clicked.connect(self.run)

        self.but_mat_back = QPushButton('Вернуться к предметам', self)
        self.but_mat_back.resize(150, 25)
        self.but_mat_back.move(100, 80)
        self.but_mat_back.clicked.connect(self.back)

    def run(self):
        global NUMBER_QUES
        global MARK
        if NUMBER_QUES > 20:
            self.mat_answer.setText('Вопросы данной категории закончились')
            self.mat_answer.resize(self.mat_answer.sizeHint())
        else:
            con = sqlite3.connect(NAME_BD)
            cur = con.cursor()
            result = cur.execute("""SELECT que, ans FROM Maths
                                WHERE id_mat = ?""", (NUMBER_QUES,)).fetchall()
            quetion, answer = result[0]
            con.close()
            answer1, ok_pressed = QInputDialog.getText(self, f'Вопрос №{NUMBER_QUES}', str(quetion))
            if ok_pressed:
                if str(answer) in str(answer1):
                    MARK += 1
                    self.mat_answer.setText('Правильный ответ +1 балл')
                    self.mat_answer.resize(self.mat_answer.sizeHint())
                else:
                    self.mat_answer.setText(f'Неправильный ответ +0 баллов, Правильный ответ {str(answer)}')
                    self.mat_answer.resize(self.mat_answer.sizeHint())
            NUMBER_QUES += 1

    def back(self):
        self.second_form = SecondForm()
        self.second_form.show()
        self.hide()


class BioForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 800, 300)
        self.setWindowTitle('Биология')

        self.bio_answer = QLabel(self)
        self.bio_answer.resize(self.bio_answer.sizeHint())
        self.bio_answer.move(5, 50)
        self.bio_answer.setText('')

        self.but_bio_1 = QPushButton('Вопрос', self)
        self.but_bio_1.resize(100, 25)
        self.but_bio_1.move(100, 150)
        self.but_bio_1.clicked.connect(self.run)

        self.but_bio_back = QPushButton('Вернуться к предметам', self)
        self.but_bio_back.resize(150, 25)
        self.but_bio_back.move(100, 80)
        self.but_bio_back.clicked.connect(self.back)

    def run(self):
        global NUMBER_QUES
        global MARK
        if NUMBER_QUES > 20:
            self.bio_answer.setText('Вопросы данной категории закончились')
            self.bio_answer.resize(self.bio_answer.sizeHint())
        else:
            con = sqlite3.connect(NAME_BD)
            cur = con.cursor()
            result = cur.execute("""SELECT que, ans FROM Biology
                                WHERE id_bio = ?""", (NUMBER_QUES,)).fetchall()
            quetion, answer = result[0]
            con.close()
            answer1, ok_pressed = QInputDialog.getText(self, f'Вопрос №{NUMBER_QUES}', str(quetion))
            if ok_pressed:
                if str(answer) in str(answer1):
                    MARK += 1
                    self.bio_answer.setText('Правильный ответ +1 балл')
                    self.bio_answer.resize(self.bio_answer.sizeHint())
                else:
                    self.bio_answer.setText(f'Неправильный ответ +0 баллов, Правильный ответ {str(answer)}')
                    self.bio_answer.resize(self.bio_answer.sizeHint())
            NUMBER_QUES += 1

    def back(self):
        self.second_form = SecondForm()
        self.second_form.show()
        self.hide()


class EnForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 800, 300)
        self.setWindowTitle('Английский язык')

        self.en_answer = QLabel(self)
        self.en_answer.resize(self.en_answer.sizeHint())
        self.en_answer.move(5, 50)
        self.en_answer.setText('')

        self.but_en_1 = QPushButton('Вопрос', self)
        self.but_en_1.resize(100, 25)
        self.but_en_1.move(100, 150)
        self.but_en_1.clicked.connect(self.run)

        self.but_en_back = QPushButton('Вернуться к предметам', self)
        self.but_en_back.resize(150, 25)
        self.but_en_back.move(100, 80)
        self.but_en_back.clicked.connect(self.back)

    def run(self):
        global NUMBER_QUES
        global MARK
        if NUMBER_QUES > 15:
            self.en_answer.setText('Вопросы данной категории закончились')
            self.en_answer.resize(self.en_answer.sizeHint())
        else:
            con = sqlite3.connect(NAME_BD)
            cur = con.cursor()
            result = cur.execute("""SELECT que, ans FROM English
                                WHERE id_en = ?""", (NUMBER_QUES,)).fetchall()
            quetion, answer = result[0]
            con.close()
            answer1, ok_pressed = QInputDialog.getText(self, f'Вопрос №{NUMBER_QUES}', str(quetion))
            if ok_pressed:
                if str(answer) in str(answer1):
                    MARK += 1
                    self.en_answer.setText('Правильный ответ +1 балл')
                    self.en_answer.resize(self.en_answer.sizeHint())
                else:
                    self.en_answer.setText(f'Неправильный ответ +0 баллов, Правильный ответ {str(answer)}')
                    self.en_answer.resize(self.en_answer.sizeHint())
            NUMBER_QUES += 1

    def back(self):
        self.second_form = SecondForm()
        self.second_form.show()
        self.hide()


class PhForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 800, 300)
        self.setWindowTitle('Физика')

        self.ph_answer = QLabel(self)
        self.ph_answer.resize(self.ph_answer.sizeHint())
        self.ph_answer.move(5, 50)
        self.ph_answer.setText('')

        self.but_ph_1 = QPushButton('Вопрос', self)
        self.but_ph_1.resize(100, 25)
        self.but_ph_1.move(100, 150)
        self.but_ph_1.clicked.connect(self.run)

        self.but_ph_1 = QPushButton('Подсказка', self)
        self.but_ph_1.resize(100, 25)
        self.but_ph_1.move(100, 200)
        self.but_ph_1.clicked.connect(self.run1)

        self.ph_help = QLabel(self)
        self.ph_help.resize(self.ph_answer.sizeHint())
        self.ph_help.move(5, 250)
        self.ph_help.setText('')

        self.but_ph_back = QPushButton('Вернуться к предметам', self)
        self.but_ph_back.resize(150, 25)
        self.but_ph_back.move(100, 80)
        self.but_ph_back.clicked.connect(self.back)

    def run(self):
        global NUMBER_QUES
        global MARK
        if NUMBER_QUES > 15:
            self.ph_answer.setText('Вопросы данной категории закончились')
            self.ph_answer.resize(self.ph_answer.sizeHint())
        else:
            con = sqlite3.connect(NAME_BD)
            cur = con.cursor()
            result = cur.execute("""SELECT que, ans, help FROM physics
                                WHERE id_ph = ?""", (NUMBER_QUES,)).fetchall()
            quetion, answer, help = result[0]
            con.close()
            answer1, ok_pressed = QInputDialog.getText(self, f'Вопрос №{NUMBER_QUES}', str(quetion))
            if ok_pressed:
                if str(answer) in str(answer1):
                    MARK += 1
                    self.ph_answer.setText('Правильный ответ +1 балл')
                    self.ph_answer.resize(self.ph_answer.sizeHint())
                else:
                    self.ph_answer.setText(f'Неправильный ответ +0 баллов, Правильный ответ {str(answer)}')
                    self.ph_answer.resize(self.ph_answer.sizeHint())
            NUMBER_QUES += 1

    def run1(self):
        con = sqlite3.connect(NAME_BD)
        cur = con.cursor()
        result = cur.execute("""SELECT help FROM physics
                                        WHERE id_ph = ?""", (NUMBER_QUES,)).fetchall()
        help = result[0][0]
        con.close()
        global HELP
        self.ph_help.setText(str(help))
        self.ph_help.resize(self.ph_help.sizeHint())
        HELP += 1

    def back(self):
        self.second_form = SecondForm()
        self.second_form.show()
        self.hide()


class GeoForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 800, 300)
        self.setWindowTitle('География')

        self.geo_answer = QLabel(self)
        self.geo_answer.resize(self.geo_answer.sizeHint())
        self.geo_answer.move(5, 50)
        self.geo_answer.setText('')

        self.but_geo_1 = QPushButton('Вопрос', self)
        self.but_geo_1.resize(100, 25)
        self.but_geo_1.move(100, 150)
        self.but_geo_1.clicked.connect(self.run)

        self.but_geo_1 = QPushButton('Подсказка', self)
        self.but_geo_1.resize(100, 25)
        self.but_geo_1.move(100, 200)
        self.but_geo_1.clicked.connect(self.run1)

        self.geo_help = QLabel(self)
        self.geo_help.resize(self.geo_answer.sizeHint())
        self.geo_help.move(5, 250)
        self.geo_help.setText('')

        self.but_geo_back = QPushButton('Вернуться к предметам', self)
        self.but_geo_back.resize(150, 25)
        self.but_geo_back.move(100, 80)
        self.but_geo_back.clicked.connect(self.back)

    def run(self):
        global NUMBER_QUES
        global MARK
        if NUMBER_QUES > 15:
            self.geo_answer.setText('Вопросы данной категории закончились')
            self.geo_answer.resize(self.geo_answer.sizeHint())
        else:
            con = sqlite3.connect(NAME_BD)
            cur = con.cursor()
            result = cur.execute("""SELECT que, ans, help FROM Geography
                                WHERE id_geo = ?""", (NUMBER_QUES,)).fetchall()
            quetion, answer, help = result[0]
            con.close()
            answer1, ok_pressed = QInputDialog.getText(self, f'Вопрос №{NUMBER_QUES}', str(quetion))
            if ok_pressed:
                if str(answer) in str(answer1):
                    MARK += 1
                    self.geo_answer.setText('Правильный ответ +1 балл')
                    self.geo_answer.resize(self.geo_answer.sizeHint())
                else:
                    self.geo_answer.setText(f'Неправильный ответ +0 баллов, Правильный ответ {str(answer)}')
                    self.geo_answer.resize(self.geo_answer.sizeHint())
            NUMBER_QUES += 1

    def run1(self):
        con = sqlite3.connect(NAME_BD)
        cur = con.cursor()
        result = cur.execute("""SELECT help FROM Geography
                                        WHERE id_geo = ?""", (NUMBER_QUES,)).fetchall()
        help = result[0][0]
        con.close()
        global HELP
        self.geo_help.setText(str(help))
        self.geo_help.resize(self.geo_help.sizeHint())
        HELP += 1

    def back(self):
        self.second_form = SecondForm()
        self.second_form.show()
        self.hide()


class HisForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 800, 300)
        self.setWindowTitle('История')

        self.his_answer = QLabel(self)
        self.his_answer.resize(self.his_answer.sizeHint())
        self.his_answer.move(5, 50)
        self.his_answer.setText('')

        self.but_his_1 = QPushButton('Вопрос', self)
        self.but_his_1.resize(100, 25)
        self.but_his_1.move(100, 150)
        self.but_his_1.clicked.connect(self.run)

        self.but_his_1 = QPushButton('Подсказка', self)
        self.but_his_1.resize(100, 25)
        self.but_his_1.move(100, 200)
        self.but_his_1.clicked.connect(self.run1)

        self.his_help = QLabel(self)
        self.his_help.resize(self.his_answer.sizeHint())
        self.his_help.move(5, 250)
        self.his_help.setText('')

        self.but_his_back = QPushButton('Вернуться к предметам', self)
        self.but_his_back.resize(150, 25)
        self.but_his_back.move(100, 80)
        self.but_his_back.clicked.connect(self.back)

    def run(self):
        global NUMBER_QUES
        global MARK
        if NUMBER_QUES > 10:
            self.his_answer.setText('Вопросы данной категории закончились')
            self.his_answer.resize(self.his_answer.sizeHint())
        else:
            con = sqlite3.connect(NAME_BD)
            cur = con.cursor()
            result = cur.execute("""SELECT que, ans FROM history
                                WHERE id_his = ?""", (NUMBER_QUES,)).fetchall()
            quetion, answer = result[0]
            con.close()
            answer1, ok_pressed = QInputDialog.getText(self, f'Вопрос №{NUMBER_QUES}', str(quetion))
            if ok_pressed:
                if str(answer) in str(answer1):
                    MARK += 1
                    self.his_answer.setText('Правильный ответ +1 балл')
                    self.his_answer.resize(self.his_answer.sizeHint())
                else:
                    self.his_answer.setText(f'Неправильный ответ +0 баллов, Правильный ответ {str(answer)}')
                    self.his_answer.resize(self.his_answer.sizeHint())
            NUMBER_QUES += 1

    def run1(self):
        con = sqlite3.connect(NAME_BD)
        cur = con.cursor()
        result = cur.execute("""SELECT help FROM history
                                        WHERE id_his = ?""", (NUMBER_QUES,)).fetchall()
        help = result[0][0]
        con.close()
        global HELP
        self.his_help.setText(str(help))
        self.his_help.resize(self.his_help.sizeHint())
        HELP += 1

    def back(self):
        self.second_form = SecondForm()
        self.second_form.show()
        self.hide()


class LitForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 800, 300)
        self.setWindowTitle('Литература')

        self.lit_answer = QLabel(self)
        self.lit_answer.resize(self.lit_answer.sizeHint())
        self.lit_answer.move(5, 50)
        self.lit_answer.setText('')

        self.but_lit_1 = QPushButton('Вопрос', self)
        self.but_lit_1.resize(100, 25)
        self.but_lit_1.move(100, 150)
        self.but_lit_1.clicked.connect(self.run)

        self.but_lit_1 = QPushButton('Подсказка', self)
        self.but_lit_1.resize(100, 25)
        self.but_lit_1.move(100, 200)
        self.but_lit_1.clicked.connect(self.run1)

        self.lit_help = QLabel(self)
        self.lit_help.resize(self.lit_answer.sizeHint())
        self.lit_help.move(5, 250)
        self.lit_help.setText('')

        self.but_lit_back = QPushButton('Вернуться к предметам', self)
        self.but_lit_back.resize(150, 25)
        self.but_lit_back.move(100, 80)
        self.but_lit_back.clicked.connect(self.back)

    def run(self):
        global NUMBER_QUES
        global MARK
        if NUMBER_QUES > 20:
            self.lit_answer.setText('Вопросы данной категории закончились')
            self.lit_answer.resize(self.lit_answer.sizeHint())
        else:
            con = sqlite3.connect(NAME_BD)
            cur = con.cursor()
            result = cur.execute("""SELECT que, ans FROM Literature
                                WHERE id_lit = ?""", (NUMBER_QUES,)).fetchall()
            quetion, answer = result[0]
            con.close()
            answer1, ok_pressed = QInputDialog.getText(self, f'Вопрос №{NUMBER_QUES}', str(quetion))
            if ok_pressed:
                if str(answer) in str(answer1):
                    MARK += 1
                    self.lit_answer.setText('Правильный ответ +1 балл')
                    self.lit_answer.resize(self.lit_answer.sizeHint())
                else:
                    self.lit_answer.setText(f'Неправильный ответ +0 баллов, Правильный ответ {str(answer)}')
                    self.lit_answer.resize(self.lit_answer.sizeHint())
            NUMBER_QUES += 1

    def run1(self):
        con = sqlite3.connect(NAME_BD)
        cur = con.cursor()
        result = cur.execute("""SELECT help FROM Literature
                                        WHERE id_lit = ?""", (NUMBER_QUES,)).fetchall()
        help = result[0][0]
        con.close()
        global HELP
        self.lit_help.setText(str(help))
        self.lit_help.resize(self.lit_help.sizeHint())
        HELP += 1

    def back(self):
        self.second_form = SecondForm()
        self.second_form.show()
        self.hide()


class PeForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 800, 300)
        self.setWindowTitle('Физическая культура')

        self.pe_answer = QLabel(self)
        self.pe_answer.resize(self.pe_answer.sizeHint())
        self.pe_answer.move(5, 50)
        self.pe_answer.setText('')

        self.but_pe_1 = QPushButton('Вопрос', self)
        self.but_pe_1.resize(100, 25)
        self.but_pe_1.move(100, 150)
        self.but_pe_1.clicked.connect(self.run)

        self.but_pe_1 = QPushButton('Подсказка', self)
        self.but_pe_1.resize(100, 25)
        self.but_pe_1.move(100, 200)
        self.but_pe_1.clicked.connect(self.run1)

        self.pe_help = QLabel(self)
        self.pe_help.resize(self.pe_answer.sizeHint())
        self.pe_help.move(5, 250)
        self.pe_help.setText('')

        self.but_pe_back = QPushButton('Вернуться к предметам', self)
        self.but_pe_back.resize(150, 25)
        self.but_pe_back.move(100, 80)
        self.but_pe_back.clicked.connect(self.back)

    def run(self):
        global NUMBER_QUES
        global MARK
        if NUMBER_QUES > 5:
            self.pe_answer.setText('Вопросы данной категории закончились')
            self.pe_answer.resize(self.pe_answer.sizeHint())
        else:
            con = sqlite3.connect(NAME_BD)
            cur = con.cursor()
            result = cur.execute("""SELECT que, ans FROM PE
                                WHERE id_pe = ?""", (NUMBER_QUES,)).fetchall()
            quetion, answer = result[0]
            con.close()
            answer1, ok_pressed = QInputDialog.getText(self, f'Вопрос №{NUMBER_QUES}', str(quetion))
            if ok_pressed:
                if str(answer) in str(answer1):
                    MARK += 1
                    self.pe_answer.setText('Правильный ответ +1 балл')
                    self.pe_answer.resize(self.pe_answer.sizeHint())
                else:
                    self.pe_answer.setText(f'Неправильный ответ +0 баллов, Правильный ответ {str(answer)}')
                    self.pe_answer.resize(self.pe_answer.sizeHint())
            NUMBER_QUES += 1

    def run1(self):
        con = sqlite3.connect(NAME_BD)
        cur = con.cursor()
        result = cur.execute("""SELECT help FROM PE
                                        WHERE id_pe = ?""", (NUMBER_QUES,)).fetchall()
        help = result[0][0]
        con.close()
        global HELP
        self.pe_help.setText(str(help))
        self.pe_help.resize(self.pe_help.sizeHint())
        HELP += 1

    def back(self):
        self.second_form = SecondForm()
        self.second_form.show()
        self.hide()


class ChForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 800, 300)
        self.setWindowTitle('Химия')

        self.ch_answer = QLabel(self)
        self.ch_answer.resize(self.ch_answer.sizeHint())
        self.ch_answer.move(5, 50)
        self.ch_answer.setText('')

        self.but_ch_1 = QPushButton('Вопрос', self)
        self.but_ch_1.resize(100, 25)
        self.but_ch_1.move(100, 150)
        self.but_ch_1.clicked.connect(self.run)

        self.but_ch_1 = QPushButton('Подсказка', self)
        self.but_ch_1.resize(100, 25)
        self.but_ch_1.move(100, 200)
        self.but_ch_1.clicked.connect(self.run1)

        self.ch_help = QLabel(self)
        self.ch_help.resize(self.ch_answer.sizeHint())
        self.ch_help.move(5, 250)
        self.ch_help.setText('')

        self.but_ch_back = QPushButton('Вернуться к предметам', self)
        self.but_ch_back.resize(150, 25)
        self.but_ch_back.move(100, 80)
        self.but_ch_back.clicked.connect(self.back)

    def run(self):
        global NUMBER_QUES
        global MARK
        if NUMBER_QUES > 5:
            self.ch_answer.setText('Вопросы данной категории закончились')
            self.ch_answer.resize(self.ch_answer.sizeHint())
        else:
            con = sqlite3.connect(NAME_BD)
            cur = con.cursor()
            result = cur.execute("""SELECT que, ans FROM Сhemistry
                                WHERE id_ch = ?""", (NUMBER_QUES,)).fetchall()
            quetion, answer = result[0]
            con.close()
            answer1, ok_pressed = QInputDialog.getText(self, f'Вопрос №{NUMBER_QUES}', str(quetion))
            if ok_pressed:
                if str(answer) in str(answer1):
                    MARK += 1
                    self.ch_answer.setText('Правильный ответ +1 балл')
                    self.ch_answer.resize(self.ch_answer.sizeHint())
                else:
                    self.ch_answer.setText(f'Неправильный ответ +0 баллов, Правильный ответ {str(answer)}')
                    self.ch_answer.resize(self.ch_answer.sizeHint())
            NUMBER_QUES += 1

    def run1(self):
        con = sqlite3.connect(NAME_BD)
        cur = con.cursor()
        result = cur.execute("""SELECT help FROM Сhemistry
                                        WHERE id_ch = ?""", (NUMBER_QUES,)).fetchall()
        help = result[0][0]
        con.close()
        global HELP
        self.ch_help.setText(str(help))
        self.ch_help.resize(self.ch_help.sizeHint())
        HELP += 1

    def back(self):
        self.second_form = SecondForm()
        self.second_form.show()
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Inte()
    ex.show()
    sys.exit(app.exec())
