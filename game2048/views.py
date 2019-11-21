import copy
import json
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
    # 把新地图放入启动函数
    array = a.start(array_new)
    # print('start nadao map',array)

    # 后端处理cookie,失败,改用js处理
    # resp = render(request, 'ht2048.html', locals())
    # arr = []
    # for item in array:
    #     i = [str(i) for i in item]
    #     for c in i:
    #         arr.append(c)
    #arr = json.dumps(array)
    #"['4'\054 '0'\054 '2'\054 '0'\054 '0'\054 '0'\054 '0'\054 '0'\054 '0'\054 '0'\054 '0'\054 '0'\054 '0'\054 '0'\054 '0'\054 '0']"
    #resp.set_cookie('arr', arr, 30 * 60 * 1000)

    return render(request, 'ht2048.html', locals())

def on(request):
    # print('这是 on ----------------')

    #拿到cook的值,转换成[[],[],[],[]]
    cook_arr = request.COOKIES.get('arr', '没有值!')
    cook_arr = cook_arr.split(',')[:16]
    cook_arr = [int(i) for i in cook_arr]
    array = []
    array.append(cook_arr[:4])
    array.append(cook_arr[4:8])
    array.append(cook_arr[8:12])
    array.append(cook_arr[12:16])
    print(array)

    # v1.0版本处理方案,深拷贝地图做到并发  ->失败(无法识别游览器用户)  解决方案(cookie)
    # array = arr_map()
    # print('nadao map',array)

    #将cookie拿到的值,传入逻辑函数处理
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
        # 积分统计
        array = num(num_array)
    except Exception as e:
        print(e)
        print('按的太快了')

    res = {'val':array}
    print(res)
    return JsonResponse(res)

# 添加排名
def top_ten_add(request):

    if request.method == 'GET':
        num = request.GET['num']
        num = int(num[:-1])
        name = request.GET['name']
        Top_ten.objects.create(nickname=name,result=num)

    return HttpResponse('ok')

# 查看排名
def top_ten(request):

    print('topten ok')
    top_all = Top_ten.objects.order_by('-result')[:10]

    return render(request,'top_ten.html',locals())

# 积分计算函数
def num(array):
    num = 0
    for i in array:
        for c in i:
            num += c
    array.append(num)
    return array


# def arr_map():
    # num_array = copy.deepcopy(array)
    # return array_new

# def arr_obj(array):
#
#     array_new = array[0:3]
#
#     return array_new