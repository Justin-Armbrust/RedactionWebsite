import boto3
import json
from pprint import pprint
import sys


def Redact(text,CS):
    client = boto3.client(service_name='comprehendmedical',
                        region_name='us-west-2')
    resp = client.detect_phi(Text=text)
    phi_list = list()
    for entity in resp['Entities']:
        if entity['Category'] == 'PROTECTED_HEALTH_INFORMATION':
            phi_list.append(entity)
    redacted_text,non_redacted_entity = entity_redaction(text,phi_list,CS)
    if non_redacted_entity > 0:
        print("There were {} entities that were not redacted".format(non_redacted_entity))
    
    return redacted_text
        
def entity_redaction(source_text,phi_list,confidence_threshold):
    redacted_text = source_text
    non_redacted = 0
    for entity in phi_list:
        confidence_score = entity['Score']
        if float(confidence_score) >= confidence_threshold:
            replace_text = '[{}]'.format(entity["Type"])
            redacted_text = redacted_text.replace(entity['Text'],replace_text,1)
        else:
            non_redacted = non_redacted +1
    return redacted_text,non_redacted


if __name__ == '__main__':
    main()