# Measurements
TEMPERATURE = 'temperature'
PRESSURE = 'pressure'
HUMIDITY = 'humidity'

MEASUREMENTS = [TEMPERATURE, PRESSURE, HUMIDITY, ]

measurements_translation = {
    TEMPERATURE: 'temperatura',
    PRESSURE: 'pressão',
    HUMIDITY: 'umidade',
}

# Metrics
AVERAGE = 'average'
MEDIAN = 'median'
MOVING_AVERAGE_24H = 'moving_average_24h'
MOVING_AVERAGE_7D = 'moving_average_7d'

METRICS = [AVERAGE, MEDIAN, MOVING_AVERAGE_24H, MOVING_AVERAGE_7D, ]

metrics_translation = {
    AVERAGE: 'média',
    MEDIAN: 'mediana',
    MOVING_AVERAGE_24H: 'média móvel 24h',
    MOVING_AVERAGE_7D: 'média móvel 7d',
}

WINDOW_SIZE_24H = 2016
WINDOW_SIZE_7D = 288
