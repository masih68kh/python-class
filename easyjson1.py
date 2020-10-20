from json import loads


class JSONObject:

    """Class for representing a JSON "object"."""

    def __init__(self, obj):
        self.__dict__.update(obj)

    def __getitem__(self, key):
        if key is ...:
            return JSONEllipsisArray(self.values())
        return self.__dict__[key]

    def __iter__(self):
        return iter(self.__dict__)

    def __len__(self):
        return len(self.__dict__)

    def __repr__(self):
        return repr(self.__dict__)

    def __eq__(self, other):
        if isinstance(other, JSONObject):
            return self.__dict__ == other.__dict__
        if isinstance(other, dict):
            return self.__dict__ == other
        return NotImplemented

    def get(self, *args, **kwargs):
        return self.__dict__.get(*args, **kwargs)

    def keys(self):
        return self.__dict__.keys()

    def values(self):
        return self.__dict__.values()

    def items(self):
        return self.__dict__.items()

    def __matmul__(self, name):
        return JSONArray(self._matches(name))

    def _matches(self, name):
        if name in self:
            yield self[name]
        for obj in self.values():
            if isinstance(obj, (JSONObject, JSONArray)):
                yield from obj._matches(name)


class JSONArray:

    """Class for representing a JSON "array"."""

    def __init__(self, data):
        self._data = list(data)

    def __getitem__(self, index):
        if index is ...:
            return JSONEllipsisArray(self)
        else:
            return self._data[index]

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return repr(self._data)

    def __eq__(self, other):
        if isinstance(other, (JSONArray, list)):
            return self._data.__eq__(other)
        return NotImplemented

    def __matmul__(self, name):
        return JSONArray(self._matches(name))

    def _matches(self, name):
        for obj in self:
            if isinstance(obj, (JSONObject, JSONArray)):
                yield from obj._matches(name)


class JSONEllipsisArray(JSONArray):

    """Class for querying attributes on all objects in a given JSON array."""

    def __getattr__(self, name):
        return self[name]

    def __getitem__(self, index):
        return JSONArray(
            obj[index]
            for obj in self
        )


def parse(json):
    return convert(loads(json))


def convert(obj):
    """Convert parsed JSON to JSONObject and JSONArray objecs."""
    if isinstance(obj, dict):
        return JSONObject({
            key: convert(value)
            for key, value in obj.items()
        })
    if isinstance(obj, list):
        return JSONArray(
            convert(value)
            for value in obj
        )
    return obj
