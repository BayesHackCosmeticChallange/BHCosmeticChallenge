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
                toxicity = 0
                pass
            else:
                toxicity_content = toxicity_query_set[0]
                toxicity = int(toxicity_content.cancer + toxicity_content.female_reproductive +
                               toxicity_content.male_reproductive + toxicity_content.developmental)
            json_response.append({'brandLabel': content.brand, 'productLabel': content.product,
                                  'label': content.brand + ' - ' + content.product,
                                  'score': {'packaging': content.efficancy_long,
                                            'efficancy_short': content.efficancy_short,
                                            'smell': content.smell, 'lavant': content.lavant,
                                            'texture': content.texture, 'rincable': content.rincable,
                                            'toxicity': toxicity}})

        return HttpResponse(json.dumps(json_response), content_type="application/json")
    except Exception as e:
        json_response = {'status': 'failure', 'status_msg': str(e)}
        return HttpResponse(json.dumps(json_response), content_type="application/json")