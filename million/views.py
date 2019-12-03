from django.shortcuts import render,HttpResponse
from .models import Million
from .tasks import add_row

# Create your views here.
def enter_million_rows(request):
    bulk_list = []
    for i in range(9000000):
        bulk_list.append(Million(**{"dump":f"dump____{i}"}))
        # add_row.delay(i)
        # m = Million.objects.create(**{"dump":f"dump____{i}"})
        # print(m.id)
    Million.objects.bulk_create(bulk_list)
    return HttpResponse("Done")
