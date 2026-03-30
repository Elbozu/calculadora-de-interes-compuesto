print("******************************************************************************")
print("********************* Calculadora de interes compuesto ***********************")
print("******************************************************************************\n")

inversion = float(input("Ingrese el monto que desea invertir: "))
tasa_anual = float(input("ingrese la tasa anual: "))
tiempo = int(input("Ingrese la cantidad de años: "))
aportaciones = float(input("coloque aportacion mensual extra: "))


capital_inicial = inversion #tuve que copiar el valor original porque no encontre otro modo de calcular las ganacias
calculo = tasa_anual / 100 #conversion a %


print("\n***************** Resultados ************************\n")

print(f"Inversion inicial: {inversion}")

for a in range(1, tiempo + 1):
    
  inversion = inversion + aportaciones * 12 #Aqui sumamos las aportaciones a la inversion inicial
  
  sub_total = inversion
    
  inversion = inversion * (1 + calculo) #Aqui el valor de inversion cambia y se convierte en (inversion * 1.la tasa que elegimos) ejem 1.5, 1.10 etc
  
  ganancias_anuales = inversion - sub_total
  
  ganancias_acumuladas = inversion - capital_inicial - (aportaciones * 12 * a) #Calcular ganancias acumuladas
  
  print(f"Año {a}:")
  print(f"Aportaciones del año: {aportaciones * 12}") #Las aportaciones que hicimos mensual
  print(f"Aportaciones totales acumuladas: {aportaciones * 12 * a}") #La cantidad de dinero de las aportaciones totales en cada año
  print(f"Total antes del interes: {sub_total:.2f}") #El monto al que se le aplicara el interes que elegimos
  print(f"Monto con el interes aplicado: {inversion:.2f}")#La cantidad que tendremos a fin de año ya con el interes aplicado
  print(f"Ganancias del año: {ganancias_anuales:.2f}") #Ganancias anuales
  print(f"Ganancias acumuladas: {ganancias_acumuladas:.2f}\n") #Ganancias acumuladas
  
  

