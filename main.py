import shutil
import os
import requests
from scraper import getURL


def saveFiles():  # esta função irá pegar os links da função anterior e salvar os arquivos em si
    urls = getURL()
    folder = "PDFs"
    path = os.path.join(os.getcwd(), folder)

    try:
        os.mkdir(path, mode=0o666)
    except FileExistsError:
        print("A pasta que você tentou criar já existe")

    for url in urls:
        file_name_start = url.rfind("/") + 1
        file_name = url[file_name_start:]
        response = requests.get(url, stream=True)

        if response.status_code == requests.codes.OK:
            with open(os.path.join(path, file_name), "wb") as new_file:
                new_file.write(response.content)
        else:
            response.raise_for_status()
    print(f"Download finalizado. Arquivos salvos em \033[31m{path}\033[m")

    anexo1 = os.path.join(
        path, "Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536.pdf"
    )

    shutil.make_archive("PDFs", "zip", path)  # compress the folder
    print("Pasta comprimida com sucesso!")
    shutil.rmtree(path)  # removendo pasta descompactada


saveFiles()
