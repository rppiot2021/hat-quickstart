import hat.aio
import hat.event.common
import hat.gui.common


json_schema_id = None
json_schema_repo = None


async def create_subscription():
    return hat.event.common.Subscription([('*', )])


async def create_adapter(conf):
    adapter = Adapter()

    adapter._async_group = hat.aio.Group()

    return Adapter()


class Adapter(hat.gui.common.Adapter):

    @property
    def async_group(self):
        self._async_group

    async def create_session(self, client):
        return Session(client, self._async_group.create_subgroup())


class Session(hat.gui.common.AdapterSession):

    def __init__(self, client, group):
        self._client = client
        self._async_group = group

    @property
    def async_group(self):
        return self._async_group
