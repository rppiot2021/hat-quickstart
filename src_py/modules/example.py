import hat.aio
import hat.event.common


json_schema_id = None
json_schema_repo = None

_source_id = 0


async def create(conf, engine):
    module = Module()

    global source_id
    module._source = hat.event.common.Source(
        type=hat.event.common.SourceType.MODULE,
        name=__name__,
        id=source_id)
    _source_id += 1

    module._subscription = hat.event.common.Subscription([('*', )])
    module._async_group = hat.aio.Group()
    module._engine = engine

    return module


class Module(hat.event.common.Module):

    @property
    def async_group(self):
        return self._async_group

    @property
    def subscription(self):
        return self._subscription

    async def create_session(self):
        return Session()


class Session(hat.event.common.ModuleSession):

    @property
    def async_group(self):
        return self._async_group

    async def process(self, changes):
        return []
