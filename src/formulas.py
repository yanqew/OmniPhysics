# 1. Механика
def calculate_speed(distance: float, time: float) -> float:
    if time == 0:
        raise ValueError("Время не может быть равно нулю.")
    return round(distance / time, 2)

def calculate_density(mass: float, volume: float) -> float:
    if volume == 0:
        raise ValueError("Объем не может быть равен нулю.")
    return round(mass / volume, 2)

def calculate_gravity_force(mass: float, g: float = 9.8) -> float:
    return round(mass * g, 2)

def calculate_mechanical_force(mass: float, acceleration: float) -> float:
    return round(mass * acceleration, 2)

def calculate_mechanical_energies(mass: float, height: float, speed: float) -> tuple[float, float, float]:
    g = 9.8
    e_pot = mass * g * height
    e_kin = (mass * (speed ** 2)) / 2
    e_full = e_pot + e_kin
    return round(e_pot, 2), round(e_kin, 2), round(e_full, 2)

# 2. Термодинамика
def calculate_heating_heat(c: float, mass: float, t1: float, t2: float) -> float:
    delta_t = t2 - t1
    return round(c * mass * delta_t, 2)

def calculate_fuel_combustion(q: float, mass: float) -> float:
    return round(q * mass, 2)

def calculate_melting_heat(lambda_param: float, mass: float) -> float:
    return round(lambda_param * mass, 2)

# 5. Свет и звук
def calculate_wave_length(speed: float, frequency: float) -> float:
    if frequency == 0:
        raise ValueError("Частота не может быть равна нулю.")
    return round(speed / frequency, 2)

def calculate_lens_power(focal_length: float) -> float:
    if focal_length == 0:
        raise ValueError("Фокусное расстояние не может быть равно нулю.")
    return round(1 / focal_length, 2)

# 3. Электродинамика
def calculate_resistance_geometry(length: float, area: float, resistivity: float) -> float:
    if area == 0:
        raise ValueError("Площадь поперечного сечения не может быть равна нулю.")
    return round(resistivity * (length / area), 2)

def calculate_resistance_ohm(voltage: float, current: float) -> float:
    if current == 0:
        raise ValueError("Сила тока не может быть равна нулю.")
    return round(voltage / current, 2)

def calculate_current_charge(charge: float, time: float) -> float:
    if time == 0:
        raise ValueError("Время не может быть равно нулю.")
    return round(charge / time, 2)

def calculate_current_ohm(voltage: float, resistance: float) -> float:
    if resistance == 0:
        raise ValueError("Сопротивление не может быть равна нулю.")
    return round(voltage / resistance, 2)

def calculate_voltage_power(power: float, current: float) -> float:
    if current == 0:
        raise ValueError("Сила тока не может быть равна нулю.")
    return round(power / current, 2)

def calculate_voltage_ohm(resistance: float, current: float) -> float:
    return round(resistance * current, 2)

def calculate_power_and_work(voltage: float, current: float, time: float) -> tuple[float, float, float]:
    power = round(voltage * current, 2)
    work_j = round(power * time, 2)
    work_kj = round(work_j / 1000, 2)
    return power, work_j, work_kj

def calculate_joule_heat(current: float, resistance: float, time: float) -> tuple[float, float]:
    heat_j = round((current ** 2) * resistance * time, 2)
    heat_kj = round(heat_j / 1000, 2)
    return heat_j, heat_kj
