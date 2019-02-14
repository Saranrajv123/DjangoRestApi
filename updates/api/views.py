from updates.models import Update as UpdateModel

class UpdateModelDetailAPIView():
    def get(self, request, *args, **kwargs):
        return