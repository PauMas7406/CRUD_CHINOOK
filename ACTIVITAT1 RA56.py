#Pau Mas Sales
#28/3/2025
#Archiu plantilla diferents programes Python


#LLibreries 
import psycopg

def connection():
	connexio="""
		dbname=chinook_v2
		user=postgres
		password=user
		host=localhost
		port=5432
	"""
	conn=psycopg.connect(connexio)
	curs=conn.cursor()
	return curs



#Definico que em mostra per consola les opcions del menu
def printar_menu():
    print("")



#Definico que demana l'ocio a l'usuari i executa la definicio corresponent
def escollir_opcio():
    opcio=int(input("Escull opcio"))
    if opcio==1 :
        consultar_artista(cursor)
    else 
        if opcio ==7:
            print("Programa finalitzat")
        else




def menu():
    cursor=connection()
    opcio=0
    while opcio !=7 :
        printar_menu()
        opcio = escollir_opcio(cursor)

#Main
def main():
	menu()


if__name__=="__main__":
	main(nomBase)