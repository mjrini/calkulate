# Calkulate: seawater total alkalinity from titration data
# Copyright (C) 2019-2020  Matthew P. Humphreys  (GNU GPLv3)
"""Convert between various properties."""

import numpy as np
from . import constants, solve

F = constants.faraday
R = constants.ideal_gas


def dilution_factor(analyte_mass, mixture_mass):
    """Calculate the factor for dilution of the analyte by the titrant."""
    return analyte_mass / mixture_mass


def emf_to_h(emf, emf0, temperature):
    """Convert EMF to [H+]."""
    # DAA03 Eq. (13) with typo corrected (i.e. EMF and EMF0 switched)
    temperature_K = temperature + constants.absolute_zero
    return np.exp((emf - emf0) * F / (R * temperature_K))


def emf_to_pH(emf, emf0, temperature):
    """Convert EMF to pH."""
    return -np.log10(emf_to_h(emf, emf0, temperature))


def h_to_emf(h, emf0, temperature):
    """Convert [H+] to EMF."""
    temperature_K = temperature + constants.absolute_zero
    return emf0 + np.log(h) * R * temperature_K / F


def f_to_dEmf0(f, temperature):
    temperature_K = temperature + constants.absolute_zero
    return np.log(f) * R * temperature_K / F


def measurement_type_to_solver(measurement_type):
    m2s = {
        "EMF": solve.complete_emf,
        "pH": solve.complete_pH,
    }
    return m2s[measurement_type]
