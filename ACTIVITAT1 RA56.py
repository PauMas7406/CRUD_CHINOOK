#Pau Mas Sales
#4/4/2025
#Activitat 1 RA56


#LLibreries 
import psycopg

# DEFINICIÓ QUE ENS PERMET CONECTAR-NOS AL POSTGRES
def connect_db():
	connexio="""
		dbname='chinook_v2'
		user='postgres'
		password='user'
		host='localhost'
		port='5432'
	"""
	conn=psycopg.connect(connexio)
	curs=conn.cursor()
	return curs



# CONSULTA 1 - Mostrar tots els artistes
def consultar_tots_els_artistes(curs):
    curs.execute("SELECT artistid, name FROM artist")
    artistes = curs.fetchall()
    if artistes:
        for artista in artistes:
            print(f"ID: {artista[0]}, NOM: {artista[1]}")
    else:
        print("No hi ha resultats per aquesta consulta")

# CONSULTA 2 - Cercar artistes pel nom
def consultar_artista_pel_nom(curs):
    nom = input("Introdueix el nom de l'artista: ")
    if len(nom) < 2:
        print("Has d'introduir almenys 2 caràcters")
        return
    curs.execute("SELECT artistid, name FROM artist WHERE name ILIKE %s", ('%' + nom + '%',))
    artistes = curs.fetchall()
    if artistes:
        for artista in artistes:
            print(f"ID: {artista[0]}, NOM: {artista[1]}")
    else:
        print("No hi ha resultats per aquesta consulta")

# CONSULTA 3 - Mostrar 5 primers àlbums d'un artista
def consultar_primers_albums(curs):
    nom = input("Introdueix el nom de l'artista: ")
    if len(nom) < 2:
        print("Has d'introduir almenys 2 caràcters")
        return
    curs.execute("""
        SELECT album.albumid, album.title, artist.name
        FROM album
        JOIN artist ON album.artistid = artist.artistid
        WHERE artist.name ILIKE %s
        ORDER BY album.albumid
        LIMIT 5
    """, (nom + '%',))
    albums = curs.fetchall()
    if albums:
        for album in albums:
            print(f"ID_ALBUM: {album[0]}, NOM_ALBUM: {album[1]}, NOM_ARTISTA: {album[2]}")
    else:
        print("No hi ha resultats per aquesta consulta")

# CONSULTA 4 - Afegir un artista
def afegir_artista(curs):
    nom = input("Introdueix el nom del nou artista: ")
    if len(nom) < 2:
        print("Has d'introduir almenys 3 caràcters")
        return
    curs.execute("SELECT MAX(artistid) FROM artist")
    max_id = curs.fetchone()[0] or 0
    nou_id = max_id + 1
    curs.execute("INSERT INTO artist (artistid, name) VALUES (%s, %s)", (nou_id, nom))
    curs.connection.commit()
    print("L'artista s'ha afegit correctament")

# CONSULTA 5 - Modificar un artista
def modificar_artista(curs):
    id_text = input("Introdueix la ID de l'artista a modificar: ")
    if not id_text.isdigit():
        print("Has d'introduir un número vàlid per a la ID")
        return
    id_artista = int(id_text)
    nou_nom = input("Introdueix el nou nom de l'artista: ")
    if len(nou_nom) < 2:
        print("Has d'introduir almenys 3 caràcters")
        return
    curs.execute("UPDATE artist SET name = %s WHERE artistid = %s", (nou_nom, id_artista))
    if curs.rowcount == 0:
        print("No s'ha trobat cap artista amb aquesta ID")
    else:
        curs.connection.commit()
        print("L'artista s'ha modificat correctament")

# CONSULTA 6 - Borrar un artista
def borrar_artista(curs):
    id_text = input("Introdueix la ID de l'artista a eliminar: ")
    if not id_text.isdigit():
        print("Has d'introduir un número vàlid per a la ID")
        return
    id_artista = int(id_text)
    curs.execute("DELETE FROM artist WHERE artistid = %s", (id_artista,))
    if curs.rowcount == 0:
        print("No s'ha trobat cap artista amb aquesta ID")
    else:
        curs.connection.commit()
        print("L'artista s'ha borrat correctament")

# MENÚ PRINCIPAL
def menu():
    curs = connect_db()

    opcio = 0
    while opcio != 7:
        print("\nMenú Principal")
        print("1 - Consultar tots els artistes")
        print("2 - Consultar artistes pel seu nom")
        print("3 - Consultar els 5 primers àlbums pel nom de l'artista")
        print("4 - Afegir un artista")
        print("5 - Modificar el nom d'un artista")
        print("6 - Borrar un artista")
        print("7 - Sortir")

        opcio_text = input("Selecciona una opció: ")
        if not opcio_text.isdigit():
            print("Has d'introduir un número vàlid")
            continue
        opcio = int(opcio_text)

        if opcio == 1:
            consultar_tots_els_artistes(curs)
        elif opcio == 2:
            consultar_artista_pel_nom(curs)
        elif opcio == 3:
            consultar_primers_albums(curs)
        elif opcio == 4:
            afegir_artista(curs)
        elif opcio == 5:
            modificar_artista(curs)
        elif opcio == 6:
            borrar_artista(curs)
        elif opcio == 7:
            print("Programa finalitzat")
            curs.close()
        else:
            print("Opció no vàlida, afegeix una opció correcte")

# EXECUCIÓ DEL PROGRAMA
if __name__ == "__main__":
    menu()
