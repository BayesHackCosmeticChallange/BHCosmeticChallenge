from django.http import HttpResponse
import json
from chart.models import Score, Toxicity


# Create your views here.
def render_chart(request, **kwargs):
    try:
        #Extract the required parameters for HTTP GET request.
        all_contents = Score.objects.all()
        json_response = []
        for content in all_contents:
            toxicity_query_set = Toxicity.objects.filter(cas=content.cas)
            if len(toxicity_query_set) == 0:
                toxicity = {'cancer': 0, 'female_reproductive': 0,
                            'male_reproductive': 0, 'developmental': 0}
                pass
            else:
                toxicity_content = toxicity_query_set[0]
                toxicity = {'cancer': toxicity_content.cancer,
                            'female_reproductive': toxicity_content.female_reproductive,
                            'male_reproductive': toxicity_content.male_reproductive,
                            'developmental': toxicity_content.developmental}

            json_response.append({'brandLabel': content.brand, 'productLabel': content.product,
                                  'label': content.brand + ' - ' + content.product,
                                  'score': {'efficancy_long': max(float(0 if content.efficancy_long is None else content.efficancy_long) * 2, 5),
                                            'efficancy_short': max(float(0 if content.efficancy_short is None else content.efficancy_short) * 2, 5),
                                            'smell': max(float(0 if content.smell is None else content.smell) * 2, 5),
                                            'quality on price': max(float(0 if content.quality is None else content.quality) * 2, 5),
                                            'texture': max(float(0 if content.texture is None else content.texture) * 2, 5),
                                            'toxicity': toxicity}})

        return HttpResponse(json.dumps(json_response), content_type="application/json")
    except Exception as e:
        json_response = {'status': 'failure', 'status_msg': str(e)}
        return HttpResponse(json.dumps(json_response), content_type="application/json")