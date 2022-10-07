class Base:

    def __repr__(self) -> str:
        return f'<{type(self).__name__} object: "{self}">'
