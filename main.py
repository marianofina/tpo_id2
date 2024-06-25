from flask_app import app as app_flask

# MySQL
from controllers.medicos import medicos_bp
from controllers.cat_esp import categorias_bp
from controllers.medicos_esp import medicos_esp_bp
from controllers.disponibilidades import disponibilidades_bp
from controllers.usuarios import usuarios_bp
from controllers.contactos_eme import contactos_eme_bp
from controllers.pacientes import pacientes_bp
from controllers.citas import citas_bp
from controllers.rep_usuarios import rep_usuarios_bp

# MongoDB
from controllers.tratamientos import tratamientos_bp
from controllers.hospitalizaciones import hospitalizaciones_bp
from controllers.historiales_medicos import historial_medico_bp

app_flask.register_blueprint(medicos_bp)
app_flask.register_blueprint(categorias_bp)
app_flask.register_blueprint(medicos_esp_bp)
app_flask.register_blueprint(disponibilidades_bp)
app_flask.register_blueprint(usuarios_bp)
app_flask.register_blueprint(contactos_eme_bp)
app_flask.register_blueprint(pacientes_bp)
app_flask.register_blueprint(citas_bp)
app_flask.register_blueprint(rep_usuarios_bp)
app_flask.register_blueprint(tratamientos_bp)
app_flask.register_blueprint(hospitalizaciones_bp)
app_flask.register_blueprint(historial_medico_bp)

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    port = 5000
    httpd = make_server('', port, app_flask)
    print("Serving on port " + str(port))
    httpd.serve_forever()
