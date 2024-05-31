from flask import Flask
from app.controllers import api_controller, view_controller
from app.models import DataModel

app = Flask(__name__)

# Configurar la ruta para los archivos estáticos
app.static_folder = 'static'

# Registrar los blueprints de los controladores
app.register_blueprint(api_controller.api_bp)
app.register_blueprint(view_controller.view_bp)

# Crear una instancia de DataModel para usarla en tu aplicación
data_model = DataModel()

