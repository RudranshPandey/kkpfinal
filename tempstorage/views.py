from django.http import JsonResponse
from .models import TempStorage
from django.core.serializers.json import DjangoJSONEncoder

import json
from django.http import JsonResponse

def store_data(request):
    if request.method == 'POST':
        # Assuming the data is sent as JSON
        try:
            data = json.loads(request.body)
            # Process the data as needed
            print(data)
            # Store the data in the database
            TempStorage.objects.create(data=data)
            # Return a JSON response indicating success
            return JsonResponse({'message': 'Data received successfully.'}, status=200)
        except json.JSONDecodeError as e:
            # Return a JSON response with an error message if JSON decoding fails
            return JsonResponse({'error': 'Invalid JSON format.'}, status=400)
    else:
        # Return a JSON response with an error message for unsupported methods
        return JsonResponse({'error': 'Method not allowed.'}, status=405)

def get_data(request):
    if request.method == 'GET':
        # Retrieve the data from the storage
        stored_data = TempStorage.objects.first()

        if stored_data:
            # Send the data as a response
            data = stored_data.data
            print(data)
            # Delete the stored data
            stored_data.delete()
            # Serialize the data using DjangoJSONEncoder
            serialized_data = DjangoJSONEncoder().encode(data)
            return JsonResponse(serialized_data, safe=False)
        else:
            return JsonResponse({'error': 'No data available'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
