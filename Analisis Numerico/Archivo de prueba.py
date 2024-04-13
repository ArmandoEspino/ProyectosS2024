def eliminacion_gaussiana(matriz):
    # Fase de eliminación
    n = len(matriz)
    for i in range(n):
        # Encuentra el pivote máximo
        max_index = i
        for j in range(i + 1, n):
            if abs(matriz[j][i]) > abs(matriz[max_index][i]):
                max_index = j
        
        # Intercambia la fila actual con la fila con el pivote máximo
        matriz[i], matriz[max_index] = matriz[max_index], matriz[i]
        
        # Hacer que el elemento de la diagonal sea igual a 1
        pivot = matriz[i][i]
        for j in range(i, n + 1):
            matriz[i][j] /= pivot
        
        # Hacer que los elementos debajo del pivote sean cero
        for j in range(i + 1, n):
            factor = matriz[j][i]
            for k in range(i, n + 1):
                matriz[j][k] -= factor * matriz[i][k]
        
        # Imprimir la matriz en cada iteración
        print("\nMatriz en la iteración", i+1)
        for fila in matriz:
            print(fila)
    
    # Fase de sustitución hacia atrás
    soluciones = [0] * n
    for i in range(n - 1, -1, -1):
        soluciones[i] = matriz[i][n]
        for j in range(i + 1, n):
            soluciones[i] -= matriz[i][j] * soluciones[j]
    
    return soluciones


def ingresar_matriz(filas, columnas):
    matriz = []
    print("Ingrese los elementos de la matriz separados por espacios, fila por fila:")
    for i in range(filas):
        fila = input(f"Ingrese los {columnas} elementos de la fila {i+1}: ").split()
        # Verificar si se han ingresado suficientes elementos
        if len(fila) != columnas:
            print("Error: Debe ingresar exactamente", columnas, "elementos por fila.")
            return None
        # Convertir los elementos a números (float) y agregar la fila a la matriz
        try:
            fila = [float(elemento) for elemento in fila]
            matriz.append(fila)
        except ValueError:
            print("Error: Todos los elementos deben ser números.")
            return None
    return matriz

def resolver_eliminacion_gaussiana():
    print("Has seleccionado Eliminación Gaussiana.")
    
    # Pedir al usuario las dimensiones de la matriz
    while True:
        try:
            filas = int(input("Ingrese el número de filas de la matriz: "))
            columnas = int(input("Ingrese el número de columnas de la matriz (debe ser una unidad mayor que el número de filas): "))
            if filas <= 0 or columnas <= 0 or columnas != filas + 1:
                raise ValueError("Las dimensiones de la matriz no cumplen con los requisitos.")
            break
        except ValueError as e:
            print("Error:", e)
    
    # Inicializar la matriz
    matriz = []
    
    # Pedir al usuario que ingrese los valores de la matriz
    print("Ingrese los elementos de la matriz:")
    for i in range(filas):
        fila = []
        for j in range(columnas):
            while True:
                try:
                    valor = float(input(f"Ingrese el elemento de la fila {i+1} y columna {j+1}: "))
                    fila.append(valor)
                    break
                except ValueError:
                    print("Error: Debe ingresar un valor numérico.")
        matriz.append(fila)
    
    # Mostrar la matriz ingresada por el usuario
    print("\nMatriz ingresada:")
    for fila in matriz:
        print(fila)
    
    # Resolver el sistema de ecuaciones mediante eliminación gaussiana
    soluciones = eliminacion_gaussiana(matriz)
    
    # Mostrar las soluciones
    print("\nSoluciones:")
    for i, solucion in enumerate(soluciones):
        print(f"x{i+1} =", solucion)


def metodo_biseccion(f, a, b, tol=1e-6, max_iter=100):
    # Verificar si f(a) y f(b) tienen signos opuestos
    if f(a) * f(b) >= 0:
        print("La función no cumple con el requisito de tener signos opuestos en los extremos del intervalo.")
        return None
    
    # Inicializar el contador de iteraciones
    iter_count = 0
    
    # Imprimir los detalles iniciales
    print(f"Iteración\tExtremo izquierdo\tExtremo derecho\tRaíz aproximada\t\tTolerancia")
    print("-------------------------------------------------------------------------------------")
    
    # Bucle principal del método de bisección
    while (b - a) / 2 > tol and iter_count < max_iter:
        c = (a + b) / 2  # Calcular el punto medio del intervalo
        if f(c) == 0:
            break  # La raíz fue encontrada exactamente
        elif f(c) * f(a) < 0:
            b = c  # La raíz está en el intervalo [a, c]
        else:
            a = c  # La raíz está en el intervalo [c, b]
        
        # Imprimir los detalles de la iteración actual
        print(f"{iter_count+1}\t\t{a:.6f}\t\t{b:.6f}\t\t{c:.6f}\t\t{(b-a)/2:.10f}")
        iter_count += 1
    
    # Calcular la aproximación de la raíz
    aproximacion_raiz = (a + b) / 2
    
    return aproximacion_raiz

def resolver_metodo_biseccion():
    print("Has seleccionado Método de Bisección.")
    
    # Solicitar al usuario que ingrese la función
    funcion_str = input("Ingrese la función para la cual desea encontrar la raíz (ej. 'x**2 - 4'): ")
    try:
        funcion = eval("lambda x: " + funcion_str)  # Convertir la cadena en una función
    except Exception as e:
        print("Error al definir la función:", e)
        return
    
    # Pedir al usuario los extremos del intervalo y la tolerancia
    while True:
        try:
            a = float(input("Ingrese el extremo izquierdo del intervalo: "))
            b = float(input("Ingrese el extremo derecho del intervalo: "))
            if a >= b:
                raise ValueError("El extremo izquierdo debe ser menor que el extremo derecho.")
            tol = float(input("Ingrese la tolerancia deseada: "))
            if tol <= 0:
                raise ValueError("La tolerancia debe ser un número positivo.")
            break
        except ValueError as e:
            print("Error:", e)
    
    # Verificar si f(a) y f(b) tienen signos opuestos en los extremos del intervalo
    if funcion(a) * funcion(b) >= 0:
        print("La función no cumple con el requisito de tener signos opuestos en los extremos del intervalo.")
        print(f"Valor de la función en el extremo izquierdo ({a}): {funcion(a)}")
        print(f"Valor de la función en el extremo derecho ({b}): {funcion(b)}")
        return
    
    # Resolver utilizando el método de bisección
    raiz = metodo_biseccion(funcion, a, b, tol)
    
    # Mostrar la aproximación de la raíz
    if raiz is not None:
        print("\nAproximación de la raíz:", raiz)
    else:
        print("\nNo se pudo encontrar una raíz dentro del intervalo especificado.")
        

def diferencias_divididas(x, y):
    n = len(x)
    coeficientes = [0] * n
    for i in range(n):
        coeficientes[i] = y[i]

    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coeficientes[i] = (coeficientes[i] - coeficientes[i - 1]) / (x[i] - x[i - j])

    return coeficientes

def evaluar_polinomio(x, coeficientes, valor):
    n = len(x)
    resultado = coeficientes[n - 1]
    for i in range(n - 2, -1, -1):
        resultado = resultado * (valor - x[i]) + coeficientes[i]
    return resultado

def interpolacion_diferencias_divididas():
    print("Has seleccionado Polinomio de Interpolacion con diferencias divididas de Newton.")
    # Pedir al usuario la información relacionada con los puntos
    while True:
        try:
            n = int(input("Ingrese el número de puntos: "))
            if n <= 0:
                raise ValueError("El número de puntos debe ser un entero positivo.")
            break
        except ValueError as e:
            print("Error:", e)

    x = []
    y = []
    for i in range(n):
        while True:
            try:
                punto_x = float(input("Ingrese el valor de x{}: ".format(i)))
                punto_y = float(input("Ingrese el valor de y{}: ".format(i)))
                x.append(punto_x)
                y.append(punto_y)
                break
            except ValueError:
                print("Error: Por favor, ingrese un número real válido.")

    # Pedir al usuario el valor a interpolar
    while True:
        try:
            valor_interpolar = float(input("Ingrese el valor a interpolar: "))
            break
        except ValueError:
            print("Error: Por favor, ingrese un número real válido.")

    # Calcular coeficientes
    coeficientes = diferencias_divididas(x, y)

    # Imprimir coeficientes
    print("Los coeficientes del polinomio interpolante son:")
    for i, coeficiente in enumerate(coeficientes):
        print("c{} = {:.6f}".format(i, coeficiente))

    # Evaluar el polinomio en el valor a interpolar
    resultado = evaluar_polinomio(x, coeficientes, valor_interpolar)

    print("El resultado de la interpolación en x =", valor_interpolar, "es y =", resultado)


def menu():
    while True:
        print("\nSeleccione una de las siguientes opciones:")
        print("1. Eliminación gaussiana")
        print("2. Método de Bisección")
        print("3. Polinomio de Interpolacion con diferencias divididas de Newton")
        print("4. ...")
        print("5. Cerrar el programa")
        
        opcion = input("Ingrese el número de la opción deseada: ")
        
        if opcion == "1":
            resolver_eliminacion_gaussiana()
        elif opcion == "2":
            resolver_metodo_biseccion()
        elif opcion == "3":
            interpolacion_diferencias_divididas()
        elif opcion == "5":
            print("Cerrando el programa...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    menu()
