#!/usr/bin/env python3
"""Generate a simple experiment report from CSV/JSON result files.

Expected columns if using CSV: run_id, metric, value, step, split, model, dataset
The script is tolerant: it will summarize whatever columns exist.
"""
import argparse
from pathlib import Path
import json
import pandas as pd
import matplotlib.pyplot as plt


def load_results(path: Path) -> pd.DataFrame:
    files = []
    if path.is_file():
        files = [path]
    elif path.exists():
        files = list(path.rglob('*.csv')) + list(path.rglob('*.json'))
    frames = []
    for f in files:
        try:
            if f.suffix.lower() == '.csv':
                df = pd.read_csv(f)
            elif f.suffix.lower() == '.json':
                data = json.loads(f.read_text())
                if isinstance(data, dict):
                    data = [data]
                df = pd.DataFrame(data)
            else:
                continue
            df['source_file'] = str(f)
            frames.append(df)
        except Exception as e:
            print(f'Could not read {f}: {e}')
    return pd.concat(frames, ignore_index=True) if frames else pd.DataFrame()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--input', default='results')
    ap.add_argument('--output', default='experiment_report.md')
    ap.add_argument('--figdir', default='figures')
    args = ap.parse_args()

    input_path = Path(args.input)
    figdir = Path(args.figdir)
    figdir.mkdir(exist_ok=True)
    df = load_results(input_path)

    lines = ['# Experiment Report', '']
    lines.append(f'Input path: `{input_path}`')
    lines.append('')

    if df.empty:
        lines.append('No CSV/JSON experiment results found yet.')
    else:
        lines.append(f'Rows loaded: **{len(df)}**')
        lines.append('')
        lines.append('## Columns')
        lines.append(', '.join(f'`{c}`' for c in df.columns))
        lines.append('')
        lines.append('## Summary')
        numeric = df.select_dtypes(include='number')
        if not numeric.empty:
            lines.append(numeric.describe().to_markdown())
            lines.append('')
            for col in numeric.columns[:6]:
                plt.figure()
                df[col].dropna().plot(kind='hist', bins=30, title=col)
                plt.xlabel(col)
                plt.ylabel('Count')
                out = figdir / f'{col}_hist.png'
                plt.tight_layout()
                plt.savefig(out)
                plt.close()
                lines.append(f'![{col} histogram]({out})')
        if {'metric', 'value'}.issubset(df.columns):
            lines.append('')
            lines.append('## Best values by metric')
            best = df.sort_values('value', ascending=False).groupby('metric').head(5)
            lines.append(best.to_markdown(index=False))

    Path(args.output).write_text('
'.join(lines) + '
')


if __name__ == '__main__':
    main()
