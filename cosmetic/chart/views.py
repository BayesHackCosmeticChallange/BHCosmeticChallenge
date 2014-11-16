from django.http import HttpResponse
import json
from chart.models import Score, Toxicity


# Create your views here.
def render_chart(request, **kwargs):
    try:
        #Extract the required parameters for HTTP GET request.
        product = str(request.GET.get('product'))
        brand = str(request.GET.get('brand'))
        brand_name = brand.lower()
        content = Score.objects.get(brand=brand_name, product=product)
        toxicity_content = Toxicity.objects.get(cas=content.cas)
        toxicity = int(toxicity_content.cancer + toxicity_content.female_reproductive +
                       toxicity_content.male_reproductive + toxicity_content.developmental)
        json_response = {'brand': content.brand, 'product': content.product,
                         'efficancy_long': content.efficancy_long,
                         'efficancy_short': content.efficancy_short,
                         'smell': content.smell, 'lavant': content.lavant,
                         'texture': content.texture, 'rincable': content.rincable, 'toxicity': toxicity}
        return HttpResponse(json.dumps(json_response), content_type="application/json")
    except:
        json_response = {'status': 'failure', 'status_msg': "Something wrong"}
        return HttpResponse(json.dumps(json_response), content_type="application/json")