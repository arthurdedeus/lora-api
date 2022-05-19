import statistics

from sensors import constants


def _get_average(_list: list) -> float:
    return statistics.mean(_list)


def _get_median(_list: list) -> float:
    return statistics.median(_list)


def _get_moving_average_24h(_list: list) -> float:
    if len(_list) > constants.WINDOW_SIZE_24H:
        return statistics.mean(_list[constants.WINDOW_SIZE_24H :])
    return statistics.mean(_list)


def _get_moving_average_7d(_list: list) -> float:
    if len(_list) > constants.WINDOW_SIZE_7D:
        return statistics.mean(_list[constants.WINDOW_SIZE_7D :])
    return statistics.mean(_list)


metrics_methods = {
    constants.AVERAGE: _get_average,
    constants.MEDIAN: _get_median,
    constants.MOVING_AVERAGE_24H: _get_moving_average_24h,
    constants.MOVING_AVERAGE_7D: _get_moving_average_7d,
}


def get_metrics(queryset):
    metrics = {}

    for measurement in constants.MEASUREMENTS:
        measurement_list = queryset.values_list(measurement, flat=True)
        metrics_list = []

        for metric in constants.METRICS:
            metrics_list.append(
                {
                    "name": constants.metrics_translation.get(metric).title(),
                    "value": globals()[f"_get_{metric}"](measurement_list),
                }
            )

        metrics.update({measurement: metrics_list})

    return metrics
