import aiohttp
import asyncio

async def geocoding(city_name: str, state_code: str, country_code: str, api_key: str):
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&limit={1}&appid={api_key}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.ok:
                data = await response.json()
                lat = data[0]['lat']
                lon = data[0]['lon']
                print(f"Координаты {city_name}: широта {lat}, долгота {lon}")
                return lat, lon
            else:
                print(f"Ошибка получения данных для {city_name}. Код ответа: {response.status}")
                print(await response.text())


async def get_weather(lat, lon, api_key: str):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={api_key}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.ok:
                data = await response.json()
                weather = data['weather'][0]['description']
                temp = data['main']['temp']
                humidity = data['main']['humidity']
                pressure = data['main']['pressure']
                print(f"Погода: {weather}, температура: {temp}°C, влажность: {humidity}%, давление: {pressure} hPa")
            else:
                print(f"Ошибка получения данных для {city_name}. Код ответа: {response.status}")
                print(await response.text())

api_key = '10b9fb2830677a4829d766df0d388cd6'
city_name = 'Бздюли'

async def main():
    coordinates = await geocoding(city_name, 'Kirov', 'RU', api_key)
    await get_weather(*coordinates, api_key)

loop = asyncio.new_event_loop()
loop.run_until_complete(main())
