# python-blynk-api

This is a simple blynk API wrapper.

### Introduction
This library created for simple using [Blynk API](http://docs.blynkapi.apiary.io/#reference/0/pin-actions) and manage your project via python. It's simple one class lib which used `urlib2` for requests.

You can also:
  - Read/write pin value
  - Check hardware network status
  - Check application network status
  - Send push notification
  - Send email
  - Get pin history data
  - Get QR for project cloning
  - Get project info
  - Query API

### Installation
Simple copy `python-blynk-api/Blynk.py` to your main python program dir and import it
```python
from Blynk import *
```

### Using
```python
from Blynk import *
# vars
server = "blynk-cloud.com"
auth_token = "sdjflksjflkdsjfkldsjfkldfkldjflk"

# create object 
room_light = Blynk(server, auth_token, pin = "V3")
# get current status
res = room_light.get_val()
print res
# set pin value to 1
room_light.on()
# set pin value to 0
room_light.off()
```



### Todos

 - Write Tests

License
----

MIT


