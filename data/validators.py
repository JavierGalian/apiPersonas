from django.http import JsonResponse

def validate_password_strength(value):
    if len(value) < 8:
        return JsonResponse({'error': 'La contraseña debe tener al menos 8 caracteres.'}, status=400)
    if not any(char.isdigit() for char in value):
        return JsonResponse({'error': 'La contraseña debe contener al menos un número.'}, status=400)
    if not any(char.isalpha() for char in value):
        return JsonResponse({'error': 'La contraseña debe contener al menos una letra.'}, status=400)
    return None