# Proyecto Flask MVC para Integración de Datos en BigQuery

Este proyecto utiliza Flask en un patrón Modelo-Vista-Controlador (MVC) para conectarse a una API externa, validar la respuesta y luego insertar los datos en BigQuery. La aplicación proporciona una interfaz web para realizar estas operaciones de manera sencilla.

## Instalación

1. Asegúrate de tener Python instalado en tu sistema. Puedes descargarlo desde [python.org](https://www.python.org/downloads/).
2. Instala las bibliotecas necesarias utilizando pip:
    ```bash
    pip install Flask requests pandas google-cloud-bigquery
    ```

## Configuración

1. Crea un archivo `config.py` en la raíz del proyecto con la configuración necesaria. Aquí puedes definir la configuración para Flask y el ID de proyecto de BigQuery.

2. Configura las credenciales de BigQuery en tu entorno para que la aplicación pueda conectarse correctamente.

## Estructura de Archivos

py-bigquery-api/
├── app/
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── api_controller.py
│   │   └── view_controller.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── data_model.py
│   ├── templates/
│   │   ├── index.html
│   │   ├── success.html
│   │   └── data_view.html
│   └── __init__.py
├── static/
│   └── styles.css
├── config.py
├── run.py
└── README.md

## Uso

1. Configura el archivo `config.py` con las variables de entorno necesarias.
2. Ejecuta el archivo `run.py` para iniciar la aplicación Flask:
    ```bash
    python run.py
    ```
3. Abre un navegador y ve a `http://localhost:5000` para acceder a la interfaz web.
4. Desde la interfaz, puedes realizar la operación de conexión a la API, validación de datos y posterior inserción en BigQuery.
5. También puedes acceder a la vista de datos en `http://localhost:5000/view_data` para visualizar la información obtenida.

## Contribuciones

Las contribuciones son bienvenidas
