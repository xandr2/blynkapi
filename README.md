# blynkapi

This is a simple blynk API wrapper.

### Introduction
This library created for simple using [Blynk API](http://docs.blynkapi.apiary.io/#reference/0/pin-actions) and manage your project via python. It's simple one class lib which used `urllib2` for requests.

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

Install via pip
```bash
pip install blynkapi
```
after installation import it in your code
```python
from blynkapi import Blynk
```

Or simple copy `blynkapi/Blynk.py` to your main python program dir and import it
```python
from Blynk import *
```

### Using
```python
# if you install it from pip, else use `from Blynk import *`
from blynkapi import Blynk
# vars
auth_token = "sdjflksjflkdsjfkldsjfkldfkldjflk"

# create object 
room_light = Blynk(auth_token, pin = "V3")
# get current status
res = room_light.get_val()
print res
# set pin value to 1
room_light.on()
# set pin value to 0
room_light.off()
```

### Available methods

All methods return values from API or error if it fixed. For detailed description of returning values and scheme read official [Blynk API guide] (http://docs.blynkapi.apiary.io/#reference)

Creating main object
```python
Blynk(token, server, protocol = "http", port = "8080", pin = None, value = None)
```
  - `token` - Your project token
  - `server` - Blynk server for API requests, default "blynk-cloud.com"
  - `protocol` - http or https, default "http"
  - `port` - Your Blynk server API port, default "8080"
  - `pin` - Pin for working with, default "None"
  - `value` - Value for method get_val, default "None"

To turn pin on (set val "1" to pin)
```python
on()
```

To turn pin off (set val "0" to pin)
```python
off()
```

To set your value for pin
```python
set_val(value)
```
  - `value` - Value in format ["x"] or multiple ["x", "y"]. [Details] (http://docs.blynkapi.apiary.io/#reference/0/pin-actions/write-pin-value)

To get data from pin
```python
get_val()
```

Send push notification
```python
push(value)
```
  - `value` - String no more than 255 chars.

Send email
```python
email(to, title, subj)
```
  - `to` - String
  - `title` - String
  - `subj` - String

Check hardware status (connection to server)
```python
hw_status()
```

Check app status (connection to server)
```python
app_status()
```

Get pin history
```python
history()
```

Get QR image
```python
qr()
```

Get project info For details see [docs] (http://docs.blynkapi.apiary.io/#reference/0/get-project/get-project)
```python
get_project()
```

Query API. For details see [docs] (http://docs.blynkapi.apiary.io/#reference/0/query-api/query-api)
```python
query_api(groupBy, aggregation, pin, value)
```
  - `groupBy` - String
  - `aggregation` - String
  - `pin` - String
  - `value` - String



### Todos

 - Write Tests

License
----

MIT


