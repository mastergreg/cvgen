#!/usr/bin/env python
# -*- coding: utf-8
#
#* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
# File Name : settings.py
# Creation Date : 23-11-2012
# Last Modified : Fri 23 Nov 2012 05:08:30 PM EET
# Created By : Greg Liras <gregliras@gmail.com>
#_._._._._._._._._._._._._._._._._._._._._.*/

from pycv.ContactInfo import *
from pycv.Education import *
from pycv.Experience import *
from pycv.Skills import *

templates = [ 'index.html' ]
dumpfolder = 'webapp/public_html'





c = { 'name' : Name(first_name = 'Mter', last_name = 'Greg'),
      'address' : Address(street_number='Str33t', street_name = 'Street Name', 
            region = 'R3g10n', postal_code = 'postal', city = 'City', country = 'Country'),
      'telephone' : Phone(country_prefix = '+11', phone_number = '1234567890'), 
      'mobile' : Phone(country_prefix = '+11', phone_number = '1234567890'), 
      'email' : 'asdf@asdf.org'}

mydata = {}
mydata['ContactInfo'] = ContactInfo(**c)
mydata['Experience'] = []
mydata['Education'] = []
mydata['Skills'] = []

mydata['Skills'].append(
        Skills(section="Foo",  comment= """
            Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim
            ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
            aliquip ex ea commodo consequat. Duis aute irure dolor in
            reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
            pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
            culpa qui officia deserunt mollit anim id est laborum.
            """, skills=["a", "b", "c"]))
mydata['Skills'].append(
        Skills(section="Foo",  comment= """
            
            Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim
            ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
            aliquip ex ea commodo consequat. Duis aute irure dolor in
            reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
            pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
            culpa qui officia deserunt mollit anim id est laborum.
            """, skills=["a", "b", "c"]))
mydata['Skills'].append(
        Skills(section="Foo",  comment= """
            
            Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim
            ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
            aliquip ex ea commodo consequat. Duis aute irure dolor in
            reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
            pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
            culpa qui officia deserunt mollit anim id est laborum.
            """, skills=["a", "b", "c"]))


mydata['Experience'].append(
        Experience(year='2012 - 2013', working_environment='National Technical Univercity of Athens (NTUA)', position='Masters', 
            body_text="""
            
            Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim
            ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
            aliquip ex ea commodo consequat. Duis aute irure dolor in
            reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
            pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
            culpa qui officia deserunt mollit anim id est laborum.
            
            
            
            
            Big comment really long"""))

mydata['Education'].append(
        Education(year='2012 - 2013', title='National Technical Univercity of Athens (NTUA)', degree='Masters', 
            body_text="""
            
            Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim
            ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
            aliquip ex ea commodo consequat. Duis aute irure dolor in
            reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
            pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
            culpa qui officia deserunt mollit anim id est laborum.
            
            
            
            
            Big comment really long text"""))
