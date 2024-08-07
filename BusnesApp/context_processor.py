from .models import DashActivities


def context(request):
    dash = DashActivities.objects.first()
    return {'dash': dash}