from flask import Flask, render_template, request, redirect, url_for, Blueprint


view_blueprint = Blueprint('views', __name__)


@view_blueprint.route('/')
def hello():
    return '<html><body><h1>Hello World</h1></body></html>'


@view_blueprint.route('/home')
def home():
    return "Hello, World ~ !!! Text Text Text ~ !!!"


@view_blueprint.route('/data/view_blueprintInfo/<name>', methods=['GET'])
def queryDataMessageByName(name):
    print("type(name) : ", type(name))
    return 'String => {}'.format(name)


@view_blueprint.route('/page/text')
def pageText():
    return render_template('page.html', text="Python Flask !")


@view_blueprint.route('/page/view_blueprint')
def pageview_blueprintInfo():
    view_blueprintInfo = {  # dict
        'id': 5,
        'name': 'Python - Flask',
        'version': '1.0.1',
        'author': 'Enoxs',
        'remark': 'Python - Web Framework'
    }
    return render_template('page.html', view_blueprintInfo=view_blueprintInfo)


@view_blueprint.route('/page/data')
def pageData():
    data = {  # dict
        '01': 'Text Text Text',
        '02': 'Text Text Text',
        '03': 'Text Text Text',
        '04': 'Text Text Text',
        '05': 'Text Text Text'
    }
    return render_template('page.html', data=data)


@view_blueprint.route('/static')
def staticPage():
    return render_template('static.html')


@view_blueprint.route('/success/<name>')
def success(name):
    return 'welcome %s' % name


@view_blueprint.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form.get('nm')  # 使用 get 方法避免可能的 KeyError
        if user:
            return redirect(url_for('views.success', name=user))
        else:
            return 'Invalid input. Please provide a name.'
    else:
        return render_template('login.html')


@view_blueprint.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
