import requests
from rest_framework.views import APIView
from rest_framework.response import Response


class WeatherView(APIView):
    def get(self, request):
        api_key = "605f642bfb6aef1cf2e6ee80d9f9df46"
        city = request.query_params.get("city")
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"

        response = requests.get(url)
        data = response.json()

        weather_data = {
            'Город': data['name'],
            "Температура:" : f'{data["main"]["temp"]}°C',
            "Погода:": data["weather"][0]["description"].title(),
            'Ощущается как': f'{data["main"]["feels_like"]}°C',
            'Макс температура' : f'{data["main"]["temp_max"]}°C',
            'Мин температура' : f'{data["main"]["temp_min"]}°C',
            'Скорость ветра' : f'{data["wind"]["speed"]}m/s',
        }

        return Response(weather_data)


class CurrencyView(APIView):
    def get(self, request):
        url = 'https://data.fixer.io/api/latest?access_key=ca329f511ffd5b97af860635609b9198&symbols=USD,RUB,KZT,KGS'

        response = requests.get(url)
        data = response.json()

        if not data.get("success"):
            return Response("Ошибка:", data["error"]["info"])
        else:
            rates = data["rates"]

            eur_to_kgs = rates["KGS"]

            usd_to_kgs = eur_to_kgs / rates["USD"]
            rub_to_kgs = eur_to_kgs / rates["RUB"]
            kzt_to_kgs = eur_to_kgs / rates["KZT"]

            currency_data = {
                "USD" :round(usd_to_kgs, 2),
                "EUR": round(eur_to_kgs, 2),
                "RUB": round(rub_to_kgs, 2),
                "KZT": round(kzt_to_kgs, 2)
            }

            return Response(currency_data)
