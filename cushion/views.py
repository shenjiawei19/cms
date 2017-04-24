# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, RequestContext
from models import play_info,n_info
import datetime


def cushion(request):
    cls1 = request.GET.get('class', "")
    typ1 = request.GET.get('type', "")
    sup = request.GET.get('support', "")
    start = request.GET.get('start', "")
    over = request.GET.get('over', "")
    cls = ['nobuffer_pro','nobuffer_pro','fluency_pro','custom_unusual_pro','average_playtime','gt3caton_pro','uv','vv'][cls1==u'零缓冲比例' and 1 or cls1==u'播放流畅比例'and 2 or cls1==u'异常比例' and 3 or cls1==u'卡顿大于三次比例' and 4 or cls1==u'平均播放时长' and 5 or cls1==u'VV变化' and 6 or cls1==u'UV变化' and 7]
    support = [1,1,0,3,9,10,14,15][sup==u'自建' and 1 or sup==u'所有' and 2 or sup==u'奇异' and 3 or sup==u'又拍' and 4 or sup==u'乐视' and 5 or sup ==u'金山' and 6 or sup==u'蛮蛮云' and 7]
    typ = ['K','K','K82','S1','S2','A21'][typ1==u'K系列' and 1 or typ1==u'K82系列'and 2 or typ1==u'S1系列' and 3 or typ1==u'S2系列' and 4 or typ1==u'A21系列' and 5 ]
    tenDayAgo = (datetime.datetime.now() - datetime.timedelta(days=50)).strftime("%Y-%m-%d")
    if start != '' and over != '':
        dd = {'cdn_id':support,'date__lte':over,'date__gte':start,'type':typ}
    elif start != '':
        dd = {'cdn_id':support,'type':typ,'date__gte':start}
    else:
        start = tenDayAgo
        dd = {'cdn_id':support,'type':typ,'date__gte':tenDayAgo}
    a = play_info.objects.filter(**dd).values('cdn_id','type',cls,'date')
    cls_index = u'零缓冲比例' if cls1 is '' else cls1
    typ_index = u'K系列' if typ1 is '' else typ1
    if len(a) > 0:
        tm, vl = zip(*map(lambda x: (x['date'], x[cls]), a))
        info = {
            'tm': map(lambda x: int((x.strftime("%Y%m%d"))), tm),
            'vl': map(float, vl),
            'type': typ_index,
            'cls': cls_index,
            'sup': sup,
            'start': start,
            'over': over
        }
    else:
        info = {}

    return render_to_response("index.html", info, context_instance=RequestContext(request))

def quality(request):
    cls1 = request.GET.get('class', "")
    typ1 = request.GET.get('type', "")
    sup = request.GET.get('support', "")
    start = request.GET.get('start', "")
    over = request.GET.get('over', "")
    cls = \
    ['nobuffer_pro', 'nobuffer_pro', 'fluency_pro', 'custom_unusual_pro', 'average_playtime', 'gt3caton_pro', 'uv', 'vv'][
        cls1 == u'零缓冲比例' and 1 or cls1 == u'播放流畅比例' and 2 or cls1 == u'异常比例' and 3 or cls1 == u'卡顿大于三次比例' and 4 or cls1 == u'平均播放时长' and 5 or cls1 == u'VV变化' and 6 or cls1 == u'UV变化' and 7]
    support = [1, 1, 0, 3, 9, 10, 14, 15][
        sup == u'自建' and 1 or sup == u'所有' and 2 or sup == u'奇异' and 3 or sup == u'又拍' and 4 or sup == u'乐视' and 5 or sup == u'金山' and 6 or sup == u'蛮蛮云' and 7]
    typ = ['K', 'K', 'K82', 'S1', 'S2', 'A21'][
        typ1 == u'K系列' and 1 or typ1 == u'K82系列' and 2 or typ1 == u'S1系列' and 3 or typ1 == u'S2系列' and 4 or typ1 == u'A21系列' and 5]
    tenDayAgo = (datetime.datetime.now() - datetime.timedelta(days=50)).strftime("%Y-%m-%d")
    if start != '' and over != '':
        dd = {'cdn_id': support, 'date__lte': over, 'date__gte': start, 'type': typ}
    elif start != '':
        dd = {'cdn_id': support, 'type': typ, 'date__gte': start}
    else:
        start = tenDayAgo
        dd = {'cdn_id': support, 'type': typ, 'date__gte': tenDayAgo}
    a = play_info.objects.filter(**dd).values('cdn_id', 'type', cls, 'date')
    cls_index = u'零缓冲比例' if cls1 is '' else cls1
    typ_index = u'K系列' if typ1 is '' else typ1
    if len(a) > 0:
        tm, vl = zip(*map(lambda x: (x['date'], x[cls]), a))
        info = {
            'tm': map(lambda x: int((x.strftime("%Y%m%d"))), tm),
            'vl': map(float, vl),
            'type': typ_index,
            'cls': cls_index,
            'sup': sup,
            'start': start,
            'over': over
        }
    else:
        info = {}
    return render_to_response("index.html", info, context_instance=RequestContext(request))

def contract(request):
    info = {

    }
    return render_to_response("contract.html", info, context_instance=RequestContext(request))

