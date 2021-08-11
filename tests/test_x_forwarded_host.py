from datasette.app import Datasette
import pytest


@pytest.mark.asyncio
@pytest.mark.parametrize("x_forwarded_host", (None, "blah.dev"))
async def test_x_forwarded_host(x_forwarded_host):
    datasette = Datasette(
        [],
        memory=True,
        metadata={
            "databases": {
                "_memory": {"queries": {"host_header": "select :_header_host"}}
            }
        },
    )
    headers = {}
    if x_forwarded_host is not None:
        headers["x-forwarded-host"] = x_forwarded_host
    response = await datasette.client.get(
        "/_memory/host_header.json?_shape=array", headers=headers
    )
    assert response.status_code == 200
    host = response.json()[0][":_header_host"]
    if x_forwarded_host is None:
        assert host == "localhost"
    else:
        assert host == x_forwarded_host
