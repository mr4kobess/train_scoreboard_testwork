from django.shortcuts import render, get_object_or_404, redirect
from .models import Train
from .forms import SearchTrainsForm, TrainForm


def index(request):
    search_form = SearchTrainsForm(request.GET)
    if search_form.is_valid():
        # Фильтрация пустых значений формы, чтобы не фильтровать по пустым полям
        _data = {key: value for key, value in search_form.cleaned_data.items() if value}
        trains = Train.objects.filter(**_data)
    else:
        trains = Train.objects.all()
        search_form = SearchTrainsForm()
    return render(request, 'index.html', context={'trains': trains, 'search_form': search_form})


def train_view(request, train_id):
    train = get_object_or_404(Train, pk=train_id)
    train_form = TrainForm(request.POST or None, instance=train)
    if request.method == 'POST':
        if train_form.is_valid():
            train_form.save()
            return redirect("train:main-view")
    return render(request, "train.html", {'train_form': train_form, 'train': train})


def create_train_view(request):
    train_form = TrainForm(request.POST)
    if request.method == 'POST':
        if train_form.is_valid():
            train_form.save()
            return redirect("train:main-view")
    return render(request, "new_train.html", {'train_form': train_form})


def delete_train_view(request, train_id):
    train = get_object_or_404(Train, pk=train_id)
    if request.method == 'POST':
        train.delete()
        return redirect("train:main-view")
    return redirect("train:main-view")
