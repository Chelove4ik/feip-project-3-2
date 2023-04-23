from flask import Flask

from flask_assets import Environment, Bundle

app = Flask(__name__, template_folder='../src/templates', static_folder='../src/static')

assets = Environment(app)
assets.url = app.static_url_path
assets.debug = True
scss = Bundle('styles/app.scss', filters='pyscss', depends=('styles/**/*.scss'), output='gen/app.css')
assets.register('scss_all', scss)
