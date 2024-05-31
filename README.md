
# Proyecto de Integración de Datos a BigQuery

Este proyecto tiene como objetivo mostrar cómo insertar datos en una tabla de BigQuery utilizando Python y la biblioteca google-cloud-bigquery. En este caso, los datos pueden ser generados programáticamente o provenir de cualquier otro origen.

## Instalación

1. Asegúrate de tener instalado Python en tu sistema. Puedes descargarlo desde [python.org](https://www.python.org/downloads/).
2. Instala la biblioteca necesaria utilizando pip:
    ```bash
    pip install google-cloud-bigquery
    ```

## Configuración

Antes de ejecutar el proyecto, asegúrate de tener un proyecto creado en Google Cloud Platform y configurar BigQuery para tu proyecto.

## Uso

1. Modifica el archivo `config.py` con las credenciales de autenticación para BigQuery y el ID de tu proyecto.
2. Ejecuta el script `main.py` para cargar los datos (ya sea generados programáticamente o provenientes de otro origen) y insertarlos en BigQuery:
    ```bash
    python main.py
    ```

## Estructura de Archivos

- `config.py`: Archivo de configuración con las credenciales y la configuración de BigQuery.
- `main.py`: Archivo principal que contiene la lógica para cargar datos y realizar la inserción en BigQuery.
- `data_model.py`: Clase que representa el modelo de datos y contiene la lógica de inserción en BigQuery.
- `README.md`: Este archivo que describe el proyecto y su funcionamiento.

## Contribuciones

Las contribuciones son bienvenidas. Si tienes sugerencias, correcciones o mejoras para este proyecto, no dudes en abrir un issue o enviar un pull request.