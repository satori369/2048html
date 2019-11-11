from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# def ht2048(request):
#     from usl import Usl
#
#     array = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
#
#     if 'on' in request.GET.keys():
#         on = request.GET['on']
#         if on == 'up':
#             print(on)
#
#
#     # return HttpResponse('ok')
#     return render(request,'ht2048.html',locals())