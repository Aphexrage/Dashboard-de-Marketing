import sys
from streamlit.web import cli as stcli

sys.argv = ["streamlit", "run", "Visão cliente.py"]
sys.exit(stcli.main())  