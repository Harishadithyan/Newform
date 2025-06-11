from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import FeedbackSerializer

@api_view(['POST'])
def submit_feedback(request):
    serializer = FeedbackSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Thank you for your feedback!'})
    return Response(serializer.errors, status=400)
