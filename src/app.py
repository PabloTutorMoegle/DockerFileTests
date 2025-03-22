import os
import time
import sys
import threading

def animate_dockerfile():
    """Anima la palabra 'Dockerfile' en la terminal."""
    word = "Dockerfile"
    while not stop_animation:
        for i in range(len(word) + 1):
            print("\r" + word[:i], end="")
            time.sleep(0.2)  # Ajusta la velocidad de la animación aquí
        for i in range(len(word), -1, -1):
            print("\r" + word[:i], end="")
            time.sleep(0.2)  # Ajusta la velocidad de la animación aquí

def get_char():
    """Obtiene un carácter de la entrada estándar sin bloquear."""
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

stop_animation = False

def main():
    """Función principal para iniciar la animación y detectar la entrada del usuario."""
    animation_thread = threading.Thread(target=animate_dockerfile)
    animation_thread.daemon = True  # Permite que el programa termine aunque el hilo esté en ejecución
    animation_thread.start()

    print("Presiona cualquier tecla para detener la animación.")

    if sys.stdin.isatty(): #Check if the script is running in a tty
        get_char()  # Espera a que se presione una tecla
    else:
        input() #Use input() if not in a tty

    global stop_animation
    stop_animation = True
    animation_thread.join()  # Espera a que el hilo de animación termine
    print("\nAnimación detenida.")

if __name__ == "__main__":
    main()