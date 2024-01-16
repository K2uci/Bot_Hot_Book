from config.Token import *
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import requests

"""
1-Crear una funcion para descargar los libros
2-Lograr traducir los libros
3-Lograr sacar la info de los libros por temas
"""

#Funcion para buscar todos los titutlos existentes
def search_title(cid,chose_page,selecc,page=1) -> list:
    dicc_res = []
    #Seleccionamos que es lo que busca el usuario 0 es busqueda por genero
    if selecc == 0:
        url = URLS_SEARCH_gen(chose_page,page)
    #Seleccionamos que es lo que busca el usuario 0 es busqueda por tema
    if selecc == 1:
        try:
            url = URL+files.themes_url()[chose_page-1]['url']
        except IndexError:
            return False
    #Hacemos la peticion a la pagina
    request = requests.get(url,headers=HEADERS)
    soup = BeautifulSoup(request.text,'html.parser')
    #Filtramos por la etiqueta h4
    alls = soup.find_all('h4')
    #Filtrado de respuestas para los nombres y autores
    for titles in alls:
        url = str(titles).split('href="/')[1].split('">')[0]
        title = str(titles).split('>')[2].replace('</a','')   
        autor = str(titles).split('>')[4].replace('</a','') 
        ans = {'title':title,'autor':autor,'url':url}
        dicc_res.append(ans)
    files.save_find(cid,dicc_res,page)
    return True
#Funcion orientada a los temas
def total_books(reques) -> list:
    #Preparamos la sopa 
    request = requests.get(URL,headers=HEADERS)
    soup = BeautifulSoup(request.text,'html.parser')
    alls = soup.find('div',id="menu")
    alls.at
    #Controlamos que hara esta funcion
    if reques == 1:
        #Filtramos los resultados por la pos 11 para generos
        gener = list(list(alls)[11])[1::2];total_books = []
        for i in gener:
            #Filtrado imposible de comentar jjjj
            total_books.append(str(i).split('(')[1].replace(')','').replace('</li>','').strip())
        #Retorna una lista con los totales de cada libros por temas
        return total_books	
    #Funcion para controlar la cantidad de libros en tiempo real
    if reques == 2:
        gener = list(list(alls)[-2]);actual_books = []
        for i in gener[1::2]:
            books = str(i).split('</a>')[1].split('</li>')[0].replace('(','').replace(')','').strip()
            actual_books.append(books)
        #Retorna una lista con los totales de cada libros por generos
        return actual_books
#Funcion para extraer y mostrar la informacion de los librps por generos    
def save_info_book(cid,reques) -> list:
    #Todo esto se ejecutara si es una seleccion por pegero
    #Cargo la url del libro que desea el usuario,la excepcion es por si la lista esta fuera de rango
    try:
        data = files.read_find(cid)[reques-1]
    except IndexError:
        return False
    reques = requests.get(URL+data['url'],headers=HEADERS)
    soup = BeautifulSoup(reques.text,'html.parser')
    #Variable para alamacenar los generos del libro
    gener_book = soup.find('div',class_='top_info').text.strip() 
    #Variable para la fecha del libro
    date_book = soup.find('div',class_='story_date').text.strip().replace('Report','')
    #Variable para almacenar la info del libro
    info_book = list(soup.find('div',class_='block_panel'))[2].text.strip()
    return gener_book,date_book,info_book,data['title'],data['autor'],data['url']

#Funcion para descargar el contenido de un libro con request
def dowload_book(cid,url) -> None:
    request = requests.get(URL+url)
    soup = BeautifulSoup(request.text,'html.parser')
    alls = soup.find_all('div',class_="block_panel")[1]
    texto = ''
    for tex in alls:
        #Si nos encontramos la etiqueta comentario se detiene el texto
        if str(type(tex)) == "<class 'bs4.element.Comment'>":
            break
        else:
            texto += tex.text
    with open(f'data/{cid}/book.doc','w') as file:file.write(texto)

