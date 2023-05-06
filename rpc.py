import json

import django
from nameko.rpc import rpc
from rest_framework.test import APIRequestFactory

django.setup()

from havij.views import HavijViewSet


class HavijRPC:
    name = "havij_wrapper"

    @rpc
    def get(self):
        self.factory = APIRequestFactory()
        request = self.factory.get("/havij", format="json")
        response = HavijViewSet.as_view({"get": "list"})(request)
        response.render()
        content = response.content

        return json.loads(content.decode("utf-8"))
