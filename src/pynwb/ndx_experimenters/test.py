from ndx_experimenters import NWBFile

from pynwb import NWBHDF5IO
from datetime import datetime

from numpy.testing import assert_array_equal

session_start_time = datetime.now().astimezone()
nwb = NWBFile('session_description', 'identifier', session_start_time, experimenters=['a', 'b'])

with NWBHDF5IO('test_experimenters.nwb', 'w') as io:
    io.write(nwb)

with NWBHDF5IO('test_experimenters.nwb', 'r') as io:
    nwb2 = io.read()
    assert_array_equal(nwb2.experimenters[:], ['a', 'b'])
