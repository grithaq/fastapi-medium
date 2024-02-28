class NewError(Exception):
    status: str
    msg: str

    def __init__(self, status: str, msg: str) -> None:
        self.status = status
        self.msg = msg

    def __repr__(self) -> str:
        return f"status: {self.status} , message: {self.msg}"