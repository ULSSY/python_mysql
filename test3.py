import mysql.connector
from mysql.connector.errors import Error
from datetime import date,datetime 
try : 
    #DB에 연결
    connection=mysql.connector.connect(
        host='yh-db.cahgiqgzpaou.ap-northeast-2.rds.amazonaws.com',
        database='streamlit_db',
        user='python_user',
        password='1234'
    )
  

    #2.쿼리문 만들고
    current_time=datetime.now()


    query='''insert into test
            (name,date)
            values
            (%s,%s);'''
    #튜플 데이터 한개 있을때 콤마를 꼭 
    #써주자
    record=[('qqq',current_time),('yyy',current_time),('ppp',current_time)]
    #3.커넥션으로부터 커서를 가져온다
    cursor=connection.cursor()
    #4쿼리문을 커서에 넣어서 실행한다
    cursor.executemany(query,record)
    #5커넥션을 커밋한다->디비에 영구적으로 반영하라는 뜻
    connection.commit()
except mysql.connector.Error as e:
    print('Error',e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print('MySQL connection is closed')
