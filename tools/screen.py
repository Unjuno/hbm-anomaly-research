#!/usr/bin/env python3
"""Offline descriptive screening of nominal HBM specifications. No hardware I/O."""
import argparse
import csv
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIELDS = ('id','name','priority','bus_status','nominal_capacity_gb','effective_bus_bits',
          'peak_bandwidth_gbps','gb_per_1024bit','nominal_bw_per_gb_s_inv',
          'inferred_pin_rate_gbps','reference_density_gb','reference_basis','q','flag','source_ids')

def positive(row, key):
    value = row.get(key, '').strip()
    if not value:
        return None
    number = float(value)
    if not math.isfinite(number) or number <= 0:
        raise ValueError(f"{row.get('id','?')}: {key} must be finite and positive")
    return number

def screen(row):
    cap = positive(row, 'nominal_capacity_gb')
    width = positive(row, 'effective_bus_bits')
    bw = positive(row, 'peak_bandwidth_gbps')
    ref = positive(row, 'reference_density_gb')
    if width is not None and not width.is_integer():
        raise ValueError('effective_bus_bits must be an integer')
    eligible = row.get('bus_status') in {'vendor', 'owner_verified', 'community_report'}
    # A conditional or unknown width must not enter a factual calculation.
    width = width if eligible else None
    ce = cap * 1024 / width if cap is not None and width is not None else None
    r = bw / cap if bw is not None and cap is not None else None
    pin = bw * 8 / width if bw is not None and width is not None else None
    # A reference requires an explicit basis; it is not an inferred physical density.
    q = ce / ref if ce is not None and ref is not None and row.get('reference_basis','').strip() else None
    flag = ('missing_width' if width is None else 'missing_capacity' if ce is None else
            'no_reference' if q is None else 'strong_relative_mismatch' if q <= 0.5 else
            'relative_mismatch' if q < 1 else 'no_relative_mismatch')
    return {**{key: row.get(key,'') for key in FIELDS},
            'effective_bus_bits': width, 'gb_per_1024bit': ce,
            'nominal_bw_per_gb_s_inv': r, 'inferred_pin_rate_gbps': pin,
            'q': q, 'flag': flag}

def read_rows(path):
    with open(path, newline='', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))
    ids = [r['id'] for r in rows]
    if len(ids) != len(set(ids)) or any(not i for i in ids):
        raise ValueError('device IDs must be unique and nonempty')
    return rows

def fmt(v):
    if v is None: return ''
    if isinstance(v, float): return f'{v:.6g}'
    return str(v)

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input', type=Path, default=ROOT/'data/devices.csv')
    p.add_argument('--format', choices=['markdown','csv'], default='markdown')
    args = p.parse_args()
    rows = [screen(row) for row in read_rows(args.input)]
    if args.format == 'csv':
        w = csv.DictWriter(sys.stdout, fieldnames=FIELDS)
        w.writeheader()
        w.writerows({k:fmt(v) for k,v in r.items()} for r in rows)
    else:
        print('| Device | Role / prediction rank | Width evidence | GB/1024 bit | BW/GB (nominal) | Pin rate (Gb/s) | q | Status |')
        print('| --- | --- | --- | ---: | ---: | ---: | ---: | --- |')
        for r in rows:
            values = [r[k] for k in ('name','priority','bus_status','gb_per_1024bit','nominal_bw_per_gb_s_inv','inferred_pin_rate_gbps','q','flag')]
            print('| ' + ' | '.join((fmt(v) or '—').replace('|', r'\|') for v in values) + ' |')
        print('\nNominal labels only; missing widths remain missing. Flags are descriptive, not predictions.')

if __name__ == '__main__':
    main()
