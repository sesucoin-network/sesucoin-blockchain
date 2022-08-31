import os
from pathlib import Path

DEFAULT_ROOT_PATH = Path(os.path.expanduser(os.getenv("SESUCOIN_ROOT", "~/.sesucoin/mainnet"))).resolve()

DEFAULT_KEYS_ROOT_PATH = Path(os.path.expanduser(os.getenv("SESUCOIN_KEYS_ROOT", "~/.sesucoin_keys"))).resolve()
