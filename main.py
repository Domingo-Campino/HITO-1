import sys
import os

# 1. FUNCIÓN PARA LEER TAREAS
def leer_tareas(ruta_archivo):
    tareas = []
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            for linea in f:
                linea = linea.strip()
                if not linea: continue
                
                # Separar por comas según los datos
                partes = linea.split(',') 
                if len(partes) >= 3:
                    tareas.append({
                        'id': partes[0].strip(),
                        'duracion': int(partes[1].strip()),
                        'categoria': partes[2].strip()
                    })
    except FileNotFoundError:
        print(f"Error: No se encontró {ruta_archivo}")
        sys.exit(1)
    return tareas

# 2. FUNCIÓN PARA LEER RECURSOS
def leer_recursos(ruta_archivo):
    recursos = {}
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            for linea in f:
                linea = linea.strip()
                if not linea: continue
                
                # Separar por comas según los datos
                partes = linea.split(',')
                r_id = partes[0].strip()
                categorias_soportadas = [c.strip() for c in partes[1:]]
                recursos[r_id] = categorias_soportadas
    except FileNotFoundError:
        print(f"Error: No se encontró {ruta_archivo}")
        sys.exit(1)
    return recursos

# 3. Algoritmo (planificación según el diagrama)
def planificar_ep(tareas, recursos):
    # Iniciar los tiempos de recurso en 0
    tiempo_recursos = {r_id: 0 for r_id in recursos}
    cronograma = []

    # Ordenar las tareas de mayor a menor duración
    tareas_ordenadas = sorted(tareas, key=lambda x: x['duracion'], reverse=True)

    # Bucle principal para asignar
    for tarea in tareas_ordenadas:
        t_id = tarea['id']
        t_duracion = tarea['duracion']
        t_categoria = tarea['categoria']

        # Filtrar los recursos compatibles con la categoría de la tarea
        recursos_compatibles = []
        for r_id, categorias in recursos.items():
            if t_categoria in categorias:
                recursos_compatibles.append(r_id)

        # Si no hay compatibles, se salta (por precaución)
        if not recursos_compatibles:
            continue

        # Seleccionar el recurso compatible que utilice menos tiempo
        mejor_recurso = min(recursos_compatibles, key=lambda r: tiempo_recursos[r])

        # Calcular tiempos
        tiempo_inicio = tiempo_recursos[mejor_recurso]
        tiempo_fin = tiempo_inicio + t_duracion

        # Guardar la asignación
        cronograma.append({
            'tarea': t_id,
            'recurso': mejor_recurso,
            'inicio': tiempo_inicio,
            'fin': tiempo_fin
        })

        # Actualizar la disponibilidad del recurso usado
        tiempo_recursos[mejor_recurso] = tiempo_fin

    return cronograma