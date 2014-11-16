#!/usr/bin/env python
#encoding: utf-8
########################################################################################################################
# Copyright (c) 2013
# Author(s): Kimi Jin <jinyinzhen@gmail.com>
# Date: 1/1/2014
########################################################################################################################

import os
import urllib2
from BeautifulSoup import BeautifulSoup
from xml.etree.ElementTree import parse

url = 'http://www.beaute-test.com/{link}.php'

all_files = os.listdir('raw/')

for file_name in all_files[5:]:
    try:
        tree = parse('raw/' + file_name)
        root = tree.getroot()
        chart_data = root.findall('chart_data')[0]
        link_name = chart_data[1].findall('string')[0].text.lower()
        link_name = link_name.replace('(', '').replace(')', '').replace(' ', '_').replace('+', '_').replace("'", '_').replace('#', '_')
        temp_url = url.format(link=link_name)
        print file_name, ' ', link_name
        parsed_html = BeautifulSoup(urllib2.urlopen(temp_url).read())
        content = [str(i) for i in parsed_html.body.findAll('p') if 'Formule' in str(i)]
        if len(content) > 0:
            f = open('formule/' + file_name, 'w')
            f.write(content[0])
        else:
            print "No formule"

    except Exception as e:
            print "Parse Error ", e