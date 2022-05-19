from rest_framework import views
from rest_auth.views import LogoutView
from rest_framework import permissions, generics
from django.template import RequestContext
from .send_email import send_conformation_email
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from .permissions import IsSelfUser
from . import serializers

# from rest_framework.pagination import PageNumberPagination
CustomUser = get_user_model()


# class PaginationClass(PageNumberPagination):
#     page_size = 5
#     page_size_query_param = 'page_size'
#     max_page_size = 1000


class RegistrationView(views.APIView):
    def post(self, request):
        serializer = serializers.RegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            if user:
                send_conformation_email(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class ActivationView(views.APIView):
    def get(self, request, activation_code):
        try:
            user = CustomUser.objects.get(activation_code=activation_code)
            user.is_active = True
            user.activation_code = ''
            user.save()
            return Response('user is active now', status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response('user doesn\'t exist', status=status.HTTP_400_BAD_REQUEST)


class LogOutView(LogoutView):
    permission_classes = permissions.IsAuthenticated


class UserDetailView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (IsSelfUser,)
    serializer_class = serializers.UserDetailSerializer


class CreateSuperUserView(views.APIView):

    def post(self, request):
        serializer = serializers.SuperUserCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            if user:
                send_conformation_email(user)
                context_instance = RequestContext(request)
            return Response('We have send you an activation code, please check your email', status=status.HTTP_200_OK,)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.UserSerializer
