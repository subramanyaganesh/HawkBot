from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .core import Core
from .serializers import JsonResponseSerializer
from embedchain import Pipeline as App
import os
from django.conf import settings

@api_view(['POST'])
def get_json_response(request):
    try:
        # Retrieve the raw text question from the request body
        question = request.body.decode('utf-8')
    except UnicodeDecodeError:
        return Response({'error': 'Invalid encoding in the request body'}, status=status.HTTP_400_BAD_REQUEST)

    if not question:
        return Response({'error': 'Question not provided in the request body'}, status=status.HTTP_400_BAD_REQUEST)

    os.environ["OPENAI_API_KEY"] = settings.OPENAI_KEY
    hawk_bot = App.from_config(config_path=os.path.join(os.path.dirname(__file__), "openai.yaml"))
    answer,sources =hawk_bot.query(question, citations=True)
    
    
    response_data = {'question': question, 'answer': answer+str(sources), 'sources': str(sources)}

    # Return the JSON response
    serializer = JsonResponseSerializer(response_data)
    return JsonResponse(serializer.data)



# if not dynamic_instance:
#         dynamic_instance = DynamicModel(data={'hawk_bot': Core.core()})
#         dynamic_instance.save()
# dynamic_instance = DynamicModel.objects.first()