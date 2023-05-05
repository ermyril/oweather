## Usage:

``` sh
docker build -t openweather .
```

The application supposed to get the credentials to access openweather api from the API_KEY environment variable

``` sh
API_KEY="your_api_key_here" docker run --rm -v $(pwd):/output openweather Prague Milan Paris London Berlin Brno
```

The resulting pdf will appear in the current working directory under the name result.pdf
