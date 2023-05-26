This project is a currency conversion API that allows users to convert between USD, EUR, and EGP. The API has token-based authentication and maintains the count of requests for each pair of currencies.
Requirements
Python 3.x
Django 3.x
Django REST framework
openexchangerates.org API
Installation
Clone the repository to your local machine.
Install the required packages using pip: pip install -r requirements.txt
Set up an account with openexchangerates.org and obtain an API key.
Set the API key in the settings.py file.
Run the server using the command: python manage.py runserver
API Endpoints
/api/token/: This endpoint is used to obtain a token for authentication.
/api/convert/: This endpoint is used to convert between currencies. It requires the following parameters:
from_currency: The currency to convert from (USD, EUR, or EGP).
to_currency: The currency to convert to (USD, EUR, or EGP).
amount: The amount to convert.
Authentication
The API uses token-based authentication. To obtain a token, send a POST request to the /api/token/ endpoint with valid credentials. The token will be returned in the response.
Currency Conversion
The API uses the openexchangerates.org API to obtain up-to-date conversion rates. The count of requests for each pair of currencies is maintained in the database.
