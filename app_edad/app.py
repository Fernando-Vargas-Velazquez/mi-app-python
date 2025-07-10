from datetime import datetime

# Pedir nombre
nombre = input("Ingresa tu nombre: ")

# Pedir fecha de nacimiento
fecha_str = input("Ingresa tu fecha de nacimiento (DD/MM/YYYY): ")

# Calcular edad
fecha_nacimiento = datetime.strptime(fecha_str, "%d/%m/%Y")
fecha_actual = datetime.now()
edad = fecha_actual.year - fecha_nacimiento.year

# Ajustar si no ha cumplido años este año
if (fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
    edad -= 1

# Mostrar resultado
print(f"Hola {nombre}, tienes {edad} años")