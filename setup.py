from setuptools import setup

dependencies = [
    "multidict==6.0.2",  # Avoid 5.2.0 due to Avast
    "blspy==1.0.15",  # Signature library
    "chiavdf==1.0.3",  # timelord and vdf verification
    "chiabip158==1.1",  # bip158-style wallet filters
    "chiapos==1.0.10",  # proof of space
    "clvm==0.9.7",
    "clvm_rs==0.1.15",
    "clvm_tools==0.4.5",
    "aiohttp==3.7.4",  # HTTP server for full node rpc
    "aiosqlite==0.17.0",  # asyncio wrapper for sqlite, to store blocks
    "bitstring==3.1.9",  # Binary data management library
    "colorama==0.4.4",  # Colorizes terminal output
    "colorlog==6.7.0",  # Adds color to logs
    "concurrent-log-handler==0.9.20",  # Concurrently log and rotate logs
    "cryptography==38.0.1",  # Python cryptography library for TLS - keyring conflict
    "fasteners==0.16.3",  # For interprocess file locking
    "keyring==23.0.1",  # Store keys in MacOS Keychain, Windows Credential Locker
    "keyrings.cryptfile==1.3.8",  # Secure storage for keys on Linux (Will be replaced)
    #  "keyrings.cryptfile==1.3.8",  # Secure storage for keys on Linux (Will be replaced)
    #  See https://github.com/frispete/keyrings.cryptfile/issues/15
    "PyYAML==5.4.1",  # Used for config file format
    "setproctitle==1.2.2",  # Gives the sesucoin processes readable names
    "sortedcontainers==2.4.0",  # For maintaining sorted mempools
    "websockets==10.3",  # For use in wallet RPC and electron UI
    "click==7.1.2",  # For the CLI
    "dnspythonchia==2.2.0",  # Query DNS seeds
    "watchdog==2.1.9",  # Filesystem event watching - watches keyring.yaml
    "nest-asyncio==1.5.5",
]

upnp_dependencies = [
    "miniupnpc==2.2.2",  # Allows users to open ports on their router
]

dev_dependencies = [
    "pytest",
    "pytest-asyncio",
    "flake8",
    "mypy",
    "black",
    "aiohttp_cors",  # For blackd
    "ipython",  # For asyncio debugging
    "types-setuptools",
]

kwargs = dict(
    name="sesucoin-blockchain",
    author="Mariano Sorgente",
    author_email="mariano@sesu.ddns.net",
    description="sesucoin blockchain full node, farmer, timelord, and wallet.",
    url="https://sesu.ddns.net/",
    license="Apache License",
    python_requires=">=3.7, <4",
    keywords="sesucoin blockchain node",
    install_requires=dependencies,
    setup_requires=["setuptools_scm"],
    extras_require=dict(
        uvloop=["uvloop"],
        dev=dev_dependencies,
        upnp=upnp_dependencies,
    ),
    packages=[
        "build_scripts",
        "sesucoin",
        "sesucoin.cmds",
        "sesucoin.clvm",
        "sesucoin.consensus",
        "sesucoin.daemon",
        "sesucoin.full_node",
        "sesucoin.timelord",
        "sesucoin.farmer",
        "sesucoin.harvester",
        "sesucoin.introducer",
        "sesucoin.plotters",
        "sesucoin.plotting",
        "sesucoin.pools",
        "sesucoin.protocols",
        "sesucoin.rpc",
        "sesucoin.server",
        "sesucoin.simulator",
        "sesucoin.types.blockchain_format",
        "sesucoin.types",
        "sesucoin.util",
        "sesucoin.wallet",
        "sesucoin.wallet.puzzles",
        "sesucoin.wallet.rl_wallet",
        "sesucoin.wallet.cc_wallet",
        "sesucoin.wallet.did_wallet",
        "sesucoin.wallet.settings",
        "sesucoin.wallet.trading",
        "sesucoin.wallet.util",
        "sesucoin.ssl",
        "mozilla-ca",
    ],
    entry_points={
        "console_scripts": [
            "sesucoin = sesucoin.cmds.sesucoin:main",
            "sesucoin_wallet = sesucoin.server.start_wallet:main",
            "sesucoin_full_node = sesucoin.server.start_full_node:main",
            "sesucoin_harvester = sesucoin.server.start_harvester:main",
            "sesucoin_farmer = sesucoin.server.start_farmer:main",
            "sesucoin_introducer = sesucoin.server.start_introducer:main",
            "sesucoin_timelord = sesucoin.server.start_timelord:main",
            "sesucoin_timelord_launcher = sesucoin.timelord.timelord_launcher:main",
            "sesucoin_full_node_simulator = sesucoin.simulator.start_simulator:main",
        ]
    },
    package_data={
        "sesucoin": ["pyinstaller.spec"],
        "": ["*.clvm", "*.clvm.hex", "*.clib", "*.clinc", "*.clsp", "py.typed"],
        "sesucoin.util": ["initial-*.yaml", "english.txt"],
        "sesucoin.ssl": ["sesucoin_ca.crt", "sesucoin_ca.key", "dst_root_ca.pem"],
        "mozilla-ca": ["cacert.pem"],
    },
    use_scm_version={"fallback_version": "unknown-no-.git-directory"},
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    zip_safe=False,
)


if __name__ == "__main__":
    setup(**kwargs)  # type: ignore
