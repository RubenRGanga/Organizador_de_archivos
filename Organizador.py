import os
import shutil
import string

# Pide al usuario el directorio que quiere organizar
dir_path = input("Introduce la ruta del directorio que quieres organizar: ")

# Verifica que el directorio existe
if not os.path.exists(dir_path):
    print("El directorio no existe. Por favor, introduce una ruta válida.")
    exit()

# Obtiene la lista de archivos en el directorio
file_list = os.listdir(dir_path)
total_files = len(file_list)

# Inicializa un contador para los archivos procesados
processed_files = 0

# Navega a través del directorio
for filename in file_list:
    # Actualiza el contador de archivos procesados
    processed_files += 1

    # Calcula y muestra el porcentaje de progreso
    percentage = (processed_files / total_files) * 100
    print(f"({percentage:.2f}% completado)")

    # Obtén la primera letra del archivo
    first_letter = filename[0]

    # Si es un número o un símbolo, usa "#" como nombre de carpeta
    if first_letter.isdigit() or first_letter not in string.ascii_letters:
        folder_name = "#"
    else:
        # Si no, usa la primera letra en mayúscula como nombre de carpeta
        folder_name = first_letter.upper()

    # Crea el nombre de la nueva carpeta
    new_folder_path = os.path.join(dir_path, folder_name)

    # Ruta del archivo original
    original_file_path = os.path.join(dir_path, filename)

    # Crea la carpeta si no existe
    if not os.path.exists(new_folder_path):
        os.mkdir(new_folder_path)

    # Mueve el archivo a la nueva carpeta
    shutil.move(original_file_path, os.path.join(new_folder_path, filename))

print("Archivos organizados con éxito.")

