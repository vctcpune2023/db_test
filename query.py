from mysql.connector import MySQLConnection, Error
import config
def insert_query(args):
    query = "INSERT INTO vctchealth.user_data(age,gender,bmi,children,smoker,region,prediction) VALUES(%s,%s,%s,%s,%s,%s,%s)"
    try:
        conn = MySQLConnection(**config.DB_PARAM)
        cursor = conn.cursor()
        cursor.execute(query,args)
        
        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')

        conn.commit()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()
if __name__ == "__main__":
    insert_query((20,"Male",20,0,"No", "Southwest",7500.30))