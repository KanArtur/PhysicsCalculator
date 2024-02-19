import sys
import io
import csv
import sqlite3
import json

from matplotlib import pyplot as plt
from numpy import linspace

from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QTableWidgetItem

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1236</width>
    <height>589</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QWidget" name="layoutWidget">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>10</y>
      <width>260</width>
      <height>531</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="verticalLayout">
     <item>
      <layout class="QVBoxLayout" name="verticalLayout_2">
       <item>
        <widget class="QLabel" name="label">
         <property name="text">
          <string> g (Ускорение свободного падения) </string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QLineEdit" name="gEdit"/>
       </item>
      </layout>
     </item>
     <item>
      <layout class="QVBoxLayout" name="verticalLayout_3">
       <item>
        <widget class="QLabel" name="label_2">
         <property name="text">
          <string>π (Число Пи)</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QLineEdit" name="piEdit"/>
       </item>
      </layout>
     </item>
     <item>
      <layout class="QVBoxLayout" name="verticalLayout_5">
       <item>
        <widget class="QLabel" name="label_5">
         <property name="text">
          <string>Округление (кол-во знаков после запятой)</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QLineEdit" name="roundEdit"/>
       </item>
      </layout>
     </item>
     <item>
      <layout class="QVBoxLayout" name="verticalLayout_7">
       <item>
        <widget class="QLabel" name="label_3">
         <property name="text">
          <string>Заметки</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QPlainTextEdit" name="notesEdit">
         <property name="sizePolicy">
          <sizepolicy hsizetype="Minimum" vsizetype="Minimum">
           <horstretch>0</horstretch>
           <verstretch>0</verstretch>
          </sizepolicy>
         </property>
        </widget>
       </item>
      </layout>
     </item>
     <item>
      <layout class="QVBoxLayout" name="verticalLayout_8">
       <item>
        <layout class="QVBoxLayout" name="verticalLayout_6">
         <item>
          <widget class="QPushButton" name="velocityGraph">
           <property name="text">
            <string>Вывести график скорости</string>
           </property>
          </widget>
         </item>
         <item>
          <widget class="QPushButton" name="coordinateGraph">
           <property name="text">
            <string>Вывести график координаты</string>
           </property>
          </widget>
         </item>
        </layout>
       </item>
       <item>
        <widget class="QLabel" name="label_4">
         <property name="text">
          <string>История вычислений</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QComboBox" name="calculationHistory"/>
       </item>
       <item>
        <layout class="QHBoxLayout" name="horizontalLayout_3">
         <item>
          <widget class="QPushButton" name="clearHistoryBtn">
           <property name="text">
            <string>Очистить историю</string>
           </property>
          </widget>
         </item>
         <item>
          <widget class="QPushButton" name="loadHistoryBtn">
           <property name="text">
            <string>Загрузить</string>
           </property>
          </widget>
         </item>
        </layout>
       </item>
      </layout>
     </item>
    </layout>
   </widget>
   <widget class="QWidget" name="layoutWidget_2">
    <property name="geometry">
     <rect>
      <x>280</x>
      <y>10</y>
      <width>551</width>
      <height>361</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="verticalLayout_4">
     <item>
      <widget class="QTableWidget" name="inputTable">
       <property name="sizeAdjustPolicy">
        <enum>QAbstractScrollArea::AdjustToContents</enum>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="calculateButton">
       <property name="text">
        <string>Вычислить</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QWidget" name="verticalLayoutWidget_4">
    <property name="geometry">
     <rect>
      <x>850</x>
      <y>120</y>
      <width>371</width>
      <height>401</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="theoryImages">
     <item>
      <widget class="QLabel" name="theoryImage1">
       <property name="text">
        <string/>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QLabel" name="theoryImage2">
       <property name="text">
        <string/>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QLabel" name="theoryImage3">
       <property name="text">
        <string/>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QLabel" name="theoryImage4">
       <property name="text">
        <string/>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QLabel" name="label_9">
    <property name="geometry">
     <rect>
      <x>850</x>
      <y>10</y>
      <width>249</width>
      <height>21</height>
     </rect>
    </property>
    <property name="text">
     <string>Теоретический материал</string>
    </property>
   </widget>
   <widget class="QLabel" name="theoryText">
    <property name="geometry">
     <rect>
      <x>850</x>
      <y>40</y>
      <width>261</width>
      <height>71</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>8</pointsize>
     </font>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QWidget" name="layoutWidget">
    <property name="geometry">
     <rect>
      <x>280</x>
      <y>380</y>
      <width>291</width>
      <height>161</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="verticalLayout_9">
     <item>
      <widget class="QLabel" name="label_8">
       <property name="text">
        <string>Результат вычислений</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPlainTextEdit" name="calculationResults">
       <property name="font">
        <font>
         <pointsize>9</pointsize>
        </font>
       </property>
       <property name="plainText">
        <string/>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QWidget" name="layoutWidget_4">
    <property name="geometry">
     <rect>
      <x>580</x>
      <y>380</y>
      <width>251</width>
      <height>161</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="verticalLayout_10">
     <item>
      <widget class="QLabel" name="label_6">
       <property name="text">
        <string>Преобразование меры угла</string>
       </property>
      </widget>
     </item>
     <item>
      <layout class="QHBoxLayout" name="horizontalLayout_2">
       <item>
        <widget class="QLabel" name="label_10">
         <property name="text">
          <string>Градусы</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QLabel" name="label_11">
         <property name="text">
          <string>Радианы</string>
         </property>
        </widget>
       </item>
      </layout>
     </item>
     <item>
      <layout class="QHBoxLayout" name="horizontalLayout">
       <item>
        <widget class="QLineEdit" name="degEdit"/>
       </item>
       <item>
        <widget class="QLabel" name="label_7">
         <property name="text">
          <string/>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QLineEdit" name="radEdit"/>
       </item>
      </layout>
     </item>
     <item>
      <widget class="QPushButton" name="radToDegBtn">
       <property name="text">
        <string>Радианы в градусы</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="degToRadBtn">
       <property name="text">
        <string>Градусы в радианы</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>1236</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class NoMotionChosenError(Exception):
    pass


class EmptyDataError(Exception):
    pass


class NotEnoughDataError(Exception):
    pass


class InvalidRoundValue(Exception):
    pass


class ImpossibleGraphError(Exception):
    pass


class TwoTimeValues(Exception):
    pass


class TimeValueDoesNotExist(Exception):
    pass


class Kinematics(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Физический калькулятор по разделу Кинематика")
        self.setFixedSize(1236, 589)

        self.theoryTexts = {"linUni": "Прямолинейным равномерным называют \nтакое движение, "
                                      "при котором тело за \nлюбые равные промежутки времени\n"
                                      "совершает одинаковые перемещения.",
                            "linAcc": "Прямолинейное равноускоренное движение — \n— движение по "
                                      "прямой, при котором за любые \nравные промежутки времени "
                                      "вектор скорости \nточки изменяется на равную величину.",
                            "perAndFreq": "Период — время, за которое тело делает \nполный оборот "
                                          "по окружности. \nЧастота — количество оборотов по \n"
                                          "окружности, совершенных за единицу времени.",
                            "velAndAcc": "Равномерное движение по окружности - движение\n"
                                         "с постоянной по модулю скоростью по траектории, \nкоторая "
                                         "описывает окружность вокруг \nнеподвижной точки, являющейся её центром."}

        self.gEdit.setText("9.8")
        self.piEdit.setText("3.14")
        self.roundEdit.setText("2")
        self.rows = 0

        self.motionChosen = False

        """Подключение базы данных и очистка истории при запуске."""
        self.con = sqlite3.connect("calculationHistory.db")
        self.cur = self.con.cursor()
        self.clearHistory()

        """Создание menubar"""
        self.createActions()

        self.menuBar = self.menuBar()
        self.setMenuBar(self.menuBar)

        linear = self.menuBar.addMenu("&Прямолинейное")
        linear.addAction(self.unifMotion)
        linear.addAction(self.accMotion)

        circular = self.menuBar.addMenu("&По окружности")
        circular.addAction(self.perAndFreq)
        circular.addAction(self.velAndAcc)

        """Привязка методов ко всем кнопкам"""
        self.degToRadBtn.clicked.connect(self.degToRadTransform)

        self.radToDegBtn.clicked.connect(self.radToDegTransform)

        self.calculateButton.clicked.connect(self.calculate)
        self.calculateButton.clicked.connect(lambda x: self.updateHistory(self.rows - 1))

        self.velocityGraph.clicked.connect(lambda x: self.showGraph("V"))

        self.coordinateGraph.clicked.connect(lambda x: self.showGraph("x"))

        self.clearHistoryBtn.clicked.connect(self.clearHistory)

        self.loadHistoryBtn.clicked.connect(self.loadHistory)

    """Создание действий для menubar."""
    def createActions(self):
        self.unifMotion = QAction("Равномерное", self)  # uniform motion
        self.unifMotion.triggered.connect(lambda: self.openTable("linUni.csv"))

        self.accMotion = QAction("Равноускоренное", self)  # accelerated motion
        self.accMotion.triggered.connect(lambda: self.openTable("linAcc.csv"))

        self.perAndFreq = QAction("Период и частота", self)  # period and frequency
        self.perAndFreq.triggered.connect(lambda: self.openTable("perAndFreq.csv"))

        self.velAndAcc = QAction("Скорости и ускорение", self)  # velocities and acceleration
        self.velAndAcc.triggered.connect(lambda: self.openTable("velAndAcc.csv"))

    """Метод очистки истории, который удаляет все записи из базы данных."""
    def clearHistory(self):
        self.cur.execute("""DELETE from History""")
        self.con.commit()
        for i in range(self.calculationHistory.count()):
            self.calculationHistory.removeItem(0)

    """Метод добавления новой записи в историю, которая записывает все введённые пользователем данные в базу
    данных, а также присваивает записи уникальный ID."""
    def updateHistory(self, n):
        if n == -1:
            return
        typeId = self.cur.execute("""SELECT id FROM Types
            WHERE title = ?""", (self.type,)).fetchone()[0]
        addData = ([self.calculationHistory.count() + 1, typeId] +
                   [self.inputTable.item(i, 3).text() for i in range(n)] + (10 - n) * [""])
        self.cur.execute(f"INSERT INTO History VALUES {tuple(addData)}")
        self.con.commit()
        self.calculationHistory.addItem(f"ID:{self.calculationHistory.count() + 1}:{self.type}")

    """Метод загрузки записи из истории, который обращается к конкретным данным по уникальному ID, вызывает метод
    открытия соответствующей таблицы, заполняет её и выводит результат вычисления."""
    def loadHistory(self):
        try:
            if self.calculationHistory.currentText() == "":
                raise EmptyDataError
            id = self.calculationHistory.currentText().split(":")[1]
            data = self.cur.execute("""SELECT DISTINCT * FROM History
                WHERE calcId = ?""", (id,)).fetchone()
            loadedType = self.cur.execute("""SELECT DISTINCT title FROM Types
                WHERE id = ?""", (data[1],)).fetchone()[0]
            self.type = loadedType
            self.openTable(f"{loadedType}.csv")
            for i in range(self.rows - 1):
                loadedItem = QTableWidgetItem(data[2:][i])
                self.inputTable.setItem(i, 3, loadedItem)
            self.calculate()
        except EmptyDataError:
            self.calculationResults.setPlainText("Не выбрана запись из истории.")
        except Exception as e:
            print(e.__class__.__name__)

    """Метод предоставления теоретического материала, который включает в себя определение выбранного вида движения,
    а также картинки с формулами, которые содержатся в папке images."""
    def openTheory(self, type):
        self.type = type
        self.theoryText.setText(self.theoryTexts[type])
        self.theoryImage1.setPixmap(QPixmap(f"Images/{type}/1.png"))
        self.theoryImage2.setPixmap(QPixmap(f"Images/{type}/2.png"))
        self.theoryImage3.setPixmap(QPixmap(f"Images/{type}/3.png"))
        self.theoryImage4.setPixmap(QPixmap(f"Images/{type}/4.png"))

    """Метод открытия таблицы физических величин. Открываемая таблица зависит от выбранного вида движения.
    Открываемая таблица берет данные из соответствующего файла csv."""
    def openTable(self, fileName):
        self.openTheory(fileName.split(".")[0])
        self.calculationResults.setPlainText("")

        self.motionChosen = True
        with open(fileName, "r", encoding="utf-8") as valuesTable:
            self.data = list(csv.reader(valuesTable, delimiter=";", quotechar='"'))
            self.rows = len(self.data)
            self.columns = len(self.data[0])
            self.inputTable.setColumnCount(self.columns)
            self.inputTable.setRowCount(self.rows - 1)
            self.inputTable.setHorizontalHeaderLabels(self.data[0])
            self.data = self.data[1:]
            for i in range(self.rows - 1):
                for j in range(self.columns):
                    item = QTableWidgetItem(str(self.data[i][j]))
                    self.inputTable.setItem(i, j, item)
            self.inputTable.resizeColumnsToContents()

    """Метод вычислений и 'сердце' калькулятора. Он позволяет находить значения, оповещает, если некоторые найти 
    невозможно и обрабатывает много исключений. Работает на основе данных из formulas.json, где хранятся
    формулы к каждому значению к каждому виду движения. Все данные метод берёт из таблицы inputTable, куда
    пользователь вводит значения."""
    def calculate(self):
        try:
            if not self.motionChosen:
                raise NoMotionChosenError

            self.givenValues = dict()

            pi = float(self.piEdit.text())
            g = float(self.gEdit.text())
            self.r = self.roundEdit.text().replace(",", ".")

            if float(self.r) < 0 or int(float(self.r)) != float(self.r):
                raise InvalidRoundValue
            self.r = int(self.r)

            """Получение данных из таблицы, получение множества известных величин, а также словаря их значений"""
            for i in range(self.rows - 1):
                if self.inputTable.item(i, 3).text() != "":
                    if self.inputTable.item(i, 1).text() == "φ":
                        self.givenValues["phi"] = self.inputTable.item(i, 3).text().replace(",", ".")
                    elif self.inputTable.item(i, 1).text() == "ꞷ":
                        self.givenValues["w"] = self.inputTable.item(i, 3).text().replace(",", ".")
                    else:
                        self.givenValues[self.inputTable.item(i, 1).text()] = \
                            self.inputTable.item(i, 3).text().replace(",", ".")

            setOfGivVal = set(self.givenValues.keys())
            startValuesAmount = len(setOfGivVal)

            """Проверка на отсутствие введённых данных."""
            if len(setOfGivVal) == 0:
                raise EmptyDataError

            resultOutput = []

            """Открытие json файла, содержащего формулы."""
            with open("formulas.json") as formulasJson:
                formulas = json.load(formulasJson)[self.type]

                """Получение множества неизвестных величин."""
                unknownValues = set(formulas.keys()).difference(setOfGivVal)

                """Далее идёт цикл, который повторяется столько, сколько есть неизвестных значений. Каждую итерацию
                перепроверяются, собственно, сами неизвестные значения, а точнее, возможно ли применить формулу
                и найти их."""
                for i in range(len(unknownValues)):

                    """Перебор все неизвестных на данный момент величин, где uV - сокращение от Unknown Value"""
                    for uV in unknownValues:
                        found = False

                        """Проверка на возможность получения значения величины uV с имеющимися данными"""
                        if not any([set(j[1]).issubset(setOfGivVal) for j in formulas[uV]]):
                            continue

                        """Перебор формул для uV, где valuesNeeded - множество необходимых величин 
                        для применения формулы"""
                        for s in formulas[uV]:
                            valuesNeeded = set(s[1])

                            """В равноускоренном движении есть возможность получить отрицательное время, не получить
                            результата вообще или получить сразу два значения. Данное условие исключает эти варианты
                            событий."""
                            if valuesNeeded.issubset(setOfGivVal):
                                calculatedValue = eval(self.reformatFormula(s[0], list(formulas.keys())))
                                unknownValues.remove(uV)
                                if str(calculatedValue) == "-":
                                    raise TimeValueDoesNotExist
                                elif ";" in str(calculatedValue):
                                    raise TwoTimeValues

                                self.givenValues[uV] = round(float(calculatedValue), self.r)
                                setOfGivVal = set(self.givenValues.keys())

                                """Так как Фи и Омега не являются буквами латинского алфавита, все связанные с ними
                                данные преобразуются в их транслитерацию для более удобноц работы. Но для вывода
                                результата они вновь становятся такими, какими должны быть."""
                                if uV == "w":
                                    metering = [i[2].split("(")[0].rstrip(" ") for i in self.data if "ꞷ" in i][0]
                                    valueSymbol = "ꞷ"
                                elif uV == "phi":
                                    metering = [i[2].split("(")[0].rstrip(" ") for i in self.data if "φ" in i][0]
                                    valueSymbol = "φ"
                                else:
                                    metering = [i[2].split("(")[0].rstrip(" ") for i in self.data if uV in i][0]
                                    valueSymbol = uV

                                resultOutput.append(valueSymbol + " = " + str(self.givenValues[uV]) + " " + metering)
                                found = True
                                break

                        if found:
                            break

                if len(set(self.givenValues.keys())) == startValuesAmount:
                    raise NotEnoughDataError

                """Вывод значений, которые невозможно найти вследствие недостатка данных."""
                if len(unknownValues) != 0:
                    resultOutput.append("")
                    for uV in unknownValues:
                        if uV == "w":
                            resultOutput.append("ꞷ" + " - невозможно найти.")
                        elif uV == "phi":
                            resultOutput.append("φ" + " - невозможно найти.")
                        else:
                            resultOutput.append(uV + " - невозможно найти.")

                self.calculationResults.setPlainText("\n".join(resultOutput))
        except NoMotionChosenError:
            self.calculationResults.setPlainText("Не выбран вид движения.")
        except EmptyDataError:
            self.calculationResults.setPlainText("Отсутствуют входные данные.")
        except NotEnoughDataError:
            self.calculationResults.setPlainText("Недостаточно данных.")
        except InvalidRoundValue:
            self.calculationResults.setPlainText("Некорректное значение округления.")
        except ValueError:
            self.calculationResults.setPlainText("Некорректные входные данные.")
        except TwoTimeValues:
            self.calculationResults.setPlainText(f"При введённых данных время может "
                                                 f"принимать два значения: {calculatedValue} (в секундах).\n"
                                                 f"Повторите ввод данных с одним из значений.\n\n"
                                                 f"Так происходит, потому что тело пересекает некоторую точку дважды "
                                                 f"в разные промежутки времени.")
        except TimeValueDoesNotExist:
            self.calculationResults.setPlainText(f"При введённых данных значение времени не существует. "
                                                 f"Перепроверьте все данные и повторите попытку.\n\n"
                                                 f"Так получилось, потому что тело никогда не "
                                                 f"пересечёт заданную точку.")

    """Метод преобразования строки формулы таким образом, чтобы значения брались из словаря givenValues.
    Этот метод позволяет сохранять данные в formulas.json и graphs.json наиболее чистыми и удобными для редакции."""
    def reformatFormula(self, line, vals):
        res = list(map(lambda x: f"float(self.givenValues[\"{x}\"])" if x in vals else x, line.split()))
        return " ".join(res)

    """Методы работы преобразования градусов в радианы и обратно. Также учитывается возможное некорректные/пустые
    данные и последующее сообщение об ошибке."""
    def degToRadTransform(self):
        r = self.roundEdit.text()

        if float(r) < 0 or int(float(r)) != float(r):
            raise InvalidRoundValue
        r = int(r)
        try:
            degrees = float(self.degEdit.text())
            radians = round(degrees * float(self.piEdit.text()) / 180, r)
            self.radEdit.setText(str(radians))
            self.calculationResults.setPlainText("")
        except ValueError:
            self.calculationResults.setPlainText("Некорректное значение градусов.")

    def radToDegTransform(self):
        r = self.roundEdit.text()

        if float(r) < 0 or int(float(r)) != float(r):
            raise InvalidRoundValue
        r = int(r)
        try:
            radians = float(self.radEdit.text())
            degrees = round(radians * 180 / float(self.piEdit.text()), r)
            self.degEdit.setText(str(degrees))
            self.calculationResults.setPlainText("")
        except ValueError:
            self.calculationResults.setPlainText("Некорректное значение радиан.")

    """Метод создания графика на основе данных из graphs.json, где содержатся: уравнение, задающее график,
    необходимые значения для графика, а также такая специальная формула для задания отображаемых границ,
    которая позволит увидеть график при любых бесконечно малых или бесконечно больших данных.
    Метод предусматривает отсутствующие данные, а также не отображает график для движения по окружности, так как
    при таком виде движении действет плоскость, а не прямая. А расположение точки в плоскости относительно времени
    двумерным графиком отобразить невозможно."""
    def showGraph(self, var):
        try:
            if self.type in ["perAndFreq", "velAndAcc"]:
                raise ImpossibleGraphError
            with open("graphs.json") as graphsJson:
                y = json.load(graphsJson)[self.type][var]
                self.calculate()
                xAxis = linspace(0, 50, 1000)
                if set(y[1]).issubset(set(self.givenValues.keys())):
                    yAxis = eval(self.reformatFormula(y[0], y[1]))
                    yBorder = eval(self.reformatFormula(y[2], y[1]))
                    plt.xlim(0, yBorder)
                    plt.ylim(-yBorder, yBorder)
                    plt.xlabel("t, с")
                    if var == "x":
                        plt.ylabel("x, м")
                    elif var == "V":
                        plt.ylabel("V, м/с")
                    plt.plot(xAxis, yAxis)
                    plt.minorticks_on()
                    plt.grid(which='major', color='#4B4B4B', linewidth=0.8)
                    plt.grid(which='minor', color='#B2B2B2', ls=':')
                    plt.show()
                else:
                    raise ImpossibleGraphError
        except ImpossibleGraphError:
            self.calculationResults.setPlainText("Создание графика невозможно.")
        except AttributeError:
            self.calculationResults.setPlainText("Отсутствует таблица данных.")
        except ValueError:
            self.calculationResults.setPlainText("Некорректные входные данные.")

    """Метод вычисления корней квадратного уравнения, учитывая возможность того, что отрицательные корни могут быть
    недействительны в фищических величинах"""
    def roots(self, a, b, c, canBeNegative=False):
        D = b ** 2 - (4 * a * c)
        if D > 0:
            x1 = (-b - D ** 0.5) / (2 * a)
            x2 = (-b + D ** 0.5) / (2 * a)
            res = [x1, x2]
            if canBeNegative:
                return "{" + "; ".join([str(round(i, self.r)) for i in res]) + "}"
            else:
                if all(i < 0 for i in res):
                    return "-"
                elif any(i < 0 for i in res):
                    return str(max(res))
                else:
                    return "{" + "; ".join([str(round(i, self.r)) for i in res]) + "}"
        elif D == 0:
            x = -b / (2 * a)
            if canBeNegative:
                return str(x)
            else:
                if x < 0:
                    return "-"
                else:
                    return str(x)
        else:
            return "-"


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Kinematics()
    ex.show()
    sys.exit(app.exec())