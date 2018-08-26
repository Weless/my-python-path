from flask import Flask,make_response

app = Flask(__name__)
app.config.from_object('config') # 参数模块路径，导入配置文件

@app.route('/hello/')
def hello_world():
    # status code
    # content-type http headers 告诉浏览器怎么解析
    # coutent-type 默认值为 text/html
    # 本质返回Response对象
    headers = {
        'content-type':'text/plain',
    }
    # response = make_response('<html></html>',301)
    # response.headers = headers

    return '<html></html>',200,headers # 用到最多

# app.add_url_rule('/hello',view_func=hello_world) 另外一种路由定义方式

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG']) # debug模式不能被外网访问，甚至同一个局域网
# app.config是字典的子类
# 部署：配置文件
# 生产环境 nginx+uwsgi
# 为什么加if？ flask内置web服务器和uwsgi服务器会冲突