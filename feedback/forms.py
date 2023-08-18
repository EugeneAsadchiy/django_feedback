from django import forms
from .models import Feedback


# class FeedbackForm(forms.Form):
#     name = forms.CharField(label="Имя", max_length=7, min_length=2, error_messages={
#         "max_lenght": "Слишком много символов",
#         "min_lenght": "Слишком мало символов",
#         "required": "Укажите хотя бы один символ"
#     })
#     surname = forms.CharField()
#     feedback = forms.CharField(widget=forms.Textarea(attrs={"rows": 2, "cols": 20}))
#     rating=forms.IntegerField(label="Рейтинг", max_value=5, min_value=1,)

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        # fields = ["name", "surname", "feedback" , "rating"]
        fields = "__all__"
        # exclude=["rating"]
        labels = {
            "name": "Имя",
            "surname": "Фамилия",
            "feedback": "Отзыв",
            "rating": "Рейтинг",
        }
