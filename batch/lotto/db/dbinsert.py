import logging
import mysql.connector
import requests

# 로그 설정
logging.basicConfig(level=logging.DEBUG)

def dbinsert_server(data):
    """
    SSH 터널 없이 MySQL 서버에 직접 연결하여 데이터 삽입.
    """
    try:
        # MySQL 직접 연결
        logging.debug("Connecting to MySQL directly...")
        conn = mysql.connector.connect(
            user='kimjungmok',  # MySQL 사용자명
            password='oo1351oo^^',  # MySQL 비밀번호
            host='kimjungmok.mysql.pythonanywhere-services.com',  # MySQL 호스트 (예: localhost 또는 IP 주소)
            port=3306,  # MySQL 포트 (기본값: 3306)
            database='kimjungmok$myload'  # MySQL 데이터베이스명
        )

        logging.debug("Connected to MySQL directly.")

        cursor = conn.cursor()

        # 데이터 삽입
        query = """
        INSERT INTO LottoResults (
            totSellamnt, returnValue, drwNoDate, firstWinamnt, 
            drwtNo1, drwtNo2, drwtNo3, drwtNo4, drwtNo5, drwtNo6, 
            bnusNo, firstPrzwnerCo, firstAccumamnt, drwNo
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        try:
            logging.debug(f"Executing query: {query}")
            cursor.execute(query, (
                data["totSellamnt"], data["returnValue"], data["drwNoDate"], data["firstWinamnt"],
                data["drwtNo1"], data["drwtNo2"], data["drwtNo3"], data["drwtNo4"],
                data["drwtNo5"], data["drwtNo6"], data["bnusNo"], data["firstPrzwnerCo"],
                data["firstAccumamnt"], data["drwNo"]
            ))
            conn.commit()
            logging.debug("Data inserted successfully!")

        except mysql.connector.Error as err:
            logging.error(f"Error executing query: {err}")

        finally:
            # 연결 종료
            cursor.close()
            conn.close()
            logging.debug("MySQL connection closed.")

    except mysql.connector.Error as e:
        logging.error(f"MySQL connection error: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
