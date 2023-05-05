## Usage:

``` sh
docker build -t openweather .
```

``` sh
docker run --rm -v $(pwd):/output openweather Prague Milan Paris London Berlin Brno
```

The resulting pdf will appear in the current working directory under the name result.pdf
