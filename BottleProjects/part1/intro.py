from bottle import run, route, template, view


@route('/')
@view('base_template')
def index():
    return dict(page='Index')

    
@route('/hello/<name>')
def greet(name='Stranger'):
    return template('Hello {{name}}, how are you?', name=name)

@route('/home')
def home():
    return template('Hello {{name}}! You are in Bottle', name='Maxim')


run(host='localhost', port=8080, debug=True)