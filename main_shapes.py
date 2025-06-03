from shapes import Circle, Triangle, Square

def main():
    circle = Circle(2)
    print('Площадь круга: ' + str(circle.area()))

    shapes = [Circle(3), Triangle(3, 4, 5), Square(5)]
    for shape in shapes:
        print(f'Площадь {shape.name()}а: ' + str(shape.area()))


if __name__ == "__main__":
    main()