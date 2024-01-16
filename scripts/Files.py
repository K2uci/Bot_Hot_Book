import os,json

class Files():
    def __init__(self):
        self.__path = os.getcwd() + '/data/'
        pass  
    #Creamos la carpeta con la que trabajara el usuario
    def mkdir(self,cid):
        try:
            os.mkdir(f'{self.__path}{cid}')
        except FileExistsError:
            pass
    #Funcion para guardr los resultados de busqueda
    def save_find(self,cid,listt_dicc,page):
        #Si estamos en la primera pagina creamos la lista desde cero
        if page == 1:
            with open(f'{self.__path}{cid}/list_titles.txt','w') as file:
                for any in listt_dicc:
                    any_dp = json.dumps(any) + '\n'
                    file.write(any_dp) 
        #Sino,agregamos a la lista de respuestas
        else:   
            with open(f'{self.__path}{cid}/list_titles.txt','a') as file:
                for any in listt_dicc:
                    any_dp = json.dumps(any) + '\n'
                    file.write(any_dp) 
    #Funcion para leer los resultados de busqueda
    def read_find(self,cid) -> list:
        with open(f'{self.__path}{cid}/list_titles.txt','r') as file:
            ans = file.readlines();base = []
            for any in ans:
                any_ld = json.loads(any)
                base.append(any_ld)
            return base        
    #Funcion paracrear pagina de indice de usuario para generos
    def new_page(self,cid):
        with open(f'{self.__path}{cid}/page_gene.txt','w') as file:
            file.write('0')
    #Funcion para modificar la pagina de indice de usuario para generos
    def change_page(self,cid,mov) -> int:
        post = self.read_page(cid)
        with open(f'{self.__path}{cid}/page_gene.txt','w') as f:f.write(str(post+int(mov)))
    #Funcion para cargar la pagina de indice de usuario para generos
    def read_page(self,cid) -> int:
        with open(f'{self.__path}{cid}/page_gene.txt','r') as f:ff = f.readline()
        return int(ff)
    #Funcion paracrear pagina de indice de usuario para temas
    def new_page_temas(self,cid):
        with open(f'{self.__path}{cid}/page_themes.txt','w') as file:
            file.write('0')
    #Funcion para modificar la pagina de indice de usuario para temas
    def change_page_temas(self,cid,mov) -> int:
        post = self.read_page_temas(cid)
        with open(f'{self.__path}{cid}/page_themes.txt','w') as f:f.write(str(post+int(mov)))
    #Funcion para cargar la pagina de indice de usuario para temas
    def read_page_temas(self,cid) -> int:
        with open(f'{self.__path}{cid}/page_themes.txt','r') as f:ff = f.readline()
        return int(ff)     
    #Funcion para crear la busqueda actual del usuario
    def find_title(self,cid,find):
        with open(f'{self.__path}{cid}/url','w') as f:f.write(f'{find}')      
    #Funcion para leer la busqueda actual del usuario
    def find_title_ans(self,cid) -> str:
        with open(f'{self.__path}{cid}/url','r') as f:ff = f.read()
        return int(ff)
    #Funcion para retornar temas y urls en busqueda por temas
    def themes_url(self) -> list:
        with open(os.getcwd()+'/config/temas_url.txt','r') as file:
            ans = file.readlines();base = []
            for any in ans:
                any_ld = json.loads(any)
                base.append(any_ld)
            return base
    #Funcion para guardar la eleccion del usuario
    def save_chose(self,cid,chose):
        with open(f'{self.__path}{cid}/chose','w') as file:
            file.write(str(chose))       
    #Funcion para leer la eleccion del usuario
    def read_chose(self,cid) -> int:
        with open(f'{self.__path}{cid}/chose','r') as file:
            chose = file.readline()
        return int(chose)  
#DESUSOOOOOOOOOOOOOOOOOOOOOOO
    
    #Funcion para leer y mostrar los generos (Decorador)
    def generos_names(self) -> list:
        with open(os.getcwd()+'/config/generos_names.txt','r') as file:
            ans = file.readlines();base = []
            for any in ans:
                any_ld = str(any).strip()
                base.append(any_ld)
            return base