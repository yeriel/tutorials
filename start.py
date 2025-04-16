import sys
import os

def main():
    # Verificar que se proporcione exactamente un argumento
    if len(sys.argv) != 2:
        print("Uso: python crear_proyecto.py <nombre_del_proyecto>")
        sys.exit(1)
    
    nombre_proyecto = sys.argv[1]
    
    # Crear la carpeta principal
    try:
        os.makedirs(nombre_proyecto)
    except FileExistsError:
        print(f"Error: La carpeta '{nombre_proyecto}' ya existe.")
        sys.exit(1)
    
    # Crear archivo README.md
    readme_path = os.path.join(nombre_proyecto, "README.md")
    with open(readme_path, "w") as f:
        f.write(f"# {nombre_proyecto}\n")
    
    print(f"Proyecto '{nombre_proyecto}' creado exitosamente con su README.md")

if __name__ == "__main__":
    main()
