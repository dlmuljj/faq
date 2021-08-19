from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from app01 import models
from app01.models import DDR, Serdes, U2, U3, Pll, Hdmi, Dp
from app01.models import TVSensor, MIPI, SARADC, VDAC, Package
# Create your views here.
import re

class Index(View):

    def get(self, request,name=None):

        table_list = [DDR, Serdes, U2, U3, Pll, Hdmi, Dp, TVSensor, MIPI, SARADC, VDAC, Package]
        name_list = ['DDR','Serdes','U2','U3','PLL','HDMI','DP','TVSensor','MIPI','SARADC','VDAC','Package']
        len_list = []
        for item in table_list:
            len_list.append(item.objects.count())
        rst_list = dict(zip(name_list,len_list))

        if name:
            name_upper = name.upper()
        else:
            name_upper = name

        if name_upper == 'DDR':
            ddr_queryset = DDR.objects.all()
        elif name_upper == 'HDMI':
            ddr_queryset = Hdmi.objects.all()
        elif name_upper == 'U2':
            ddr_queryset = U2.objects.all()
        elif name_upper == 'U3':
            ddr_queryset = U3.objects.all()
        elif name_upper =='PLL':
            ddr_queryset = Pll.objects.all()
        elif  name_upper == 'SERDES':
            ddr_queryset = Serdes.objects.all()
        elif name_upper == 'DP':
            ddr_queryset = Dp.objects.all()
        elif name_upper == 'TVSENSOR':
            ddr_queryset = TVSensor.objects.all()
        elif name_upper == 'MIPI':
            ddr_queryset = MIPI.objects.all()
        elif name_upper == 'SARADC':
            ddr_queryset = SARADC.objects.all()
        elif name_upper == 'VDAC':
            ddr_queryset = VDAC.objects.all()
        elif name_upper == 'PACKAGE':
            ddr_queryset = Package.objects.all()
        else:
            ddr_queryset = DDR.objects.all()
        return render(request,'index.html', locals())
        # return HttpResponse('this is a test')



class Search(View):
    def get(self,request):
        table_list = [DDR, Serdes, U2, U3, Pll, Hdmi, Dp, TVSensor, MIPI, SARADC, VDAC, Package]
        name_list = ['DDR', 'Serdes', 'U2', 'U3', 'PLL', 'HDMI', 'DP', 'TVSensor', 'MIPI', 'SARADC', 'VDAC', 'Package']
        len_list = []
        ddr_queryset = []

        val = request.GET.get('val')
        print(f'查询内容:{val}')

        for item in table_list:
            len_list.append(item.objects.count())
            obj_rst = item.objects.filter(question__contains=val)
            if obj_rst is not None:
                for obj in obj_rst:
                    a_rst = re.findall(val, obj.question, flags=re.IGNORECASE)
                    for a in set(a_rst):
                        obj.question = obj.question.replace(a,f'<span style="color: red; font-weight: bold">{a}</span>')
                    ddr_queryset.append(obj)

        rst_list = dict(zip(name_list, len_list))

        return render(request,'search.html',locals())