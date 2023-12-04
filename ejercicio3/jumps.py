def jump(num, step = 0, count = 0):
    # Caso base
    if step == num:
        return count
    # Recursividad
    elif step < 0:
        count = step * - 1
        step = 0
        return jump(num, step, count)

    elif step <= num / 2:
        step = step + (step + 1)
        count = count + 1
        return jump(num, step, count)
    
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