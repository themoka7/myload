from flask import Flask, render_template, jsonify, session, url_for

from flask_cors import CORS
from process.hexagram_process import get_hexagram_data  # process 폴더에서 모듈 불러오기


# CORS(app)


# Flask가 현재 디렉터리에서 템플릿을 찾을 수 있도록 설정
app = Flask(__name__, static_folder='static', template_folder='templates')
app.secret_key = '1qa2ws3ed4rf5tg&&'  # 세션을 사용하려면 필요합니다

@app.route('/')
def index():
    return render_template('hexagram/index.html')

@app.route('/intro')
def intro():
    return render_template('intro/intro.html')

@app.route('/hexagram')
def hexagram():
    return render_template('hexagram/index.html')

@app.route('/hexagram/result')
def hexagram_result():
    # 세션에 저장된 처리된 데이터 불러오기
    data = session.get('data', {})
    return render_template('hexagram/result.html', data=data)  # 결과 페이지에서 데이터 표시

@app.route('/hexagram_process', methods=['POST'])
def hexagram_process():
    # process 폴더의 hexagram_process.py에서 get_hexagram_data 함수 호출
    data = get_hexagram_data()

    print(data)

    # 세션에 처리된 데이터 저장
    session['data'] = data

    # 처리된 데이터를 JSON으로 반환하고, 리디렉션 URL 포함
    return jsonify({'redirect': url_for('hexagram_result')})  # 리디렉션 URL을 AJAX로 반환

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
