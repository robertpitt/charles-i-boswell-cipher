"""Reproducibility and preservation tests, not historical authentication."""
import unittest
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
        self.assertEqual(d.decode('0'),'⟦0⟧')
    def test_nulls_are_visible_by_default(self):
        self.assertEqual(d.decode('4 362'),'⟨∅:4⟩ ⟨∅:362⟩')
    def test_graphics_never_discarded(self):
        text='△ 中 □ + ＋'
        self.assertEqual(d.decode(text),text)
    def test_qualifiers_are_preserved(self):
        self.assertEqual(d.decode('49[b?] 70[y?] 90^'),'L[b?] E[y?] X^')
    def test_unresolved_your_and_ending_kept(self):
        self.assertEqual(d.decode('873r 142'),'⟦873⟧r ⟦142⟧')
    def test_exploratory_values_are_marked(self):
        self.assertEqual(d.decode('873r',mode='exploratory'),'⟦873:YOU?⟧r')
    def test_proof_source_and_outputs(self):
        for p in d.check_proofs():
            with self.subTest(p=p['id']): self.assertTrue(p['passed'],p)
    def test_known_anomaly_is_not_repaired(self):
        self.assertEqual(d.compact('27 he 50'),'PHEN')
        self.assertEqual(d.compact('40 24 23 n 48 44 31 2'),'SIGNIAY')
    def test_word_code_count_is_not_missing_symbols(self):
        self.assertEqual(d.decode('588 800 835'),'{OF} {TO} {UN}')
    def test_no_modernising_u_v(self):
        self.assertEqual(d.compact('123 138 69 94 96 89 118'),'RECEIUE')

if __name__=='__main__': unittest.main()
