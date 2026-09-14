#!/usr/bin/env python3
"""Find exact numerical tokens without loading a key or proposed plaintext."""
from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
NUMBERS = re.compile(r'(?<!\d)\d{1,3}(?!\d)')


def find_occurrences(text: str, codes: set[int], document: str = '') -> list[dict]:
    records = []
    for match in NUMBERS.finditer(text):
        number = int(match.group())
        if number not in codes:
            continue
        start, end = match.span()
        field_start, field_end = start, end
        while field_start and not text[field_start - 1].isspace():
            field_start -= 1
        while field_end < len(text) and not text[field_end].isspace():
            field_end += 1
        records.append({
            'document': document,
            'number': number,
            'source_line': text.count('\n', 0, start) + 1,
            'source_start': start,
            'source_end': end,
            'source_field': text[field_start:field_end],
            'left_context': text[max(0, start - 60):start],
            'right_context': text[end:end + 60],
        })
    return records


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('codes', nargs='+', type=int)
    parser.add_argument('--include-external', action='store_true',
                        help='Also search the separately published Courland reference spans.')
    args = parser.parse_args()
    if any(number < 0 or number > 999 for number in args.codes):
        parser.error('codes must be between 0 and 999')
    codes = set(args.codes)
    sources = json.loads((ROOT / 'input/sources.json').read_text(encoding='utf-8'))
    texts = {name: doc['cipher_bearing_extract']
             for name, doc in sources['documents'].items()}
    if args.include_external:
        external = json.loads((ROOT / 'input/external_evidence.json').read_text(encoding='utf-8'))
        for span in external['ciphertext_spans']:
            texts[f'External {span["id"]}'] = span['ciphertext']
    records = [record for name, text in texts.items()
               for record in find_occurrences(text, codes, name)]
    counts = {}
    for name in texts:
        observed = Counter(record['number'] for record in records if record['document'] == name)
        counts[name] = {str(number): observed[number] for number in sorted(codes)}
    print(json.dumps({'counts': counts, 'occurrences': records}, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
