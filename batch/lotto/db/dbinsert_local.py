import logging
from sshtunnel import SSHTunnelForwarder
import mysql.connector

# 로그 설정
logging.basicConfig(level=logging.DEBUG)


def dbinsert_local(data):

    # SSH 터널 설정 (타임아웃을 제거하고 기본 값 사용)
    logging.debug("Starting SSH Tunnel connection...")
    try:
        with SSHTunnelForwarder(
                ('ssh.pythonanywhere.com', 22),
                ssh_username='kimjungmok',
                ssh_password='oo1351oo^^',
                remote_bind_address=('kimjungmok.mysql.pythonanywhere-services.com', 3306),
                local_bind_address=('127.0.0.1', 0)  # 로컬 포트 자동 바인딩
        ) as tunnel:
            logging.debug(f"SSH Tunnel established. Local bind port: {tunnel.local_bind_port}")

            # MySQL 연결
            logging.debug("Connecting to MySQL...")
            conn = mysql.connector.connect(
                user='kimjungmok',
                password='oo1351oo^^',
                host='127.0.0.1',
                port=tunnel.local_bind_port,  # SSH 터널을 통해 로컬 바인딩 포트 사용
                database='kimjungmok$myload'
            )

            logging.debug("Connected to MySQL successfully.")

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

    except Exception as e:
        logging.error(f"Error occurred: {e}")


data = {
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

dbinsert_local(data)