from evaluator import evaluar_password
from storage import agregar_resultado, mostrar_analizadas, mostrar_estadisticas, exportar_reporte
from generator import generar_contraseña

# ¡Hola! Este es el cerebro de la operación.
# Aquí juntamos todo para que puedas probar tus contraseñas.

def bienvenida():
    print("\n" + "="*50)
    print("      LABORATORIO DE CONTRASEÑAS 'EL HACKER AMABLE'")
    print("="*50)
    print("¡Qué onda! Bienvenido a tu laboratorio de seguridad.")
    print("Aquí vamos a ver si tus contraseñas aguantan o si dan risa.")
    print("Recuerda: ¡La seguridad es lo primero, pero no tiene que ser aburrida!")
    print("="*50 + "\n")

def menu_principal():
    while True:
        print("\n¿Qué quieres hacer hoy?")
        print("1. Probar una contraseña (a ver qué tan chida es)")
        print("2. Ver el historial de lo que hemos probado")
        print("3. Ver estadísticas (números y esas cosas)")
        print("4. Generar una contraseña segura (para que no pienses tanto)")
        print("5. Exportar reporte (para llevar)")
        print("6. Salir (ir a tomar un café)")
        
        opcion = input("\nElige una opción (1-6): ")
        
        if opcion == "1":
            contraseña = input("\nA ver, échale la contraseña (tranqui, no la voy a robar): ")
            if not contraseña:
                print("¡Oye! No escribiste nada. Inténtalo de nuevo.")
                continue
                
            puntaje, es_comun, el_hash, entropia = evaluar_password(contraseña)
            
            print("\n" + "-"*30)
            print(f"Análisis para: {contraseña}")
            if es_comun:
                print("¡ALERTA! Esta contraseña es súper común. ¡Cámbiala ya!")
                print("Puntaje: 0 (Directo al suelo por ser común)")
                puntaje = 0 # Castigo máximo
            else:
                print(f"Puntaje de seguridad: {puntaje}/85")
                print(f"Entropía: {entropia} bits (Ciencia pura, amigo)")
                
                if puntaje < 40:
                    print("Mmm... está medio débil. Ponle más ganas.")
                elif puntaje < 70:
                    print("Va mejorando, pero puede estar más chida.")
                else:
                    print("¡Eso es! Una contraseña digna de un pro.")
            print("-"*30)
            
            agregar_resultado(contraseña, puntaje, es_comun, el_hash)
            
        elif opcion == "2":
            mostrar_analizadas()
            
        elif opcion == "3":
            mostrar_estadisticas()
            
        elif opcion == "4":
            print("\nGenerando una contraseña bien potente...")
            nueva_pass = generar_contraseña()
            print(f"Aquí tienes: {nueva_pass}")
            print("¡Úsala sabiamente!")
            
        elif opcion == "5":
            exportar_reporte()
            
        elif opcion == "6":
            print("\n¡Sale pues! Cuida tus contraseñas y nos vemos luego.")
            print("Cerrando el laboratorio...")
            break
            
        else:
            print("\nEsa opción no existe, carnal. Intenta con 1, 2, 3, 4, 5 o 6.")

if __name__ == "__main__":
    bienvenida()
    menu_principal()
