x1, y1 = input("Введите x и y координаты первой точки через пробел: ").split(' ')
x2, y2 = input("Введите x и y координаты второй точки через пробел: ").split(' ')

k = (float(y2) - float(y1)) / (float(x2) - float(x1))
b = float(y1) - k * float(x1)

print(f"Уравнение прямой, содержащей эти точки будет иметь вид y = {k}x - {b}")
