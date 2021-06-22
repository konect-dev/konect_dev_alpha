from .serializers import *
from .models import *
from rest_framework import viewsets, permissions, generics
from rest_framework import status
from rest_framework.response import Response
from knox.models import AuthToken

# status api


class StatusViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = StatusSerializer

    def queryset(self):
        # using the related name 'statuses' as declared in models
        return self.request.user.statuses.all()

    def perform_create(self, serializer):
        query = self.request.user.statuses.all()

        if len(query) == 0:
            serializer.save(user=self.request.user)

        else:
            serializers.ValidationError(
                {'status': 'A status already exists'}
            )

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

# register api


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": Authtoken.objects.create(user)[1]
        })

# Login api


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": Authtoken.objects.create(user)[1]
        })

# get user api


class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = UserSerializer

    def get(self, request):
        user = request.user
        queryset = Status.objects.filter(user=user)
        serializer = UserSerializer(user, many=True)
        get_status = StatusSerializer(queryset, many=True)

        print(get_status)
        return Response({
            "user": serializer.data,
            "status": get_status.data
        })

# auto complete api


class AutoComplete(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny, ]
    serializer_class = UserSerializer
    http_method_names = ['get']

    def get(self, request):
        serializer = UserSerializer(request.user, many=False)
        suggestions = ["wiring", "alignment", "electrics", "engines",
                       "wheel_balancing", "flat_tyres", "computer_aided_mechanics"]
        return Response({
            "suggestions": suggestions
        })

# profile viewsets


class ProfileViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = ProfileSerializer

    def get_queryset(self):
        statuses = self.request.user.profiles.all()
        return statuses

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)


class ProfileViewSet_(viewsets.ModelViewSet):
    def get_permissions(self):
        if self.action == "retrieve":
            self.permission_classes = [permissions.AllowAny, ]
        else:
            self.permission_classes = [permissions.IsAuthenticated, ]

        return super(ProfileViewSet_, self).get_permissions()

    serializer_class = ProfileSerializer
    queryset = ServiceProvider.objects.all()
    http_method_names = ['get']
