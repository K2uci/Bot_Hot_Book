from config.Token import *
from scripts.Scrap import *
from telebot.types import InlineKeyboardMarkup,InlineKeyboardButton
import time

"""
Completar
2-terminar la funcion raking
"""

#Funcio para mostrar la seleccion del libro al usuario y interactuar
def show_info_book_ans(cid,data_book):
    #Comprobamos si el libro tiene informacion,sino tiene le ponemos
    if len(str(data_book[2])) < 2:
        inff = False
    else:
        inff = True
    markup = InlineKeyboardMarkup(row_width=2)
    byes = InlineKeyboardButton('🔥Descargar🔥',callback_data=f'{data_book[5]}')
    bno = InlineKeyboardButton('❄️Pasar❄️',callback_data='close')
    markup.add(bno,byes)
    info = f'<b>Titulo:</b>  {data_book[3]}  \n<b>Autor:</b>  {data_book[4]}\n<b>Genero:</b>  {data_book[0]}\n'
    info += f'<b>Fecha:</b>  {data_book[1]}  \n<b>Info: </b> {data_book[2] if inff else "<b>N/A</b>"}'
    #Execpcion no controlada,no se porque sale
    try:
        bot.send_message(cid,info,parse_mode='html',reply_markup=markup)
    except:
        info = f'<b>📕!!Muy buena eleccion,pero todavia no hemos conseguido los '
        info += f'derechos de autor por este libro,en futuras actualiaciones '
        info += f'estara disponible de forma gratuita!!📕</b>'
        msg = bot.send_message(cid,info,parse_mode='html')
        time.sleep(5)
        bot.delete_message(cid,msg.message_id)

#Funcion para mostrar todos los temas 
def show_find_themes(cid,msg_old=None):
    #Cargamos la pagina actual de temas
    page = files.read_page_temas(cid)
    markup = InlineKeyboardMarkup(row_width=5)
    b1 = InlineKeyboardButton(f'{page+1}',callback_data=f'chose_tem{page+1}')
    b2 = InlineKeyboardButton(f'{page+2}',callback_data=f'chose_tem{page+2}')
    b3 = InlineKeyboardButton(f'{page+3}',callback_data=f'chose_tem{page+3}')
    b4 = InlineKeyboardButton(f'{page+4}',callback_data=f'chose_tem{page+4}')
    b5 = InlineKeyboardButton(f'{page+5}',callback_data=f'chose_tem{page+5}')
    b6 = InlineKeyboardButton(f'{page+6}',callback_data=f'chose_tem{page+6}')
    b7 = InlineKeyboardButton(f'{page+7}',callback_data=f'chose_tem{page+7}')
    b8 = InlineKeyboardButton(f'{page+8}',callback_data=f'chose_tem{page+8}')
    b9 = InlineKeyboardButton(f'{page+9}',callback_data=f'chose_tem{page+9}')
    b10 = InlineKeyboardButton(f'{page+10}',callback_data=f'chose_tem{page+10}')  
    bup = InlineKeyboardButton('⏩',callback_data='up_tem')
    bdown = InlineKeyboardButton('⏪',callback_data='down_tem')
    bclose = InlineKeyboardButton('❌',callback_data='close')
    bbigup = InlineKeyboardButton('⏭',callback_data='big_up_tem')
    bbigdown = InlineKeyboardButton('⏮',callback_data='big_down_tem')
    markup.add(b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,bbigdown,bdown,bclose,bup,bbigup) 
    temas = files.themes_url()
    info = f'<b>Lista de temas picantes: 🔔{page+1}-{page+10}🔔</b>'
    #Recorremos la lista de los temas actuales
    for tema in temas[page:page+10]:
        info += f'\n<b>{page+1}-> </b> {tema["name"]}'
        page+=1
    #Si no existia mensaje lo enviamos y sino lo editamos
    if not msg_old:
        bot.send_message(cid,info,parse_mode='html',reply_markup=markup)
        time.sleep(10)
    else:
        bot.edit_message_text(message_id=msg_old,chat_id=cid,text=info,parse_mode='html',reply_markup=markup)     
  
#Funcion para mostrar los elementos encontrados
def show_find(cid,msg_old=None):
    page = files.read_page(cid)
    elements = files.read_find(cid)
    markup = InlineKeyboardMarkup(row_width=5)
    b1 = InlineKeyboardButton(f'{page+1}',callback_data=f'chose_ans{page+1}')
    b2 = InlineKeyboardButton(f'{page+2}',callback_data=f'chose_ans{page+2}')
    b3 = InlineKeyboardButton(f'{page+3}',callback_data=f'chose_ans{page+3}')
    b4 = InlineKeyboardButton(f'{page+4}',callback_data=f'chose_ans{page+4}')
    b5 = InlineKeyboardButton(f'{page+5}',callback_data=f'chose_ans{page+5}')
    b6 = InlineKeyboardButton(f'{page+6}',callback_data=f'chose_ans{page+6}')
    b7 = InlineKeyboardButton(f'{page+7}',callback_data=f'chose_ans{page+7}')
    b8 = InlineKeyboardButton(f'{page+8}',callback_data=f'chose_ans{page+8}')
    b9 = InlineKeyboardButton(f'{page+9}',callback_data=f'chose_ans{page+9}')
    b10 = InlineKeyboardButton(f'{page+10}',callback_data=f'chose_ans{page+10}')
    bup = InlineKeyboardButton('⏩',callback_data='up_gener')
    bdown = InlineKeyboardButton('⏪',callback_data='down_gener')
    bclose = InlineKeyboardButton('❌',callback_data='close')
    bbigup = InlineKeyboardButton('⏭',callback_data='big_up_gener')
    bbigdown = InlineKeyboardButton('⏮',callback_data='big_down_gener')
    markup.add(b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,bbigdown,bdown,bclose,bup,bbigup)
    info = f'<b>Pagina actual : 🔔 {page}-{page+10} 🔔</b> '
    #Bucle para recorrer los 10 elementos que pidan buscar
    for element in elements[page:page+10]:
        info += f'<b>\n{elements.index(element)+1}</b> - {element["title"]} <u><i>por</i></u> {element["autor"]}\n'
    #Condicional para saber si es la primera vez que se le muesta la botonera al usuario
    if not msg_old:
        bot.send_message(cid,info,parse_mode='html',reply_markup=markup)
    else:
        bot.edit_message_text(message_id=msg_old,chat_id=cid,text=info,parse_mode='html',reply_markup=markup)

#Funcion para manejar las llamadas
@bot.callback_query_handler(func=lambda any:True)
def bottoms_aux(call):
    cid = call.from_user.id
    mid = call.message.id
    #Funcion para cerrar la botonera
    if call.data == 'close':
        bot.delete_message(cid,mid) 
    #Funcion para retroceder la botonera de los generos
    elif call.data == 'down_gener':
        #Comprobamos en que pagina se encuentra el usuario
        if files.read_page(cid) == 0:
            msg = bot.send_message(cid,'🤷🏽‍♂️<b>Sen encuentra en la pagina inicial</b>🤷🏽‍♂️',parse_mode='html')
            time.sleep(3)
            bot.delete_message(cid,msg.message_id)   
        else:
            files.change_page(cid,-10)
            show_find(cid,mid) 
    #Funcion para avanzar la botonera de los generos
    elif call.data == 'up_gener':
        #Comprobamos si no ha visto todos los libros
        if int((int(total_books(1)[(files.read_chose(cid))-1])/10)*10) < files.read_page(cid)+11:
            msg = bot.send_message(cid,'😅<b>Ups parece que llego al final</b>😅',parse_mode='html')
            time.sleep(3)
            bot.delete_message(cid,msg.message_id)
            return 1
        files.change_page(cid,10)
        #Comprobamos el limite de busqueda del usuario
        if files.read_page(cid) % 70 == 0 and not files.read_page(cid) == 0:
            #Si el usuario alcanzo el limite abrimos otra pagina
            search_title(cid,files.read_chose(cid),0,page=int(files.read_page(cid)/60)+1)
        show_find(cid,mid)
    #Funcion para retroceder la botonera por generos rapido
    elif call.data == 'big_down_gener':
        #Comprobamos en que pagina se encuentra el usuario
        if files.read_page(cid) == 0:
            msg = bot.send_message(cid,'🤷🏽‍♂️<b>Se encuentra en la pagina inicial</b>🤷🏽‍♂️',parse_mode='html')
            time.sleep(3)
            bot.delete_message(cid,msg.message_id)  
        elif files.read_page(cid)-30 < 0:
            msg = bot.send_message(cid,'🧏🏽<b>Casi llegas al comiezo,ve lento🧏🏽</b>',parse_mode='html')
            time.sleep(3)
            bot.delete_message(cid,msg.message_id)
        else:
            files.change_page(cid,-30)
            show_find(cid,mid)  
    #Funcion para avanzar la botonera por generos rapido
    elif call.data == 'big_up_gener':
        #Comprobamos si no ha visto todos los libros
        if int((int(total_books(1)[(files.read_chose(cid))-1])/10)*10) < files.read_page(cid)+41:
            msg = bot.send_message(cid,'😅<b>Ups parece que llegara al final</b>😅',parse_mode='html')
            time.sleep(3)
            bot.delete_message(cid,msg.message_id)
            return 1
        files.change_page(cid,30)
        #Comprobamos el limite de busqueda del usuario
        if files.read_page(cid)+30 > len(files.read_find(cid)):
            search_title(cid,files.read_chose(cid),0,page=int(files.read_page(cid)/60)+1)
        show_find(cid,mid)
    #Funcion para retroceder la botonera por temas
    elif call.data == 'down_tem':
        #Comprobamos en que pagina se encuentra el usuario
        if files.read_page_temas(cid) == 0:
            msg = bot.send_message(cid,'🤷🏽‍♂️<b>Se encuentra en la pagina inicial</b>🤷🏽‍♂️',parse_mode='html')
            time.sleep(3)
            bot.delete_message(cid,msg.message_id)   
        else:
            files.change_page_temas(cid,-10)
            show_find_themes(cid,mid) 
    #Funcion para avanzar la botonera por temas
    elif call.data == 'up_tem':
        #Comprobamos el limite de busqueda del usuario
        if files.read_page_temas(cid) > 100:
            msg = bot.send_message(cid,'😅<b>Ups parece que llego al final</b>😅',parse_mode='html')
            time.sleep(2)
            bot.delete_message(cid,msg.message_id)
        else:
            files.change_page_temas(cid,10)
            show_find_themes(cid,mid)
    #Funcion para avanzar la botonera por temas rapido
    elif call.data == 'big_up_tem':
        #Comprobamos el limite de busqueda del usuario
        if files.read_page_temas(cid) > 100:
            msg = bot.send_message(cid,'😅<b>Ups parece que llego al final</b>😅',parse_mode='html')
            time.sleep(2)
            bot.delete_message(cid,msg.message_id)
        elif files.read_page_temas(cid)+30 > 100:
            msg = bot.send_message(cid,'🧏🏽<b>Casi llegas al final,ve lento🧏🏽</b>',parse_mode='html')
            time.sleep(2)
            bot.delete_message(cid,msg.message_id)
        else:
            files.change_page_temas(cid,30)
            show_find_themes(cid,mid)
    #Funcion para retroceder la botonera por temas rapido
    elif call.data == 'big_down_tem':
        #Comprobamos en que pagina se encuentra el usuario
        if files.read_page_temas(cid) == 0:
            msg = bot.send_message(cid,'🤷🏽‍♂️<b>Sen encuentra en la pagina inicial</b>🤷🏽‍♂️',parse_mode='html')
            time.sleep(3)
            bot.delete_message(cid,msg.message_id)  
        elif files.read_page_temas(cid)-30 < 0:
            msg = bot.send_message(cid,'🧏🏽<b>Casi llegas al comiezo,ve lento🧏🏽</b>',parse_mode='html')
            time.sleep(3)
            bot.delete_message(cid,msg.message_id)          
        else:
            files.change_page_temas(cid,-30)
            show_find_themes(cid,mid) 
    #Condicional para manejar lo que deseaa buscar el usuario por genero
    elif str(call.data).startswith('chose_g'):
        chose = int(str(call.data).split('_')[1].replace('g',''))
        #Borramos la botonera
        bot.delete_message(cid,mid)
        #Creamos el archivo para conocer la pagina 
        files.new_page(cid)
        #Buscamos los resultados por temas
        search_title(cid,chose,0)
        #Guardamos la eleccion del usuario 
        files.save_chose(cid,chose)
        #Mostramos
        show_find(cid)
    #Condicional para manejar lo que deseaa buscar el usuario por rakings
    elif str(call.data).startswith('chose_r'):
        chose = int(str(call.data).split('_')[1].replace('r','')) 
    #Condicional para manejar lo que deseaa buscar el usuario por temas
    elif str(call.data).startswith('chose_tem'):
        chose = int(str(call.data).split('_')[1].replace('tem','')) 
        #Creamos el archivo para conocer la pagina 
        files.new_page(cid)
        #Realizamos la busqueda de acorde con la seleccion del usuario  el 1 indica lo deseado a buscar
        if search_title(cid,chose,1):  
            #Borramos la botonera
            bot.delete_message(cid,mid)
            #Guardamos la eleccion del usuario 
            files.save_chose(cid,chose)
            #Mostramos
            show_find(cid) 
        #Condisional ara saber si el usuario se encuentra en rango o no   
        else:
            msg = bot.send_message(cid,'<b>🤷🏽‍♂️Ups,estas fuera del rango🤷🏽‍♂️</b>',parse_mode='html')
            time.sleep(2)
            bot.delete_message(cid,msg.message_id,timeout=2)
    #Condicional para la seleccion de libro por genero
    elif str(call.data).startswith('chose_ans'):
        chose_book = int(str(call.data).split('_')[1].replace('ans','')) 
        #Orden del retorno de la funcion show_info 1Genero 2Fecha 3Info 4Titulo 5Autor
        data_book = save_info_book(cid,chose_book)
        if not data_book:
            msg = bot.send_message(cid,'<b>🤷🏽‍♂️Ups,estas fuera del rango🤷🏽‍♂️</b>',parse_mode='html')
            time.sleep(2)
            bot.delete_message(cid,msg.message_id,timeout=2)
            return 0
        show_info_book_ans(cid,data_book)
    #Condicional para descargar el libro !!
    elif str(call.data).startswith('story'):
        url = call.data
        bot.delete_message(cid,mid)
        info = '😈Su libro gratis esta siendo descargado,esto podra tomar algunos segundos😈'
        msg = bot.send_message(cid,info)
        #Funcion para obtener el libro traducido
        time.sleep(10)
        bot.delete_message(cid,msg.message_id)
        dowload_book(cid,url)
        with open(f'data/{cid}/book.doc', 'rb') as doc:
            bot.send_document(cid, doc)
        
#Funcion informativa para acomenzar el promgrama
@bot.message_handler(commands=['start'])
def cmd_start(message):
    info = '<b>👋Bienvenido a tu biblioteca secreta👋</b>\nSoy tu bot de historias 🔥<b>HOTS</b>🔥 y poseo,'
    info += 'la mejor coleccion de libros ordenados por <i>generos</i>,<i>temas</i> o <i>rankings</i>.\n'
    info += 'Seleccione alguno de los metodos para comenzar su busqueda:\n'
    info += 'Busqueda por: /generos <code>Para la categoria generos</code>\n'
    info += 'Busqueda por: /temas <code>Para la categoria temas</code>\n'
    info += 'Busqueda por: /rakings <code>Para la categoria rakings</code>\n'
    info += 'Informacion: /info <code>Obtendras informacion util con respecto a mi</code>'
    bot.send_message(message.chat.id,info,parse_mode='html') 
    files.mkdir(message.chat.id)   

#Funcion par abuscar por generos
@bot.message_handler(commands=['generos'])
def cmd_generos(message):
    books = total_books(1)
    info = f'<b>Lista de generos mas populares actualizada en tiempo real:</b>\n'
    info += f'<b>1-></b> Diarios                         <b>Libros:</b>{books[0]}\n<b>2-></b> Ensayos                       <b>Libros:</b>{books[1]}\n<b>3-></b> Fantasmas                  <b>Libros:</b>{books[2]}'
    info += f'\n<b>4-></b> Fantasticos                 <b>Libros:</b>{books[3]}\n<b>5-></b> Fantasia                       <b>Libros:</b>{books[4]}\n<b>6-></b> Ficcion                         <b>Libros:</b>{books[5]}'
    info += f'\n<b>7-></b> Informativos                <b>Libros:</b>{books[6]}\n<b>8-></b> Nuevos                        <b>Libros:</b>{books[7]}\n<b>9-></b> Poemas                       <b>Libros:</b>{books[8]}'
    info += f'\n<b>10-></b> Ciencia Ficcion        <b>Libros:</b>{books[9]}\n<b>11-></b> Bromas Sexuales     <b>Libros:</b>{books[10]}\n<b>12-></b> Historia real              <b>Libros:</b>{books[11]}'
    info += f'\n\n                  ❤️‍🔥<b>Total: {sum(map(int,books))}</b>❤️‍🔥'
    info += '\n\nAyudanos a crecer,contamos con el tuyo....'
    markup = InlineKeyboardMarkup(row_width=6)
    b1 = InlineKeyboardButton('1',callback_data='chose_g1')
    b2 = InlineKeyboardButton('2',callback_data='chose_g2')
    b3 = InlineKeyboardButton('3',callback_data='chose_g3')
    b4 = InlineKeyboardButton('4',callback_data='chose_g4')
    b5 = InlineKeyboardButton('5',callback_data='chose_g5')
    b6 = InlineKeyboardButton('6',callback_data='chose_g6')
    b7 = InlineKeyboardButton('7',callback_data='chose_g7')
    b8 = InlineKeyboardButton('8',callback_data='chose_g8')
    b9 = InlineKeyboardButton('9',callback_data='chose_g9')
    b10 = InlineKeyboardButton('10',callback_data='chose_g10')
    b11 = InlineKeyboardButton('11',callback_data='chose_g11')
    b12 = InlineKeyboardButton('12',callback_data='chose_g12')
    bclose = InlineKeyboardButton('❌',callback_data='close')
    markup.add(b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,bclose)
    msg = bot.send_message(message.chat.id,info,reply_markup=markup,parse_mode='html')

#funcion para buscar por temas
@bot.message_handler(commands=['temas'])
def cmd_start(message):
    #Informacion introductoria del comando temas
    info = f'<b>Actualmente cuento con:</b> <i>117 temas</i>\n\nEstoy cargando la lista para usted,'
    info += 'seleccione uno de los siguentes a continuacion...'
    msg = bot.send_message(message.chat.id,info,parse_mode='html')
    #Esperamos 4 segundos y borramos la informacion
    time.sleep(4)
    bot.delete_message(message.chat.id,msg.message_id)
    #Iniciamos una pagina para buscar por temas
    files.new_page_temas(message.chat.id)
    show_find_themes(message.chat.id)

#Funcion para buscar por rakings
@bot.message_handler(commands=['rakings'])
def cmd_start(message):
    markup = InlineKeyboardMarkup(row_width=4)
    info = '<b>Listados actualizados en tiempo real:</b>\n'
    info += '1-> Top de historias mas leidas en el ultimo mes'
    info += '\n2-> Top de historias mejor valoradas'
    info += '\n3-> Top de historias peor valoradas'
    info += '\n4-> Ultimas actualizaciones'
    b1 = InlineKeyboardButton('1',callback_data='chose_r1')
    b2 = InlineKeyboardButton('2',callback_data='chose_r2')
    b3 = InlineKeyboardButton('3',callback_data='chose_r3')
    b4 = InlineKeyboardButton('4',callback_data='chose_r4')
    bclose = InlineKeyboardButton('X',callback_data='close')
    markup.add(b1,b2,b3,b4,bclose)
    bot.send_message(message.chat.id,info,parse_mode='html',reply_markup=markup)

#Funcion para describir la biblioteca
@bot.message_handler(commands=['info'])
def cmd_start(message):
    info = '<strong>😎Hola,gracias por elegirme para realizar tus descargar😎</strong>'
    info += '\n\n<b>1-> Idioma:</b> He sido desarrollado con una interfaz en castellano para poder'
    info += ' alcanzar,a muchos mas usuarios,mis libros te los ofrecere en ese mismo idioma,pero'
    info += ' por convencion los datos introductorios de estos estar en el idioma del autor'
    info += '\n\n<b>2-> Limitantes:</b> Actualmente me encuentro en la fase !!Beta!!,por lo que muchos de los libros'
    info += 'que te ofrecere de manera gratuita no han sido pagados,espero con tus contribuciones poder comprar'
    info += 'mas y ampliar nuestra biblioteca\n\n<b>3-> Contactar: </b>Con el comando  /contact podras'
    info += 'contactar directamente con mi creador,esta esperando ansiosamente por sus <i>opiniones,comentarios</i> y <i>reportes</i>'
    msg = bot.send_message(message.chat.id,info,parse_mode='html')
    time.sleep(30)
    bot.delete_message(message.chat.id,msg.message_id)

if __name__ == '__main__':
    bot.infinity_polling()
