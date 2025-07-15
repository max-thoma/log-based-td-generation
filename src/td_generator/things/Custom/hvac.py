from td import ThingDescription

def td():
    return ThingDescription(
        **{
            "@type": "AirConditioner",
            "title": "Air Conditioner",
            "id": "urn:uuid:981e557a-e3a9-4482-bbcb-d76649830bd8",
            "description": "The Air Conditioning (AC) unit in the office room",
            "properties": {
                "state": {
                    "title": "AC Mode",
                    "description": "Mode of the AC unit",
                    "observable": True,
                    "type": "string",
                    "enum": ["UNKNOWN", "COOL", "OFF", "STANDBY", "FAN_ONLY"],
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "upstairs/office/ac/status",
                            "mqv:retain": True,
                            "op": ["observeproperty", "readproperty"],
                        }
                    ],
                },
                "swing": {
                    "title": "Swing state",
                    "description": "The swing of the AC unit can be 'ON' or 'OFF'",
                    "observable": True,
                    "type": "string",
                    "enum": ["ON", "OFF"],
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "upstairs/office/ac/swing",
                            "mqv:retain": False,
                            "op": ["observeproperty"],
                        }
                    ],
                },
                "fanMode": {
                    "title": "Fan Mode",
                    "description": "Fan mode of the AC unit",
                    "observable": True,
                    "type": "string",
                    "enum": ["OFF", "LOW", "MEDIUM", "HIGH"],
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "upstairs/office/ac/fan",
                            "mqv:retain": False,
                            "op": ["observeproperty"],
                        }
                    ],
                },
                "temperature": {
                    "title": "Air temperature",
                    "description": "Current air temperature measured by the AC unit",
                    "observable": True,
                    "type": "integer",
                    "minimum": 0,
                    "maximum": 68,
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "upstairs/office/ac/temp",
                            "mqv:retain": True,
                            "op": ["observeproperty", "readproperty"],
                        }
                    ],
                },
            },
            "events": {
                "setPoint": {
                    "title": "Target temperature reached",
                    "description": "The target temperature has been reached",
                    "data": {"type": "null"},
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "upstairs/office/ac/setpoint/ok",
                            "mqv:retain": False,
                            "op": ["subscribeevent", "unsubscribeevent"],
                        }
                    ],
                },
            },
            "actions": {
                "setTemp": {
                    "title": "Target Temperature",
                    "description": "Set the target temperature of the AC unit",
                    "input": {
                        "observable": True,
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 50,
                    },
                    "output": None,
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "upstairs/office/ac/setpoint/set",
                            "mqv:retain": False,
                            "op": ["invokeaction"],
                        }
                    ],
                },
                "setPower": {
                    "title": "AC Power Mode",
                    "description": "Set the power mode of the AC unit",
                    "input": {
                        "observable": True,
                        "type": "string",
                        "enum": ["eco", "sleep", "full"],
                    },
                    "output": None,
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "contentType": "text/plain",
                            "mqv:topic": "upstairs/office/ac/mode/set",
                            "mqv:retain": False,
                            "op": ["invokeaction"],
                        }
                    ],
                },
                "setFan": {
                    "title": "Fan Mode",
                    "description": "Set the fan mode of the AC unit",
                    "input": {
                        "observable": True,
                        "type": "string",
                        "enum": ["off", "low", "medium", "high"],
                    },
                    "output": None,
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "contentType": "text/plain",
                            "mqv:topic": "upstairs/office/ac/fan/set",
                            "mqv:retain": False,
                            "op": ["invokeaction"],
                        }
                    ],
                },
            },
        }
    )
