from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.generics import get_object_or_404
from .models import Fundraiser, Pledge, Favourite
from .permissions import IsOwnerOrReadOnly
from .serializers import FundraiserSerializer, PledgeSerializer, FundraiserDetailSerializer, FavouriteSerializer

class FundraiserList(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    def get(self, request):
        fundraisers = Fundraiser.objects.all()
        serializer = FundraiserSerializer(fundraisers, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = FundraiserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
class FundraiserDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    def get(self, request,pk):
        fundraiser = get_object_or_404(Fundraiser, pk=pk)
        serializer = FundraiserDetailSerializer(fundraiser)
        return Response(serializer.data)
    
    def put(self, request, pk) :
        fundraiser = get_object_or_404(Fundraiser, pk=pk) #update Fundraiser, we do care about the pk (PUT).
        self.check_object_permissions(request, fundraiser)
        serializer = FundraiserDetailSerializer( #Business rule > only owner of fundraiser can update
            instance=fundraiser, 
            data=request.data,
            partial=True #special option in Django. PUT(update something > all fields), PATCH (some fields updated). 
        ) #HTTP spec - not all frameworks will follow HTTP methods > HTTP methods were added in later. Some firewalls don't allow PATCH requests.
        if serializer.is_valid(): #telling serializer > JSON data come in > is it valid or not > required fields come from DB table
            serializer.save()
            return Response(serializer.data) #return JSON object of what we saved 
        
        return Response(
            serializer.error_messages,
            status=status.HTTP_400_BAD_REQUEST
        ) #added in functionality to update a Fundraiser
                
class PledgeList(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]
    
    def get(self, request):
        pledges = Pledge.objects.all()
        serializer = PledgeSerializer(pledges, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PledgeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(supporter=request.user) #can
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class FavouriteCreate(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        fundraiser = get_object_or_404(Fundraiser, pk=pk)
        # Check if already favourited
        if Favourite.objects.filter(user=request.user, fundraiser=fundraiser).exists():
            return Response(
                {"detail": "You have already favourited this puppy."},
                status=status.HTTP_400_BAD_REQUEST
            )
        favourite = Favourite.objects.create(user=request.user, fundraiser=fundraiser)
        serializer = FavouriteSerializer(favourite)
        return Response(serializer.data, status=status.HTTP_201_CREATED)