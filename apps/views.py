from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class TestView(viewsets.GenericViewSet):

    @action(methods='get', detail=False)
    def test_method(self, request):
        return Response({
            "test": 'test response'
        })
