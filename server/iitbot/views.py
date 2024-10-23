from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .core import Core
from .serializers import JsonResponseSerializer
from embedchain import Pipeline as App
import os
from django.conf import settings
import json

Core.core()
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
    stanford_bot = App.from_config(config_path=os.path.join(os.path.dirname(__file__), "openai.yaml"))
    
    creator_questions = [
    "who created you",
    "who are your creators",
    "who is your creator",
    "who created you?",
    "who are your creators?",
    "who is your creator?"
    ]
    check=False
    if question.lower().strip() in creator_questions:
        check=True
        answer, sources = "I was created by Subramanya Ganesh ", [(
    {'url': 'https://www.linkedin.com/in/subramanyaganesh/', 'score': 1},

    )

]
    else :
        answer,sources =stanford_bot.query(question, citations=True)
    
    unique_elements = {element['url'] for source in sources for element in source if isinstance(element, dict) and element.get('score', 0) > 0}

    
    response_data = {'question': question, 'answer': answer, 'sources':unique_elements, 'flag':check}

    # Return the JSON response
    serializer = JsonResponseSerializer(response_data)
    return JsonResponse(serializer.data)



# if not dynamic_instance:
#         dynamic_instance = DynamicModel(data={'stanford_bot': Core.core()})
#         dynamic_instance.save()
# dynamic_instance = DynamicModel.objects.first()