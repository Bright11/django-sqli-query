from django.shortcuts import render

from django.views import View
# Create your views here.
from .models import AnnouncedLgaResults,PollingUnit,AnnouncedPuResults,Party,Ward,Lga

class index(View):
    def get(self,request):
        title="INEC"
        results=AnnouncedLgaResults.objects.all()
        pullinguint=PollingUnit.objects.select_related('lga_id')
        # if pullinguint.exists():
        #     for p in pullinguint:
        #         print("lag",p.lga_id.state_id.state_name)
        #     else:
        #         print("none")
        # print(pullinguint.query)
        context={"title":title,"results":results,"pullinguint":pullinguint}
        return render(request,"pages/index.html",context)



class pullingresult(View):
    def get(self,request):
        
        announcedpresults=AnnouncedPuResults.objects.all()
        context={"announcedpresults":announcedpresults}
        return render(request,'pages/pullingresults.html',context)
    


class newresults(View):
    def get(self,request):
        party=Party.objects.all()
        pullingunit=PollingUnit.objects.all()
        ward=Ward.objects.all()
        lga=Lga.objects.all()
        context={"party":party,'pullingunit':pullingunit,'ward':ward,"lga":lga}

        return render(request,'pages/newresults.html',context)

    def post(self,request):
        pass