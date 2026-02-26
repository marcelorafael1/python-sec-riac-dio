Projeto Prático: Simulação de Malware para Estudos de Segurança

Este repositório contém a implementação de scripts em Python desenvolvidos para fins estritamente educacionais, simulando o comportamento de Ransomware e Keylogger. O objetivo é compreender o funcionamento dessas ameaças para fortalecer as camadas de defesa e resposta a incidentes.

- Estrutura do Projeto
ransomware.py: Script de criptografia e descriptografia de arquivos.
keylogger.py: Script de captura de teclas com armazenamento local.
targets/: Diretório contendo arquivos de teste (txt) para validação.

1. Ransomware Simulado

- O script utiliza a biblioteca cryptography para realizar uma criptografia simétrica (Fernet).

Ação: Ele varre um diretório, criptografa o conteúdo e gera uma chave única.
Prevenção: Uso de backups offline (3-2-1), proteção contra modificação de arquivos em massa (FSRM) e soluções de EDR.

2. Keylogger Simulado

- Implementado com a biblioteca pynput, este script registra a atividade do teclado.

Ação: Captura as teclas e as salva em um arquivo log.txt.
Prevenção: Uso de teclados virtuais, bloqueio de portas SMTP não autorizadas e monitoramento de processos de background.

- Camadas de Defesa Recomendadas

Endpoint: Antivírus de Próxima Geração (NGAV).
Rede: Segmentação de rede e Firewall com inspeção profunda (DPI).
Humana: Conscientização sobre Phishing e Engenharia Social.
