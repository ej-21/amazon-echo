from play_service import play
from txt_to_speech import text_to_speech
from database_entry import sqlite_connect


def retrieve_file(file_name: str) -> str:
    """
    takes in a string and searches the string value in
    the database
    when found BLOB in data format is returned/played
    else not found error returned
    """
    db_name = 'sample.db'
    table_name = 'audio'
    connection = sqlite_connect(db_name)
    print(f"Connected to the database `{db_name}`")
    try:
        cursor = connection.cursor()
        sql_retrieve_file_query = f"""SELECT data FROM {table_name}
        WHERE SHORT_DESC LIKE ? """
        cursor.execute(sql_retrieve_file_query, ("%"+file_name+"%",))
        record = cursor.fetchone()
        x = record[0]
        connection.close()
        return play(x)
    except (ValueError,TypeError):
        return text_to_speech("Could not find, please ask something else")
