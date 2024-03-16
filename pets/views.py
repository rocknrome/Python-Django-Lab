from django.http import JsonResponse
from django.core.serializers import serialize
from django.views import View
from .models import Turtle, Dog, Cat, Bird
from .helpers import GetBody
import json

class TurtleView(View):
    def get(self, request):
        all_turtles = Turtle.objects.all()
        serialized_turtles = serialize("json", all_turtles)
        final_data = json.loads(serialized_turtles)
        return JsonResponse(final_data, safe=False)

    def post(self, request):
        body = GetBody(request)
        turtle = Turtle.objects.create(name=body["name"], age=body["age"])
        final_data = json.loads(serialize("json", [turtle]))
        return JsonResponse(final_data, safe=False)

class TurtleViewID(View):
    def get(self, request, id):
        turtle = Turtle.objects.get(id=id)
        final_data = json.loads(serialize("json", [turtle]))
        return JsonResponse(final_data, safe=False)

    def put(self, request, id):
        body = GetBody(request)
        Turtle.objects.filter(id=id).update(**body)
        turtle = Turtle.objects.get(id=id)
        final_data = json.loads(serialize("json", [turtle]))
        return JsonResponse(final_data, safe=False)

    def delete(self, request, id):
        turtle = Turtle.objects.get(id=id)
        turtle.delete()
        final_data = json.loads(serialize("json", [turtle]))
        return JsonResponse(final_data, safe=False)

class DogView(View):
    def get(self, request):
        all_dogs = Dog.objects.all()
        serialized_dogs = serialize("json", all_dogs)
        final_data = json.loads(serialized_dogs)
        return JsonResponse(final_data, safe=False)

    def post(self, request):
        body = GetBody(request)
        dog = Dog.objects.create(name=body["name"], age=body["age"])
        final_data = json.loads(serialize("json", [dog]))
        return JsonResponse(final_data, safe=False)

class DogViewID(View):
    def get(self, request, id):
        dog = Dog.objects.get(id=id)
        final_data = json.loads(serialize("json", [dog]))
        return JsonResponse(final_data, safe=False)

    def put(self, request, id):
        body = GetBody(request)
        Dog.objects.filter(id=id).update(**body)
        dog = Dog.objects.get(id=id)
        final_data = json.loads(serialize("json", [dog]))
        return JsonResponse(final_data, safe=False)

    def delete(self, request, id):
        dog = Dog.objects.get(id=id)
        dog.delete()
        final_data = json.loads(serialize("json", [dog]))
        return JsonResponse(final_data, safe=False)

class CatView(View):
    def get(self, request):
        all_cats = Cat.objects.all()
        serialized_cats = serialize("json", all_cats)
        final_data = json.loads(serialized_cats)
        return JsonResponse(final_data, safe=False)

    def post(self, request):
        body = GetBody(request)
        cat = Cat.objects.create(name=body["name"], age=body["age"])
        final_data = json.loads(serialize("json", [cat]))
        return JsonResponse(final_data, safe=False)

class CatViewID(View):
    def get(self, request, id):
        cat = Cat.objects.get(id=id)
        final_data = json.loads(serialize("json", [cat]))
        return JsonResponse(final_data, safe=False)

    def put(self, request, id):
        body = GetBody(request)
        Cat.objects.filter(id=id).update(**body)
        cat = Cat.objects.get(id=id)
        final_data = json.loads(serialize("json", [cat]))
        return JsonResponse(final_data, safe=False)

    def delete(self, request, id):
        cat = Cat.objects.get(id=id)
        cat.delete()
        final_data = json.loads(serialize("json", [cat]))
        return JsonResponse(final_data, safe=False)

class BirdView(View):
    def get(self, request):
        all_birds = Bird.objects.all()
        serialized_birds = serialize("json", all_birds)
        final_data = json.loads(serialized_birds)
        return JsonResponse(final_data, safe=False)

    def post(self, request):
        body = GetBody(request)
        bird = Bird.objects.create(name=body["name"], age=body["age"])
        final_data = json.loads(serialize("json", [bird]))
        return JsonResponse(final_data, safe=False)

class BirdViewID(View):
    def get(self, request, id):
        bird = Bird.objects.get(id=id)
        final_data = json.loads(serialize("json", [bird]))
        return JsonResponse(final_data, safe=False)

    def put(self, request, id):
        body = GetBody(request)
        Bird.objects.filter(id=id).update(**body)
        bird = Bird.objects.get(id=id)
        final_data = json.loads(serialize("json", [bird]))
        return JsonResponse(final_data, safe=False)

    def delete(self, request, id):
        bird = Bird.objects.get(id=id)
        bird.delete()
        final_data = json.loads(serialize("json", [bird]))
        return JsonResponse(final_data, safe=False)
