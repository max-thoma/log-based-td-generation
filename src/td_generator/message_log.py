from typing import List

from pydantic import BaseModel, RootModel

from td import Forms


class MessageLog(BaseModel):
    topic: str
    payload: str
    retain: bool
    subscribed: bool

    def __str__(self):
        if self.payload == "":
            pl = "null"
        else:
            pl = f"{self.payload}"
        return f"topic: {self.topic}; payload: {pl}; retain: {str(self.retain).lower()}"

    def to_td_form(self, broker_str="mqtt://broker.emqx.io:1883"):
        d = {"href": broker_str, "mqv:topic": self.topic, "mqv:retain": self.retain}
        return Forms(**d)


class MessageLogList(BaseModel):
    logs: List[MessageLog]

    def __str__(self):
        s = ""
        for log in self.logs:
            s += f"{str(log)}\n"
        return s

    def to_enum(self) -> List[str]:
        enum_set = set()
        for log in self.logs:
            enum_set.add(log.payload)
        return list(enum_set)


class DeviceMessageLog(BaseModel):
    device: str
    logs: List[MessageLogList]

    def __str__(self):
        s = ""
        for log in self.logs:
            s += f"{str(log)}"
        return s


class DeviceMessageLogList(BaseModel):
    logs: List[DeviceMessageLog]

    def __str__(self):
        s = ""
        for log in self.logs:
            s += f"{log}"
        return s
