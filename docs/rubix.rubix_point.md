<!-- markdownlint-disable -->

<a href="../rubix/rubix_point.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `rubix.rubix_point`






---

<a href="../rubix/rubix_point.py#L5"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `RubixPoint`




<a href="../rubix/rubix_point.py#L6"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(connection: RubixSession, global_uuid: str, master: bool = None)
```








---

<a href="../rubix/rubix_point.py#L75"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_by_name`

```python
get_by_name(network_name: str, device_name: str, point_name: str)
```

get a point value names as in network, device and point names slave/<g_uuid>/ps/api/generic/points/name/<network_name>/<device_name>/<point_name> network_name: string device_name: string point_name: string :return: JSON 

---

<a href="../rubix/rubix_point.py#L15"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_by_uuid`

```python
get_by_uuid(point_uuid: str)
```

get point by its uuid slave/<g_uuid>/ps/api/generic/points_value/uuid/<point_uuid> point_uuid: string :return: JSON 

---

<a href="../rubix/rubix_point.py#L50"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `patch_by_name`

```python
patch_by_name(
    network_name: str,
    device_name: str,
    point_name: str,
    value: float,
    priority: int
)
```

write a point value by its names as in network, device and point names slave/<g_uuid>/ps/api/generic/points/name/<network_name>/<device_name>/<point_name> network_name: string device_name: string point_name: string value: float priority: int between 1 and 16 :return: JSON 

---

<a href="../rubix/rubix_point.py#L29"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `patch_by_uuid`

```python
patch_by_uuid(point_uuid: str, value: float, priority: int)
```

write a point value by its uuid slave/<g_uuid>/ps/api/generic/points_value/uuid/<point_uuid> point_uuid: string value: float priority: int between 1 and 16 :return: JSON 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
