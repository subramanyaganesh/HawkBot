from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .core import Core
from .serializers import JsonResponseSerializer

@api_view(['POST'])
def get_json_response(request):
    try:
        # Retrieve the raw text question from the request body
        question = request.body.decode('utf-8')
    except UnicodeDecodeError:
        return Response({'error': 'Invalid encoding in the request body'}, status=status.HTTP_400_BAD_REQUEST)

    if not question:
        return Response({'error': 'Question not provided in the request body'}, status=status.HTTP_400_BAD_REQUEST)

    answer = Core.core(question)
    print('The answer from the view is', answer)
    print('The question from the request is', question)

    # You can customize the response data as needed
    response_data = {'question': question, 'answer': answer}
    serializer = JsonResponseSerializer(response_data)
    return JsonResponse(serializer.data)
