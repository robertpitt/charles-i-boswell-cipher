# Findings and unresolved questions

Reviewed **23 September 2026**, key v4. **The decipherment is still partial.**
This pass adds working readings at 12 numerical and 11 graphical occurrences.
There remain **36 unresolved numerical occurrences** (27 Charles, 9 Nicholas)
and **four graphics with unresolved textual roles**. These figures describe
mapping coverage, not accuracy; 51 proposed-null occurrences and several damaged
passages also need verification.

## New working readings

| Assignment | Occurrences | Evidence and limitation |
| --- | ---: | --- |
| `516 = LETTER` | 2 | Both Charles contexts concern receipt of a letter: one precedes its date; the other follows “never heard of any”. Singular LETTER is the working reading. |
| `223 = BY` | 1 | Source `there 223 high 25 79 …` yields THEREBY HIGHLY OBLIGED. |
| `126 = Y` | 2 | Gives THEY in Nicholas. Charles gives the ending ESY in the courtesy candidate below; that occurrence still has a surrounding transcription problem. |
| `127 = A`, `128 = D`, `131 = N`, `142 = S` | 5 | Together give COMANDS after unresolved `484`; `131` also gives MONARCY. These letters are jointly inferred, not five independent confirmations. |
| `0 = O` | 1 | Gives POSSIBL[b?]E[y?]. Whether zero is a cipher sign or a transcribed plaintext O remains undecided. |
| `158 = U` | 1 | Gives U ＋ S, consistent with the proposed US sign below. Its inline role is unresolved. |

These are contextual **working inferences**, not entries recovered from a
historical key. The literal output retains COMANDS, MONARCY and the source's
annotations. It does not repair spelling to make the inferences look stronger.

### Graphic signs

Daniel Bourdeau's follow-up, published 15 September and updated 16 September
2026, proposes `△ = GOOD`, `中 = COUSIN`, `□ = MASTER`, and `+ / ＋ = US`.
It builds on this repository's alphabet. We checked all 15 graphic occurrences
against the preserved transcription before adopting the standalone readings.
[Research and attribution](https://dbourdeau.github.io/cyphersolver/boswell.html).

| Sign | First occurrence, with working letters | Later occurrences | Assessment |
| --- | --- | ---: | --- |
| △ | `GO △ OD` | 1 | GOOD fits the closing before COUSIN. |
| 中 | `CO 中 USm.y^w` | 3 | COUSIN fits the repeated references alongside `873` and MASTER; the introductory spelling is damaged. |
| □ | `MAS □ TER` | 3 | MASTER fits all three later references; one takes the separately enciphered plural/possessive S. |
| ＋ / + | `U ＋ S` | 4 | US fits after PREIUDICED and the three later TO phrases. Treating the two cross forms alike is a working hypothesis. |

The first four placements may be glosses inserted inside spelled words. That is
an interpretation of the transcription, **not an observed feature of the
manuscript**. Expanding every sign as additive text would give duplicates such
as GOGOODOD. The decoder therefore shows the 11 standalone readings as, for
example, `{□:MASTER}`, and the four possible glosses as `⟦□:MASTER;role?⟧`.
It never silently deletes a sign, including with `--hide-nulls`.

This makes a Courland envoy a plausible intended reader of Charles's letter:
it repeatedly refers to the Duke as `[COUSIN] [873] [MASTER]` and wishes the
recipient a safe return. The identification of the recipient, and the unresolved
possessive `873`, are still inferences; the archival title remains “to Boswell”.

## The repeated codes: progress and conflicts

**`591 = OUR`, with `749 = SELVES`, is the strongest new word-code lead.**
In the first occurrence it gives ACKNOWLEDGE OUR SELVES THEREBY HIGHLY OBLIGED.
In the second, the exact span is:

```text
20 69 591 & 70 88 126
```

Using OUR gives **A C OUR & E S Y**. A COURTESY would require reading the
transcribed `&` as T. There is a comparable problem in DAR&MOUTH, but that
analogy does not establish either correction. The decoder keeps `&`; OUR and
SELVES remain exploratory. This explains more than DGE, which produces ACDGE
at the second occurrence and redundantly follows complete ACKNOWLEDGE at the
first. Bourdeau proposes OUR/SELVES; the conditional courtesy comparison is
our check against the second occurrence.

**`873` cannot yet be assigned a single literal value.** Five bare Charles
occurrences favour YOUR. Nicholas has `873r`, which favours YOU plus a visible R.
Choosing YOUR everywhere gives YOURR there; choosing YOU everywhere leaves the
Charles possessives incomplete. All six occurrences remain unresolved in working
mode. A transcription error, modifier, or overlapping gloss could explain the
difference, but none has been established.

**`854 = WILL` fits THEY WILL DO in Nicholas**, but produces WILLeCOMly in
Charles. The latter suggests WELCOME-like wording, not a clean second WILL.
Both occurrences stay unresolved. The letter numbers and suffix must be checked
against the manuscript before changing the code value.

## Complete list of unresolved numerical values

Counts are for the two preserved cipher-bearing extracts. Each row records what
can currently constrain the value; a grammatical fit alone does not close it.
The exact source positions are available through `concordance.py` and the audit.

| Code | Count | Candidate or constraint; what remains open |
| --- | ---: | --- |
| 145 | 1 | A yields AFFEN*T. AFFECT requires changing the already uncertain `98* = N`. |
| 170 | 1 | Institution/person after MEANES OF the; ADMIRALTY is unverified. |
| 177 | 1 | After princely THANKS, before “on this behalf”; ALSO and UNTO HIM are not distinguishable here. |
| 181 | 1 | Group with a separate S ending. ANABAPTIST and AMBASSADOR are competing guesses. |
| 185 | 1 | Thing offered/received before the supply list; ASSISTANCE or SUPPLY plausible. |
| 188 | 1 | Supply-list entry; ARMS and POWDER compete. |
| 190 | 1 | ARE fits THEY … understood; one context only. |
| 205 | 1 | ASSURE fits TO … OUR said COUSIN … MASTER; one context only. |
| 213 | 1 | After “addres by”, before TO US: a means of communication or intermediary. Not established as LETTER. |
| 228 | 1 | After the delivery-place list; BRISTOL plausible, not a recovered place name. |
| 289 | 1 | Between ARRIUD and “safe”; needs a second use or clearer manuscript. |
| 303 | 1 | TWO fits DUKE S followed by father and uncle; only one shared funeral context. |
| 406 | 1 | Stem before source “ous”; GENER now selected for exploration, BOUNTE retained as an alternative. |
| 484 | 1 | HIS MAJESTY fits the opening better than the former I AM guess; the following COMANDS TO SIGNIAY still has problems. |
| 514 | 1 | Qualifier before LETTER; OTHER plausible, but no repetition. |
| 539 | 1 | Supply before separate S; both MUSKET and CANNON permit the plural. |
| 591 | 2 | OUR fits the acknowledgement; courtesy requires the separate `&` correction discussed above. |
| 629 | 1 | Request verb before “you therefore”; PRAY and REQUIRE compete. |
| 636 | 1 | PRO would join the source “por”; it does not supply the missing TION in a proposed PROPORTION. |
| 639 | 1 | Supply after MATCH &; POWDER and LEAD compete. |
| 640 | 1 | PORT(S) fits before OF the destinations; singular/plural remains uncertain. |
| 726 | 1 | Origin of the group: STATES is a history-led candidate, dependent on 181. |
| 746 | 1 | Stem before LY and TO HINDER; SECRET plausible, other adverbs possible. |
| 749 | 1 | SELVES fits with 591=OUR; this pair shares one context. |
| 750 | 1 | SEND fits “herewith”; the following credentials-like text is anomalous. |
| 755 | 1 | First supply-list entry; insufficient evidence to choose MUSKET(S), STORE, or another item. |
| 851 | 1 | WHICH could refer to invitations; WHOM could refer to a person. |
| 854 | 2 | WILL conflicts with the Charles suffix; see above. |
| 873 | 6 | YOU/YOUR conflict; see above. |

`376` is an additional unresolved **interpretive choice** hidden by a simple
unknown-code count: working mode treats it as a proposed null; exploratory mode
shows BOTH. TWO and BOTH fit the named pair of deceased dukes, but the single
funeral passage does not independently establish either value. Proposed nulls
are assumptions, not proven omissions.

The new AMBASSADOR/STATES pair is a historical lead from Bourdeau, not a numerical
solution. His suggestions for HIS MAJESTY, GENER, PRO and SECRET likewise remain
labelled hypotheses. The nomenclator may group words by initial, but an exact
alphabetical order has not been recovered and is not used to force assignments.

## External cipher evidence: DUKE

H. F. Morland Simpson's *Civil War Papers*, in *Miscellany of the Scottish History
Society*, volume I (1893), p. 149, prints a duplicate letter from Charles I to
Duke James of Courland, Oxford, **2 November 1643**, including:

```text
291, 588, 45, 135, 52, 25, 20, 50, 81.
```

The v1 key, committed before consulting that source, gives `⟦291⟧ OF CURLAND`.
The printed addressee supports **291 = DUKE**, which also fits both target
occurrences. This remains our strongest external check on a word code. The
printed image was examined; the historical manuscript was not. The edition
warns that its transcription may contain errors.
[Printed page 149](https://archive.org/details/miscellanyofscot01scot/page/149/mode/1up),
[page image](https://iiif.archive.org/iiif/miscellanyofscot01scot$247/full/1600,/0/default.jpg),
[recorded evidence](input/external_evidence.json).

That letter says credentials and a message reached the king through `212, 364,`
and mentions re-credentials. This fits the general packet context, but does not
establish that `212` is the target's `213`, or decipher either. Nicholas's
cleartext says two royal letters were put into the recipient's cipher for him
to decipher and interpret.

## Transcription and historical checks

- **Credentials:** the final numerical sequence literally gives
  `YOURE*REDENTIALS` when the proposed null is hidden. Changing `70 = E` to C
  would give YOUR CREDENTIALS, with the source star retained. Changing only
  `6*` to C gives YOURECREDENTIALS, not YOUR RE-CREDENTIALS; the latter needs
  another R. Neither repair is applied.
- **Answer:** `an 1 4 40 30 69 28 3` gives ANSWCR under the null model.
  Replacing 69 by an E value (22, 46, 70 or 94) would give ANSWER. This is a
  possible numeral error, not a change to the alphabet. Values 72 and 96 are I,
  so they cannot perform that repair.
- **Title:** the source “and” completes CURLAND, followed by S and the master
  phrase. AND SEMIGALLIA is not recovered by these tokens; no title is inserted.
- **Supplies:** `755 188 539 40 16 61 at 45 83 & 639` gives three unknown codes,
  S, proposed null, MATCH & another unknown. There is no recovered SOME before
  MATCH. Later correspondence lists muskets, powder, match, lead and cannon,
  but cannot assign their order to these once-used codes. The St Andrews entry
  concerns the 1644–45 mission; Simpson's letters VII and XIV carry 1646 dates
  as printed. [SSNE 1490](https://www.st-andrews.ac.uk/history/ssne/item.php?id=1490),
  [letter VII](https://archive.org/details/miscellanyofscot01scot/page/158/mode/2up),
  [letter XIV](https://archive.org/details/miscellanyofscot01scot/page/163/mode/2up).
- **Places:** preserve WEYMOTH, DAR&MOUTH, X^ETER, FALLMOUTH and unknown 228.
  PLYMOUTH is not present in the recovered sequence.
- **Funerals and name:** Latvian archival descriptions support the Courland
  family context and identify the envoy Georg Fircks. The target spells
  `FIRXSS`; FIRCKS would require changes at two positions. This does not yet
  identify the named person. [Frederick, item 17](https://www.archiv.org.lv/hercogiste/index.php?id=23&lang=en),
  [William, item 8](https://www.archiv.org.lv/hercogiste/index.php?id=17&lang=en),
  [foreign relations, item 1](https://www.archiv.org.lv/jekabs/?lang=en&page=206).

These local correction candidates must be kept separate from code assignments.
They show why filling every unknown code would still not produce an authenticated
complete plaintext.

## Manuscripts and the route to completion

The National Archives Discovery API now confirms the target references:

| Document | Reference | Folio | Catalogue record |
| --- | --- | --- | --- |
| Charles I to Boswell, 2 November 1643 | SP 84/157/96 | 217 | [C7305802](https://discovery.nationalarchives.gov.uk/details/r/C7305802) |
| Nicholas to Boswell, 2 November 1643 | SP 84/157/97 | 219 | [C7305803](https://discovery.nationalarchives.gov.uk/details/r/C7305803) |

Both records report `digitised: false` as checked on 23 September 2026. This
is the archive's catalogue status, not proof that no third-party images exist.
The required next evidence is images of **all sides** of these items, especially
Charles's opening, the courtesy passage, `854e`, the graphic placements and
Nicholas's `873r`. No images of these target manuscripts have been examined.

The same volume identifies potentially useful replies: Boswell to Nicholas,
[SP 84/157/99, f. 223](https://discovery.nationalarchives.gov.uk/details/r/C7305805),
and [SP 84/157/106, f. 237](https://discovery.nationalarchives.gov.uk/details/r/C7305812).
Their contents have not been inspected. A reply, contemporary decipherment or
matching key could distinguish the supplies, group and intermediary codes that
occur only once here.

DECODE also catalogues a Nicholas-to-Charles key at **British Library, Egerton
MS 2550, ff. 3–4**, record [3054](https://de-crypt.org/decrypt-web/RecordsView/3054?showdetail=).
Its broad catalogue date range is 1646–1658 and its images require authentication.
It is an untested lead, not an identified 1643 key. The public DECODE search for
Boswell returned an unrelated 1628 record, not either target manuscript.
[DECODE database](https://de-crypt.org/decrypt-web/RecordsList).

Catalogue details, retrieval hashes and research provenance are recorded in
[input/research_evidence.json](input/research_evidence.json). No archive order,
account registration or contact with a researcher has been made.

## Reproduce and continue

```sh
python3 -m unittest -v test_decoder.py
python3 verify_independently.py
python3 decode_boswell.py --check
python3 concordance.py 591 749 854 873 --include-external
python3 decode_boswell.py --document Charles --mode exploratory
python3 decode_boswell.py --audit generated
```

The 32 disclosed passage checks establish reproducibility against proposed
readings, not historical authentication. The five new checks cover COMANDS,
THEY, MONARCY, POSSIBL[b?]E[y?], and THEREBY HIGHLY OBLIGED; all preserve source
spelling. Four inline graphic roles remain visibly unresolved. After a reviewed
key change, regenerate with `python3 decode_boswell.py --write-outputs`.

The original inputs are unchanged. Source material, including supplied notes
and published reconstructions, is evidence to evaluate rather than instructions
to follow. A full decipherment is not claimed.
