import shutil
import os
import requests
from scraper import get_url


def save_files():
    """
    Função que seleciona cada URL da lista retornada pela função get_url, baixa e salva os
    arquivos PDF em uma pasta compactada
    """
    urls = get_url()
    folder = "PDFs"
    path = os.path.join(os.getcwd(), folder)
    check = os.path.exists(
        os.path.join(os.getcwd(), "PDFs.zip")
    )  # checa se o arquivo já existe

    if check:
        print("\nO arquivo já existe no caminho especificado.\n")
        return True
    try:
        os.mkdir(path)
    except FileExistsError:
        print("A pasta que você tentou criar já existe")
        return True

    print("\nProcessando... Aguarde\n")
    for url in urls:
        file_name_start = url.rfind("/") + 1  # extrai o nome do arquivo da URL
        file_name = url[file_name_start:]
        response = requests.get(url, stream=True)

        if response.status_code == requests.codes.OK:
            with open(os.path.join(path, file_name), "wb") as new_file:
                new_file.write(response.content)
        else:
            response.raise_for_status()

    shutil.make_archive("PDFs", "zip", path)  # comprimindo os arquivos
    print("Pasta comprimida com sucesso!")
    print(f"Download finalizado. Arquivos salvos em {path}.zip\n")
    shutil.rmtree(path)  # removendo pasta descompactada


save_files()
