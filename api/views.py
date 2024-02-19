from rest_framework.response import Response
from rest_framework.decorators import api_view
# from blog.models import Task
# from .serializers import TaskSerializer

from rest_framework import viewsets
from .serializers import UserSerializer
from django.contrib.auth.models import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
      
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'user_id': token.user_id})
    
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes

def send_password_reset_email(user):
    # Generate a unique token for password reset
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    # Send email with reset link containing token and uid
    # (You'll need to implement this part)

# In your view:
user = User.objects.get(email=request.data['email'])
send_password_reset_email(user)


import random

def generate_otp():
    return str(random.randint(1000, 9999))

# In your view:
otp = generate_otp()


from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_text

def reset_password(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        if default_token_generator.check_token(user, token):
            # Valid token, allow user to reset password
            # (You'll need to implement this part)
        else:
            # Invalid token
            # (You'll need to handle this case)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        # Invalid user ID
        # (You'll need to handle this case)
 
       
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_password(request):
    user = request.user
    old_password = request.data['old_password']
    new_password = request.data['new_password']
    if user.check_password(old_password):
        user.set_password(new_password)
        user.save()
        return Response({'message': 'Password changed successfully'})
    else:
        return Response({'error': 'Incorrect old password'}, status=400)


















# @api_view(['GET'])
# def apiOverview(request):
#     api_urls = {
#         'List':'/task-list/',
#         'Detail View':'/task-detail/<str:pk>/',
#         'Create':'/task-create/',
#         'Update':'/task-update/<str:pk>/',
#         'Delete':'/task-delete/<str:pk>/',
#     }
#     return Response(api_urls)

# @api_view(['GET'])
# def taskList(request):
#     tasks = Task.objects.all()
#     serializer= TaskSerializer(tasks, many= True)
#     return Response(serializer.data)
    
# @api_view(['GET'])
# def taskDetail(request, pk):
#     tasks = Task.objects.get(id= pk)
#     serializer= TaskSerializer(tasks, many= False)
#     return Response(serializer.data)

# @api_view(['POST'])
# def taskCreate(request):
#     serializer= TaskSerializer(data= request.data)
    
#     if serializer.is_valid():
#         serializer.save()
        
#     return Response (serializer.data)

# @api_view(['POST'])
# def taskUpdate(request, pk):
#     task = Task.objects.get(id=pk)
#     serializer= TaskSerializer(instance=task, data=request.data)
    
#     if serializer.is_valid():
#         serializer.save()
        
#     return Response (serializer.data)

# @api_view(['DELETE'])
# def taskDelete(request, pk):
#     task = Task.objects.get(id=pk)
#     task.delete()
#     return Response ('Item successfully deleted!')





# @api_view(['GET'])
# def getData(request):
#     items = Item.objects.all()
#     serializer = ItemSerializer (items, many= True)
#     return Response (serializer.data) 

# @api_view(['POST'])
# def addItem(request):
#     serializer = ItemSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response (serializer.data)
