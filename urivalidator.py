from uuid import UUID
from urllib.parse import urlparse


class URIhandler:
    _valid_scheme = "visma-identity"
    _valid_actions = ("login", "confirm", "sign")
    _valid_parameters = {"login": {"source": str},
                         "confirm": {"source": str, "paymentnumber": str},
                         "sign": {"source": str, "documentid": UUID}}
    action = ""
    params = {}

    def __init__(self) -> None:
        return

    def __init__(self, url: str) -> None:
        self.changeURI(url)
        return

    @classmethod
    def changeURI(self, inputstr: str):
        parse = urlparse(inputstr)
        if parse.path != "":
            raise ValueError(f"{parse.path} is not a valid URI")
        if parse.scheme != self._valid_scheme:
            raise ValueError(f"{parse.scheme} is not a valid scheme")
        if parse.netloc not in self._valid_actions:
            raise ValueError(f"{parse.netloc} is not a valid action")

        params = {}
        paramlines = parse.query.split("&")
        for paramline in paramlines:
            param, value = paramline.split("=")
            if param not in self._valid_parameters[parse.netloc].keys():
                raise ValueError(f"{param} is not a valid parameter")
            if param == "documentid":
                try:
                    UUID(value)
                except ValueError:
                    raise ValueError(f"{value} is not a valid UUID")
            params[param] = [value]
        try:
            params["source"]
            if parse.netloc == "confirm":
                params["paymentnumber"]
            elif parse.netloc == "sign":
                params["documentid"]
        except KeyError:
            raise ValueError("Missing required parameters")

        self.action = parse.netloc
        self.params = params

    @ classmethod
    def getAction(self) -> str:
        return self.action

    @ classmethod
    def getParams(self) -> tuple:
        return self.params

    @ classmethod
    def getValue(self, key: str) -> str:
        if key in self.params.keys():
            return self.params[key][0]
        raise ValueError(f"No such key as {key}")
