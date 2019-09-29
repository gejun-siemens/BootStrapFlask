from flask import Flask,render_template

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

#4.Flask应用程序实例的run方法,启动WEB服务器
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)
    print('dasd')