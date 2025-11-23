import re
from database import verificar_contraseña, hashear_contraseña

# Aquí vamos a ver qué tan chida está tu contraseña
# (O sea, si es segura o si te la adivinan en dos segundos)

def calcular_puntaje(contraseña):
    # Empezamos desde cero, hay que ganarse los puntos
    puntaje = 0
    
    # Si está larguita (8 o más), ya empezamos bien
    if len(contraseña) >= 8:
        puntaje += 20
        # print("¡Bien! Tiene buen tamaño.")
        
    # Si tiene numeritos, mejor
    if re.search(r"\d", contraseña):
        puntaje += 15
        # print("Con numeritos es más difícil de adivinar.")
        
    # Caracteres especiales (tipo !@#$), eso le da el toque pro
    if re.search(r"[ !#$%&'()*+,-./:;<=>?@[\]^_`{|}~" + r'"]', contraseña):
        puntaje += 25
        # print("¡Uff! Con esos símbolos nadie se mete.")
        
    # Mayúsculas para gritar seguridad
    if re.search(r"[A-Z]", contraseña):
        puntaje += 15
        
    # Minúsculas, porque el equilibrio es importante
    if re.search(r"[a-z]", contraseña):
        puntaje += 10
        
    return puntaje

def calcular_entropia(contraseña):
    import math
    # Calculamos la entropía de Shannon (bits de información)
    # Es matemáticas puras para saber qué tan impredecible es esto.
    
    if not contraseña:
        return 0
        
    # Determinamos el tamaño del "pool" de caracteres usados
    pool_size = 0
    if re.search(r"[0-9]", contraseña): pool_size += 10
    if re.search(r"[a-z]", contraseña): pool_size += 26
    if re.search(r"[A-Z]", contraseña): pool_size += 26
    if re.search(r"[^a-zA-Z0-9]", contraseña): pool_size += 32 # Símbolos aprox
    
    if pool_size == 0: return 0
    
    # Fórmula: Longitud * log2(pool_size)
    entropia = len(contraseña) * math.log2(pool_size)
    return round(entropia, 2)

def es_debil(hash_contraseña):
    # Checamos si está en la lista negra de database.py
    # Si está ahí, tache, no está chida.
    return verificar_contraseña(hash_contraseña)

def evaluar_password(contraseña):
    # Primero sacamos el hash para ver si no es de las comunes
    el_hash = hashear_contraseña(contraseña)
    
    # Si es débil, ni nos molestamos en contar puntos, es un cero rotundo (o bueno, avisamos)
    es_comun = es_debil(el_hash)
    
    puntaje = calcular_puntaje(contraseña)
    entropia = calcular_entropia(contraseña)
    
    return puntaje, es_comun, el_hash, entropia
