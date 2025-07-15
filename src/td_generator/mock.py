import os

from generate import things_list
from message_log import (
    MessageLog,
    DeviceMessageLog,
    MessageLogList,
    DeviceMessageLogList,
)
from td import ThingDescription

def log_message(topic, payload, retain, subscribed, file):
    l = MessageLog(
        topic=topic, payload=str(payload), retain=retain, subscribed=subscribed
    )
    file.write(f"{l}\n")
    return l


count = 0


def mock_thing(td: ThingDescription):
    global count

    device_log_lst = []

    if not os.path.exists("logs"):
        os.mkdir("logs")

    message_log_file = open(f"logs/Message_log_{count}_{td.type}.txt", "w")
    count += 1
    props = td.properties
    events = td.events
    actions = td.actions
    if props is not None:
        for prop, attr in props.items():
            message_log_lst = []
            messages = attr.forms[0].mock(
                attr.type, attr.minimum, attr.maximum, attr.enum, prop
            )

            for m in messages:
                message_log_lst.append(
                    log_message(
                        attr.forms[0].topic,
                        m,
                        attr.forms[0].retain,
                        False,  # Device is not subscribed to its own property
                        message_log_file,
                    )
                )
            device_log_lst.append(MessageLogList(logs=message_log_lst))

    if events is not None:
        for event, attr in events.items():
            message_log_lst = []
            messages = attr.forms[0].mock(
                attr.data.type,
                attr.data.minimum,
                attr.data.maximum,
                attr.data.enum,
                event,
            )
            for m in messages:
                message_log_lst.append(
                    log_message(
                        attr.forms[0].topic,
                        m,
                        attr.forms[0].retain,
                        False,  # Device is not subscribed to its own events
                        message_log_file,
                    )
                )
            device_log_lst.append(MessageLogList(logs=message_log_lst))

    if actions is not None:
        for action, attr in actions.items():
            message_log_lst = []
            messages = attr.forms[0].mock(
                attr.input.type,
                attr.input.minimum,
                attr.input.maximum,
                attr.input.enum,
                action,
            )
            for m in messages:
                message_log_lst.append(
                    log_message(
                        attr.forms[0].topic,
                        m,
                        attr.forms[0].retain,
                        True,  # Device is subscribed to its own actions
                        message_log_file,
                    )
                )
            device_log_lst.append(MessageLogList(logs=message_log_lst))
    message_log_file.flush()
    message_log_file.close()
    return device_log_lst


def mock_thing_str(td: ThingDescription):
    props = td.properties
    events = td.events
    actions = td.actions

    s = ""

    if props is not None:
        for prop, attr in props.items():
            messages = attr.forms[0].mock(
                attr.type, attr.minimum, attr.maximum, attr.enum, prop
            )

            for m in messages:
                s += f"topic: '{attr.forms[0].topic}'; payload: '{m}'; retain: '{str(attr.forms[0].retain).lower()}'\n"

    if events is not None:
        for event, attr in events.items():
            messages = attr.forms[0].mock(
                attr.data.type,
                attr.data.minimum,
                attr.data.maximum,
                attr.data.enum,
                event,
            )
            for m in messages:
                s += f"topic: '{attr.forms[0].topic}'; payload: '{m}'; retain: '{str(attr.forms[0].retain).lower()}'\n"

    if actions is not None:
        for action, attr in actions.items():
            messages = attr.forms[0].mock(
                attr.input.type,
                attr.input.minimum,
                attr.input.maximum,
                attr.input.enum,
                action,
            )
            for m in messages:
                s += f"topic: '{attr.forms[0].topic}'; payload: '{m}'; retain: '{str(attr.forms[0].retain).lower()}'\n"

    return s


def generate_message_logs() -> DeviceMessageLogList:
    message_log_lst = []
    for thing in things_list:
        device_message_logs = mock_thing(thing.td())
        message_log_lst.append(
            DeviceMessageLog(device=thing.td().title, logs=device_message_logs)
        )
    return DeviceMessageLogList(logs=message_log_lst)


def generate_device_message_log(thing):
    return DeviceMessageLog(device=thing.td().title, logs=mock_thing(thing.td()))


if __name__ == "__main__":
    logs = generate_message_logs()
    print()

    print(logs)
