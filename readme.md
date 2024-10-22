# Uniflow

## Setup

On Windows
```bash
.\venv\Scripts\activate
```

On Linux/Unix
```bash
source ./venv/bin/activate
```

## Build the lib

```bash
python setup.py bdist_wheel
```

## How to use

```bash
pip install \\unimedsc.net\ud976\AIRFLOW\NUCLEO-DADOS\uniflow\dist\uniflow-<version>-py3-none-any.whl
```

Exemple:

```bash
pip install \\unimedsc.net\ud976\AIRFLOW\NUCLEO-DADOS\uniflow\dist\uniflow-0.0.1-py3-none-any.whl
```

```python
import uniflow
from uniflow import hello_world
```