from typing import Any, Dict

import vertica_python as v

DEFAULT_PORT = 5433

user = "power"
passw = ",1234"


def vconn_info() -> Dict[str, Any]:
    return dict(
        host="127.0.0.1",
        port=DEFAULT_PORT,
        user=user,
        password=passw,
        session_label="Will start using python with vertica",
        autocommit=False,
        connection_load_balance=True,
        backup_server_node=["127.0.0.1", "127.0.0.1", "127.0.0.1"],
        connection_timeout=300,
        use_prepared_statements=True,
    )
