from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub

pnconfig = PNConfiguration()
pnconfig.subscribe_key = 'sub-c-2ebd9ad8-6cdb-11e8-902b-b2b3cb3accda'
pnconfig.publish_key = 'pub-c-84d6b42f-9d4d-48c1-b5a7-c313289e1792'
pnconfig.secret_key = 'sec-c-NTU2MzMzNjEtOGE3Zi00NmUxLWE4YzgtMTg3OTkxNjllNzFh'

pubnub = PubNub(pnconfig)

envelope = pubnub.grant().read(True).write(True).channels(['sagar', 'sapkota']).auth_keys('sagar_auth_key').ttl(0).sync()
