from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Classroom
class ClassroomListViewTest(APITestCase):
    def setUp(self):
        user = User.objects.create_user(username="laila", password="1234567890-=")
        classroom1 = {'year': '4', 'name': "yaaay", 'teacher': user}
        classroom2 = {'name':"booo" , 'year': '5', 'teacher': user}
        Classroom.objects.create(**classroom1)
        Classroom.objects.create(**classroom2)
    def test_url(self):
        response = self.client.get(reverse('api-classroom-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_serializer(self):
        response = self.client.get(reverse('api-classroom-list'))
        classrooms = Classroom.objects.all()
        for index, classroom in enumerate(classrooms):
            self.assertEqual(classroom.name, response.data[index]['name'])
            self.assertEqual(str(classroom.year), str(response.data[index]['year']))
            self.assertEqual(classroom.teacher.id, response.data[index]['teacher'])
class ClassroomDetailViewTest(APITestCase):
    def setUp(self):
        user = User.objects.create_user(username="laila", password="1234567890-=")
        classroom1 = {'name': "yaaay", 'year': 4, 'teacher': user}
        classroom2 = {'name':"booo" , 'year': 5, 'teacher': user}
        Classroom.objects.create(**classroom1)
        Classroom.objects.create(**classroom2)
    def test_url(self):
        response = self.client.get(reverse('api-classroom-detail', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_serializer(self):
        id = 1
        response = self.client.get(reverse('api-classroom-detail', args=[id]))
        classroom = Classroom.objects.get(id=id)
        self.assertEqual(classroom.name, response.data['name'])
        self.assertEqual(classroom.year, response.data['year'])
        self.assertEqual(classroom.teacher.id, response.data['teacher'])
class ClassroomCRUDTest(APITestCase):
    def setUp(self):
        user = User.objects.create_user(username="laila", password="1234567890-=")
        classroom1 = {'name': "yaaay", 'year': '4', 'teacher': user}
        classroom2 = {'name':"booo" , 'year': '5', 'teacher': user}
        Classroom.objects.create(**classroom1)
        Classroom.objects.create(**classroom2)
        self.data = {'name': "y", 'year': '8', 'subject': 'Django'}
    def test_authorized_create(self):
        response = self.client.post(reverse('api-login'), {"username" : "laila", "password": "1234567890-="})
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + response.data['access'])
        response = self.client.post(reverse('api-classroom-create'), data=self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        classrooms = Classroom.objects.all()
        self.assertEqual(classrooms.count(), 3)
        self.assertEqual(classrooms.last().teacher.username, "laila")
        self.assertEqual(classrooms.last().name, self.data['name'])
        self.assertEqual(str(classrooms.last().year), str(self.data['year']))
    def test_update(self):
        id = 1
        response = self.client.put(reverse('api-classroom-update', args=[id]), data=self.data)
        classroom = Classroom.objects.get(id=id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(classroom.teacher.username, "laila")
        self.assertEqual(classroom.name, self.data['name'])
        self.assertEqual(str(classroom.year), str(self.data['year']))
    def test_delete(self):
        id = 1
        response = self.client.delete(reverse('api-classroom-delete', args=[id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        classroom_exists = Classroom.objects.filter(id=id).exists()
