#!/usr/bin/env python3

import os
import sys
import asyncio
import aiohttp
# from pprint import pprint as print

cities = sys.argv[1:]
API_KEY = os.environ.get("API_KEY")
API_URL = 'https://api.openweathermap.org'


def print_help():
    print("""
    Usage: oweather [CITYNAME ...]
           oweather --help
    """)

def check_input():
    if '--help' in cities:
        print_help()
        sys.exit(0)

    if len(cities) == 0:
        print("""    Error: The following required arguments were not provided: <CITYNAME> """, file=sys.stderr)
        print_help()
        sys.exit(1)

    if API_KEY == None:
        print("""    Error: Please provide environment variable API_KEY, containing the key to access the openweather api """, file=sys.stderr)
        sys.exit(1)

async def main():
    responses = {
        'success': [],
        'error': [],
    }

    async with aiohttp.ClientSession(API_URL) as session:
        for city in cities:
            params = {
                'q': city,
                'appid': API_KEY,
                'units': 'metric',
            }
            async with session.get('/data/2.5/weather', params=params) as response:
                status = 'success' if response.status == 200 else 'error'
                responses[status].append((city, await response.json()))


    for response in responses['error']:
        print(f"Error getting temperature for city: {response[0]}", file=sys.stderr)
    for response in responses['success']:
        print('{} {}°C'.format(response[1]['name'], response[1]['main']['temp']))

    sys.exit(int(len(responses['success']) == 0))

check_input()
asyncio.run(main())


