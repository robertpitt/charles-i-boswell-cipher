"""Reproducibility and preservation tests, not historical authentication."""
import unittest
import json
from copy import deepcopy
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch
import concordance
import decode_boswell as d

class DecoderTests(unittest.TestCase):
    def test_core_has_exactly_96_positions(self):
        self.assertEqual(sum(d.core_letter(n) is not None for n in range(1000)),96)
    def test_two_row_derivation_independently(self):
        alphabet='ABCDEFGHIKLMNOPQRSTUWXYZ'
        for n in range(20,116):
            r=(n-20)%24
            j=2*r if r<12 else 2*(r-12)+1
            self.assertEqual(d.core_letter(n),alphabet[j])
    def test_period_24(self):
        for n in range(20,92): self.assertEqual(d.core_letter(n),d.core_letter(n+24))
    def test_no_extension_after_115(self):
        self.assertIsNone(d.core_letter(116))
        self.assertIsNone(d.core_letter(159))
    def test_original_dates_retained(self):
        self.assertEqual(d.decode('6_ 8_ 1643'), '6_ 8_ 1643')
    def test_zero_not_silently_null(self):
        self.assertEqual(d.decode('0'),'O')
        self.assertEqual(d.decode('0',mode='core'),'⟦0⟧')
    def test_nulls_are_visible_by_default(self):
        self.assertEqual(d.decode('4 362'),'⟨∅:4⟩ ⟨∅:362⟩')
    def test_graphics_never_discarded(self):
        text='△ 中 □ + ＋'
        self.assertEqual(d.decode(text,mode='core'),text)
        self.assertEqual(d.decode(text),'{△:GOOD} {中:COUSIN} {□:MASTER} {+:US} {＋:US}')
    def test_qualifiers_are_preserved(self):
        self.assertEqual(d.decode('49[b?] 70[y?] 90^'),'L[b?] E[y?] X^')
    def test_unresolved_your_and_new_ending_kept(self):
        self.assertEqual(d.decode('873r 142'),'⟦873⟧r S')
    def test_exploratory_values_are_marked(self):
        self.assertEqual(d.decode('873r',mode='exploratory'),'⟦873:YOU?⟧r')
    def test_funeral_hypotheses_stay_exploratory(self):
        self.assertEqual(d.decode('303 376',mode='core'),'⟦303⟧ ⟦376⟧')
        self.assertEqual(d.decode('303 376'),'⟦303⟧ ⟨∅:376⟩')
        self.assertEqual(d.decode('303 376',mode='exploratory'),
                         '⟦303:TWO?⟧ ⟦376:BOTH?⟧')
        self.assertEqual(d.decode('303 376 16',mode='exploratory',hide_nulls=True),
                         '⟦303:TWO?⟧ ⟦376:BOTH?⟧ ')
        records=d.audit_text('303 376',mode='exploratory')
        self.assertEqual([r['category'] for r in records],['word_code_hypothesis']*2)
    def test_proof_source_and_outputs(self):
        for p in d.check_proofs():
            with self.subTest(p=p['id']): self.assertTrue(p['passed'],p)
    def test_known_anomaly_is_not_repaired(self):
        self.assertEqual(d.compact('27 he 50'),'PHEN')
        self.assertEqual(d.compact('40 24 23 n 48 44 31 2'),'SIGNIAY')
        self.assertEqual(d.compact('20 69 591 & 70 88 126',mode='exploratory'),
                         'AC⟦591:OUR?⟧&ESY')
        self.assertEqual(d.compact('854e 45 62 120 ly',mode='exploratory'),
                         '⟦854:WILL?⟧ECOMLY')
    def test_graphic_gloss_roles_remain_unresolved(self):
        text=d.SOURCES['documents']['Charles']['cipher_bearing_extract']
        records=[r for r in d.audit_text(text) if r['number'] is None]
        self.assertEqual(len(records),15)
        self.assertEqual(sum(r['category']=='working_graphic_code' for r in records),11)
        self.assertEqual(sum(r['category']=='unresolved_graphic_role' for r in records),4)
        for mode in ('working','exploratory'):
            for gloss in d.KEY['inline_graphic_glosses']:
                for hide in (True,False):
                    result=d.decode(gloss['source'],mode=mode,hide_nulls=hide)
                    self.assertIn(gloss['symbol'],result)
                    self.assertIn(';role?⟧',result)
        self.assertEqual(d.decode('47 86 △ 110 33'),'G O ⟦△:GOOD;role?⟧ O D')
    def test_word_code_count_is_not_missing_symbols(self):
        self.assertEqual(d.decode('588 800 835'),'{OF} {TO} {UN}')
    def test_no_modernising_u_v(self):
        self.assertEqual(d.compact('123 138 69 94 96 89 118'),'RECEIUE')
    def test_external_ciphertext_and_existing_assignments(self):
        evidence=json.loads((d.ROOT/'input/external_evidence.json').read_text(encoding='utf-8'))
        for number,output in evidence['unchanged_assignments_checked'].items():
            self.assertEqual(d.value_for(int(number))[0],output)
        for span in evidence['ciphertext_spans']:
            with self.subTest(span=span['id']):
                self.assertEqual(d.decode(span['ciphertext']),span['working_literal_expected'])
        self.assertEqual(d.decode('291'),'{DUKE}')
        self.assertEqual(d.decode('291',mode='core'),'⟦291⟧')
    def test_new_weapons_crib_does_not_change_working_decode(self):
        self.assertEqual(d.decode('755 188 539 40 16 61 at 45 83 & 639'),
                         '⟦755⟧ ⟦188⟧ ⟦539⟧ S ⟨∅:16⟩ M at C H & ⟦639⟧')
    def test_concordance_exact_numbers_and_qualifiers(self):
        text='188 1188 873r 291, 6_ 1643'
        records=concordance.find_occurrences(text,{188,873,291,6})
        self.assertEqual([r['source_field'] for r in records],['188','873r','291,','6_'])
        self.assertEqual([text[r['source_start']:r['source_end']] for r in records],
                         ['188','873','291','6'])
    def test_concordance_counts_in_main_corpus(self):
        from collections import Counter
        codes={755,188,539,639,228,291,873}
        counts=Counter(r['number'] for name,doc in d.SOURCES['documents'].items()
                       for r in concordance.find_occurrences(doc['cipher_bearing_extract'],codes,name))
        self.assertEqual(dict(counts),{755:1,188:1,539:1,639:1,228:1,291:2,873:6})
    def test_full_published_inputs_and_outputs(self):
        d.validate_sources()
        for result in d.check_outputs():
            with self.subTest(document=result['document']):
                self.assertTrue(result['passed'])
    def test_regeneration_detects_stale_or_missing_outputs(self):
        with TemporaryDirectory() as folder:
            root=Path(folder)
            (root/'input').mkdir()
            for name in d.SOURCES['documents']:
                filename=f'{name.lower()}.txt'
                (root/'input'/filename).write_bytes((d.ROOT/'input'/filename).read_bytes())
            (root/'proof_passages.json').write_bytes((d.ROOT/'proof_passages.json').read_bytes())
            with patch.object(d,'ROOT',root):
                self.assertFalse(any(item['passed'] for item in d.check_outputs()))
                d.write_outputs()
                self.assertTrue(all(item['passed'] for item in d.check_outputs()))
                path=root/'output/charles.txt'
                path.write_text('stale output',encoding='utf-8')
                self.assertEqual(d.check_outputs(),[
                    {'document':'Charles','passed':False},
                    {'document':'Nicholas','passed':True},
                ])
                d.write_outputs()
                d.create_audit(root/'audit')
                for name in d.SOURCES['documents']:
                    self.assertEqual((root/'output'/f'{name.lower()}.txt').read_bytes(),
                                     (root/'audit'/f'{name.lower()}_working_literal.txt').read_bytes())
                # A changed continuation in the readable copy must block writes.
                path=root/'input/nicholas.txt'
                path.write_bytes(path.read_bytes()+b'changed continuation')
                before=(root/'output/charles.txt').read_bytes()
                with self.assertRaisesRegex(ValueError,'Readable input differs'):
                    d.write_outputs()
                self.assertEqual((root/'output/charles.txt').read_bytes(),before)
    def test_source_corruption_blocks_audit_before_writing(self):
        sources=deepcopy(d.SOURCES)
        sources['documents']['Charles']['cipher_bearing_extract']+=' altered'
        with TemporaryDirectory() as folder, patch.object(d,'SOURCES',sources):
            destination=Path(folder)/'audit'
            with self.assertRaisesRegex(ValueError,'Source checksum failed: Charles'):
                d.create_audit(destination)
            self.assertFalse(destination.exists())

if __name__=='__main__': unittest.main()
