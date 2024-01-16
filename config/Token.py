from scripts.Files import *
#from scripts.Driver import *
#from scripts.Traductor_Google import *
import telebot
#Token del Bot actual
token = '6819418638:AAEJRUAItiUPixtt9N-T5TwMDkfqc5POsXc'

#Mi ID actual de telegram
MY_ID = '5170682276'

#Cabezeras definidas para poder navegar con requests
HEADERS = {"user-agent":"Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0",
           "Accept-Language":"es-419,es;q=0.9"
           }

#Principal fuente de usqueda
URL = 'https://www.sexstories.com/'

#Funcion para buscar urls por generos
def URLS_SEARCH_gen(ques,page):
    if ques == 1:
        #Url de los libros de diarios
        URL_diarios = f'https://www.sexstories.com/genres/5/Diary/s-rate/p-{page}'
        return URL_diarios
    if ques == 2:
        #Url de los libros de Ensayos
        URL_ensayos = f'https://www.sexstories.com/genres/6/Essay/s-rate/p-{page}'
        return URL_ensayos
    if ques == 3:
        #Url de los libros de Fantasmas
        URL_fantasmas = f'https://www.sexstories.com/genres/7/Fantasm/s-rate/p-{page}'
        return URL_fantasmas
    if ques == 4:
        #Url de los libros de Fantasticos
        URL_fantasticos = f'https://www.sexstories.com/genres/8/Fantastic/s-rate/p-{page}'
        return URL_fantasticos
    if ques == 5:
        #Url de los libros de Fantasia
        URL_fantasia = f'https://www.sexstories.com/genres/9/Fantasy/s-rate/p-{page}'
        return URL_fantasia
    if ques == 6:
        #Url de los libros de Ficcion
        URL_ficcion = f'https://www.sexstories.com/genres/1/Fiction/s-rate/p-{page}'
        return URL_ficcion
    if ques == 7:
        #Url de los libros de Informativos
        URL_informativos = f'https://www.sexstories.com/genres/10/Information/s-rate/p-{page}'
        return URL_informativos
    if ques == 8:
        #Url de los libros de Nuevos
        URL_nuevos = f'https://www.sexstories.com/genres/11/News/s-rate/p-{page}'
        return URL_nuevos
    if ques == 9:
        #Url de los libros de Poemas
        URL_poemas = f'https://www.sexstories.com/genres/3/Poem/s-rate/p-{page}'
        return URL_poemas
    if ques == 10:
        #Url de los libros de Ciencia Ficcion
        URL_ciencia = f'https://www.sexstories.com/genres/12/Science-Fiction/s-rate/p-{page}'
        return URL_ciencia
    if ques == 11:
        #Url de los libros de Bromas Sexuales
        URL_bromas = f'https://www.sexstories.com/genres/2/Sex+Joke/s-rate/p-{page}'
        return URL_bromas
    if ques == 12:
        #Url de los libros de Historia real
        URL_real = f'https://www.sexstories.com/genres/13/True+Story/s-rate/p-{page}'
        return URL_real

#Funcion para buscar urls por raking
def URLS_SEARCH_rank(ques):
    if ques == 1:
        #Url de los mejores en ultimos 30 dias
        URL_top_30 = 'https://www.sexstories.com/toplists/bests30d'
        return URL_top_30
    if ques == 2:
        #Url de historias mejor valoradas
        URL_top = 'https://www.sexstories.com/toplists/bests'
        return URL_top
    if ques == 3:
        #Url de historias peor valoradas
        URL_low = 'https://www.sexstories.com/toplists/lowrated'
        return URL_low
    if ques == 4:
        #Url de las ultimas actualizaciones 
        URL_last = 'https://www.sexstories.com/toplists/last'
        return URL_last
    
#Instancia del bot en telegram
bot = telebot.TeleBot(token)

#Instancia de la clase files
files = Files()

#Instaciamos la clase driver
#Firefox = Driver()
#driver = Firefox.run_firefox()

#Instanciamos la clase traductor
#traductor = Traductor_Google()


#' <span class="tg-spoiler">Hola</span>'
    #Funcion para realizar scroll en la pagina
    #driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')