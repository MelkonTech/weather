
# YOYO Weather App

This project represents a REST API for getting information about weather forecasts (maximum, minimum, average, and median) for a specific location.


## Installation

Install project with pipenv

```bash
  pipenv shell
  pipenv install
  python manage.py runserver 
```

or using virtual enviroment
```bash
  pip install -r requiraments.txt
  python manage.py runserver 
```

    
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`SECRET_KEY`

`WEATHER_API_KEY`

  
## API Reference

#### Get infromation about weather in city.

```http
  GET /api/locations/${city}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `days` | `string` | **Required**. Number of days 1-3 (Weather API allows only up to 3 days) |

## Tech Stack

**Server:** Python, Django, REST Framework, Swagger UI

  
## Acknowledgements

 - [Weather API](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Django Framework](https://www.djangoproject.com/)
 - [Django REST Framework](https://www.django-rest-framework.org/)
 - [Python Documentation](https://www.python.org/)
 - [Swagger UI](https://swagger.io/tools/swagger-ui/)
 

  
## Support

For support, email melkon.hovhannisian@gmail.com.

  