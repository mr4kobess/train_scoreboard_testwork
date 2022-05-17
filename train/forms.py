from django import forms
from .models import Train, City


class SearchTrainsForm(forms.Form):
    departure_city = forms.ModelChoiceField(queryset=City.objects.all(), label='Откуда', required=False)
    arrival_city = forms.ModelChoiceField(queryset=City.objects.all(), label='Куда', required=False)
    status = forms.ChoiceField(choices=Train.STATUS, label='Статус', required=False, )

    class Meta:
        fields = ('departure_city', 'arrival_city', 'status')


class TrainForm(forms.ModelForm):
    departure_city = forms.ModelChoiceField(queryset=City.objects.all(), label='Город отправления')
    arrival_city = forms.ModelChoiceField(queryset=City.objects.all(), label='Город прибытия')

    class Meta:
        model = Train
        fields = (
            'num',
            'departure_city',
            'departure_time',
            'arrival_city',
            'arrival_time',
            'status',
            'platform_number',
            'detained_time',
        )