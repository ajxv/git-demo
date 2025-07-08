from jose import jwe
import base64
import json

SECRET_KEY = base64.b64decode("SyK1NeTlnbuwklhUW5RhQPgOkJrncr+ao1JgD39vDwM=")
assert len(SECRET_KEY) == 32

token = "eyJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiZGlyIn0..JDV_avaYXRI3OkTt.YZc_XtHqzMf9GMPlyznkS30JepHcKfJtqz0o2VH9f7xbj9mQNpjTce_C06mhAtq4wb31Kyu5ajJEb2pvaAGWpcAq9Cxl7b-2_qV4TM9btsu91p2Kpjcfocr3dAmabONmaHOCYPQS7T4_.QZh1xKRPPts1Fbh2CTJwYw"

decrypted = jwe.decrypt(token, SECRET_KEY)

print(jwe.get_unverified_header(token))
print(json.loads(decrypted.decode()))
