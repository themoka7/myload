import logging
import mysql.connector
import requests

from process.common.dbCon import dbConn

# 로그 설정
logging.basicConfig(level=logging.DEBUG)

def dbinsert(data):
    """
    SSH 터널 없이 MySQL 서버에 직접 연결하여 데이터 삽입.
    """
    try:
        conn = dbConn()

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

'''data = {
    "totSellamnt": 112146718000,
    "returnValue": "success",
    "drwNoDate": "2024-12-07",
    "firstWinamnt": 1613380765,
    "drwtNo6": 36,
    "drwtNo4": 21,
    "firstPrzwnerCo": 17,
    "drwtNo5": 32,
    "bnusNo": 38,
    "firstAccumamnt": 27427473005,
    "drwNo": 1149,
    "drwtNo2": 15,
    "drwtNo3": 19,
    "drwtNo1": 8
}

dbinsert(data)'''