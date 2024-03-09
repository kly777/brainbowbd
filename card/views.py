from django.forms import model_to_dict
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# 添加rest framework,的api_view装饰器
from rest_framework.decorators import api_view
# 添加response 把数据以json格式发送回去，响应
from rest_framework.response import Response
import json
# 书写定义的视图返回规则
from .models import Card


@api_view(['GET'])
def first_api(request):
    return Response({'data': 'ok'})


def dispatcher(request):
    # 将请求参数统一放入request 的 params 属性中，方便后续处理
    # GET请求 参数在url中，同过request 对象的 GET属性获取
    if request.method == 'GET':
        request.params = request.GET

    # POST/PUT/DELETE 请求 参数 从 request 对象的 body 属性中获取
    elif request.method in ['POST', 'PUT', 'DELETE']:
        # 根据接口，POST/PUT/DELETE 请求的消息体都是 json格式
        request.params = json.loads(request.body)

    # 根据不同的action分派给不同的函数进行处理
    action = request.params['action']
    if action == 'list_card':
        return listcards(request)
    elif action == 'get_card':
        return getcard(request)
    elif action == 'add_card':
        return addcard(request)
    elif action == 'modify_card':
        return modifycard(request)
    elif action == 'del_card':
        return deletecard(request)

    else:
        return JsonResponse({'ret': 1, 'msg': '不支持该类型http请求'})


def listcards(request):
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    qs = Card.objects.values()

    # 将 QuerySet 对象 转化为 list 类型
    # 否则不能 被 转化为 JSON 字符串
    retlist = list(qs)

    return JsonResponse({'ret': 0, 'retlist': retlist})


def getcard(request):
    cardid = request.params['id']
    try:
        # 根据 id 从数据库中找到相应的客户记录
        card = Card.objects.get(id=cardid)
    except Card.DoesNotExist:
        return {
            'ret': 1,
            'msg': f'id 为`{cardid}`的客户不存在'
        }
    cardinfo = {"id": card.id, "title": card.title, "content": card.content, }
    return JsonResponse({'ret': 0, 'data': cardinfo})


def addcard(request):

    info = request.params['data']

    # 从请求消息中 获取要添加客户的信息
    # 并且插入到数据库中
    # 返回值 就是对应插入记录的对象
    record = Card.objects.create(
        name=info['name'],
        phonenumber=info['phonenumber'],
        address=info['address']
    )

    return JsonResponse({'ret': 0, 'id': record.id})


def modifycard(request):

    # 从请求消息中 获取修改客户的信息
    # 找到该客户，并且进行修改操作

    cardid = request.params['id']
    newdata = request.params['newdata']

    try:
        # 根据 id 从数据库中找到相应的客户记录
        card = Card.objects.get(id=cardid)
    except Card.DoesNotExist:
        return {
            'ret': 1,
            'msg': f'id 为`{cardid}`的客户不存在'
        }
    if 'name' in newdata:
        card.name = newdata['name']
    if 'phonenumber' in newdata:
        card.phonenumber = newdata['phonenumber']
    if 'address' in newdata:
        card.address = newdata['address']
    # 注意，一定要执行save才能将修改信息保存到数据库
    card.save()
    return JsonResponse({'ret': 0})


def deletecard(request):

    cardid = request.params['id']

    try:
        # 根据 id 从数据库中找到相应的客户记录
        card = Card.objects.get(id=cardid)
    except Card.DoesNotExist:
        return {
            'ret': 1,
            'msg': f'id 为`{cardid}`的客户不存在'
        }

    # delete 方法就将该记录从数据库中删除了
    card.delete()

    return JsonResponse({'ret': 0})


def carddetail(request, cardId):
    cardid = cardId
    try:
        # 根据 id 从数据库中找到相应的客户记录
        card = Card.objects.get(id=cardid)
        print(card.createdTime)
    except Card.DoesNotExist:
        return JsonResponse({
            'ret': 1,
            'msg': f'id 为`{cardid}`的客户不存在'
        })
    cardinfo = model_to_dict(card)
    cardinfo['createdTime'] = card.createdTime.strftime('%Y-%m-%d %H:%M:%S')
    cardinfo['revisedTime'] = card.revisedTime.strftime('%Y-%m-%d %H:%M:%S')
    # 这个函数的功能是将card对象的tags属性中的所有tag对象的tagname,id属性值存储到cardinfo字典的tags键对应的列表中
    cardinfo['tags'] = [tag.id for tag in card.tags.all()]
    return JsonResponse({'ret': 0, 'data': cardinfo})
