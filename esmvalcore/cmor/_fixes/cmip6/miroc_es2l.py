"""Fixes for MIROC-ES2L model."""
from ..common import (
    ClFixHybridPressureCoord,
    MsftRenameOceanRegionCoord,
)


Cl = ClFixHybridPressureCoord


Cli = ClFixHybridPressureCoord


Clw = ClFixHybridPressureCoord


Msftmz = MsftRenameOceanRegionCoord
