# Proyecto Flask MVC para Integración de Datos en BigQuery

Este proyecto utiliza Flask en un patrón Modelo-Vista-Controlador (MVC) para conectarse a una API externa, validar la respuesta y luego insertar los datos en BigQuery. La aplicación proporciona una interfaz web para realizar estas operaciones de manera sencilla.

## Instalación

1. Asegúrate de tener Python instalado en tu sistema. Puedes descargarlo desde [python.org](https://www.python.org/downloads/).
2. Instala las bibliotecas necesarias utilizando pip:
    ```bash
    pip install Flask requests pandas google-cloud-bigquery
    ```

## Configuración

1. Crea un archivo `config.py` en la raíz del proyecto con la configuración necesaria. Aquí puedes definir la configuración para Flask, la URI de la base de datos (si es necesario) y el ID de proyecto de BigQuery.

2. Configura las credenciales de BigQuery en tu entorno para que la aplicación pueda conectarse correctamente.

## Estructura de Archivos

```
proyecto_flask/
├── app/
│   ├── controllers/
│   │   └── api_controller.py
│   ├── models/
│   │   └── data_model.py
│   ├── templates/
│   │   ├── index.html
│   │   └── success.html
│   └── app.py
├── config.py
└── README.md
```

## Uso

1. Configura el archivo `config.py` con las variables de entorno necesarias.
2. Ejecuta el archivo `app.py` para iniciar la aplicación Flask:
    ```bash
    python app.py
    ```
3. Abre un navegador y ve a `http://localhost:5000` para acceder a la interfaz web.
4. Desde la interfaz, puedes realizar la operación de conexión a la API, validación de datos y posterior inserción en BigQuery.

## Contribuciones

Las contribuciones son bienvenidas. Si tienes sugerencias, correcciones o mejoras para este proyecto, no dudes en abrir un issue o enviar un pull request.

