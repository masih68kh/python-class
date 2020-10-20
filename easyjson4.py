from json import loads


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


class JSONObject(dict):

    """Class for representing a JSON "object"."""

    def __getattr__(self, name):
        return self[name]

    def __getitem__(self, key):
        if key is ...:
            return JSONEllipsisArray(self.values())
        return super().__getitem__(key)

    def __matmul__(self, name):
        return JSONArray(self._matches(name))

    def _matches(self, name):
        if name in self:
            yield self[name]
        for obj in self.values():
            if isinstance(obj, (JSONObject, JSONArray)):
                yield from obj._matches(name)


class JSONArray(list):

    """Class for representing a JSON "array"."""

    def __getitem__(self, index):
        if index is ...:
            return JSONEllipsisArray(self)
        return super().__getitem__(index)

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
        return JSONArray(obj[index] for obj in self)
