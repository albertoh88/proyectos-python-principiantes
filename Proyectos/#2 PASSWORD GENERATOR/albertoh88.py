import secrets
import pyperclip as pc

def generar_contrasena(longitud=16, usar_letras_up=True, usar_letras_down=True,
                       usar_numeros=True, usar_caracteres=True, copiar_portapapeles=True):
    """
    Genera una contraseña segura y opcionalmente la copia al portapapeles.

    Parámetros:
    - longitud: int, longitud de la contraseña (mínimo recomendado 8)
    - usar_letras_up: bool, incluir letras mayúsculas
    - usar_letras_down: bool, incluir letras minúsculas
    - usar_numeros: bool, incluir números
    - usar_caracteres: bool, incluir caracteres especiales
    - copiar_portapapeles: bool, si True copia la contraseña al portapapeles

    Retorna:
    - str: contraseña generada
    """
    if longitud < 8:
        raise ValueError("La longitud mínima recomendada es 8")

    letras_down = 'abcdefghijklmnopqrstuvwxyz'
    letras_up = letras_down.upper()
    numeros = '1234567890'
    especiales = '#$%&()*+,-./:;<=>?@[]^_`{|}~'

    caracteres_posibles = ''
    if usar_letras_up:
        caracteres_posibles += letras_up
    if usar_letras_down:
        caracteres_posibles += letras_down
    if usar_numeros:
        caracteres_posibles += numeros
    if usar_caracteres:
        caracteres_posibles += especiales
    if not caracteres_posibles:
        caracteres_posibles = letras_up + letras_down + numeros + especiales

    contrasena = ''.join(secrets.choice(caracteres_posibles) for _ in range(longitud))

    if copiar_portapapeles:
        pc.copy(contrasena)

    return contrasena


# EJEMPLO DE USO
if __name__ == "__main__":
    pwd = generar_contrasena(longitud=20, usar_caracteres=True)
    print("Contraseña generada:", pwd)
