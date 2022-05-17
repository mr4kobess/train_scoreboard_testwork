from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from train.forms import SearchTrainsForm
from train.models import Train
from .serializers import TrainSerializer


class TrainViewSet(ModelViewSet):
    serializer_class = TrainSerializer
    queryset = Train.objects.all()

    # def list(self, request):
    #     search_form = SearchTrainsForm(request.GET)
    #     if search_form.is_valid():
    #         _data = {key: value for key, value in search_form.cleaned_data.items() if value}
    #         trains = Train.objects.filter(**_data)
    #     else:
    #         trains = Train.objects.all()
    #     serializer = TrainSerializer(trains, many=True)
    #     return Response(serializer.data)

    def get_queryset(self):
        search_form = SearchTrainsForm(self.request.GET)
        if search_form.is_valid():
            _data = {key: value for key, value in search_form.cleaned_data.items() if value}
            trains = Train.objects.filter(**_data)
        else:
            trains = Train.objects.all()
        return trains
