# py-time-series

Python implementations of time series analysis examples from **Shumway & Stoffer** — *Time Series Analysis and Its Applications*.

> Repo: https://github.com/pfei/py-time-series

## Contents

- `src/` — standalone Python scripts, one per book figure
- `notebooks/` — Jupyter notebooks with step-by-step walkthroughs
- `data/raw/` — source datasets (J&J earnings, global temperature anomalies)

## Figures implemented

| Script | Figure | Topic |
|---|---|---|
| `shumway_stoffer_fig1.1_p3.py` | 1.1 p.3 | Johnson & Johnson quarterly earnings |
| `shumway_stoffer_fig1.2_p3.py` | 1.2 p.3 | Global surface temperature anomalies |
| `shumway_stoffer_fig1.9_p11.py` | 1.9 p.11 | Gaussian white noise & 3-point moving average |
| `shumway_stoffer_fig1.10_p13.py` | 1.10 p.13 | Simulated AR(2) process |
| `shumway_stoffer_fig1.11_p14.py` | 1.11 p.14 | Random walk with and without drift |

## Setup

```sh
git clone https://github.com/pfei/py-time-series
cd py-time-series
pip install -r requirements.txt
```

## Reference

Robert H. Shumway & David S. Stoffer — *Time Series Analysis and Its Applications: With R Examples*

## License

MIT — see [`LICENSE`](./LICENSE).
