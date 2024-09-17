from turtle import pd

from django.http import HttpResponse
from rest_framework import viewsets, permissions
from .serializers import *


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    def get_permissions(self):
        if self.action in ("create", "update", "destroy"):
            self.permission_classes = (permissions.IsAuthenticated,)
        else:
            self.permission_classes = (permissions.AllowAny,)

        return super().get_permissions()


class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer

    def get_permissions(self):
        if self.action in ("create", "update", "destroy"):
            self.permission_classes = (permissions.IsAuthenticated,)
        else:
            self.permission_classes = (permissions.AllowAny,)

        return super().get_permissions()


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def get_permissions(self):
        if self.action in ("create", "update", "destroy"):
            self.permission_classes = (permissions.IsAuthenticated,)
        else:
            self.permission_classes = (permissions.AllowAny,)

        return super().get_permissions()


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action in ("update", "destroy"):
            self.permission_classes = (permissions.IsAuthenticated,)
        else:
            self.permission_classes = (permissions.AllowAny,)

        return super().get_permissions()


def ExportData(request):
    format = request.GET.get("format", "xlsx")
    data = Country.objects.all()

    if format == "xlsx":
        df = pd.DataFrame(list(data.values()))
        response = HttpResponse(
            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        response["Content-Disposition"] = 'attachment; filename="exported_data.xlsx"'
        df.to_excel(response, index=False)
        return response
    elif format == "csv":
        df = pd.DataFrame(list(data.values()))
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="exported_data.csv"'
        df.to_csv(response, index=False)
        return response
    else:
        return HttpResponse(
            'Invalid format parameter. Please specify "xlsx" or "csv".', status=400
        )
