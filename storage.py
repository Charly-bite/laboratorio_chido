import datetime

# Aquí guardamos todo lo que vamos encontrando
# (Como una bitácora de hacker, pero en buena onda)

contraseñas_encontradas = []     # Las que sí estaban en la lista negra (uy, qué mal)
contraseñas_no_encontradas = []  # Las que se salvaron (bien ahí)

def agregar_resultado(contraseña, puntaje, es_debil, el_hash):
    # Guardamos la fecha para saber cuándo pasó el crimen (broma)
    fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    dato = {
        "password": contraseña,
        "hash": el_hash,
        "puntaje": puntaje,
        "timestamp": fecha
    }
    
    if es_debil:
        contraseñas_encontradas.append(dato)
        # print("Guardada en la lista de la vergüenza (comunes).")
    else:
        contraseñas_no_encontradas.append(dato)
        # print("Guardada en la lista de las chidas.")

def mostrar_analizadas():
    print("\n--- Bitácora de Contraseñas Analizadas ---")
    
    print(f"\n[!] Contraseñas Débiles ({len(contraseñas_encontradas)}):")
    if not contraseñas_encontradas:
        print("   (Ninguna por ahora, ¡qué nivel!)")
    else:
        for item in contraseñas_encontradas:
            print(f"   - {item['password']} (Puntaje: {item['puntaje']}) -> Hash: {item['hash'][:10]}...")

    print(f"\n[+] Contraseñas Chidas ({len(contraseñas_no_encontradas)}):")
    if not contraseñas_no_encontradas:
        print("   (Ninguna todavía, échale ganas)")
    else:
        for item in contraseñas_no_encontradas:
            print(f"   - {item['password']} (Puntaje: {item['puntaje']}) -> Hash: {item['hash'][:10]}...")
    print("------------------------------------------\n")

def mostrar_estadisticas():
    total = len(contraseñas_encontradas) + len(contraseñas_no_encontradas)
    
    print("\n--- Estadísticas del Laboratorio ---")
    print(f"Total analizadas: {total}")
    
    if total > 0:
        # Promedio de las chidas
        if contraseñas_no_encontradas:
            suma_chidas = sum(d['puntaje'] for d in contraseñas_no_encontradas)
            promedio_chidas = suma_chidas / len(contraseñas_no_encontradas)
            print(f"Promedio de seguridad en las chidas: {promedio_chidas:.2f}")
        else:
            print("Promedio de seguridad en las chidas: N/A")
            
        print(f"Cantidad de débiles encontradas: {len(contraseñas_encontradas)}")
    else:
        print("Aún no hay datos para presumir.")
    print("------------------------------------\n")

def exportar_reporte(nombre_archivo="reporte_seguridad.txt"):
    try:
        with open(nombre_archivo, "w") as f:
            f.write("REPORTE DE LABORATORIO DE CONTRASEÑAS\n")
            f.write("=====================================\n\n")
            f.write(f"Fecha de corte: {datetime.datetime.now()}\n\n")
            
            f.write("CONTRASEÑAS DÉBILES ENCONTRADAS:\n")
            if contraseñas_encontradas:
                for item in contraseñas_encontradas:
                    f.write(f"- {item['password']} (Puntaje: {item['puntaje']})\n")
            else:
                f.write("(Ninguna, ¡excelente!)\n")
                
            f.write("\nCONTRASEÑAS SEGURAS ANALIZADAS:\n")
            if contraseñas_no_encontradas:
                for item in contraseñas_no_encontradas:
                    f.write(f"- {item['password']} (Puntaje: {item['puntaje']})\n")
            else:
                f.write("(Ninguna todavía)\n")
                
        print(f"\n[+] Reporte exportado exitosamente a '{nombre_archivo}'.")
        print("    (Llévalo con orgullo, o escóndelo si te fue mal jeje)")
    except Exception as e:
        print(f"\n[!] Ups, hubo un error al exportar: {e}")
