from urllib.request import urlopen
from urllib.error import HTTPError, URLError
import requests
from bs4 import BeautifulSoup
import re


def get_content(url):
    """
    Esta função irá acessar a url requisitada e retornar todo o conteúdo da página
    """
    try:
        page = urlopen(url)
    except HTTPError:
        print(
            "\033[31mHouve um erro ao obter a página. Por favor, verifique a URL fornecida.\033[m"
        )
        return False
    except URLError:
        print(
            "\033[31mO servidor não foi encontrado. Verifique se a URL está correta.\033[m"
        )
        return False
    try:
        bs = BeautifulSoup(page.read(), "lxml")
        content = bs
    except AttributeError:
        print("\033[31mA tag não foi encontrada.\033[m")
        return False
    return content


def get_url():
    """
    Esta função irá pegar o conteúdo da página da função anterior, filtrar e salvar
    as URLs alvo em uma lista
    """
    pdfs = []
    content = get_content(
        "https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/o-que-e-o-rol-de-procedimentos-e-evento-em-saude"
    )

    if content == None:
        print("O conteudo não foi encontrado")
        return None

    for link in content.find_all("a", attrs={"href": re.compile("^https://")}):
        filter = link.get("href")
        if "pdf" in filter and "Anexo" in link.text:
            pdfs.append(filter)
    return pdfs
