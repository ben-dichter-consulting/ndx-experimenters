# ndx-experimenters Extension for NWB:N


## python

### Installation
```bash
pip install git+https://github.com/bendichter/ndx-experimenters.git
```

### Usage

```python
from ndx_experimenters import NWBFile
from datetime import datetime

nwb = NWBFile('session_description', 'identifier', datetime.now().astimezone(),
      experimenters=['a', 'b'])
```