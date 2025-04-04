#Pau Mas Sales
#4/4/2025
#Activitat 1 RA56


#LLibreries 
import psycopg
#definicio que ens permet conetar-nos al PostgresSQL
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
    conn=connection()
    print("Menú Principal")
    print("1 - Consultar tots els artistes")
    print("2 - Consultar artistes pel seu nom")
    print("3 - Consultar els 5 primers àlbums pel nom de l'artista")
    print("4 - Afegir un artista")
    print("5 - Modificar el nom d'un artista")
    print("6 - Borrar un artista")
    print("7 - Sortir")
    opcio=input("Selecciona una opció: ")



#Definico que demana l'opcio a l'usuari i executa la definicio corresponent
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




#PER A EXECUTAR PRIMERAMENT LA FUNCIÓ menu
if __name__ == "__main__":
    menu()
