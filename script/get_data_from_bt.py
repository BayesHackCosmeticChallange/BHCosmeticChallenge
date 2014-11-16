#!/usr/bin/env python
#encoding: utf-8
########################################################################################################################
# Copyright (c) 2013
# Author(s): Kimi Jin <jinyinzhen@gmail.com>
# Date: 1/1/2014
########################################################################################################################

import urllib2

url = 'http://www.beaute-test.com/service/chartsxml.php?ID=P{id}'

for i in xrange(35000, 60000):
    print i
    content = urllib2.urlopen(url.format(id=i)).read()
    if content == '':
        pass
    output_file = 'raw/{id}.csv'.format(id=i)
    f = open(output_file, 'w')
    f.write(content)
