import formulas

def safe_float_input(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: Введите корректное число!")

def main():
    while True:
        print("\n" + "="*30)
        print("ПОМОЩНИК ПО ФИЗИКЕ")
        print("="*30)
        print("1. Расчет сопротивления проводника")
        print("2. Сила тока")
        print("3. Напряжение")
        print("4. Мощность и работа тока")
        print("5. Выделение тепла тока (Закон Джоуля-Ленца)")
        print("0. Выход из программы")
        
        choice = input("\nВыберите пункт меню: ").strip()

        if choice == '0':
            print("\nСпасибо за использование! Удачи в физике! 🚀")
            break

        try:
            if choice == '1':
                print('\n1. Известны длина, площадь и удельное сопротивление\n2. Известны Напряжение и Сила тока')
                sub_choice = input('Выбор: ')
                if sub_choice == '1':
                    l = safe_float_input('Введите длину проводника (м): ')
                    s = safe_float_input('Площадь поперечного сечения (мм²): ')
                    p = safe_float_input('Удельное сопротивление материала (Ом·мм²/м): ')
                    res = formulas.calculate_resistance_geometry(l, s, p)
                    print(f"Сопротивление проводника: {res} Ом")
                elif sub_choice == '2':
                    u = safe_float_input('Напряжение (В): ')
                    i = safe_float_input('Сила тока (А): ')
                    res = formulas.calculate_resistance_ohm(u, i)
                    print(f"Сопротивление проводника: {res} Ом")

            elif choice == '2':
                print('\n1. Известны заряд и время\n2. Известны Сопротивление и Напряжение')
                sub_choice = input('Выбор: ')
                if sub_choice == '1':
                    q = safe_float_input('Заряд (Кл): ')
                    t = safe_float_input('Время (с): ')
                    res = formulas.calculate_current_charge(q, t)
                    print(f"Сила тока: {res} А")
                elif sub_choice == '2':
                    r = safe_float_input('Сопротивление (Ом): ')
                    u = safe_float_input('Напряжение (В): ')
                    res = formulas.calculate_current_ohm(u, r)
                    print(f"Сила тока: {res} А")

            elif choice == '3':
                print('\n1. Известны Мощность и Сила тока\n2. Известны Сопротивление и Сила тока')
                sub_choice = input('Выбор: ')
                if sub_choice == '1':
                    p = safe_float_input('Мощность (Вт): ')
                    i = safe_float_input('Сила тока (А): ')
                    res = formulas.voltage_power(p, i)
                    print(f"Напряжение: {res} В")
                elif sub_choice == '2':
                    r = safe_float_input('Сопротивление (Ом): ')
                    i = safe_float_input('Сила тока (А): ')
                    res = formulas.calculate_voltage_ohm(r, i)
                    print(f"Напряжение: {res} В")

            elif choice == '4':
                u = safe_float_input('\nНапряжение (В): ')
                i = safe_float_input('Сила тока (А): ')
                t = safe_float_input('Время работы (с): ')
                power, work = formulas.calculate_power_and_work(u, i, t)
                print(f"\nМощность: {power} Вт")
                print(f"Работа: {work} Дж ({work/1000:.2f} кДж)")

            elif choice == '5':
                i = safe_float_input('\nСила тока (А): ')
                r = safe_float_input('Сопротивление (Ом): ')
                t = safe_float_input('Время (с): ')
                heat = formulas.calculate_joule_heat(i, r, t)
                print(f"Выделенное количество теплоты: {heat} Дж ({heat/1000:.2f} кДж)")
                
            else:
                print("Неверный пункт меню, попробуйте еще раз.")

        except ValueError as e:
            print(f"Ошибка вычислений: {e}")

if __name__ == '__main__':
    main()
