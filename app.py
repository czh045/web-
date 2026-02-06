
# import hashlib
# data="czh"
# obj=hashlib.md5()
# obj.update(data.encode('utf-8'))
# print(obj.hexdigest())
from flask import Flask, render_template,request

app = Flask(__name__)
@app.route('/show/infer')
def show_infer():
    return render_template("index.html")

@app.route('/get/manager')
def get_manager():
    return render_template("manager.html")

@app.route('/get/user')
def get_user():
    return render_template("user.html")

@app.route('/get/register')
def get_register():
    return render_template("register.html")

# @app.route('/do/reg',methods=['get'])
# def do_reg():
#     print(request.args)
#     return "注册成功"

@app.route('/do/reg',methods=['POST'])
def do_reg():
    print(request.form)
    return "注册成功"

if __name__ == '__main__':
    app.run()

