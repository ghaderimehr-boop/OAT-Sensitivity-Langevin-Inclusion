# OAT Sensitivity Analysis for Fractional Langevin Differential Inclusion

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXXX)

## Overview

This repository contains Python codes for the numerical simulation and One-Factor-At-a-Time (OAT) sensitivity analysis of a fractional-order hybrid Langevin system formulated as a differential inclusion. The work accompanies the research article:

> M. Ghaderi, S. Rezapour, "Dynamic analysis of fractional-order and viscous damping effect on differential inclusion modeling of Langevin nonlinear hybrid system", *Mathematics and Computers in Simulation* (2026).

## Features

- Two numerical examples validating the existence theorem (Theorem 3.2 in the paper).
- 3D surface and contour plots of the hybrid functions α(t,ζ), β(t,ζ), γ(t,ζ).
- OAT sensitivity analysis for three key parameters:
  - τ₁ (global memory)
  - τ₂ (local memory)
  - ℓ (viscous damping coefficient)

## Files Description

| File | Description |
|------|-------------|
| `3dsurf.py` | 3D plots for Example 1 (α, β, γ) |
| `3dsurfex2.py` | 3D plots for Example 2 (α, β, γ) |
| `sensivity.py` | OAT sensitivity for Example 1 (τ₁, τ₂, ℓ) |
| `sensivityex2.py` | OAT sensitivity for Example 2 (τ₁, τ₂, ℓ) |

## Requirements

- Python 3.8+
- NumPy
- Matplotlib
- SciPy (only for `sensivityex2.py`)

Install dependencies:
```bash
pip install -r requirements.txt
