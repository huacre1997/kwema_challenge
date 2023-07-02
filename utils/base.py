def calculate_bacteria(days, maturation_period, life_expectancy, reproduction_rate):
    # Definición de la función "calculate_bacteria" con los parámetros requeridos.

    initial_bacteria = [2, 3, 3, 1, 2] # Inicializar bacterias iniciales
    for _ in range(days):  # Bucle que se ejecuta "days" veces.
        counter = initial_bacteria.count(0)  # Contador de bacterias con contador interno con valor 0.
        for index,bc in enumerate(initial_bacteria):
            if bc > 0:
                # Si la bacteria es diferente a 0, la resta 1.
                initial_bacteria[index]-=1
            else:
                # Reemplaza el valor de 0 por la esperanza de vida de la bacteria.
                initial_bacteria[index]=life_expectancy
        if counter != 0:
            # Agregar nuevas bacterias maduras a la lista, según el periodo de maduración, la tasa de reproducción y el valor de counter.
            initial_bacteria.extend([maturation_period] * counter * reproduction_rate)

    return len(initial_bacteria)
