import os
import shutil
import datetime

def mover_arquivos(origem, destino, extensoes_permitidas):
    print("\nMovendo arquivos...")

    caminho_do_log = os.path.join(origem, "log_backup.txt")
    with open(caminho_do_log, "a", encoding="utf-8") as log:

        itens_origem = os.listdir(origem)

        for item in itens_origem:
            caminho_completo_item = os.path.join(origem, item)

            if os.path.isdir(caminho_completo_item):
                continue

            nome_item, extensao_item = os.path.splitext(item)

            if extensao_item in extensoes_permitidas:
                data_atual = datetime.datetime.now().strftime("%Y%m%d")
                pasta_backup = f"backup_{data_atual}"
                caminho_pasta_backup = os.path.join(destino, pasta_backup)

                if not os.path.exists(caminho_pasta_backup):
                    os.mkdir(caminho_pasta_backup)
                    log.write(f"INFO: Pasta de backup '{pasta_backup}' criada.\n")

                shutil.move(caminho_completo_item, caminho_pasta_backup)
                log.write(f"INFO: Arquivo '{item}' movido para a pasta '{pasta_backup}'.\n")