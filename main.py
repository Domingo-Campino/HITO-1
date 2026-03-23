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
