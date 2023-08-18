from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=40, validators=[MinLengthValidator(3)])
    surname = models.CharField(max_length=60)
    feedback = models.TextField()
    rating=models.PositiveIntegerField()
    error_messages = {
        'name': {'max_length': 'ой как много символов',
                 'min_length': 'ой как мало символов',
                 'required': 'Не должно быть пустым'
                 },
        'surname': {'max_length': 'ой как много символов',
                    'min_length': 'ой как мало символов',
                    'required': 'Не должно быть пустым'
                    },
        'feedback': {'max_length': 'ой как много символов',
                     'min_length': 'ой как мало символов',
                     'required': 'Не должно быть пустым'
                     }
    }