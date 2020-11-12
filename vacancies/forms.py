from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import ModelForm

from vacancies.models import Resume


class UserResumeForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Сохранить'))

    class Meta:
        model = Resume
        fields = ['status', 'salary', 'specialty', 'grade', 'education', 'experience', 'portfolio']
        labels = {
            'status': 'Готовность к работе',
            'salary': 'Ожидаемое вознаграждение',
            'specialty': 'Специализация',
            'grade': 'Квалификация',
            'education': 'Образование',
            'experience': 'Опыт работы',
            'portfolio': 'Ссылка на портфолио'
        }
