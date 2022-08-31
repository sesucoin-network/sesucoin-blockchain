from typing import Generator, KeysView

SERVICES_FOR_GROUP = {
    "all": "sesucoin_harvester sesucoin_timelord_launcher sesucoin_timelord sesucoin_farmer sesucoin_full_node sesucoin_wallet".split(),
    "node": "sesucoin_full_node".split(),
    "harvester": "sesucoin_harvester".split(),
    "farmer": "sesucoin_harvester sesucoin_farmer sesucoin_full_node sesucoin_wallet".split(),
    "farmer-no-wallet": "sesucoin_harvester sesucoin_farmer sesucoin_full_node".split(),
    "farmer-only": "sesucoin_farmer".split(),
    "timelord": "sesucoin_timelord_launcher sesucoin_timelord sesucoin_full_node".split(),
    "timelord-only": "sesucoin_timelord".split(),
    "timelord-launcher-only": "sesucoin_timelord_launcher".split(),
    "wallet": "sesucoin_wallet sesucoin_full_node".split(),
    "wallet-only": "sesucoin_wallet".split(),
    "introducer": "sesucoin_introducer".split(),
    "simulator": "sesucoin_full_node_simulator".split(),
}


def all_groups() -> KeysView[str]:
    return SERVICES_FOR_GROUP.keys()


def services_for_groups(groups) -> Generator[str, None, None]:
    for group in groups:
        for service in SERVICES_FOR_GROUP[group]:
            yield service


def validate_service(service: str) -> bool:
    return any(service in _ for _ in SERVICES_FOR_GROUP.values())
