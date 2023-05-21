

# Create your views here.


from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from Sansa import core


@csrf_exempt
#@utils.token_required
def asset_report(request):
    print(request.GET)
    if request.method == 'POST':
        ass_handler = core.Asset(request)
        if ass_handler.data_is_valid():
            print("----asset data valid:")
            ass_handler.data_inject()
            # return HttpResponse(json.dumps(ass_handler.response))

        return HttpResponse(json.dumps(ass_handler.response))
        # return render(request,'assets/asset_report_test.html',{'response':ass_handler.response})
        # else:
        # return HttpResponse(json.dumps(ass_handler.response))

    return HttpResponse('--test--')