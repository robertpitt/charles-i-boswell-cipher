# Findings and unresolved questions

Reviewed **23 September 2026**. The historical evidence and candidate review
below were assembled on 14 September; the cleanup review adds no deciphered
values. **An external cipher specimen supports `291 = DUKE`.** `303 = TWO` and
`376 = BOTH` remain exploratory. Supplied research notes and candidate tables
are treated as hypotheses, not authenticated plaintext.

## Funeral leads: TWO and BOTH

The supplied candidate table offers two useful leads in the same passage.
Each occurs **once**, in Charles's letter; neither occurs in Nicholas's extract.

| Code | New candidate | Support and remaining uncertainty |
| --- | --- | --- |
| 303 | TWO | Precedes `291 40 = DUKE S`, followed by the father-and-uncle phrase. TWO fits the named pair, but there is no repeated use to distinguish it from another qualifier. |
| 376 | BOTH | Follows that pair and precedes cleartext `deceased of happy memory`. BOTH fits, but the existing proposed-null interpretation also permits the phrase. |

The unchanged source span is:

```text
303 291 40 his 34 44 29 hir &
65 50 60 25 22 16 376 deceased of happy memory
```

Working output:

```text
⟦303⟧ {DUKE} S his F A T hir &
U N K L E ⟨∅:16⟩ ⟨∅:376⟩ deceased of happy memory
```

Exploratory output:

```text
⟦303:TWO?⟧ {DUKE} S his F A T hir &
U N K L E ⟨∅:16⟩ ⟦376:BOTH?⟧ deceased of happy memory
```

Both candidates are recorded in `partial_key.json`. Exploratory mode tests BOTH
in place of the proposed null; working mode keeps `303` unresolved and `376`
marked as a proposed null. These are two inferences from **one context**, not
independent confirmations of each other. No source spelling is repaired and
neither candidate is added to the proof passages.

The other suggestions do not justify new selected key values. Several repeat
existing hypotheses; the remaining plausible words lack a distinguishing
constraint. Two stronger claims conflict with the current transcription:
`and` completes `CURLand`, followed by `S ⟦873⟧ M A S □ T E R`, which does not
recover AND SEMIGALLIA; and `591 = DGE` would append DGE to already-complete
ACKNOWLEDGE and produce ACDGE at its second occurrence. These claims are not
added to the key. [Published transcription](https://cryptiana.blogspot.com/2021/09/charles-i-boswell-cipher-1643.html).

The v3 key changes only Charles's exploratory reading, at `303` and `376`.
The two committed working outputs remain identical to v2. Working coverage
remains **48 unresolved numerical occurrences** and **15 unresolved graphical
occurrences**. The proposed-null count remains 51.

## A separate letter from the same date

H. F. Morland Simpson's *Civil War Papers*, in *Miscellany of the Scottish History
Society*, volume I (1893), prints a duplicate of Charles I's letter to Duke James
of Courland, Oxford, **2 November 1643**. Page 149 contains this numerical line:

```text
291, 588, 45, 135, 52, 25, 20, 50, 81.
```

Using the working key already committed at `165dd0c`, before this source was
consulted, it reads:

```text
⟦291⟧, {OF}, C, U, R, L, A, N, D.
```

Six letters follow the existing periodic alphabet; `135 = U` and `588 = OF`
were also already in the key. No new letter value or local correction is needed.
The printed addressee supports interpreting the remaining code as **DUKE**.
This also fits both occurrences of `291` in the target Charles letter: before
`OF CURLand`, and before the plural `S` in the funeral passage.
[Printed page 149](https://archive.org/details/miscellanyofscot01scot/page/149/mode/1up),
[page image](https://iiif.archive.org/iiif/miscellanyofscot01scot$247/full/1600,/0/default.jpg).

`291 = DUKE` was therefore promoted from exploratory to **working** in v2.
The exact printed sequences, baseline result, source details, and image hash are recorded
in [input/external_evidence.json](input/external_evidence.json). The image was
visually checked; the original manuscript was not. The edition warns that its
transcription may contain errors. This is an external consistency check, found
through the Courland lead, rather than a blind accuracy test or a recovered key.

The external letter says an envoy's credentials and message reached the king
through `212, 364,` and that the king is sending a reply and re-credentials. That is
consistent with the target Nicholas letter's mention of two enclosed royal
letters, but a shared packet is **not established**. Neither `212` nor the
target letter's `213` has been identified, and they must not be conflated.

## Arms: a useful crib, with competing assignments

The St Andrews SSNE entry for John Cochrane describes negotiations with Duke
James involving muskets, powder, match, lead, and cannon. Its itinerary places
the Baltic mission in 1644–45, rather than directly documenting our November
1643 letter. It establishes a relevant supply relationship, not the values of
our numerical codes.
[SSNE 1490](https://www.st-andrews.ac.uk/history/ssne/item.php?id=1490).

Following that bibliography led to printed primary correspondence: letter VII
requests muskets, powder, match, and lead bullets; letter XIV reports receipt
of cannon and muskets. Their headings date them **5 January and 2/12 May 1646**
respectively. These are dates as printed, not a resolution of the chronology:
the edition's later historical notes also discuss events of 1645. The supplies
cannot be assigned to the 1643 ciphertext merely by matching a later list.
[Letter VII, pp. 158–159](https://archive.org/details/miscellanyofscot01scot/page/158/mode/2up),
[letter XIV, pp. 163–165](https://archive.org/details/miscellanyofscot01scot/page/163/mode/2up).

The relevant source sequence is:

```text
755 188 539 40 16 61 at 45 83 & 639
```

The working key produces:

```text
⟦755⟧ ⟦188⟧ ⟦539⟧ S ⟨∅:16⟩ M at C H & ⟦639⟧
```

**MATCH is partly enciphered:** the numbers supply M, C, H; `at` was already
readable. `40 = S` could be a plural ending for either MUSKET or CANNON. Each
unknown supplies code occurs once in the two-letter corpus; no second local
occurrence distinguishes the competing readings.

| Code | Original exploratory candidate | New history-led candidate | Main-corpus occurrences |
| --- | --- | --- | ---: |
| 755 | Unresolved | MUSKET(S) | 1 |
| 188 | ARMS | POWDER | 1 |
| 539 | MUSKET | CANNON | 1 |
| 639 | POWDER | LEAD | 1 |

These alternatives are recorded in `partial_key.json`; **none is promoted to
working**. Exploratory decoding still displays the original selected candidates
with question marks. The `alternatives` fields retain the new suggestions for
comparison; they are not silently substituted into the output.

## Historical and transcription constraints

- **Funerals:** the Latvian archives record Frederick's funeral in February
  1643 and William's death in 1640, with his remains ordered home two years
  later. This supports the Courland family context. The cipher literally gives
  `FAT` plus cleartext `hir`, and `UNKLE`; it does not cleanly produce modern
  `FATHER`. [Frederick, item 17](https://www.archiv.org.lv/hercogiste/index.php?id=23&lang=en),
  [William, item 8](https://www.archiv.org.lv/hercogiste/index.php?id=17&lang=en).
- **Ports:** retain `WEYMOTH`, `DAR&MOUTH`, `X^ETER`, `FALLMOUTH`, and unresolved
  `228`. There is no established PLYMOUTH reading. Plymouth remained under
  Parliament during the siege, so inserting it into a list of Royalist delivery
  ports is additionally questionable. `228 = BRISTOL` remains a hypothesis.
  [The Box Plymouth](https://www.theboxplymouth.com/blog/art/collection-insight-execution-of-a-traitor).
- **Personal name:** Nicholas's `82 48 52 42 40 64` gives `FIRXSS`. The archives
  identify Georg Fircks as Courland's envoy who signed the French agreement in
  December 1643. `FIRCKS` is a useful manuscript-check candidate, but it would
  require different values at two positions: C instead of X, K instead of S.
  No source numeral or alphabet assignment has been altered to obtain it.
  [Latvian archives, foreign relations, item 1](https://www.archiv.org.lv/jekabs/?lang=en&page=206).

## Remaining evidence

The working result still contains 32 unresolved numerical occurrences in Charles
and 16 in Nicholas. No further assignment was established in the cleanup review.
The strongest next checks concern repeated codes and the provisional transcription:

| Target | Current constraint | Evidence needed |
| --- | --- | --- |
| `873` (6 occurrences) and nearby graphics | Bare, suffixed, and graphic-enclosed forms may differ; YOU does not explain them all. | Manuscript images showing the actual symbols and their boundaries. |
| `854` (2 occurrences, both letters) | WILL fits Nicholas's tentative THEY … DO, but gives `WILLeCOMly` in Charles. | Inspect the Charles numeral and adjacent cleartext before selecting one value. |
| `591` (2 occurrences) | A value must fit both `ACKNOWLEDGE [591] [749]` and `AC [591]`; DGE fails. | A clearer transcription or a matching key covering both uses. |
| `303`, `376` (1 occurrence each) | TWO and BOTH fit a single shared context; `376` may still be null. | A second occurrence or a historical key that distinguishes the alternatives. |
| Supplies, `228`, and Nicholas's `170`, `181`, `726` | Context suggests categories but does not identify the words, place, institution, or group. | Another letter using these codes or a matching nomenclator. |
| `212`/`213`, `FIRXSS`, and the final credentials-like passage | Proposed identities and spelling repairs are not established. | Original numeral and letter forms; keep possible transcription corrections separate from key changes. |

The original target manuscript references and a matching historical key have
not been established. A full decipherment requires additional evidence; the
repository makes the current partial result reproducible and the gaps explicit.

## Reproduce and continue

```sh
python3 -m unittest -v test_decoder.py
python3 verify_independently.py
python3 decode_boswell.py --check
python3 concordance.py 303 376
python3 decode_boswell.py --document Charles --mode exploratory
python3 concordance.py 755 188 539 639 228 291 873 --include-external
python3 decode_boswell.py --audit generated
```

The checks cover input integrity, complete committed outputs, and the disclosed
passage examples. To refresh `output/` after an intentional key change, run
`python3 decode_boswell.py --write-outputs`, then rerun the checks. Audit
generation and published outputs share a renderer, preserving the same notation.

The concordance searches exact numerical tokens and preserves suffixes,
punctuation, source offsets, and context. It loads no key or proposed plaintext.
It searches only the two supplied extracts and, optionally, the two external
reference spans; it is not a search of an entire archival collection.

In the original corpus, `291` occurs twice and `873` six times; each other code
in these commands occurs once. Three occurrences of `873` appear with nearby
graphical signs, two are bare, and one has an `r` suffix. Their interpretation
may depend on those signs; counting them together does not establish a single
word value.

The earlier research checked the linked historical sources, the 1893
correspondence, and Cryptiana's unsolved-cipher and Stuart-cipher surveys. It
found the external `291` example above, but no second specimen resolving a
weapons code or `228`.
The supplied CORE PDF could not be retrieved and is not relied on here.

Original target inputs remain unchanged. The external reference is counted
separately from the two-letter corpus; no complete solution is claimed.
