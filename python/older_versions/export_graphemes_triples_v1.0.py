#!/usr/bin/python3.8
# -*- coding: utf-8 -*-

# Import modules

import owlready2
import rdflib


# Load ontology

onto = owlready2.get_ontology('../graphematics.owl')
onto.load()


# Get set of graphemes from a text

t = 'aaa è ü 😱😱😱 dd, ef'
s = set(t)


# Create tuple of tuples with (Unicode Character, Unicode code point)

chars = tuple((g, hex(ord(g))) for g in s)
for c in chars:
    print('char:', c[0], ' | codepoint:', c[1])


# Create rdflib graph

# Create triples

for c in chars:
    subj = URIRef("http://example.org/donna")
