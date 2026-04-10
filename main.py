import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"

resposta = requests.get(url)

# validacao da resposta
if resposta.status_code != 200:
    print(f"Erro ao acessar o site. Status code: {resposta.status_code}")
    raise SystemExit()

print("Conexão bem-sucedida!")

soup = BeautifulSoup(resposta.text, "html.parser")

print(soup.title)

# busca os livros da pagina principal
livros_html = soup.find_all("article", class_="product_pod")

# impressao encontrados
print(len(livros_html))