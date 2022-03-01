# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 10:36:56 2022

@author: liu  kang
"""

from pybtex.database.input import bibtex
import re
import glob

def search_acl(keyword, year):
    parser = bibtex.Parser()
    if type(year)==int:
        patr = '*%d*.bib' % year
    elif type(year)==list:
        patr = '*[' + ",".join(str(i) for i in year) + ']*.bib'
    else:
        patr = ''
    titles = []
    for name in glob.glob(patr):
        titles = _search_acl(keyword, name) + titles
    return titles
        
def _search_acl(keyword, filename:str):
    parser = bibtex.Parser()
    bib_data = parser.parse_file(filename)
    Keys = list(bib_data.entries.keys())
    Title = [bib_data.entries[Keys[i]].fields['title'] for i in range(len(Keys))]
    Title = [re.sub("[{}\\\_'`]", '', Title[i]) for i in range(len(Title))]
    matching = [s for s in Title if keyword in s.lower()]
    return matching
    
match = search_acl('cleaning', [2020, 2021])
print(match)