import tkinter as tk
import subprocess
from tkinter import messagebox, simpledialog
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lexer import ruby_lexer  
from lexer.log_lexico import analizar_y_log
from parser.log_sintactico import analizar_sintactico_y_log
from parser.ruby_parser import construir_parser

# Importar analizador semántico para ejecutarlo desde la GUI
from semantic.ruby_semantico import RubySemanticAnalyzer
from semantic.logg_semantico import agregar_error, guardar_log


#  FUNCION PARA CAMBIAR VENTANAS
ventanas = {}

def mostrar_ventana(nombre):
    # Crear la ventana si no existe (lazy loading)
    if nombre not in ventanas:
        if nombre == "ventana2":
            crear_ventana2()
        elif nombre == "ventana3":
            crear_ventana3()
        elif nombre == "ventana4":
            crear_ventana4()
        elif nombre == "ventana5":
            crear_ventana5()
    
    # Ocultar todas las ventanas
    for v in ventanas.values():
        v.withdraw()
    # Mostrar la ventana solicitada
    ventanas[nombre].deiconify()


def show_result_window(title: str, content: str, error: bool = False):
    """
    Muestra una ventana modal con un Text y scrollbar para resultados largos.
    - `title`: título de la ventana
    - `content`: texto a mostrar
    - `error`: si True, el fondo del Text será claro y se usará `showerror` estilo (solo para semántica visual)
    """
    win = tk.Toplevel(ventana1)
    win.title(title)
    win.geometry("700x400")

    frame = tk.Frame(win)
    frame.pack(fill=tk.BOTH, expand=True)

    text = tk.Text(frame, wrap=tk.NONE)
    text.insert("1.0", content)
    text.config(state=tk.DISABLED)
    text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    vscroll = tk.Scrollbar(frame, orient=tk.VERTICAL, command=text.yview)
    vscroll.pack(side=tk.RIGHT, fill=tk.Y)
    text['yscrollcommand'] = vscroll.set

    hscroll = tk.Scrollbar(win, orient=tk.HORIZONTAL, command=text.xview)
    hscroll.pack(side=tk.BOTTOM, fill=tk.X)
    text['xscrollcommand'] = hscroll.set

    # Botón para cerrar
    btn = tk.Button(win, text="Cerrar", command=win.destroy)
    btn.pack(pady=6)


ventana1 = tk.Tk()
ventana1.title("Analizador de Ruby")
ventana1.geometry("400x400")

frame1 = tk.Frame(ventana1)
frame1.pack(expand=True)

tk.Label(frame1, text="Bienvenido al analizador de Ruby", font=("Arial", 16)).pack(pady=20)

texto = (
    "Este es un programa desarrollado por el grupo MonkeyDevs, que permitirá hacer un análisis "
    "al lenguaje Ruby, de forma sintáctica, léxica y semántica."
)

tk.Label(frame1, text=texto, wraplength=350, justify="center").pack(pady=20)

tk.Button(
    ventana1,
    text="Empecemos",
    command=lambda: mostrar_ventana("ventana2")
).pack(pady=20)

ventanas["ventana1"] = ventana1


# VENTANA 2 - FUNCIÓN FACTORY
def crear_ventana2():
    ventana2 = tk.Toplevel(ventana1)
    ventana2.title("Menú Principal")
    ventana2.geometry("400x350")
    ventana2.withdraw()

    frame2 = tk.Frame(ventana2)
    frame2.pack(expand=True)

    tk.Label(frame2, text="Menú del Analizador Ruby", font=("Arial", 18, "bold")).pack(pady=20)

    tk.Button(frame2, text="Análisis Léxico", width=20, height=2,
              command=lambda: mostrar_ventana("ventana3")).pack(pady=10)

    tk.Button(frame2, text="Análisis Sintáctico", width=20, height=2,
              command=lambda: mostrar_ventana("ventana4")).pack(pady=10)

    tk.Button(frame2, text="Análisis Semántico", width=20, height=2,
              command=lambda: mostrar_ventana("ventana5")).pack(pady=10)

    tk.Button(frame2, text="Volver", command=lambda: mostrar_ventana("ventana1")).pack(pady=20)

    ventanas["ventana2"] = ventana2


# VENTANA 3 - LEXICO - FUNCIÓN FACTORY
def crear_ventana3():
    ventana3 = tk.Toplevel(ventana1)
    ventana3.title("Análisis Léxico")
    ventana3.geometry("500x400")
    ventana3.withdraw()

    frame3 = tk.Frame(ventana3)
    frame3.pack(expand=True)

    tk.Label(frame3, text="Analizador Léxico", font=("Arial", 18, "bold")).pack(pady=20)

    entrada_lexico = tk.Text(frame3, width=60, height=10)
    entrada_lexico.pack(pady=10)

    def analizar_lexico():
        codigo = entrada_lexico.get("1.0", tk.END)  # Obtiene el texto del Text widget
        
        if not codigo.strip():
            messagebox.showwarning("Aviso", "Por favor ingresa código para analizar")
            return
        
        # Pedir nombre de usuario
        usuario = simpledialog.askstring("Usuario", "Ingresa tu nombre de usuario:")
        if usuario is None or usuario.strip() == "":
            messagebox.showwarning("Aviso", "Debes ingresar un nombre de usuario")
            return
        
        usuario = usuario.strip()

        # Ejecutar análisis léxico y guardar log
        try:
            from lexer.log_lexico import analizar_y_log
            resultados, ruta_log = analizar_y_log(codigo, usuario)
            
            if resultados:
                contenido = "\n".join(resultados)
            else:
                contenido = "No se encontraron tokens"

            show_result_window("Resultado - Léxico", contenido, error=False)
        except Exception as e:
            messagebox.showerror("Error", f"Error al ejecutar análisis léxico:\n{str(e)}")

    tk.Button(frame3, text="Analizar", width=15, height=2, command=analizar_lexico).pack(pady=20)
    tk.Button(frame3, text="Volver al menú", command=lambda: mostrar_ventana("ventana2")).pack()

    ventanas["ventana3"] = ventana3


#  VENTANA 4 - SINTACTICO - FUNCIÓN FACTORY
def crear_ventana4():
    ventana4 = tk.Toplevel(ventana1)
    ventana4.title("Analizador Sintáctico")
    ventana4.geometry("500x400")
    ventana4.withdraw()

    frame4 = tk.Frame(ventana4)
    frame4.pack(expand=True)

    tk.Label(frame4, text="Analizador Sintáctico", font=("Arial", 18, "bold")).pack(pady=20)

    entrada_sintactico = tk.Text(frame4, width=50, height=10)
    entrada_sintactico.pack(pady=10)

    def ejecutar_sintactico():
        codigo = entrada_sintactico.get("1.0", tk.END).strip()
        if codigo == "":
            messagebox.showwarning("Aviso", "Escribe algo para analizar")
            return
        
        # Pedir nombre de usuario
        usuario = simpledialog.askstring("Usuario", "Ingresa tu nombre de usuario:")
        if usuario is None or usuario.strip() == "":
            messagebox.showwarning("Aviso", "Debes ingresar un nombre de usuario")
            return
        
        usuario = usuario.strip()
        
        try:
            # Generar log llamando a analizar_sintactico_y_log
            ruta_log = analizar_sintactico_y_log(codigo, usuario)
            
            # Leer el archivo de log
            try:
                with open(ruta_log, "r", encoding="utf-8") as f:
                    contenido = f.read()
            except Exception:
                contenido = f"Análisis completado.\nNo se pudo leer el archivo de log en:\n{ruta_log}"
            
            show_result_window("Resultado - Sintáctico", contenido)
        except Exception as e:
            messagebox.showerror("Error de sintaxis", f"Ocurrió un error al ejecutar el analizador sintáctico:\n{str(e)}")

    tk.Button(frame4, text="Analizar", width=20, height=2, command=ejecutar_sintactico).pack(pady=20)
    tk.Button(frame4, text="Volver al menú", command=lambda: mostrar_ventana("ventana2")).pack()

    ventanas["ventana4"] = ventana4


# -------------------- VENTANA 5 - SEMANTICO - FUNCIÓN FACTORY --------------------
def crear_ventana5():
    ventana5 = tk.Toplevel(ventana1)
    ventana5.title("Analizador Semántico")
    ventana5.geometry("500x400")
    ventana5.withdraw()

    frame5 = tk.Frame(ventana5)
    frame5.pack(expand=True)

    tk.Label(frame5, text="Analizador Semántico", font=("Arial", 18, "bold")).pack(pady=20)

    entrada_semantico = tk.Text(frame5, width=50, height=10)
    entrada_semantico.pack(pady=10)

    def ejecutar_analisis_semantico():
        codigo = entrada_semantico.get("1.0", tk.END).strip()

        if codigo == "":
            messagebox.showwarning("Aviso", "No hay código para analizar")
            return

        # Pedir nombre de usuario
        usuario = simpledialog.askstring("Usuario", "Ingresa tu nombre de usuario:")
        if usuario is None or usuario.strip() == "":
            messagebox.showwarning("Aviso", "Debes ingresar un nombre de usuario")
            return
        
        usuario = usuario.strip()

        with open("codigo_temp.rb", "w", encoding="utf-8") as f:
            f.write(codigo)

        try:
            # Ejecutar el analizador semántico directamente en este proceso
            analizador = RubySemanticAnalyzer()
            errores = analizador.analizar("codigo_temp.rb")

            # Llenar el logger de semántica (para guardar archivo) y guardar el log
            for err in errores:
                agregar_error(err)

            guardar_log(usuario)

            # Preparar mensaje para el usuario y mostrar con el mismo formato
            if errores:
                contenido = "ERRORES SEMÁNTICOS DETECTADOS:\n" + "\n".join(errores)
                show_result_window("Resultado - Semántico", contenido, error=True)
            else:
                contenido = "✔️ No se encontraron errores semánticos."
                show_result_window("Resultado - Semántico", contenido, error=False)
        except:
            messagebox.showerror("Error", "Ocurrió un error al ejecutar el análisis semántico.")

    tk.Button(frame5, text="Analizar", width=20, height=2, command=ejecutar_analisis_semantico).pack(pady=20)
    tk.Button(frame5, text="Volver al menú", command=lambda: mostrar_ventana("ventana2")).pack()

    ventanas["ventana5"] = ventana5


# -------------------- INICIAR APP --------------------
ventana1.mainloop()


