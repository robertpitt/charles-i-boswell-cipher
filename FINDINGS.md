# Follow-up findings — 14 September 2026

**An external cipher specimen now supports `291 = DUKE`.** The proposed weapons
list remains unresolved. This update follows leads in a supplied research note;
its reconstructed plaintext was treated as a set of hypotheses.

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

`291 = DUKE` is therefore promoted from exploratory to **working**. The exact
printed sequences, baseline result, source details, and image hash are recorded
in [input/external_evidence.json](input/external_evidence.json). The image was
visually checked; the original manuscript was not. The edition warns that its
transcription may contain errors. This is an external consistency check, found
through the Courland lead, rather than a blind accuracy test or a recovered key.

The new letter says an envoy's credentials and message reached the king through
`212, 364,` and that the king is sending a reply and re-credentials. That is
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

## Reproduce and continue

```sh
python3 -m unittest -v test_decoder.py
python3 verify_independently.py
python3 concordance.py 755 188 539 639 228 291 873 --include-external
python3 decode_boswell.py --audit generated
```

The concordance searches exact numerical tokens and preserves suffixes,
punctuation, source offsets, and context. It loads no key or proposed plaintext.
It searches only the two supplied extracts and, optionally, the two external
reference spans; it is not a search of an entire archival collection.

In the original corpus, `291` occurs twice and `873` six times; each other code
in the command occurs once. Three occurrences of `873` appear with nearby
graphical signs, two are bare, and one has an `r` suffix. Their interpretation
may depend on those signs; counting them together does not establish a single
word value.

This iteration checked the linked historical sources, the 1893 correspondence,
and Cryptiana's unsolved-cipher and Stuart-cipher surveys. It found the external
`291` example above, but no second specimen resolving a weapons code or `228`.
The supplied CORE PDF could not be retrieved and is not relied on here.

The most useful next evidence is a manuscript image or a related key: inspect
the `212`/`213` intermediary references, the graphical forms surrounding `873`,
and the two disputed letters in `FIRXSS`. Original target inputs remain
unchanged. The one adopted code change reduces unresolved numerical occurrences
from 50 to **48**, with all 15 graphical occurrences still unresolved. The
external reference is counted separately; no complete solution is claimed.
