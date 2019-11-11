import copy

from django.shortcuts import render
from game2048.lwgame.usl import GameConsoleView
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from game2048.models import Top_ten

array_new = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
a = GameConsoleView(array_new)

def ht2048(request):
    # array = [[2, 8, 4, 2], [4, 32, 16, 8], [16, 128, 8, 2], [32, 2, 32, 16]]
    array = arr_map()
    print('get nadao map',array)
    array = a.start(array)

    print('start nadao map',array)
    return render(request,'ht2048.html',locals())

def on(request):
    print('这是 on ----------------')
    arr = request.COOKIES.get('arr', '没有值!')
    print("cookie my_var1 = ", arr)
    array = arr_map()
    print('nadao map',array)
    if 'on' in request.GET.keys():
        on = request.GET['on']
        if on == 'up':
            array = a.update('w',array)
        elif on == 'down':
            array = a.update('s',array)
        elif on == 'left':
            array = a.update('a',array)
        elif on == 'right':
            array = a.update('d',array)

    if array[len(array)-1] == 'over':
        print('游戏结束')

    if array == '没有变化':
        res = {'val': array}
        print(res)
        return JsonResponse(res)

    num_array = copy.deepcopy(array)
    try:
        array = num(num_array)
    except Exception as e:
        print(e)
        print('按的太快了')

    res = {'val':array}
    print(res)
    return JsonResponse(res)

def top_ten_add(request):

    if request.method == 'GET':
        num = request.GET['num']
        name = request.GET['name']
        Top_ten.objects.create(nickname=name,result=num)

    return HttpResponse('ok')

def top_ten(request):

    print('topten ok')
    top_all = Top_ten.objects.all()
    return render(request,'top_ten.html',locals())

def num(array):
    num = 0
    for i in array:
        for c in i:
            num += c
    array.append(num)
    return array


def arr_map():
    # num_array = copy.deepcopy(array)
    return array_new

# def arr_obj(array):
#
#     array_new = array[0:3]
#
#     return array_new