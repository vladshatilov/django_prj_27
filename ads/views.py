from django.core.serializers import serialize
from django.http import JsonResponse
from django.shortcuts import render

import csv
import json

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Ads, Categories


def str2bool(v):
    return v.lower() in ("yes", "true", "t", "1")


def get(request):
    return JsonResponse({"status": "ok"}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class Category(View):
    def get(self, request):
        cats = Categories.objects.all()
        # cats_serialized = serialize('python', cats)
        cat_list = []
        for cat_item in cats:
            cat_list.append({
                "id": cat_item.id,
                "name": cat_item.name
            })
        return JsonResponse(cat_list, status=200, safe=False, json_dumps_params={'ensure_ascii': False})

    def post(self, request):
        try:
            data = json.loads(request.body)
            cat_item = Categories()
            cat_item.id = data.get('id',None)
            cat_item.name = data["name"]
            cat_item.save()
            return JsonResponse({"id": cat_item.id, "name": cat_item.name}, status=201)
        except Exception:
            return JsonResponse({"error": "incorrect payload"}, status=404)


@method_decorator(csrf_exempt, name='dispatch')
class Ad(View):
    def get(self, request):
        ads = Ads.objects.all()
        # cats_serialized = serialize('python', cats)
        ads_list = []
        for ad_item in ads:
            ads_list.append({
                "id": ad_item.id,
                "name": ad_item.name,
                "author": ad_item.author,
                "price": ad_item.price,
                "description": ad_item.description,
                "address": ad_item.address,
                "is_published": ad_item.is_published
            })
        return JsonResponse(ads_list, status=200, safe=False, json_dumps_params={'ensure_ascii': False})

    def post(self, request):
        try:
            data = json.loads(request.body)
            ad_item = Ads()
            ad_item.id = data.get('id', None)
            ad_item.name = data.get("name", None)
            ad_item.author = data.get("author", None)
            ad_item.price = data.get("price", None)
            ad_item.description = data.get("description", None)
            ad_item.address = data.get("address", None)
            ad_item.is_published = data.get("is_published", False)
            ad_item.save()
            return JsonResponse({"id": ad_item.id, "name": ad_item.name, "author": ad_item.author}, status=201)
        except Exception:
            return JsonResponse({"error": "incorrect payload"}, status=404)


@method_decorator(csrf_exempt, name='dispatch')
class CategoryDetail(DetailView):
    def get(self, request, pk):
        try:
            cat_item = Categories.objects.get(pk=pk)
            cat_list = []
            cat_list.append({
                "id": cat_item.id,
                "name": cat_item.name
            })
            return JsonResponse(cat_list, status=200, safe=False, json_dumps_params={'ensure_ascii': False})
        except Categories.DoesNotExist:
            return JsonResponse({"error": "do not exist"}, status=404)


@method_decorator(csrf_exempt, name='dispatch')
class AdDetail(DetailView):
    def get(self, request, pk):
        try:
            ad_item = Ads.objects.get(pk=pk)
            ads_list = []
            ads_list.append({
                "id": ad_item.id,
                "name": ad_item.name,
                "author": ad_item.author,
                "price": ad_item.price,
                "description": ad_item.description,
                "address": ad_item.address,
                "is_published": ad_item.is_published
            })
            return JsonResponse(ads_list, status=200, safe=False, json_dumps_params={'ensure_ascii': False})
        except Ads.DoesNotExist:
            return JsonResponse({"error": "do not exist"}, status=404)

        # Convert to JSON
        # with open('./datasets/ads.csv', encoding='utf-8') as f:
        #     reader = csv.DictReader(f)
        #     rows = list(reader)
        # with open('./datasets/ads.json', 'w', encoding='utf-8') as f:
        #     f.write(json.dumps(rows, ensure_ascii=False, indent=4))
        # with open('./datasets/categories.csv', encoding='utf-8') as f:
        #     reader = csv.DictReader(f)
        #     rows = list(reader)
        # with open('./datasets/categories.json', 'w', encoding='utf-8') as f:
        #     f.write(json.dumps(rows, ensure_ascii=False, indent=4))

        # Load data into model
        # with open('./ads/categories.json', encoding='utf-8') as data_file:
        #     json_data = json.loads(data_file.read())
        #     for item_data in json_data:
        #         item = Categories()
        #         item.id = item_data['id']
        #         item.name = item_data['name']
        #         item.save()
        # with open('./ads/ads.json', encoding='utf-8') as data_file:
        #     json_data = json.loads(data_file.read())
        #     for item_data in json_data:
        #         item = Ads()
        #         item.id = item_data['id']
        #         item.name = item_data['name']
        #         item.author = item_data['author']
        #         item.price = item_data['price']
        #         item.description = item_data['description']
        #         item.address = item_data['address']
        #         item.is_published = str2bool(item_data['is_published'])  # .replace("“", "")
        #         item.save()
