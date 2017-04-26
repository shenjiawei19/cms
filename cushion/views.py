# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, RequestContext
from models import n_info,epg
from django.db.models import Sum
import datetime
import numpy as np

S2 = ['LENOVOTV_55S9I','LENOVOTV_55S9I','17TV_55S9i','17TV_39S9i','17TV_43S9i','17TV_50S9i','LENOVOTV_49K3',
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
K82 = ['K82','IDEATV_K82','K82_SHARP']
K = ['BESTVOTT','SBOX8940','SHADTOTT','DAISY','A11','ANDROID_PAD','CK81','ANDROID_PHONE','A11C','K81','MOZILLA',
     'LENOVOPC','ALPHA2','LENOVOALPHA','LENOVOTV_49E82','LENOVOTV_55E82','LENOVOTV_55A3X','LENOVOTV_39E6',
     'LENOVOTV_43E6','LENOVOTV_49E6','LENOVOTV_55E6','LENOVOTV_32A5','LENOVOTV_39A5','LENOVOTV_42A5',
     'LENOVOTV_55A5','LENOVOTV_43E5','LENOVOTV_49E5','LENOVOTV_55E5','LENOVOTV_39E5','K91','IDEATV_K91',
     'IDEA_TV_K91','17TV_SC-I3','AQUOS_80XU35A','AQUOS_70XU30A','AQUOS_70UG30A','AQUOS_60UG30A',
     'IDEATV_K91_V1.1','K91_V1','IDEATV_K91_V1','IDEA_TV_K91_V1','IDEA_TV_K91_V1.1']
S1 = ['IDEATV_S61','IDEATV_S61A','FREUD','IDEATV_S51A','BERLIN_BG2_FREUD','IDEATV_S51','LENOVOAIO',
      'IDEATV_S31A','S31','IDEATV_S31']
A21 = ['IDEATV_50E21X','IDEATV_42E31X','IDEATV_42E31Y','IDEATV_32E31Y','IDEATV_32E31X','IDEATV_55E31X',
       'IDEATV_55E31Y','IDEATV_32A21X','IDEATV_32A21Y','IDEATV_42A21X','IDEATV_A21','IDEATV_39E31Y',
       'IDEATV_50E31Y','IDEATV_50E31X','A21','IDEATV_50A21Y','IDEATV_39A21Y','IDEATV_42A21Y','IDEATV_55A21Y',
       'IDEATV_55A21X','IDEATV_55A3Y','IDEATV_42A3Y']
sky_shape = ['sky_a11a','sky_lcd_s3a01','sky_lcd_uf30a','sky_lcd_xxbel6a_b','sky_lcd_xxbel7a_b','sky_lcd_xxbel8a',
             'sky_lcd_xxcae5a','sky_lcd_xxcae5a_b','sky_lx460a','sky_lx560a','sky_lx565ab','sky_v3a']
shy_changhong = ['sky_mt5520_ll','sky_mt5520_ll_15g','sky_mt5520_ll_15g_rtk','sky_mt5520_ll_srs','sky_full_changhong']
sky_baofeng = ['sky_baofeng_tv']
sky_tencent = ['sky_full_mstaredison','sky_rk3288']
sky_kukai = ['sky_kukai']
sky_kangjia = ['sky_rtd2995d_2d','sky_rtd2995d_6200','sky_rtd2995d_6610','sky_rtd2995d_kktv','sky_rtd2995d_6680',
              'sky_rtd2995d_reduce','sky_rtd2995d_slim','sky_rtd299x_tv035','sky_rtd2995d_tencenttv']
sky_lenovo = ['sky_yt-x703f','sky_yt-x703l','sky_yt3_10_prc_lte_ref','sky_yt3_10_prc_wifi_ref']


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
    support = u'所有' if sup == '' else sup
    typ = ['K', 'K', 'K82', 'S1', 'S2', 'A21','shape','changhong','baofeng','tencent','kukai','kangjia','lentv'][
        typ1 == u'K系列' and 1 or typ1 == u'K82系列' and 2 or typ1 == u'S1系列' and 3 or typ1 == u'S2系列' and 4 or
        typ1 == u'A21系列' and 5 or typ1 == u'sky夏普' and 6 or typ1 == u'sky长虹' and 7 or typ1 == u'sky暴风' and 8 or
        typ1 == u'sky腾讯' and 9 or typ1 == u'sky酷开' and 10 or typ1 == u'sky康佳' and 11 or typ1 == u'sky联想' and 12]
    tenDayAgo = (datetime.datetime.now() - datetime.timedelta(days=15)).strftime("%Y-%m-%d")
    select = [K,K,K82,S1,S2,A21,sky_shape,shy_changhong,sky_baofeng,sky_tencent,sky_kukai,sky_lenovo
              ][typ=='K' and 1 or typ== 'K82' and 2 or typ=='S1' and 3 or typ== 'S2'and  4 or typ== 'A21' and 5 or
                typ== 'shape' and 6 or typ== 'changhong'and 7 or typ== 'baofeng'and 8 or typ== 'tencent'and 9 or
                typ== 'kukai'and 10 or typ== 'kangjia'and 11 or  typ== 'lentv'and 12 ]
    if start != '' and over != '' and support != '':
        dd = {'ip': support, 'date__lte': over, 'date__gte': start, 'type__in': select}
    elif support == u'所有' and (cls not in ['uv', 'search', 'arrive', 'expense', 'purchase', 'error']):
        if start == '':
            start = tenDayAgo
        dd = {'type__in': select, 'date__gte': tenDayAgo}
    elif start != '' and support != '':
        dd = {'ip': support, 'type__in': select, 'date__gte': start}
    else:
        start = tenDayAgo
        dd = {'ip': support, 'type__in': select, 'date__gte': start}


    if cls in ['uv', 'search', 'arrive', 'expense', 'purchase', 'error']:
        dd.pop('ip')
        a = epg.objects.using('n_quality').filter(**dd).values('date').annotate(select_sum=Sum(cls))
    elif support == u'所有':
        a = n_info.objects.using('n_quality').filter(**dd).values('ip','date').annotate(select_sum=Sum(cls),vv_sum=Sum('vv'))
    else:
        a = n_info.objects.using('n_quality').filter(**dd).values('ip','date').annotate(select_sum=Sum(cls),vv_sum=Sum('vv'))
    cls_index = u'零缓冲比例' if cls1 is '' else cls1
    typ_index = u'K系列' if typ1 is '' else typ1
    if len(a) > 0 and support == u'所有' and (cls not in ['uv', 'search', 'arrive', 'expense', 'purchase', 'error']):
        info = {
            'letv':[],
            'jindong':[],
            'bestv':[],
            'jinshan':[],
            'up':[],
            'qiyi':[],
            'wangsu':[],
            'manman':[],
            'tm':[],
            'type': typ_index,
            'cls': cls_index,
            'sup': support,
            'start': start,
            'over': over,
            'lv':''
        }
        tm, ip, vl, vv = zip(*map(lambda x: (x['date'], x['ip'], x['select_sum'], x['vv_sum']), a))
        l = []
        for i in ip:
            if i not in l:
                l.append(i)
        c = len(l)
        for i in xrange(len(ip)/c):
            for t in xrange(c):
                check = ip[c * i + t]
                name = ['letv','jindong','bestv','jinshan','up','qiyi','wangsu','manman'][check==u'乐视' and 0 or check==u'京东'
                                                                        and 1 or check==u'视云' and 2 or
                                                                        check==u'金山' and 3 or check==u'又拍'
                                                                        and 4 or check==u'奇异' and 5 or
                                                                        check==u'网宿' and 6 or  check==u'蛮蛮' and 7]
                if cls in ['unusual', 'gt3']:
                    info[name].append(round((vl[c * i + t] * 1.0 / vv[c * i + t]), 2))
                elif cls in ['vv','average','fbuffer']:
                    info[name].append(vl[c * i + t])
                else:
                    info[name].append(round((1-vl[c*i+t]*1.0/vv[c*i+t]),2))
            info['tm'].append(tm[c*i+t])
        info['tm'] = map(lambda x: int((x.strftime("%Y%m%d"))), info['tm'])
    elif len(a) > 0 and (cls not in ['uv', 'search', 'arrive', 'expense', 'purchase', 'error']):
        tm,ip,vl,vv = zip(*map(lambda x: (x['date'],x['ip'],x['select_sum'],x['vv_sum']), a))
        if cls in ['unusual','gt3']:
            rate = (np.array(map(float, vl)) / np.array(map(float, vv))).tolist()
        elif cls in ['vv','average','fbuffer']:
            rate = vl
        else:
            rate = (1-np.array(map(float, vl))/np.array(map(float, vv))).tolist()
        info = {
            'letv': '',
            'jindong': '',
            'bestv': '',
            'jinshan': '',
            'up': '',
            'qiyi': '',
            'wangsu': [],
            'manman': [],
            'tm': map(lambda x: int((x.strftime("%Y%m%d"))), tm),
            'vl': map(lambda x: float('%.2f' % x), rate),
            'type': typ_index,
            'cls': cls_index,
            'sup': sup,
            'start': start,
            'over': over
        }
    elif len(a) > 0 :
        tm, vl = zip(*map(lambda x: (x['date'],x['select_sum']), a))
        info = {
            'letv': '',
            'jindong': '',
            'bestv': '',
            'jinshan': '',
            'up': '',
            'qiyi': '',
            'wangsu': [],
            'manman': [],
            'tm': map(lambda x: int((x.strftime("%Y%m%d"))), tm),
            'vl': map(lambda x: float('%.2f' % x), vl),
            'type': typ_index,
            'cls': cls_index,
            'sup': u'视云',
            'start': start,
            'over': over
        }
    else:
        info = {
            'letv': '',
            'jindong': '',
            'bestv': '',
            'jinshan': '',
            'up': '',
            'qiyi': '',
            'wangsu': [],
            'manman': [],
            'type': typ_index,
            'cls': cls_index,
            'sup': sup,
            'start': start,
            'over': over
        }
    return render_to_response("index2.html", info, context_instance=RequestContext(request))

def contract(request):
    info = {

    }
    return render_to_response("contract.html", info, context_instance=RequestContext(request))

