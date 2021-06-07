import hat.aio
import hat.gateway.common


json_schema_id = None
json_schema_repo = None


async def create(conf, client, event_type_prefix):
    device = Device()

    device._group = hat.aio.Group()
    device._client = client
    device._event_type_prefix = event_type_prefix

    return device


class Device(hat.gateway.common.Device):

    @property
    def async_group(self):
        return self._async_group
