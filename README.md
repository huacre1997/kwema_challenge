# Kwema Challenge

## Descripción

El proyecto Kwema Challenge es una aplicación web desarrollada en Django que proporciona una API para calcular el número de bacterias en base a ciertos parámetros.

## Tecnologías Utilizadas

El proyecto utiliza las siguientes tecnologías:

- Python (v3.10.7)
- Django (v4.2.2)
- Django REST Framework (v3.14.0)

## Instalación

1. Clona este repositorio en tu máquina local:

   ```bash
   git clone https://github.com/huacre1997/kwema_challenge.git
   ```

2. Navega hasta el directorio del proyecto:

   ```bash
   cd kwema_challenge
   ```

3. Crea y activa un entorno virtual :

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

4. Instala las dependencias del proyecto:

   ```bash
   pip install -r requirements.txt
   ```

5. Ejecuta el proyecto:

   ```bash
   python manage.py runserver
   ```

6. Accede a la aplicación :

   ```
   http://localhost:8000
   ```

## Uso

La API proporciona un endpoint `/bacteria/count` que acepta una solicitud POST para calcular el número de bacterias. La solicitud debe incluir los siguientes parámetros en formato JSON:

```json
{
  "days": 60,
  "maturation_period": 4,
  "life_expectancy": 3,
  "reproduction_rate": 2
}
```

- `days`: Número de días para calcular el número de bacterias.
- `maturation_period`: Período de maduración de las bacterias.
- `life_expectancy`: Esperanza de vida de las bacterias.
- `reproduction_rate`: Tasa de reproducción de las bacterias.

Puedes utilizar herramientas como cURL o aplicaciones como Postman para enviar solicitudes a la API.

## Pruebas

Se han incluido pruebas unitarias para garantizar el correcto funcionamiento de los componentes clave del proyecto. Para ejecutar las pruebas, puedes utilizar el siguiente comando:

```bash
python manage.py test apps.bacteria.tests
```
