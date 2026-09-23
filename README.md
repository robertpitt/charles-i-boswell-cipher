# Charles I–Boswell cipher (1643)

A reproducible **partial decipherment** of two letters labelled Charles I to
Boswell and Nicholas to Boswell, dated 2 November 1643. The main result is a
repeating numerical alphabet that produces readable passages in both letters.
Several word codes, graphical signs, and anomalous passages remain unresolved.

| Material | Files |
| --- | --- |
| Input transcriptions | [Charles](input/charles.txt), [Nicholas](input/nicholas.txt) |
| Exact decoder input, provenance, and source hashes | [input/sources.json](input/sources.json) |
| Partial key, evidence, and separately labelled hypotheses | [partial_key.json](partial_key.json) |
| Complete output of the working partial key | [Charles](output/charles.txt), [Nicholas](output/nicholas.txt) |
| Decoder | [decode_boswell.py](decode_boswell.py) |
| 27 passage checks with exact source offsets | [proof_passages.json](proof_passages.json) |
| External cipher evidence and follow-up research | [FINDINGS.md](FINDINGS.md), [reference data](input/external_evidence.json) |

## The key

For numbers **20 through 115 inclusive**, use this 24-letter row:

```python
row = "ACEGILNPRTWYBDFHKMOQSUXZ"
letter = row[(number - 20) % 24]  # only for 20 <= number <= 115
```

The row takes the odd positions, then the even positions, of
`ABCDEFGHIKLMNOPQRSTUWXYZ` (counting from 1). This alphabet has no separate J or V.
Each letter has four numerical equivalents, 24 apart: `20 = 44 = 68 = 92 = A`,
for example. The rule predicts 96 entries; 80 distinct values occur in the
inputs. It is not extended beyond 115.

The **working** key adds 24 explicitly listed letter assignments, 24 proposed
null values (numbers assumed to contribute no text), and four word, syllable,
or title codes: `588 = OF`, `800 = TO`, `835 = UN`, and `291 = DUKE`.
Each additional assignment has its evidence in the key file; some rely on a
single context. Further guesses are confined to **exploratory** mode.

## What the letters say

Charles's letter concerns the Duke of Courland, family funerals, offers of help,
thanks, and delivery destinations. Nicholas's letter appears to instruct the
recipient to hinder the coming over of an unidentified group. Its cleartext
says that two enclosed royal letters use the recipient's cipher and must be
deciphered and interpreted.

This is a summary of the cleartext and partial readings. The exact supplies,
the unidentified group and its origin, and several phrases remain unresolved.
The repository is a reproducible research result, not a complete plaintext.

## Decoded examples and findings

Spaces between tokens are removed in these examples. Proposed nulls are omitted
only where stated; original U/V usage and spelling are retained.

| Cipher or mixed source text | Literal result | Basis |
| --- | --- | --- |
| `62 89 100` | `OUR` | Main alphabet only |
| `30 70 31 61 110 77 107` | `WEYMOTH` | Main alphabet only |
| `21 41 52 49 and` | `CURLAND` | Main alphabet; `and` is already cleartext |
| `37 94 20 26 118 112` | `MEANES` | Working key, including `118 = E` |
| `123 138 69 94 96 89 118` | `RECEIUE` | Working key; U is preserved |
| `147 150 107 94 123 118 12` | `ISHERE` | Working key; `12` is a proposed null |

In Nicholas's letter, the last example continues directly into `APPREHENDED`,
giving `ISHEREAPPREHENDED` entirely from numerical tokens. Charles's letter
includes `WEYMOTH` and `FALLMOUTH` (the latter includes cleartext `all`). Its
`CURLAND` reading occurs near already-readable funeral references. A Latvian
archives description records Duke Frederick's funeral in February 1643; this
offers historical context, without authenticating the reading.
[Source: The Duke's Court, item 17](https://www.archiv.org.lv/hercogiste/index.php?id=23&lang=en).

Across both cipher-bearing extracts, the working model classifies **451 numerical
and 15 graphical occurrences**:

| Category | Occurrences |
| --- | ---: |
| Main alphabet letters | 274 |
| Additional letter assignments | 52 |
| Proposed nulls | 51 |
| Working word/syllable codes | 24 |
| Date/annotation fields | 2 |
| Unresolved numbers | 48 |
| Unresolved graphical signs | 15 |

These counts measure mapping coverage, **not decipherment accuracy**. Anomalies
such as `PHEN`, `SIGNIAY`, and `DAR&MOUTH` are retained. The group mentioned in
Nicholas's letter, proposed supplies in Charles's letter, and a possible fifth
port are not established by this key. A separate letter printed in 1893, also
dated 2 November 1643, contains a numerical line that the original v1 key reads as
`⟦291⟧ OF CURLAND`. Its printed addressee supports the working `291 = DUKE`
assignment. See [follow-up findings](FINDINGS.md) for the source image, comparison,
and unresolved weapons alternatives. This external reference is counted separately.
`303 = TWO` and `376 = BOTH` are exploratory funeral-passage hypotheses.
See the [remaining questions](FINDINGS.md#remaining-evidence) for the evidence
needed to advance beyond this partial result.

## Reading the output

Uppercase letters mark decoder outputs; interspersed source prose is unchanged.
`⟦n⟧` marks an unresolved number, `⟨∅:n⟩` a proposed null, `{WORD}` a working
code, and `⟦n:guess?⟧` an exploratory hypothesis. In exploratory mode, `376`
displays `⟦376:BOTH?⟧` as an alternative to its working proposed-null reading.
Source annotations and graphical signs remain visible. The embedded date fields
`6_` and `8_` are preserved; unencrypted continuations are included separately
and excluded from cipher counts.

## Reproduce

Python 3.9 or newer; no third-party dependencies. Run from the repository root:

```sh
python3 decode_boswell.py --check
python3 verify_independently.py
python3 -m unittest -v test_decoder.py
```

`--check` verifies source hashes, the readable input copies, all 27 passage
examples, and both complete committed outputs. A missing or stale output makes
it fail. To regenerate after reviewing a key change:

```sh
python3 decode_boswell.py --write-outputs
python3 decode_boswell.py --audit generated
python3 decode_boswell.py --check
```

`--write-outputs` refreshes the two files in `output/`. `--audit` writes all three
reading modes, an audit JSON file, and a token CSV to the ignored `generated/`
directory. Both commands use the same document renderer. Every decoder command
checks the source hashes and readable input copies before proceeding.

To inspect readings or locate a code:

```sh
python3 decode_boswell.py --document Charles --mode core
python3 decode_boswell.py --document Charles --mode exploratory --hide-nulls
python3 concordance.py 303 376 591 854 873 --include-external
```

The default display uses the working key and both documents. `--document`,
`--mode`, and `--hide-nulls` customize display; generation and checks always
cover both documents and preserve the full output notation.

Decoding does not load proposed plaintext. The 27 passage checks deliberately
compare against disclosed proposed readings, covering 147 distinct numerical
positions, with overlaps between examples. The separate verifier checks those
examples and the external numerical address without importing the decoder.
The concordance locates exact numerical tokens without loading a key.
Passing these checks establishes computational reproducibility, not independent
historical confirmation.

## Provenance and limits

Prepared from the supplied `boswell_breakthrough_evidence.zip` evidence package.
The original inputs are preserved unchanged; subsequent key and evidence updates
are documented in [FINDINGS.md](FINDINGS.md). Source: S. Tomokiyo,
[“Charles I–Boswell Cipher (1643)”](https://cryptiana.blogspot.com/2021/09/charles-i-boswell-cipher-1643.html),
Cryptiana Discussion Forum, 17 September 2021. The author describes the
transcriptions as provisional and the recipient's identity as uncertain.

This investigation has not examined the original target manuscripts, a matching
historical key, or an authenticated plaintext of either target letter. Neither a
complete solution nor first-ever priority is claimed.

## License

[MIT](LICENSE). The repository's code, original analysis, and key data are free
to use, modify, and redistribute, including commercially, under that license.
Historical transcriptions are attributed to their source above; no ownership
of the underlying historical letters is claimed.
