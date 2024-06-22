from flask_app import app as app_flask

# MySQL
from controllers.medicos import medicos_bp
from controllers.cat_esp import categorias_bp
from controllers.medicos_esp import medicos_esp_bp
from controllers.disponibilidades import disponibilidades_bp

# MongoDB
from controllers.tratamientos import tratamientos_bp

app_flask.register_blueprint(medicos_bp)
app_flask.register_blueprint(categorias_bp)
app_flask.register_blueprint(medicos_esp_bp)
app_flask.register_blueprint(disponibilidades_bp)
app_flask.register_blueprint(tratamientos_bp)

if __name__ == '__main__':
    app_flask.run(debug=False, port=5000)
