import random
import string

# Aquí cocinamos contraseñas frescas y crujientes
# (Garantizadas para no ser "123456")

def generar_contraseña(longitud=12, incluir_todo=True):
    if longitud < 8:
        print("Oye, 8 caracteres es lo mínimo para que valga la pena. Ajustando a 8...")
        longitud = 8
        
    # Ingredientes para la receta
    letras_min = string.ascii_lowercase
    letras_may = string.ascii_uppercase
    numeros = string.digits
    simbolos = "!@#$%^&*()-_=+[]{}|;:,.<>?"
    
    if incluir_todo:
        # Aseguramos que tenga al menos uno de cada uno
        contraseña = [
            random.choice(letras_min),
            random.choice(letras_may),
            random.choice(numeros),
            random.choice(simbolos)
        ]
        
        # El resto lo rellenamos al azar con todo mezclado
        todos_los_caracteres = letras_min + letras_may + numeros + simbolos
        for _ in range(longitud - 4):
            contraseña.append(random.choice(todos_los_caracteres))
            
        # Revolvemos bien para que no quede predecible
        random.shuffle(contraseña)
        
        return "".join(contraseña)
    else:
        # Versión "light" (solo letras y números)
        caracteres = letras_min + letras_may + numeros
        return "".join(random.choice(caracteres) for _ in range(longitud))
