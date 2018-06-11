from simple_rest_client.api import API
from product import Product
from cli import cli


def create_api():
    api = API(
        api_root_url='http://127.0.0.1:8000/api/',
        params={},
        headers={},
        timeout=2,
        append_slash=True,
        json_encode_body=True
    )

    api.add_resource(resource_name='product')

    return api

cli(create_api())
