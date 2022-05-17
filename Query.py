import psycopg2
from configuration import connectBD

connect = connectBD.func_connect_bd()
cursor = connect.cursor()

class Scripts:

    def all_films(people_id):
        cursor.execute(f"""SELECT film_name FROM films where user_id = {people_id}""")
        query_results = cursor.fetchall()
        text = '\n\n'.join([', '.join(map(str, x)) for x in query_results])
        return (str(text)) 
        
    def all_tasks(people_id):   
        cursor.execute(f"SELECT task_name FROM todo_list where user_id = {people_id}")
        query_results = cursor.fetchall()
        text = '\n\n'.join([', '.join(map(str, x)) for x in query_results])
        return (str(text)) 

    def add_task(task_text,user_id):
        cursor = connect.cursor()
        with connect.cursor() as cursor:
                cursor.execute("""INSERT INTO todo_list (task_name,user_id) VALUES(%s,%s);""",(task_text,user_id))
        return connect.commit()

    def Delete_all_tasks(people_id):
        cursor = connect.cursor()
        with connect.cursor() as cursor:
                cursor.execute(f"""Delete from todo_list where user_id = {people_id}""")
        return connect.commit()

    def select_favoritefilms(people_id):
        cursor.execute(f"""SELECT favorites_name FROM filmsfavorites where user_id = {people_id}""")
        query_results = cursor.fetchall()
        text = '\n\n'.join([', '.join(map(str, x)) for x in query_results])
        return (str(text))

    def add_favoritefilm(name_film,user_id):
        cursor = connect.cursor()
        with connect.cursor() as cursor:
                cursor.execute("""INSERT INTO filmsfavorites ("favorites_name",user_id) VALUES(%s,%s);""",(name_film,user_id))
        return connect.commit()
    
    def delete_all_favorites(people_id):
        cursor = connect.cursor()
        with connect.cursor() as cursor:
                cursor.execute(f"""Delete from filmsfavorites where user_id = {people_id}""")
        return connect.commit()   
    