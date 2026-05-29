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
        raise ValueError("Сопротивление не может быть равно нулю.")
    return round(voltage / resistance, 2)

def calculate_voltage_power(power: float, current: float) -> float:
    if current == 0:
        raise ValueError("Сила тока не может быть равна нулю.")
    return round(power / current, 2)

def calculate_voltage_ohm(resistance: float, current: float) -> float:
    return round(resistance * current, 2)

def calculate_power_and_work(voltage: float, current: float, time: float) -> tuple[float, float]:
    power = round(voltage * current, 2)
    work = round(power * time, 2)
    return power, work

def calculate_joule_heat(current: float, resistance: float, time: float) -> float:
    return round((current ** 2) * resistance * time, 2)
