print("Bienvenido a la calculadora de tu salario mínimo")

while True:
    nombre = input("Ingrese el nombre del trabajador: ")

    # Validación salario mensual
    while True:
        try:
            salario_mensual = float(input("Ingrese el salario mensual: "))
            if salario_mensual < 0:
                print("Error: el salario no puede ser negativo")
                continue
            break
        except ValueError:
            print("Error: debe ingresar un número válido")

    # Validación días trabajados
    while True:
        try:
            dias_trabajados = int(input("Ingrese los días trabajados: "))
            if dias_trabajados < 0 or dias_trabajados > 30:
                print("Error: los días deben estar entre 0 y 30")
                continue
            break
        except ValueError:
            print("Error: debe ingresar un número entero")

    # Validación horas extras
    while True:
        try:
            horas_extras = int(input("Ingrese horas extras trabajadas: "))
            if horas_extras < 0:
                print("Error: las horas extras no pueden ser negativas")
                continue
            break
        except ValueError:
            print("Error: debe ingresar un número entero")

    # Validación días dominicales
    while True:
        try:
            dias_dominicales = int(input("Ingrese días dominicales o festivos trabajados: "))
            if dias_dominicales < 0:
                print("Error: los días dominicales no pueden ser negativos")
                continue
            break
        except ValueError:
            print("Error: debe ingresar un número entero")

    # Cálculos
    salario_diario = salario_mensual / 30
    valor_hora = salario_diario / 8
    salario_base = salario_diario * dias_trabajados

    # Auxilio transporte
    if salario_mensual <= 3501810:
        auxilio_transporte = 249095
    else:
        auxilio_transporte = 0

    # Bono por productividad
    if dias_trabajados > 20:
        bono = 100000
    else:
        bono = 0

    # Advertencia
    if dias_trabajados < 10:
        print("Advertencia: el trabajador laboró menos de 10 días.")

    # Horas extras y dominicales
    pago_horas_extras = valor_hora * 1.25 * horas_extras
    pago_dominical = salario_diario * 0.75 * dias_dominicales

    # Descuentos
    descuento_salud = salario_base * 0.04
    descuento_pension = salario_base * 0.04

    # Salario total
    salario_total = salario_base + auxilio_transporte + bono + pago_horas_extras + pago_dominical - descuento_salud - descuento_pension

    # Resultados
    print("\n===== RESULTADO =====")
    print("Trabajador:", nombre)
    print("Salario base:", round(salario_base))
    print("Auxilio transporte:", auxilio_transporte)
    print("Bono productividad:", bono)
    print("Pago horas extras:", round(pago_horas_extras))
    print("Pago dominical:", round(pago_dominical))
    print("Descuento salud:", round(descuento_salud))
    print("Descuento pensión:", round(descuento_pension))
    print("SALARIO TOTAL A PAGAR:", round(salario_total))

    opcion = input("\n¿Desea calcular otro salario? (si/no): ")
    if opcion.lower() == "no":
        print("Programa finalizado")
        break
           
           
           
           
           
           
           
            
        
      
          
      
      
