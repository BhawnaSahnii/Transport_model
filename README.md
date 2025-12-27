## Band structure model

The transport model assumes a single isotropic parabolic band:

E(k) = ħ²k² / (2m*)

This dispersion is explicitly plotted in `bandstructure.py`
to demonstrate consistency between the assumed band structure,
velocity expression, and density of states used in transport
calculations.

The code outline:
Transport_model
|
|__Constant_relaxation_time
  |_one-band_model
  |_two-band_model
|__Scattering_mechanism_model
  |_one-band_model
  |_two-band_model
  
