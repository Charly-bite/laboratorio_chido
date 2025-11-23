# Lista de contraseñas súper comunes (de esas que no deberías usar ni de broma)
contraseñas_comunes = [            
    "123456", "123456789", "12345", "qwerty", "password", "12345678", "111111", "123123", "1234567890", "1234567",
    "password", "123123", "987654321", "qwertyuiop", "asdfghjkl", "zxcvbnm", "1q2w3e4r5t6y", "admin", "1234", "000000",
    "555555", "666666", "777777", "888888", "999999", "121212", "112233", "654321", "123321", "1234567890",
    "pass1", "pass", "admin123", "admin1", "admin1234", "administrator", "root", "toor", "user", "guest",
    "welcome", "welcome1", "temp", "temp123", "1234567890a", "123456a", "password123", "iloveyou", "dragon",
    "monkey", "access", "michael", "jordan", "andrew", "daniel", "princess", "rockstar", "shadow", "sunshine",
    "freedom", "hacker", "trustno1", "win", "lose", "barcelona", "realmadrid", "liverpool", "arsenal", "chelsea",
    "manchester", "superman", "batman", "pokemon", "naruto", "minecraft", "fortnite", "roblox", "starwars",
    "hello", "killer", "master", "charlie", "mustang", "cookie", "flower", "soccer", "baseball", "football",
    "Aa123456", "Pass@123", "P@ssw0ord", "Aa@123456", "admintelecom", "Admin@123", "abcd1234", "letmein", "contraseña",
    # Contraseñas comunes en español
    "hola", "teamo", "teamo123", "madrid", "barcelona", "futbol", "familia", "carlos", "maria", "juan", 
    "alejandro", "america", "chivas", "mexico", "colombia", "argentina", "peru", "chile", "venezuela", "españa", 
    "amor", "bebe", "princesa", "corazon", "dios", "jesus", "fe", "paz", "sol", "luna", "estrella", 
    "cielo", "mar", "playa", "gato", "perro", "casa", "mama", "papa", "hermano", "hermana", "tio", 
    "tia", "abuelo", "abuela", "primo", "prima", "novio", "novia", "esposo", "esposa", "hijo", "hija", 
    "amigo", "amiga", "escuela", "trabajo", "dinero", "salud", "vida", "feliz", "bueno", "malo", 
    "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez",
    "micontraseña", "clave", "clave123", "usuario", "prueba", "sistema", "acceso", "seguridad"
]


# Aquí armamos el diccionario de hashes (para que nadie sepa qué escribiste jeje)
import hashlib

hashes_contraseñas = []
# Vamos a hashear todas esas claves facilitas
for contra in contraseñas_comunes:
    hash_hexa = hashlib.sha256(contra.encode()).hexdigest()
    hashes_contraseñas.append({"password": contra, "hash": hash_hexa})
    # Esto es solo para que veas que sí funciona, luego lo quitamos si quieres
    # print(f"Clave: {contra} => hash : {hash_hexa}")

# Función para encriptar una contraseña (oye, esto evita que cualquiera vea tu clave :))
def hashear_contraseña(contraseña):
    return hashlib.sha256(contraseña.encode()).hexdigest()

# Esta parte de abajo era del código viejo, pero la dejaremos comentada o la borraremos
# porque la lógica principal va a estar en password_lab.py
# Pero dejaremos las funciones útiles aquí para que las usen los demás.

# Función para pedir una contraseña (esto se usará en el menú principal)
def pedir_contraseña_teclado():
    contraseña = input("Ingresa una contraseña para verificar si está chida: ")
    contraseña_hash = hashear_contraseña(contraseña)
    return contraseña, contraseña_hash

# Checamos si el hash existe en nuestra lista negra
def verificar_contraseña(contraseña_hash):
    for entrada in hashes_contraseñas:
        if entrada["hash"] == contraseña_hash:
            return True
    return False

