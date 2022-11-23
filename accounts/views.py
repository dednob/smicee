
# Create your views here.
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import *


# Create your views here.
@api_view(['POST'])
def RegisterView(request):
    user_data = request.data
    serializer_user = UserSerializer(data = user_data)

    account_data = {
        'role':request.data['role'],
        'phone_no': request.data['phone_no']

    }
    serializer_account = AccountSerializer(data = account_data)
    if serializer_account.is_valid() and serializer_user.is_valid():
        user = serializer_user.save()
        
        account = serializer_account.save(user=user)
        refresh = RefreshToken.for_user(user)
        return Response(
            {
                'success': 'You are authenticated',
                'user Id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'role': account.role,
                'refresh': str(refresh),
                'access': str(refresh.access_token)}
        )
    else:
            return Response(serializers.errors)
