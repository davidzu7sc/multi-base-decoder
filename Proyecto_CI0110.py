''' Entregable #3: Programa en Python, Grupo#4
    Roger Fabricio Valverde Arias - C6N647
    Matthew Kinkelaar Fuentes - C6H469
    David Fabian Zúñiga Torres - C6Q167 '''



from tkinter import filedialog, Tk
import os 

# 1. Configuración del selector gráfico de archivos 
interfaz = Tk()
interfaz.withdraw() 

VERDE = '\033[92m'
ROJO = '\033[91m'
AZUL = '\033[94m'
RESET = '\033[0m'

print("Por favor, seleccione el archivo de texto a procesar...")
nombre_archivo = filedialog.askopenfilename(
    title="Seleccione el archivo codificado",
    filetypes=[("Texto", "*.txt"), ("Todos", "*.*")]
)

if not nombre_archivo:
    print(f"\n{ROJO}No se seleccionó ningún archivo. Fin del programa.{RESET}")
    exit()

mensaje_completo_lista = []

# 2. Apertura y procesamiento del archivo en modo lectura
try:
    with open(nombre_archivo, 'r', encoding='utf-8-sig') as archivo:
        for linea in archivo:
            
            # Omitir líneas completamente vacías
            if not linea.strip():
                continue
            
            # Partimos la línea por espacios en blanco inmediatamente
            elementos = linea.split()
            
            # Extraemos el indicador de base ("B02", "B03", "B05", "B16")
            indicador_base = elementos[0].strip()
            grupos_numericos = elementos[1:]
            
            # Asignación de la base numérica matemática
            if indicador_base == "B02":
                base_numerica = 2
            elif indicador_base == "B03":
                base_numerica = 3
            elif indicador_base == "B05":
                base_numerica = 5
            elif indicador_base == "B16":
                base_numerica = 16
            else:
                continue
            
            palabra_decodificada = ""
            
            # 3. Ciclo de conversión de los grupos de la línea actual
            for grupo in grupos_numericos:
                try:
                    valor_decimal = int(grupo, base_numerica)
                    
                    if valor_decimal >= 0 or valor_decimal <= 255:
                        palabra_decodificada += chr(valor_decimal)
                except ValueError:
                    print(f"\n{ROJO}Nota: El grupo '{grupo}' no pertenece a la base {base_numerica}.{RESET}")
            
            if palabra_decodificada:
                mensaje_completo_lista.append(palabra_decodificada)
                
except FileNotFoundError:
    print(f"{ROJO}Error: El archivo en la ruta '{nombre_archivo}' no existe.{RESET}")
    exit()

# 4. Unificar las palabras con un espacio intermedio    
mensaje_final = " ".join(mensaje_completo_lista)

print(f"\n{AZUL}--------------- MENSAJE DECODIFICADO ---------------{RESET}")
if mensaje_final:
    print(mensaje_final)
else:
    print("{ROJO}(No se pudo extraer texto válido){RESET}")
print(f"{AZUL}----------------------------------------------------{RESET}\n")

# 5. Preguntar y guardar el mensaje en un archivo
ruta_absoluta = os.path.abspath(nombre_archivo)
ultima_posicion = ruta_absoluta.rfind(chr(92)) + 1
ruta = ruta_absoluta[:ultima_posicion]

print("¿Deseas guardar el mensaje decodificado en un archivo de texto?")
guardar_archivo = input(f"Escribe ({VERDE}Sí{RESET} /{ROJO}No{RESET}): ").strip().upper()

if guardar_archivo == "SI" or guardar_archivo == "SÍ":

    with open(ruta + "Mensaje decodificado.txt", 'w') as arcivo_salida:
        arcivo_salida.write(mensaje_final)
        print(f"\n{VERDE}Se guardó el texto en el archivo: Mensaje decodificado.txt{RESET}")

else:
    print(f"\n{ROJO}No se guardó en ningún archivo el texto decodificado{RESET}")