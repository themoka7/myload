import time

from flask import Flask, render_template, jsonify, session, url_for,request,Response, send_from_directory

from flask_cors import CORS

from process.common.rss import generate_rss
from process.hexagram.hexagram_process import get_hexagram_data  # process 폴더에서 모듈 불러오기
from process.tarot.tarot_process import get_tarot_data  # process 폴더에서 모듈 불러오기
from process.chizodiac.chizodiac_process import get_chizodiac_data  # process 폴더에서 모듈 불러오기
from process.dailystarzodiac.dailystarzodiac import get_dailystarzodiac_data  # process 폴더에서 모듈 불러오기
from process.eightzodiac.eightzodiac_process import get_eightzodiac_data
from process.mansae.mansae_process import get_mansae_data




# CORS(app)


# Flask가 현재 디렉터리에서 템플릿을 찾을 수 있도록 설정
app = Flask(__name__, static_folder='static', template_folder='templates')
app.secret_key = '1qa2ws3ed4rf5tg&&'  # 세션을 사용하려면 필요합니다

@app.route('/')
def index():
    return render_template('intro/intro.html')

@app.route('/intro')
def intro():
    return render_template('intro/intro.html')



#########################################
#               hexagram                #
#########################################
@app.route('/mansae')
def mansae_intro():
    return render_template('mansae/mansae_intro.html')


# AJAX POST 요청을 처리할 라우트
@app.route('/mansae_process', methods=['POST'])
def mansae_process():

    data = request.get_json()  # 클라이언트에서 보낸 JSON 데이터를 받음

    result = get_mansae_data(data.get('year', 'Unknown'), data.get('month', 'Unknown'))
    # 간단한 응답 메시지를 JSON 형식으로 반환
    response = {
        'data': result
    }
    return jsonify(response)


#########################################
#               hexagram                #
#########################################


#########################################
#               hexagram                #
#########################################
@app.route('/hexagram')
def hexagram():
    return render_template('hexagram/hexagram_index.html')

@app.route('/hexagram/result')
def hexagram_result():
    # 세션에 저장된 처리된 데이터 불러오기

    data = session.get('data', {})

    return render_template('hexagram/hexagram_result.html', data=data)  # 결과 페이지에서 데이터 표시

@app.route('/hexagram_process', methods=['POST'])
def hexagram_process():
    data = get_hexagram_data()
    session.clear()
    session['data'] = data
    return jsonify({'redirect': url_for('hexagram_result')})  # 리디렉션 URL을 AJAX로 반환


#########################################
#               hexagram                #
#########################################



#########################################
#            chizodiac(당사주)           #
#########################################

@app.route('/chizodiac_intro')
def chizodiac_intro():
    return render_template('chizodiac/chizodiac_intro.html')

@app.route('/chizodiac')
def chizodiac():
    return render_template('chizodiac/chizodiac_index.html')


@app.route('/chizodiac/result')
def chizodiac_result():
    chizodiac_result = session.get('chizodiac_result', None)

    data = session.get('data', {})
    return render_template('chizodiac/chizodiac_result.html', chizodiac_result=chizodiac_result)  # 결과 페이지에서 데이터 표시

@app.route('/chizodiac_process', methods=['POST'])
def chizodiac_process():
    # 클라이언트로부터 JSON 데이터를 받음
    chizodiac_data = request.get_json()


    if not chizodiac_data:
        return jsonify({'error': 'No data provided'}), 400  # 데이터가 없으면 400 에러 반환

    data = get_chizodiac_data(chizodiac_data)

    session.clear()
    # 받은 card_data를 처리 (여기서는 단순 출력)
    session['chizodiac_result'] = data
    return jsonify({'redirect': url_for('chizodiac_result')})


#########################################
#            chizodiac(당사주)           #
#########################################



#########################################
#            chizodiac(자평)           #
#########################################


@app.route('/eightzodiac_intro')
def eightzodiac_intro():
    return render_template('eightzodiac/eightzodiac_intro.html')


@app.route('/eightzodiac')
def eightzodiac():
    return render_template('eightzodiac/eightzodiac_index.html')

@app.route('/eightzodiac/result', methods=['GET'])
def eightzodiac_result_get():

    return render_template('eightzodiac/eightzodiac_result.html')  # 결과 페이지에서 데이터 표시

@app.route('/eightzodiac/pre', methods=['POST'])
def eightzodiac_result():

    session['eightzodiac_data'] = request.get_json()

    return jsonify({'redirect': url_for('eightzodiac_result')})
    #return render_template('eightzodiac/eightzodiac_result.html', eightzodiac_data=eightzodiac_data)  # 결과 페이지에서 데이터 표시

@app.route('/eightzodiac_process', methods=['POST'])
def eightzodiac_process():
    # 클라이언트로부터 JSON 데이터를 받음

    eightzodiac_data = session.get('eightzodiac_data', None)
    result = get_eightzodiac_data(eightzodiac_data)
    # 간단한 응답 메시지를 JSON 형식으로 반환
    response = {
        'data': result
    }
    return jsonify(response)


#########################################
#            eightzodiac_process(자평)           #
#########################################


#########################################
#                  타로                 #
#########################################

@app.route('/tarot_intro')
def tarot_intro():
    return render_template('tarot/tarot_intro.html')
@app.route('/tarot')
def tarot():
    return render_template('tarot/tarot_index.html')

@app.route('/tarot/result')
def tarot_result():
    tarot_result = session.get('tarot_result', None)

    data = session.get('data', {})
    return render_template('tarot/tarot_result.html', tarot_result=tarot_result)  # 결과 페이지에서 데이터 표시

@app.route('/tarot_process', methods=['POST'])
def tarot_process():
    # 클라이언트로부터 JSON 데이터를 받음
    card_data = request.get_json()


    if not card_data:
        return jsonify({'error': 'No data provided'}), 400  # 데이터가 없으면 400 에러 반환

    data = get_tarot_data(card_data)

    # 받은 card_data를 처리 (여기서는 단순 출력)
    session.clear()
    session['tarot_result'] = data
    return jsonify({'redirect': url_for('tarot_result')})

#########################################
#                  타로                 #
#########################################



#########################################
#                 별자리                 #
#########################################
@app.route('/dailystarzodiac')
def dailystarzodiac():
    data = get_dailystarzodiac_data()

    # 받은 card_data를 처리 (여기서는 단순 출력)
    session.clear()
    session['dailystarzodiac_result'] = data

    return render_template('dailystarzodiac/dailystarzodiac_index.html')

#########################################
#                 별자리                 #
#########################################





#########################################
#                사이트맵                #
#########################################
@app.route('/sitemap.xml')
def sitemap():
    # 사이트의 URL 목록
    urls = [

        {'loc': url_for('index', _external=True), 'lastmod': '2024-11-05', 'changefreq': 'daily', 'priority': 1.0},
        {'loc': url_for('intro', _external=True), 'lastmod': '2024-11-05', 'changefreq': 'daily', 'priority': 0.9},
        {'loc': url_for('hexagram', _external=True), 'lastmod': '2024-11-05', 'changefreq': 'daily', 'priority': 0.7},


        {'loc': url_for('tarot', _external=True), 'lastmod': '2024-11-05', 'changefreq': 'daily', 'priority': 0.7},
        {'loc': url_for('tarot_intro', _external=True), 'lastmod': '2024-11-05', 'changefreq': 'daily', 'priority': 0.7},
        {'loc': url_for('chizodiac', _external=True), 'lastmod': '2024-11-05', 'changefreq': 'daily', 'priority': 0.7},
        {'loc': url_for('chizodiac_intro', _external=True), 'lastmod': '2024-11-05', 'changefreq': 'daily', 'priority': 0.7},
        {'loc': url_for('eightzodiac', _external=True), 'lastmod': '2024-11-05', 'changefreq': 'daily','priority': 0.7},
        {'loc': url_for('eightzodiac_intro', _external=True), 'lastmod': '2024-11-05', 'changefreq': 'daily','priority': 0.7},

        {'loc': url_for('dailystarzodiac', _external=True), 'lastmod': '2024-10-28', 'changefreq': 'daily','priority': 0.7}

        # 추가 URL을 여기에 추가
    ]

    # XML 사이트맵 생성
    xml = '''<?xml version="1.0" encoding="UTF-8"?>
    <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'''  # 네임스페이스 수정

    for url in urls:
        xml += f'''
        <url>
            <loc>{url['loc']}</loc>
            <lastmod>{url['lastmod']}</lastmod>
            <changefreq>{url['changefreq']}</changefreq>
            <priority>{url['priority']}</priority>
        </url>'''

    xml += '''</urlset>'''
    return Response(xml, mimetype='application/xml')

#########################################
#                사이트맵                #
#########################################




#########################################
#                robots                 #
#########################################
@app.route('/robots.txt')
def serve_robots():
    return send_from_directory('', 'robots.txt')  # '' means the current directory

#########################################
#                robots                 #
#########################################

#########################################
#                rss                    #
#########################################
@app.route('/rss.xml')
def rss():
    rss_feed = generate_rss()
    return Response(rss_feed, mimetype="application/rss+xml")

#########################################
#                rss                 #
#########################################



if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=80)
