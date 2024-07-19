from flask import Flask, render_template
import os
import socket

app = Flask(__name__)

# 색상 코드 정의
color_codes = {
    'grey': '#A7C7E7',
    'blue': '#30336b',
    'beige': '#F5F5DC'
}

# 환경 변수에서 색상 가져오기
COLOR = os.getenv('COLOR', 'white')
color = color_codes.get(COLOR, 'white')

@app.route("/")
def main():
    # return 'Hello'
    return render_template('hello.html', name=socket.gethostname(), color=color)

# route by color pass color
@app.route("/<user>")
def user(user):
    return render_template('hello.html', name=socket.gethostname(), color=color, user=user) 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
