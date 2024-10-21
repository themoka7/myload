from flask import Flask, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__)
#CORS(app)

# Flask가 현재 디렉터리에서 템플릿을 찾을 수 있도록 설정
app = Flask(__name__, static_folder='static', template_folder='.')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hexagram')
def hexagram():
    return render_template('hexagram/index.html')
@app.route('/execute', methods=['POST'])
def execute():


    result = "파이썬 코드가 실행되었습니다!"
    print("파이썬 코드가 실행되었습니다!")
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=80)
