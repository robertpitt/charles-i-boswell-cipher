#!/usr/bin/env python3
"""A separate implementation checks the 25 disclosed examples.

This script does not import the decoder. It verifies arithmetic, source offsets
and proposed readings. It does NOT prove priority or historical authenticity.
"""
from pathlib import Path
import json,re,hashlib
root=Path(__file__).resolve().parent
key=json.loads((root/'partial_key.json').read_text())
src=json.loads((root/'input'/'sources.json').read_text())
proofs=json.loads((root/'proof_passages.json').read_text())
alphabet='ABCDEFGHIKLMNOPQRSTUWXYZ'
for name,doc in src['documents'].items():
    assert hashlib.sha256(doc['cipher_bearing_extract'].encode()).hexdigest()==doc['extract_sha256'],name

def independently_decode(text,mode):
    def replacement(m):
        n=int(m.group())
        if 20<=n<=115:
            r=(n-20)%24
            p=2*r if r<12 else 2*(r-12)+1
            return alphabet[p]
        if mode=='working':
            if str(n) in key['additional_letters']:
                return key['additional_letters'][str(n)]['output'].upper()
            if n in key['proposed_nulls']:return ''
            if str(n) in key['working_word_codes']:
                return key['working_word_codes'][str(n)]['output'].upper()
        raise ValueError('Unresolved number in a purported clean example: '+str(n))
    result=re.sub(r'(?<!\d)\d{1,3}(?!\d)',replacement,text)
    return re.sub(r'\s+','',result).upper()

for p in proofs:
    text=src['documents'][p['document']]['cipher_bearing_extract'][p['source_start']:p['source_end']]
    assert text==p['source'],p['id']+' source mismatch'
    actual=independently_decode(text,p['mode'])
    assert actual==p['literal_compact_expected'],(p['id'],actual,p['literal_compact_expected'])
    print(p['id']+': '+actual)
print('All 25 examples reproduced by the separate implementation. This is not independent historical review.')
