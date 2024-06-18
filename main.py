from flask_app import app as app_flask
from controllers.medicos import medicos_bp
from controllers.cat_esp import categorias_bp
from controllers.tratamientos import tratamientos_bp

app_flask.register_blueprint(medicos_bp)
app_flask.register_blueprint(categorias_bp)
app_flask.register_blueprint(tratamientos_bp)

if __name__ == '__main__':
    app_flask.run(debug=False, port=5000)
