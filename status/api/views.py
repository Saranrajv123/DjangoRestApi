from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response

from Status.models import Status
from .serializers import StatusSerializer

class StatusListSearchApiView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        qs = Status.objects.all()
        serializer = StatusSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        qs = Status.objects.all()
        serializer = StatusSerializer(qs, many=True)
        return Response(serializer.data)



class StatusApiView(generics.ListAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = StatusSerializer

    def get_queryset(self):
        qs = Status.objects.all()
        query = self.request.GET.get('s')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs


class StatusCreateApiView(generics.CreateAPIView):
    permission_classses = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class StatusDetailApiView(generics.RetrieveAPIView):
    permission_classes = []
    authentication_class = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    lookup_field = 'id'

    # pass id to url 
    # def get_object(self, *args, *kwargs):
    #     kw_args = self.kwargs
    #     kw_id = kw_args.get('id')
    #     return Status.objects.get(id=kw_id)


class StatusUpdateApiView(generics.UpdateAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    lookup_field = 'id'

class StatusDeleteApiView(generics.DestroyAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    lookup_field = 'id'


     