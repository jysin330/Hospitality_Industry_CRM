from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from pymongo import MongoClient
from datetime import datetime, timedelta

@method_decorator(csrf_exempt, name='dispatch')
class MetricsView(View):
    def get(self, request, *args, **kwargs):
        city = request.GET.get('city', None)
        
        if not city:
            return JsonResponse({'code': 400, 'status': 'Bad Request', 'message': 'City parameter is required'})

        # MongoDB connection string
        connection_string = "mongodb+srv://pb_test_user:xQvWQKoM9L6ELtyQ@cluster0.msnrykh.mongodb.net/test_db"
        
        # Connect to MongoDB
        client = MongoClient(connection_string)
        
        # Access the daily-total-summary collection
        collection = client.test_db.daily_total_summary

        # Calculate the date 15 days ago from the last day
        end_date = datetime(2024, 2, 5)
        start_date = end_date - timedelta(days=15)

        # Query MongoDB for data for the specified city within the date range
        query = {
            'city': city,
            'date': {'$gte': start_date, '$lte': end_date}
        }

        result = list(collection.find(query, {'_id': 0}))

        # Close MongoDB connection
        client.close()

        response_data = {'code': 200, 'status': 'Success', 'data': result}
        return JsonResponse(response_data)
