def jump(num, step = 0, count = 0):
    """
    Recursive function that returns the required steps to reach an specific X number.
    The only movements allowed are:
        y + k, where y is the actual position and k the immediate next number
        y - 1, where y is the actual position

    Inputs:
        - num (int): the objetive number to reach
        - step (int): the actual position
        - count (int): the count of steps that the program has taken so far
    
    Outputs:
        - count (int): the count of steps that the program took to reach the objective
    """
    # Caso base
    if step == num:
        return count
    
    # Recursividad
    # If the initial steps are negative
    elif step < 0:
        count = step * - 1
        step = 0
        return jump(num, step, count)

    # If the actual step is less than the half of the objective
    elif step <= num / 2:
        step = step + (step + 1)
        count = count + 1
        return jump(num, step, count)
    
    # If the actual step is higher than the half of the objective
    else:
        step = step - 1
        count = count + 1
        return jump(num, step, count)
    
number = int(input("Ingrese un numero entre el 1 y 106: "))
start = int(input("Ingrese el punto de origen: "))
if number < 1 or number > 106:
    print("Numero fuera de rango")
else:
    print(jump(number, start, 0))