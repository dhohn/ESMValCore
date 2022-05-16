"""Fixes for MPI-ESM1-2-LR model."""
from ..common import (
    ClFixHybridPressureCoord,
    MsftRenameOceanRegionCoord,
)

Cl = ClFixHybridPressureCoord


Cli = ClFixHybridPressureCoord


Clw = ClFixHybridPressureCoord


Msftmz = MsftRenameOceanRegionCoord
