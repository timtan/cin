# -*- coding: utf-8 -*- 
from __future__ import unicode_literals
from cin import Cin

def test_basic():
    fs = open("test/test.cin")    
    cin = Cin(fs)
    assert u"測試米" == cin.getCname() 
    assert u"Ａ" == cin.getKeyName("a") 
    assert u"對" == cin.getCharDef("a")[0]
    assert 3 == len(cin.getCharDef("lzo")) 
