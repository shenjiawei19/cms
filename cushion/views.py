# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, RequestContext
from models import play_info,n_info
from django.db.models import Count,Sum
import datetime
import numpy as np

def model_version():
    s2 = ['LENOVOTV_55S9I','LENOVOTV_55S9I','17TV_55S9i','17TV_39S9i','17TV_43S9i','17TV_50S9i','LENOVOTV_49K3',
          'LENOVOTV_55K3','17TV_55S9IA','17TV_50S9IA','17TV_39S9C','17TV_55I','17TV_50I','S52','LenovoTV_50S52',
          'IDEATV_S52','LENOVOTV_50S52','AQUOS_50U3A','AQUOS_58U3A','AQUOS_65UR30A','S52_SHARP','AQUOS_70LX765A',
          'AQUOS_46LX765A','AQUOS_52LX765A','AQUOS_60LX765A','AQUOS','AQUOS_50S1','LENOVOTV_32A3','LENOVOTV_40A3',
          'LENOVOTV_43A3','LENOVOTV_49A3','LENOVOTV_39A3','LENOVOTV_32A3X','LENOVOSTB_C5','LENOVOTV_42E82',
          'LENOVOTV_E82','AQUOS_40U1','AQUOS_60UE20A','AQUOS_50U1','AQUOS_58U1','AQUOS_60UD30A','AQUOS_70UE20A',
          'S9_SHARP','AQUOS_52UE20A','AQUOS_80UD30A','AQUOS_70UD30A','17TV_55I2','17TV_50I2','S9','LENOVOTV_58S9',
          'LENOVOTV_40S9','LENOVOTV_50S9','IDEATV_S9','17TV_39S9i','17TV_43S9i','17TV_50S9i','LENOVOTV_49K3',
          'LENOVOTV_55K3','17TV_55S9IA','17TV_50S9IA','17TV_39S9C','17TV_55I','17TV_50I','S52','LenovoTV_50S52',
          'IDEATV_S52','LENOVOTV_50S52','AQUOS_50U3A','AQUOS_58U3A','AQUOS_65UR30A','S52_SHARP','AQUOS_70LX765A',
          'AQUOS_46LX765A','AQUOS_52LX765A','AQUOS_60LX765A','AQUOS','AQUOS_50S1','LENOVOTV_32A3','LENOVOTV_40A3',
          'LENOVOTV_43A3','LENOVOTV_49A3','LENOVOTV_39A3','LENOVOTV_32A3X','LENOVOSTB_C5','LENOVOTV_42E82',
          'LENOVOTV_E82','AQUOS_40U1','AQUOS_60UE20A','AQUOS_50U1','AQUOS_58U1','AQUOS_60UD30A','AQUOS_70UE20A',
          'S9_SHARP','AQUOS_52UE20A','AQUOS_80UD30A','AQUOS_70UD30A','17TV_55I2','17TV_50I2','S9','LENOVOTV_58S9',
          'LENOVOTV_40S9','LENOVOTV_50S9','IDEATV_S9']



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
    cls = ['nobuffer', 'nobuffer', 'fluency', 'unusual', 'average', 'gt3', 'fbuffer', 'vv',
           'uv', 'search', 'arrive', 'expense', 'purchase', 'error'][
        cls1 == u'零缓冲比例' and 1 or cls1 == u'播放流畅比例' and 2 or cls1 == u'异常比例' and 3 or
        cls1 == u'平均播放时长' and 4 or cls1 == u'卡顿大于三次比例' and 5 or cls1 == u'首次缓冲时长' and 6 or
        cls1 == u'VV变化' and 7 or cls1 == u'整体UV' and 8 or cls1 == u'检索次数' and 9 or
        cls1 == u'检索命中次数' and 10 or cls1 == u'点击视频购买次数' and 11 or cls1 == u'购买成功次数' and 12 or
        cls1 == u'异常次数' and 13]
    support = u'视云' if sup == '' else sup
    typ = ['K', 'K', 'K82', 'S1', 'S2', 'A21'][
        typ1 == u'K系列' and 1 or typ1 == u'K82系列' and 2 or typ1 == u'S1系列' and 3 or typ1 == u'S2系列' and 4 or typ1 == u'A21系列' and 5]
    tenDayAgo = (datetime.datetime.now() - datetime.timedelta(days=15)).strftime("%Y-%m-%d")
    if start != '' and over != '' and support != '':
        dd = {'ip': support, 'date__lte': over, 'date__gte': start, 'type__contains': typ}
    elif support == u'所有':
        dd = {'type__contains': typ, 'date__gte': tenDayAgo}
    elif start != '' and support != '':
        dd = {'ip': support, 'type__contains': typ, 'date__gte': start}
    else:
        start = tenDayAgo
        dd = {'ip': support, 'type__contains': typ, 'date__gte': start}
    a = n_info.objects.using('n_quality').filter(**dd).values('ip','date').annotate(select_sum=Sum(cls),vv_sum=Sum('vv'))
    cls_index = u'零缓冲比例' if cls1 is '' else cls1
    typ_index = u'K系列' if typ1 is '' else typ1
    print cls_index,typ_index
    if len(a) > 0:
        tm,ip,vl,vv = zip(*map(lambda x: (x['date'],x['ip'],x['select_sum'],x['vv_sum']), a))
        if cls in ['unusual','gt3']:
            rate = (np.array(map(float, vl)) / np.array(map(float, vv))).tolist()
        elif cls in ['vv','average','fbuffer']:
            rate = vl
        else:
            rate = (1-np.array(map(float, vl))/np.array(map(float, vv))).tolist()
        info = {
            'tm': map(lambda x: int((x.strftime("%Y%m%d"))), tm),
            'vl': map(lambda x: float('%.2f' % x), rate),
            'type': typ_index,
            'cls': cls_index,
            'sup': sup,
            'start': start,
            'over': over
        }
    else:
        info = {}
    return render_to_response("index2.html", info, context_instance=RequestContext(request))

def contract(request):
    info = {

    }
    return render_to_response("contract.html", info, context_instance=RequestContext(request))

