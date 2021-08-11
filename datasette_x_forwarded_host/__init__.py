from datasette import hookimpl
from functools import wraps


@hookimpl
def asgi_wrapper(datasette):
    def wrap_with_x_forwarded_host(app):
        @wraps(app)
        async def rewrite_host_header(scope, receive, send):
            x_forwarded_host = dict(scope.get("headers") or []).get(b"x-forwarded-host")
            if x_forwarded_host:
                new_headers = []
                for key, value in scope["headers"]:
                    if key == b"host":
                        value = x_forwarded_host
                    new_headers.append((key, value))
                scope = dict(scope, headers=new_headers)
            await app(scope, receive, send)

        return rewrite_host_header

    return wrap_with_x_forwarded_host
