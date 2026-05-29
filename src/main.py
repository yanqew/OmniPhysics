import formulas

def safe_float_input(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: Введите корректное число!")

def execute_calculation(prompts: list[str], formula_func, message_template: str):
    args = [safe_float_input(p) for p in prompts]
    try:
        result = formula_func(*args)
        if isinstance(result, tuple):
            print(message_template.format(*result))
        else:
            print(message_template.format(result))
    except ValueError as e:
        print(f"\nОшибка вычислений: {e}")
    input('\n[ Нажмите ENTER, чтобы продолжить ]')

def main():
    while True:
        print("\n" + "="*30)
        print("   ГЛАВНОЕ МЕНЮ ПОМОЩНИКА")
        print("="*30)
        print("1. Механика")
        print("2. Термодинамика (В разработке)")
        print("3. Электродинамика и Магнетизм")
        print("4. Свет и Звук (В разработке)")
        print("0. Выход из программы")
        
        choice1 = input('\nВыберите тему: ').strip()

        if choice1 == '0':
            print("\nСпасибо за использование! Удачи в физике! 🚀")
            break

        if choice1 == '1':
            print("\n--- РАЗДЕЛ: МЕХАНИКА ---")
            print("1. Расчет силы тяжести")
            print("2. Механическая Сила (F = m * a)")
            print("3. Скорость (v = s / t)")
            print("4. Плотность (p = m / V)")
            print("5. Механическая энергия (Потенциальная и Кинетическая)")
            print("0. Назад")
            
            choice = input('\nВыбор: ').strip()
            
            if choice == '0':
                continue
                
            if choice == '1':
                m = safe_float_input('\nВведите массу (кг): ')
                f98 = formulas.calculate_gravity_force(m, g=9.8)
                f10 = formulas.calculate_gravity_force(m, g=10.0)
                print(f"\nСила тяжести: {f98} Н (при g = 9.8 м/с²) ИЛИ {f10} Н (при g = 10 м/с²)")
                input('\n[ Нажмите ENTER, чтобы продолжить ]')
            
            elif choice == '2':
                execute_calculation(
                    prompts=['\nВведите массу (кг): ', 'Введите ускорение (м/с²): '],
                    formula_func=formulas.calculate_mechanical_force,
                    message_template="\nМеханическая сила: {} Н"
                )
            elif choice == '3':
                execute_calculation(
                    prompts=['\nВведите расстояние (м): ', 'Введите время (с): '],
                    formula_func=formulas.calculate_speed,
                    message_template="\nСкорость: {} м/с"
                )
            elif choice == '4':
                execute_calculation(
                    prompts=['\nВведите массу (кг): ', 'Введите объем (м³): '],
                    formula_func=formulas.calculate_density,
                    message_template="\nПлотность вещества: {} кг/м³"
                )
            elif choice == '5':
                execute_calculation(
                    prompts=['\nВведите массу тела (кг): ', 'Введите высоту (м): ', 'Введите скорость (м/с): '],
                    formula_func=formulas.calculate_mechanical_energies,
                    message_template="\n Потенциальная энергия: {} Дж\n Кинетическая энергия: {} Дж\n Полная энергия: {} Дж"
                )

        elif choice1 == '3':
            print("\n--- РАЗДЕЛ: ЭЛЕКТРОДИНАМИКА ---")
            print("1. Расчет сопротивления проводника")
            print("2. Сила тока")
            print("3. Напряжение")
            print("4. Мощность и работа тока")
            print("5. Выделение тепла тока (Закон Джоуля-Ленца)")
            print("0. Назад")

            choice = input("\nВыберите пункт меню: ").strip()

            if choice == '0':
                continue

            if choice == '1':
                print('\n1. Известны длина, площадь и удельное сопротивление\n2. Известны Напряжение и Сила тока')
                sub_choice = input('Выбор: ')
                if sub_choice == '1':
                    execute_calculation(
                        prompts=['Введите длину проводника (м): ', 'Площадь сечения (мм²): ', 'Удельное сопротивление (Ом·мм²/м): '],
                        formula_func=formulas.calculate_resistance_geometry,
                        message_template="\n Сопротивление проводника: {} Ом"
                    )
                elif sub_choice == '2':
                    execute_calculation(
                        prompts=['Напряжение (В): ', 'Сила тока (А): '],
                        formula_func=formulas.calculate_resistance_ohm,
                        message_template="\n Сопротивление проводника: {} Ом"
                    )

            elif choice == '2':
                print('\n1. Известны заряд и время\n2. Известны Сопротивление и Напряжение')
                sub_choice = input('Выбор: ')
                if sub_choice == '1':
                    execute_calculation(
                        prompts=['Заряд (Кл): ', 'Время (с): '],
                        formula_func=formulas.calculate_current_charge,
                        message_template="\n Сила тока: {} А"
                    )
                elif sub_choice == '2':
                    execute_calculation(
                        prompts=['Сопротивление (Ом): ', 'Напряжение (В): '],
                        formula_func=formulas.calculate_current_ohm,
                        message_template="\n Сила тока: {} А"
                    )

            elif choice == '3':
                print('\n1. Известны Мощность и Сила тока\n2. Известны Сопротивление и Сила тока')
                sub_choice = input('Выбор: ')
                if sub_choice == '1':
                    execute_calculation(
                        prompts=['Мощность (Вт): ', 'Сила тока (А): '],
                        formula_func=formulas.calculate_voltage_power,
                        message_template="\n Напряжение: {} В"
                    )
                elif sub_choice == '2':
                    execute_calculation(
                        prompts=['Сопротивление (Ом): ', 'Сила тока (А): '],
                        formula_func=formulas.calculate_voltage_ohm,
                        message_template="\n Напряжение: {} В"
                    )

            elif choice == '4':
                execute_calculation(
                    prompts=['\nНапряжение (В): ', 'Сила тока (А): ', 'Время работы (с): '],
                    formula_func=formulas.calculate_power_and_work,
                    message_template="\n Мощность: {} Вт\n Работа: {} Дж ({} кДж)"
                )

            elif choice == '5':
                execute_calculation(
                    prompts=['\nСила тока (А): ', 'Сопротивление (Ом): ', 'Время (с): '],
                    formula_func=formulas.calculate_joule_heat,
                    message_template="\n Выделенное количество теплоты: {} Дж ({} кДж)"
                )
        
        elif choice1 in ['2', '4']:
            print("\n" + "."*30)
            print("Этот раздел сейчас находится в разработке.")
            print("."*30)
            input('\n[ Нажмите ENTER, чтобы вернуться ]')

if __name__ == '__main__':
    main()
