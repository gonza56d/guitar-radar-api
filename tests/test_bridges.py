from tests.base import APITest


class TestBridges(APITest):

    @property
    def domain_prefix(self) -> str:
        return '/components/bridges'
