from .ocsn_types import OCSNTenant, OCSNUser, OCSNVBucket
from .redis_client import *


class OCSNTenantCtl:
    def __init__(self):
        pass

    def list(self):
        for item in redis_client.list(OCSNTenant.get_prefix()):
            yield OCSNTenant().decode_json(item)

class OCSNUserCtl:
    def __init__(self, tenant_id):
        self.tenant_id = tenant_id

    def list(self):
        u = OCSNUser(self.tenant_id)
        prefix = u.get_prefix()
        for item in redis_client.list(prefix):
            yield u.decode_json(item)

class OCSNVBucketCtl:
    def __init__(self, tenant_id, user_id):
        self.tenant_id = tenant_id
        self.user_id = user_id

    def list(self):
        vb = OCSNVBucket(self.tenant_id, self.user_id)
        prefix = vb.get_prefix()
        for item in redis_client.list(prefix):
            yield vb.decode_json(item)

