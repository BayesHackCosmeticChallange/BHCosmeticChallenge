#!/usr/bin/env python
#encoding: utf-8
########################################################################################################################
# Copyright (c) 2013
# Author(s): Kimi Jin <jinyinzhen@gmail.com>
# Date: 1/1/2014
########################################################################################################################
import goslate
import os
import json
import pandas as pd
from xml.etree.ElementTree import parse


# Clean the data from the beaute test
def format_file(input_dir='raw/'):

    gs = goslate.Goslate()
    all_files = os.listdir(input_dir)
    for file_name in all_files:

        print "Processing file {filename}".format(filename=file_name)
        #parse the data from the website
        try:
            tree = parse(input_dir + file_name)
            root = tree.getroot()
            chart_data = root.findall('chart_data')[0]
            attributes_names = [i.text for i in chart_data[0].findall('string')]
            scores = [i.text for i in chart_data[1].findall('number')]

            # this is the product and brand name
            product, brand = chart_data[1].findall('string')[0].text.split(' (')
            product = gs.translate(product, 'en', 'fr')
            brand = brand[:-1]
            output_json = {'product': product, 'brand': brand, 'chart_data': {}}

            # Charts data
            for i in xrange(len(attributes_names)):
                output_json['chart_data'][attributes_names[i]] = scores[i]

            json.dump(output_json, open('clean/' + file_name, 'w'))

        except Exception as e:
            print "Parse Error ", e


def to_csv(input_dir='clean/'):
    all_files = os.listdir(input_dir)
    product_names = []
    brand_names = []
    # Efficacite a long terme
    efficancy_long = []
    # Efficacite a court terme
    efficancy_short = []
    # Rapport qualite/prix
    quality = []
    # Texture
    texture = []
    # Pouvoir lavant
    lavant = []
    # Odeur
    smell = []
    # Rincabilite
    rincable = []
    # Presentation
    present = []

    for file_name in all_files:
        print file_name
        try:
            content = json.load(open('clean/' + file_name, 'r'))
            product_names.append(content['product'])
            brand_names.append(content['brand'])
            chart_data = content['chart_data']
            if 'Efficacite a long terme' in chart_data.keys():
                efficancy_long.append(chart_data['Efficacite a long terme'])
            else:
                efficancy_long.append('')

            if 'Efficacite a court terme' in chart_data.keys():
                efficancy_short.append(chart_data['Efficacite a court terme'])
            else:
                efficancy_short.append('')

            if 'Rapport qualite/prix' in chart_data.keys():
                quality.append(chart_data['Rapport qualite/prix'])
            else:
                quality.append('')

            if 'Texture' in chart_data.keys():
                texture.append(chart_data['Texture'])
            else:
                texture.append('')

            if 'Pouvoir lavant' in chart_data.keys():
                lavant.append(chart_data['Pouvoir lavant'])
            else:
                lavant.append('')

            if 'Odeur' in chart_data.keys():
                smell.append(chart_data['Odeur'])
            else:
                smell.append('')

            if 'Rincabilite' in chart_data.keys():
                rincable.append(chart_data['Rincabilite'])
            else:
                rincable.append('')

            if 'Presentation' in chart_data.keys():
                present.append(chart_data['Presentation'])
            else:
                present.append('')

        except:
            print "no content"

    df = pd.DataFrame({'efficancy_long': efficancy_long, 'efficancy_short': efficancy_short,
                       'quality': quality, 'brand': brand_names, 'product': product_names,
                       'texture': texture, 'lavant': lavant, 'smell': smell, 'rincable': rincable,
                       'presentation': present})
    df.to_csv('clean.csv', encoding='utf-8')

if __name__ == '__main__':
    #format_file()
    to_csv()