print ("bienvenido a la calculadora de tu salario minimo")
nombre= input("ingrese el nombre del trabajador:")
salario_mensual= float(input("ingrese el salario mensual:"))
dias_trabajados=int(input("ingrese los dias trabajados:"))
horas_extras=int(input("ingrese horas extras trabajadas:"))
dias_dominicales=int(input(" ingrese dias dominicales o festivos trabajados:"))

while True:
      
       if dias_trabajados > 30:
          print("Error: no se puede trabajar mas de 30 dias en un mes")
          continue
       if dias_trabajados < 0:
          print("Error: los dias no pueden ser negativos")
          continue
          break 
          
       salario_diario = salario_mensual /30
       valor_hora = salario_diario / 8
      
       salario_base= salario_diario * dias_trabajados
      
       if salario_mensual <= 3501810:
          auxilio_transporte = 249095
          
       else:
          auxilio_transporte = 0
       if dias_trabajados > 20:
           bono = 100000
       else:
           bono = 0
           
       if dias_trabajados < 10:
           print("advertencia: el trabajador laboro menos de 10 dias")
           pago_horas_extras = valor_hora + 1.25 * horas_extras
           pago_dominical = salario_diario + 0.75 * dias_dominicales
           
           descuento_salud = salario_base * 0.04
           descuento_pension = salario_base * 0.04
           
           salario_total= salario_base + auxilio_transporte + bono + pago_horas_extras + pago_dominical - descuento_salud - descuento_pension
           
           print("\n= RESULTADO=")
           print("trabajador:",nombre)
           print("salario base:", round(salario_base))
           print("Auxilio de transporte:", auxilio_transporte)
           print("Bono productividad:", bono)
           print("pago horas extras:", round(pago_horas_extras))
           print("pago dominicales:", round( pago_dominical))
           print("descuento salud:", round( descuento_salud))
           print("descuento pension:", round(descuento_pension))
           print(" SALARIO TOTAL A PAGAR:",round(salario_total))
           
           opcion = input("\n¿ desea calcular otro salario? (si/no): ")
           
           if opcion.lower() == "no":
               print("programa finalizado")
               break