import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate
V1 = 15
V2 = 20
delta_t = 1
start_time_1 = 8
start_time_2 = 9
S0 = V1 * delta_t
V_rel = V2 - V1
t_meet_after_second = S0 / V_rel
t1_total = delta_t + t_meet_after_second
S_meet = V1 * t1_total
meet_hour = start_time_1 + t1_total
meet_hours = int(meet_hour)
meet_minutes = int((meet_hour - meet_hours) * 60)
print("=" * 60)
print("                ЛАБОРАТОРНАЯ РАБОТА ПО ФИЗИКЕ")
print("                Тема: График движения двух тел")
print("=" * 60)
print("\n┌────────────── ДАНО ──────────────┐")
print(f"│ Скорость первого велосипедиста: V₁ = {V1} км/ч")
print(f"│ Скорость второго велосипедиста: V₂ = {V2} км/ч")
print(f"│ Время старта первого: 8:00")
print(f"│ Время старта второго: 9:00")
print(f"│ Разница во времени старта: Δt = {delta_t} час")
print("└─────────────────────────────────┘")
print("\n┌────────────── РЕШЕНИЕ ──────────────┐")
print(f"│ 1. За {delta_t} час первый проехал: S₀ = V₁ × Δt = {V1} × {delta_t} = {S0} км")
print(f"│ 2. Относительная скорость: V_отн = V₂ - V₁ = {V2} - {V1} = {V_rel} км/ч")
print(f"│ 3. Время встречи после выезда второго:")
print(f"│    t = S₀ / V_отн = {S0} / {V_rel} = {t_meet_after_second:.2f} ч")
print(f"│ 4. Общее время движения первого до встречи:")
print(f"│    t₁ = Δt + t = {delta_t} + {t_meet_after_second:.2f} = {t1_total:.2f} ч")
print(f"│ 5. Расстояние до встречи:")
print(f"│    S = V₁ × t₁ = {V1} × {t1_total:.2f} = {S_meet:.2f} км")
print("└─────────────────────────────────┘")
print("\n┌────────────── ОТВЕТ ──────────────┐")
print(f"│ Второй велосипедист догонит первого:")
print(f"│ через {t_meet_after_second:.2f} часа после своего выезда")
print(f"│ в {meet_hours:02d}:{meet_minutes:02d}")
print(f"│ на расстоянии {S_meet:.1f} км от пункта отправления")
print("└─────────────────────────────────┘")
print("\n" + "=" * 60)
print("                   ТАБЛИЦА ДВИЖЕНИЯ")
print("=" * 60)
table_data = []
times = []
for hour in range(8, 13):
    for minute in [0, 30]:
        if hour == 12 and minute > 0:
            continue
        time_h = hour + minute / 60
        if time_h >= 8:
            S1 = V1 * (time_h - 8)
        else:
            S1 = 0
        if time_h >= 9:
            S2 = V2 * (time_h - 9)
        else:
            S2 = 0
        time_str = f"{hour:02d}:{minute:02d}"
        if abs(time_h - meet_hour) < 0.01:
            meeting_mark = "← ВСТРЕЧА"
        else:
            meeting_mark = ""
        table_data.append([time_str, f"{S1:.1f}", f"{S2:.1f}", meeting_mark])
        times.append(time_h)
try:
    headers = ["Время", "Путь 1-го (км)", "Путь 2-го (км)", ""]
    print(tabulate(table_data, headers=headers, tablefmt="grid"))
except:
    print("\nВремя | Путь 1-го (км) | Путь 2-го (км) |")
    print("-" * 50)
    for row in table_data:
        print(f"{row[0]:^6} | {row[1]:^14} | {row[2]:^14} | {row[3]}")
print("\n" + "=" * 60)
print("                   ГРАФИК ДВИЖЕНИЯ")
print("=" * 60)
print("Закройте график, чтобы продолжить...")
t_detailed = np.linspace(8, 12, 100)
S1_detailed = np.zeros_like(t_detailed)
S2_detailed = np.zeros_like(t_detailed)
for i, t in enumerate(t_detailed):
    if t >= 8:
        S1_detailed[i] = V1 * (t - 8)
    if t >= 9:
        S2_detailed[i] = V2 * (t - 9)
plt.figure(figsize=(10, 6))
plt.plot(t_detailed, S1_detailed, 'b-', linewidth=2, label='Первый велосипедист (15 км/ч)')
plt.plot(t_detailed, S2_detailed, 'r-', linewidth=2, label='Второй велосипедист (20 км/ч)')
plt.plot(meet_hour, S_meet, 'go', markersize=10, label=f'Встреча в {meet_hours:02d}:{meet_minutes:02d}')
plt.grid(True, linestyle='--', alpha=0.7)
plt.xlabel('Время (часы)', fontsize=12)
plt.ylabel('Расстояние от старта (км)', fontsize=12)
plt.title('График движения двух велосипедистов', fontsize=14)
plt.legend(fontsize=10)
plt.xticks(np.arange(8, 12.5, 0.5), [f"{int(h)}:{'30' if h%1 else '00'}" for h in np.arange(8, 12.5, 0.5)])
plt.yticks(np.arange(0, 70, 10))
plt.xlim(8, 12)
plt.ylim(0, 65)
plt.axvline(x=meet_hour, color='green', linestyle='--', alpha=0.5)
plt.axhline(y=S_meet, color='green', linestyle='--', alpha=0.5)
plt.annotate(f'({meet_hours:02d}:{meet_minutes:02d}, {S_meet:.0f} км)',
             xy=(meet_hour, S_meet), xytext=(meet_hour + 0.2, S_meet - 5),
             arrowprops=dict(arrowstyle='->', color='green'),
             fontsize=10, color='green')
plt.tight_layout()
plt.show()
print("\n" + "=" * 60)
print("                        ВЫВОД")
print("=" * 60)
print("В ходе выполнения лабораторной работы была решена")
print("задача на относительность движения. Установлено, что")
print(f"при заданных начальных условиях второй велосипедист")
print(f"догонит первого через {t_meet_after_second:.2f} часа после")
print(f"своего старта (в {meet_hours:02d}:{meet_minutes:02d}) на расстоянии")
print(f"{S_meet:.1f} км от точки отправления. Результаты получены")
print("аналитическим методом и подтверждены графически.")
print("=" * 60)