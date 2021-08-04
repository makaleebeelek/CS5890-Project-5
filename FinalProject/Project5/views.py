from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Template

import re
import scispacy
import spacy
from spacy import displacy

ICD_10_CM_PAT = re.compile(r'\b(?<!#)([A-Z]\d[A-Z0-9]{1,5})\b')
ICD_10_PCS_PAT = re.compile(r'\b(?<!#)([0-9A-HJ-NP-Z]{7})\b')
nlp = spacy.load("en_ner_bc5cdr_md")


def index(request):
    if (request.POST.get('highlight1')):
        string = getHighlight(1)
    elif (request.POST.get('highlight2')):
        string = getHighlight(2)
    elif (request.POST.get('highlight3')):
        string = getHighlight(3)
    elif (request.POST.get('submitText')):
        text = request.POST['textInput']
        string = getHighlight(3, text)
    else:
        string = "<h4>Click a button above to run the code!</h4>"
    return render(request, 'Project5/index.html', {'string': string})

def getHighlight(num, text="I am testing T10. My next test is AA23B56."):
    doc = nlp(text)
    myHtmlStr = highlight(doc)
    string = '<h4>Highlight '+ str(num) + myHtmlStr
    return string


def highlight(doc):
    myHtml = displacy.render(doc, style='ent', options=get_entity_options())
    myHtml = ICD_10_CM_PAT.sub(
        '\n<mark class="entity" style="background: #E5EB34; padding: 0.45em 0.6em; margin: 0 0.25em; line-height: 1; border-radius: 0.35em;">\n    \g<1>\n    <span style="font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; vertical-align: middle; margin-left: 0.5rem">ICD-10-CM</span>\n</mark>\n',
        str(myHtml))
    myHtml = ICD_10_PCS_PAT.sub(
        '\n<mark class="entity" style="background: #EB344; padding: 0.45em 0.6em; margin: 0 0.25em; line-height: 1; border-radius: 0.35em;">\n    \g<1>\n    <span style="font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; vertical-align: middle; margin-left: 0.5rem">ICD-10-PCS</span>\n</mark>\n',
        str(myHtml))
    return myHtml

def get_entity_options():
    entities = ["DISEASE", "CHEMICAL"]
    my_colors = {"DISEASE": "#ADFF2F", "CHEMICAL": "#00FFFF"}
    options = {"ents": entities, "colors": my_colors}
    return options


