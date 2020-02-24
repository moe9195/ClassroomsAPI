from django.shortcuts import render
from classes.models import Classroom
from API.serializers import ListSerializer, DetailSerializer, UpdateSerializer, CreateSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView

class ListView(ListAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ListSerializer

class DetailView(RetrieveAPIView):
	queryset = Classroom.objects.all()
	serializer_class = DetailSerializer
	lookup_field = "id"
	lookup_url_kwarg = "classroom_id"

class CreateView(CreateAPIView):
	serializer_class = UpdateSerializer

	def perform_create(self, serializer):
		serializer.save(teacher=self.request.user)

class UpdateView(RetrieveUpdateAPIView):
    queryset = Classroom.objects.all()
    serializer_class = UpdateSerializer
    lookup_field = "id"
    lookup_url_kwarg = "classroom_id"

class DeleteView(DestroyAPIView):
    queryset = Classroom.objects.all()
    lookup_field = "id"
    lookup_url_kwarg = "classroom_id"
