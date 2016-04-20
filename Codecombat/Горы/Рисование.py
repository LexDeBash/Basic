# Теперь у тебя есть Кольца Цветов! Ты можешь:
# toggleFlowers(true/false) - включить или выключить.
# setFlowerColor("random") - также можно выбрать "pink", "red", "blue", "purple", "yellow", или "white".

# Вот некоторые функции для рисования фигур:
# х, у - центр фигуры
# size - размер фигуры (radius, side length)
def drawCircle(x, y, size):
    angle = 0
    self.toggleFlowers(False)
    while angle <= Math.PI * 2:
        newX = x + (size * Math.cos(angle))
        newY = y + (size * Math.sin(angle))
        self.moveXY(newX, newY)
        self.toggleFlowers(True)
        angle += 0.2

def drawSquare(x, y, size):
    self.toggleFlowers(False)
    cornerOffset = size / 2
    self.moveXY(x - cornerOffset, y - cornerOffset)
    self.toggleFlowers(True)
    self.moveXY(x + cornerOffset, y - cornerOffset)
    self.moveXY(x + cornerOffset, y + cornerOffset)
    self.moveXY(x - cornerOffset, y + cornerOffset)
    self.moveXY(x - cornerOffset, y - cornerOffset)


redX = {"x": 28, "y": 36}
whiteX = {"x": 44, "y": 36}

# Выбери цвет.
self.setFlowerColor("red")
# Нарисуй круг размером 10 на красной метке.
#self.moveXY(28, 36)
drawCircle(28, 36, 10)
# Измени цвет!
self.setFlowerColor("blue")
# Нарисуй квадрат размером 10 на белой метке.
#self.moveXY(44, 36)
drawSquare(44, 36, 10)
# Теперь экспериментируй, рисуя все что угодно!
drawSquare(28, 36, 10)
