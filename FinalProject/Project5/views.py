from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Template
import os

import re
import scispacy
import spacy
from spacy import displacy
import pandas as pd
import numpy as np

ICD_10_CM_PAT = re.compile(r'\b(?<!#)([A-Z]\d[A-Z0-9]{1,5})\b')
ICD_10_PCS_PAT = re.compile(r'\b(?<!#)([0-9A-HJ-NP-Z]{7})\b')
REMOVE_PRIVATE_INFO = re.compile('(\[\*\*.+\*\*\])')
nlp = spacy.load("en_ner_bc5cdr_md")




def index(request):
    if (request.POST.get('highlight1')):
        string = getHighlight(getCSVData(0))
    elif (request.POST.get('highlight2')):
        string = getHighlight(getCSVData(1))
    elif (request.POST.get('highlight3')):
        string = getHighlight(getCSVData(2))
    elif (request.POST.get('submitText')):
        text = request.POST['textInput']
        string = getHighlight(text)
    else:
        string = "<h4>Click a button above or input text into the textbox to run the code!</h4>"
    return render(request, 'Project5/index.html', {'string': string})

def getHighlight(text):
    text = removeNamePattern(text)
    doc = nlp(text)
    myHtmlStr = highlight(doc)
    return myHtmlStr


def highlight(doc):
    myHtml = displacy.render(doc, style='ent', options=getEntityOptions())
    myHtml = ICD_10_CM_PAT.sub(
        '\n<mark class="entity" style="background: #E5EB34; padding: 0.45em 0.6em; margin: 0 0.25em; line-height: 1; border-radius: 0.35em;">\n    \g<1>\n    <span style="font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; vertical-align: middle; margin-left: 0.5rem">ICD-10-CM</span>\n</mark>\n',
        str(myHtml))
    myHtml = ICD_10_PCS_PAT.sub(
        '\n<mark class="entity" style="background: #EB344; padding: 0.45em 0.6em; margin: 0 0.25em; line-height: 1; border-radius: 0.35em;">\n    \g<1>\n    <span style="font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; vertical-align: middle; margin-left: 0.5rem">ICD-10-PCS</span>\n</mark>\n',
        str(myHtml))
    return myHtml

def getEntityOptions():
    entities = ["DISEASE", "CHEMICAL"]
    my_colors = {"DISEASE": "#ADFF2F", "CHEMICAL": "#00FFFF"}
    options = {"ents": entities, "colors": my_colors}
    return options

def getCSVData(num):
    urlString = 'NOTEEVENTS-' + str(num) + ".csv"
    module_dir = os.path.dirname(__file__)
    url = os.path.join(module_dir, urlString)
    notes = pd.read_csv(url, header=None)
    splitNotes = np.array_split(notes, 200)
    return combineText(splitNotes[0])

def combineText(textDF):
    returnText = ""
    for i in range(len(textDF)):
        returnText += "\n" + textDF[0].iloc[i]
    return returnText

def removeNamePattern(text):
    text = REMOVE_PRIVATE_INFO.sub('', str(text))
    return text




