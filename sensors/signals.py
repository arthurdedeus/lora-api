from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from sensors.models import Warning


from sensors.models import Log

@receiver(post_save, sender=Log)
def check_thresholds(instance, created, **kwargs):
    if created:
        sensor = instance.sensor
        thresholds = sensor.warning_thresholds

        warnings_to_create = []
        for quantity, value in instance.measurements().items():
            max_threshold, min_threshold = thresholds.get_thresholds(quantity)
            if value:
                if value > max_threshold:
                    warnings_to_create.append(
                        Warning(
                            sensor=sensor,
                            timestamp=timezone.now(),
                            measurement=quantity,
                            message=f'A medida de {quantity} ultrapassou o limite máximo de {max_threshold}. '
                                    f'O valor medido foi de {value}.'
                        )
                    )
                if value < min_threshold:
                    warnings_to_create.append(
                        Warning(
                            sensor=sensor,
                            timestamp=timezone.now(),
                            measurement=quantity,
                            message=f'A medida de {quantity} está abaixo do limite mínimo de {max_threshold}. '
                                    f'O valor medido foi de {value}.'
                        )
                    )

        if warnings_to_create:
            Warning.objects.bulk_create(warnings_to_create)