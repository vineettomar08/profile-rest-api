from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test APi View"""

    def get(self,request,format=None):
        """Returns a list of api Views"""

        an_apiview = [
            'Use to get all the views as a list',
            'vineet tomar',
            'keen to learning new things',
            'focused towards carrier'
        ]
        return Response({'message':'Hello!','an_apiview':an_apiview})
