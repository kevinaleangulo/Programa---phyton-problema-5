recursos = [
    ["Carlos", 8, 9, 8, 10, 9],
    ["Ana", 7, 8, 7, 8, 7],
    ["Luis", 9, 10, 9, 8, 10],
    ["María", 6, 7, 8, 7, 6]
]
def calcular_jornada(recurso):
    nombre = recurso[0]
    horas = recurso[1:]

    total_horas = sum(horas)

    if total_horas > 40:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario Estándar"

    return nombre, total_horas, clasificacion

for recurso in recursos:
    nombre, total, clasificacion = calcular_jornada(recurso)

    print("Recurso:", nombre)
    print("Total de horas:", total)
    print("Clasificación:", clasificacion)
    print("-" * 30)
