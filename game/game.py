class Character:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power
    def attack(self):
        print("Персонаж атакует!")
    def __str__(self):
        return f"{self.__class__.__name__} {self.name}: HP={self.hp}, Power={self.power}"
class Warrior(Character):
    def __init__(self, name, hp, power):
        super().__init__(name, hp + 20, power + 10)
    def attack(self):
        print("Воин наносит мощный удар мечом!")
class Mage(Character):
    def __init__(self, name, hp, power, mana=100):
        super().__init__(name, hp, max(0, power - 2))
        self.mana = mana
    def attack(self):
        print("Маг выпускает огненный шар!")
    def __str__(self):
        return super().__str__() + f", Mana={self.mana}"
def main():
    chars = []
    chars.append(Warrior("Арагорн", 120, 20))
    chars.append(Mage("Гендальф", 80, 10, 200))
    while True:
        print("\nМеню:")
        print("1. Создать персонажа")
        print("2. Показать всех персонажей")
        print("3. Атака персонажа")
        print("4. Выход")
        choice = input("Выберите пункт: ").strip()
        if choice == "1":
            t = input("Тип (warrior/mage): ").strip().lower()
            name = input("Имя: ").strip()
            hp = int(input("HP: ").strip())
            power = int(input("Сила (power): ").strip())
            if t == "warrior":
                chars.append(Warrior(name, hp, power))
            elif t == "mage":
                mana = int(input("Mana: ").strip())
                chars.append(Mage(name, hp, power, mana))
            else:
                print("Неизвестный тип. Введите 'warrior' или 'mage'.")
        elif choice == "2":
            if not chars:
                print("Персонажей нет.")
            for i, c in enumerate(chars):
                print(i, c)
        elif choice == "3":
            if not chars:
                print("Персонажей нет.")
                continue
            for i, c in enumerate(chars):
                print(i, c)
            idx = int(input("Выберите индекс персонажа для атаки: ").strip())
            if 0 <= idx < len(chars):
                chars[idx].attack()
            else:
                print("Неправильный индекс.")
        elif choice == "4":
            print("Выход.")
            break
        else:
            #print('Macan xuesos')
            print("Неверный выбор. Попробуйте ещё.")
if name == "__main__":
    main()