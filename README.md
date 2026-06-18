# small_SDR

A collection of Software Defined Radio experiments and signal processing projects built with GNU Radio. Projects range from FM broadcast reception to RF signal analysis, with hardware spanning consumer-grade dongles to professional research radios.

---

## Hardware

| Device | Type | Notes |
|---|---|---|
| RTL-SDR v3 | Receive only | 500 kHz – 1.75 GHz, 8-bit ADC, USB 2.0 |
| Vert900 | Antenna | Vertical dipole, 824–960 MHz / 1710–1990 MHz |

## Software

- **GNU Radio** — signal processing flowgraph environment
- **Python** — custom block development and automation
- **gr-osmosdr** — RTL-SDR hardware driver interface

---

## Projects

| Project | Hardware | Description |
|---|---|---|
| [FM Receiver](./decode-fm.grc/) | RTL-SDR v3 | WBFM broadcast receiver with audio output and spectrum display |
| [RF Spectrum Analyzer](./spectral-display.grc/) | RTL-SDR v3 | Wideband spectrum analyzer with waterfall display|

---

## Background

These projects are built around learning practical RF signal processing — tuning, filtering, decimation, demodulation, and resampling. The hardware combination of an RTL-SDR for quick experiments.

New projects are added as they are completed. Large standalone projects get their own dedicated repository.

---

## Author

Alex Malakar — Electrical Engineering, Oklahoma State University  
Areas of interest: RF systems, FPGA-based signal processing, SDR, defense and aerospace applications
