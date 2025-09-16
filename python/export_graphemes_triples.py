#!/usr/bin/python3.8
# -*- coding: utf-8 -*-

# Import modules

import owlready2
# import rdflib
import types


# Load graphematics ontology

og = owlready2.get_ontology('../graphematics.owl')
og.load()

# Create Ursus ontology

# ou = owlready2.get_ontology(
#    'https://www1.unipa.it/paolo.monella/ursus/ursus_graphemes_from_text.owl')
ou = owlready2.get_ontology('ursus_graphemes_from_text.owl')
ou.load()
# www1.unipa.it/paolo.monella/ursus/
# www1.unipa.it/paolo.monella/ursus/
# www1.unipa.it/paolo.monella/ursus/


# Import graphematics ontology into Ursus ontology

ou.imported_ontologies.append(og)

# Get set of graphemes from a text

t = 'aaa è ü 😱😱😱 dd, ef'
s = set(t)

# NewClass = types.new_class('GraphemeA', (og.Grapheme,),
# kwds = { 'namespace' : 'ursus_graphemes_from_text.owl' })


class GraphemeD(og.Grapheme):
    pass


for g in s:
    my_code = hex(ord(g))
    # NewClass = types.new_class('GraphemeA', (og.Grapheme,))
    ou.my_grapheme = types.new_class(
        my_code,
        (og.Grapheme,),
        # kwds={'namespace': 'http://www.foo.it'}
    )
    print('ou.my_grapheme:', ou.my_grapheme)
    # ou.my_grapheme = og.Grapheme(my_code)
    ou.my_grapheme.label = g
    my_iri = ou.my_grapheme.iri
    # print(my_iri)


# Create tuple of tuples with (Unicode Character, Unicode code point)

codes = tuple((g, hex(ord(g))) for g in s)
# for c in codes:
#    print('char:', c[0], ' | codepoint:', c[1])

ou.save(file='out.xml')
