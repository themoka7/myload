import MySQLdb
import os


def dbConn():
    # 환경 변수에 따라 로컬 및 서버 설정 분기
    IS_LOCAL = os.environ.get('IS_LOCAL', 'true').lower() == 'true'

    # MySQL 데이터베이스 연결 설정
    if IS_LOCAL:
        # 로컬 환경의 MySQL 연결 정보
        connection = MySQLdb.connect(
            user='root',
            passwd='oo1351oo^^',
            host='127.0.0.1',
            port=3306,
            db='localmyload',
        )
    else:
        # 서버 환경의 MySQL 연결 정보
        connection = MySQLdb.connect(
            user='kimjungmok',
            passwd='oo1351oo^^',  # 서버에서 사용할 비밀번호
            host='kimjungmok.mysql.pythonanywhere-services.com',
            port=3306,
            db='kimjungmok$myload',   # 서버의 데이터베이스 이름
        )

    connection.ping()

    return connection

