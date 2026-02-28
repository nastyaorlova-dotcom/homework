class Flower:
    kingdom: str = "Растения"
    needs_water: bool = True
    def __init__(self, name: str, color: str, petals: int, height: float, fragrance: str) -> None:
        self.name: str = name
        self.color: str = color
        self.petals: int = petals
        self.height: float = height
        self.fragrance: str = fragrance
        self.is_blooming: bool = True  # Цветет ли сейчас
    """
       Инициализация объекта цветка.
       Args:
           name: Название цветка
           color: Цвет цветка
           petals: Количество лепестков
           height: Высота цветка (в см)
           fragrance: Аромат цветка (сладкий, свежий, без запаха и т.д.)
           """
    def __str__(self) -> str:
        return f"{self.color} {self.name}, Лепестки: {self.petals}, Высота: {self.height} см, Аромат: {self.fragrance}"

    def water(self, amount: int) -> str:
        if amount < 100:
            return f"{self.name} получил мало воды ({amount} мл), нужно еще"
        elif amount > 500:
            return f"{self.name} получил слишком много воды ({amount} мл), может загнить"
        else:
            return f"{self.name} получил достаточно воды ({amount} мл)"

    def bloom(self) -> str:
        self.is_blooming = True
        return f"Цветок {self.name} распустился!"

    def wither(self) -> str:
        self.is_blooming = False
        return f" Цветок {self.name} завял."

    def grow(self, cm: int) -> None:
        if cm > 0:
            self.height += cm
            print(f"{self.name} вырос на {cm} см! Теперь его высота {self.height} см")
        else:
            print("Высота не может уменьшиться")
flower1 = Flower("Роза", "Красная", 25, 50, "сладкий")
flower2 = Flower("Кактус", "Зеленый", 0, 15.0, "без запаха")
flower3 = Flower("Тюльпан", "Желтый", 6, 40.0, "нежный")
print(flower1) # информацию о цветах выводим
print(flower2)
print(flower3)
print(f"Царство: {Flower.kingdom}") # атрибуты класса выводим
print(f"Нуждаются в воде: {Flower.needs_water}")
print(flower2.bloom())
flower1.grow(5) # на сколько выросли цветы
flower3.grow(10)
