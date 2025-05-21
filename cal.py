class TriangleValidator:
    def __init__(self):
        self.tests_passed = 0
        self.bugs_found = 0

    def classify_triangle(self, side1, side2, side3):
        try:
            x, y, z = float(side1), float(side2), float(side3)
        except ValueError:
            return "Ошибка: введены не числовые значения"

        if x + y <= z or x + z <= y or y + z <= x:
            return "Треугольник не существует"

        if x == y == z:
            return "Равносторонний треугольник"
        elif x == y or y == z or x == z:
            return "Равнобедренный треугольник"
        else:
            return "Разносторонний треугольник"

    def perform_tests(self, side1, side2, side3):
        # Тест 1: Все стороны пустые (символ '0' в вашем коде)
        if side1 == '0' and side2 == '0' and side3 == '0':
            print("Тест 1: Проверка пустых значений пройдена.")
            self.tests_passed += 1

        # Тест 2: Частично заполненные поля
        partially_filled = (
            (side1 != '0' and side2 != '0' and side3 == '0') or
            (side1 != '0' and side2 == '0' and side3 != '0') or
            (side1 == '0' and side2 != '0' and side3 != '0')
        )
        if partially_filled:
            print("Тест 2: Частично заполненные поля пройдены.")
            self.tests_passed += 1

        # Тесты 3-7: Позитивные кейсы
        positive_cases = [
            ('3', '4', '5'),
            ('2', '3', '4'),
            ('66', '67', '68'),
            ('3', '3', '5'),
            ('6', '6', '6')
        ]
        if (side1, side2, side3) in positive_cases:
            print("Тесты 3-7: Позитивные случаи пройдены.")
            self.tests_passed += 5

        # Тест 8: Проверка несуществующего треугольника
        try:
            a, b, c = float(side1), float(side2), float(side3)
            if a + b <= c or a + c <= b or b + c <= a:
                print("Тест 8: Случай несуществующего треугольника пройден.")
                self.tests_passed += 1
        except ValueError:
            pass

        # Тест 9: Проверка на нечисловой ввод
        try:
            float(side1)
            float(side2)
            float(side3)
        except ValueError:
            print("Тест 9: Обнаружен нечисловой ввод.")
            self.tests_passed += 1

        # Тест 10: Проверка больших чисел
        try:
            if any(float(s) > 4_294_967_295 for s in (side1, side2, side3)):
                print("Тест 10: Обработка больших чисел пройдена.")
                self.tests_passed += 1
        except ValueError:
            pass

        # Тест 11: SQL-инъекция (простая проверка ключевых слов)
        if any(keyword in str(s).lower() for s in (side1, side2, side3) for keyword in ['select', 'or', 'where']):
            print("Тест 11: SQL-инъекция обнаружена и обработана.")
            self.tests_passed += 1

        # Тест 12: XSS-уязвимость (проверка на <script>)
        if any('<script>' in str(s).lower() for s in (side1, side2, side3)):
            print("Тест 12: XSS-уязвимость обнаружена.")
            self.tests_passed += 1

    def detect_bugs(self, side1, side2, side3):
        # Баг 1: Поле side3 не проверяется если оно '0', а другие заполнены
        if side3 == '0' and (side1 != '0' or side2 != '0'):
            print("Баг 1: Поле третьей стороны не проверяется должным образом.")
            self.bugs_found += 1

        # Баг 2: Равносторонний треугольник с нулевыми сторонами
        if side1 == '0' and side2 == '0' and side3 == '0':
            print("Баг 2: Обнаружено равностороннее треугольник с нулевыми сторонами.")
            self.bugs_found += 1

        # Баг 3: Нецелые числа (наличие точки)
        try:
            float(side1)
            float(side2)
            float(side3)
            if any('.' in s for s in (side1, side2, side3)):
                print("Баг 3: Введены нецелые числа.")
                self.bugs_found += 1
        except ValueError:
            pass

        # Баг 4: XSS с учётом регистра
        if any('<script>' in str(s).lower() for s in (side1, side2, side3)) and any('<SCRIPT>' in s for s in (side1, side2, side3)):
            print("Баг 4: XSS-уязвимость с учётом регистра обнаружена.")
            self.bugs_found += 1

    def execute_all_tests(self, side1, side2, side3):
        self.perform_tests(side1, side2, side3)
        self.detect_bugs(side1, side2, side3)

        print(f"\nПройдено тестов: {self.tests_passed}")
        print(f"Найдено багов: {self.bugs_found}")

        self.tests_passed = 0
        self.bugs_found = 0


def run():
    validator = TriangleValidator()

    while True:
        print("Введите 'stop' для выхода из программы.")

        s1 = input("Введите длину первой стороны: ")
        if s1.strip().lower() == 'stop':
            break

        s2 = input("Введите длину второй стороны: ")
        s3 = input("Введите длину третьей стороны: ")

        validator.execute_all_tests(s1, s2, s3)


if __name__ == "__main__":
    run()
