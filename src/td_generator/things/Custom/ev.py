from td import ThingDescription

def td():
    return ThingDescription(
        **{
            "@type": "ElectricVehicle",
            "title": "Electric Vehilce",
            "id": "urn:uuid:609e0187-2c32-47d5-ab77-2c831aab3bc5",
            "description": "An electric vehicle",
            "properties": {
                "chargeStatus": {
                    "title": "Charger Status Code",
                    "description": "Charge status compliant to SAE_J1772",
                    "observable": True,
                    "type": "string",
                    "enum": ["A", "B", "C", "D", "E", "F"],
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "garage/ev/charge/status",
                            "mqv:retain": True,
                            "op": ["observeproperty", "readproperty"],
                        }
                    ],
                },
                "SoC": {
                    "title": "State of Charge",
                    "description": "State of Charge of the EV in percent",
                    "observable": True,
                    "type": "number",
                    "minimum": 0,
                    "maximum": 100,
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "garage/ev/soc",
                            "mqv:retain": True,
                            "op": ["observeproperty", "readproperty"],
                        }
                    ],
                },
                "charged": {
                    "title": "Charged",
                    "description": "The amount of energy that has been charged",
                    "observable": True,
                    "type": "number",
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "garage/ev/charged",
                            "mqv:retain": True,
                            "op": ["observeproperty", "readproperty"],
                        }
                    ],
                },
                "capacity": {
                    "title": "Capacity",
                    "description": "Capacity of the EV battery",
                    "observable": True,
                    "type": "number",
                    "minimum": 5,
                    "maximum": 75,
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "garage/ev/capacity",
                            "mqv:retain": True,
                            "op": ["observeproperty", "readproperty"],
                        }
                    ],
                },
                "range": {
                    "title": "Range of the EV",
                    "description": "Range in km that is left",
                    "observable": True,
                    "type": "number",
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "garage/ev/range",
                            "mqv:retain": True,
                            "op": ["observeproperty", "readproperty"],
                        }
                    ],
                },
                "odometer": {
                    "title": "Odometer",
                    "description": "Number of km that the EV has been driven",
                    "observable": True,
                    "type": "number",
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "garage/ev/odometer",
                            "mqv:retain": True,
                            "op": ["observeproperty", "readproperty"],
                        }
                    ],
                },
                "power": {
                    "title": "Power",
                    "description": "Current power draw of charger",
                    "observable": True,
                    "type": "number",
                    "minimum": -3600,
                    "maximum": 3600,
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "garage/ev/charger/power",
                            "mqv:retain": True,
                            "op": ["observeproperty", "readproperty"],
                        }
                    ],
                },
            },
            "events": {
                "charging": {
                    "title": "EV Charging",
                    "description": "Charging event EV",
                    "data": {"type": "string", "enum": ["START", "STOP"]},
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "garage/ev/charging",
                            "mqv:retain": False,
                            "op": ["subscribeevent", "unsubscribeevent"],
                        }
                    ],
                }
            },
            "actions": {
                "setChargeLimit": {
                    "title": "Charging Limit",
                    "description": "Set the charging limit of EV",
                    "input": {
                        "observable": True,
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 100,
                    },
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "garage/ev/charging/limit",
                            "mqv:retain": False,
                            "op": ["invokeaction"],
                        }
                    ],
                },
            },
        }
    )
