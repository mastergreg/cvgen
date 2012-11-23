#!/usr/bin/env python
# -*- coding: utf-8
#
#* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
# File Name : generate.py
# Creation Date : 23-11-2012
# Last Modified : Fri 23 Nov 2012 03:17:58 PM EET
# Created By : Greg Liras <gregliras@gmail.com>
#_._._._._._._._._._._._._._._._._._._._._.*/

from jinja2 import Environment, PackageLoader
import settings

def main():
    env = Environment(loader=PackageLoader('webapp', 'templates'))
    for templatename in settings.templates:
        template = env.get_template(templatename)
        fp = "{0}/{1}".format(settings.dumpfolder, templatename)
        print "Generating:",fp
        template.stream(data = settings.mydata).dump(fp)

if __name__=="__main__":
    main()

