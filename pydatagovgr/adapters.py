from requests.adapters import HTTPAdapter


class TimeoutHTTPAdapter(HTTPAdapter):
    """A custom Transport Adapter with default timeouts.
    Ensures that a timeout policy is always in place, which is recommended.
    Inspired by: https://github.com/psf/requests/issues/3070#issuecomment-205070203
    """

    DEFAULT_TIMEOUT = 10

    def __init__(self, *args, **kwargs):

        self.timeout = self.DEFAULT_TIMEOUT
        if "timeout" in kwargs:
            self.timeout = kwargs["timeout"]
            del kwargs["timeout"]

        super().__init__(*args, **kwargs)

    def send(self, request, **kwargs):

        timeout = kwargs.get("timeout")
        if timeout is None:
            kwargs["timeout"] = self.timeout

        return super().send(request, **kwargs)
