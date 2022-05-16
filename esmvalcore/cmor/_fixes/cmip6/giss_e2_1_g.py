"""Fixes for GISS-E2-1-G model."""
from ..common import (
    ClFixHybridPressureCoord,
    MsftRenameOceanRegionCoord,
)



Cl = ClFixHybridPressureCoord


Cli = ClFixHybridPressureCoord


Clw = ClFixHybridPressureCoord


Msftmz = MsftRenameOceanRegionCoord
