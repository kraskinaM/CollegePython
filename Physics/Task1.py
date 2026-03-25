import math

print("=" * 50)
print("Задача 4.1: Колесо обозрения")
print("=" * 50)

R = 20
T = 40
h_osi = 22

omega = 2 * math.pi / T
print(f"1. Угловая скорость ω = {omega:.4f} рад/с")

V = omega * R
print(f"2. Линейная скорость V = {V:.2f} м/с")

a_cs = V**2 / R
print(f"3. Центростремительное ускорение a_цс = {a_cs:.2f} м/с²")
print(f"   (альтернативно: ω²·R = {omega**2 * R:.2f} м/с²)")

t = 20  # с
S = V * t
peremeshenie = 2 * R
print(f"4. За t = {t} с (половина оборота):")
print(f"   Путь S = {S:.2f} м")
print(f"   Перемещение |Δr| = {peremeshenie:.2f} м")

S_full = 2 * math.pi * R
print(f"\nПроверка за полный оборот ({T} с):")
print(f"   Путь = {S_full:.2f} м")
print(f"   Перемещение = 0 м")

print(f"\n5. Высота кабинки над землей:")
times = [0, 5, 10, 15, 20, 25, 30, 35, 40]
for t_moment in times:

    h = h_osi + R * math.sin(omega * t_moment - math.pi / 2)
    print(f"   t = {t_moment:3d} с → h = {h:.2f} м")

print("\n")

print("=" * 50)
print("Задача 4.2: Спутник Земли")
print("=" * 50)

R_z = 6370
h = 200
T_min = 88

R_orb_km = R_z + h
R_orb_m = R_orb_km * 1000
print(f"1. Радиус орбиты:")
print(f"   R_орб = {R_orb_km} км = {R_orb_m:.0f} м")

T_s = T_min * 60
omega = 2 * math.pi / T_s
print(f"2. Угловая скорость ω = {omega:.6f} рад/с")

V = omega * R_orb_m
V_kms = V / 1000
print(f"3. Линейная скорость:")
print(f"   V = {V:.2f} м/с = {V_kms:.2f} км/с")

a_cs = V**2 / R_orb_m
g = 9.81
print(f"4. Центростремительное ускорение:")
print(f"   a_цс = {a_cs:.2f} м/с² (≈ {a_cs/g:.2f}g)")

L_km = 2 * math.pi * R_orb_km
print(f"5. Длина орбиты:")
print(f"   L = {L_km:.2f} км")

N = 24 * 60 / T_min
print(f"6. Количество оборотов за сутки:")
print(f"   N = {N:.2f} оборота")

print("\n")
print("=" * 50)
print("Проверка (теоретические значения для низкой орбиты):")
print("   V ≈ 7.8 км/с (первая космическая)")
print("   T ≈ 88-90 мин")
print("   N ≈ 16 оборотов в сутки")
print("=" * 50)