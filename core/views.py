import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
currency_count = {}
def convert_currency(from_currency, to_currency, amount, currency_count):
    currency_key = f"{from_currency}_{to_currency}"
    
    if currency_key in currency_count:
        currency_count[currency_key] += 1
    else:
        currency_count[currency_key] = 1

    url = f"https://api.apilayer.com/currency_data/live?source={from_currency}"
    headers= {
        "apikey": "vYjKswNmxToPlFALdrwPQLQRwISb6prI"
    }
    response = requests.get(url, headers=headers)
    data = response.json()

    if 'quotes' not in data:
        return {'error': 'Could not retrieve exchange rates'}, status.HTTP_400_BAD_REQUEST

    exchange_rates = data['quotes']
    if f'{from_currency}{to_currency}' not in exchange_rates:
        return {'error': 'Could not retrieve exchange rates for specified currencies'}, status.HTTP_400_BAD_REQUEST

    converted_amount = float(amount) * exchange_rates[f'{from_currency}{to_currency}']

    response_data = {
        'converted_amount': converted_amount,
        'request_count': currency_count[currency_key]
    }

    return response_data, status.HTTP_200_OK

class CurrencyConverterView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        from_currency = request.GET.get('from_currency').upper()
        to_currency = request.GET.get('to_currency').upper()
        amount = request.GET.get('amount')

        response_data, status_code = convert_currency(from_currency, to_currency, amount, currency_count)

        return Response(response_data, status=status_code)