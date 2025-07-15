import random

from td import ThingDescription
from td import MESSAGE_NUM


def _mock(type=None, min=None, max=None, enum=None, name=None):
    msg = []
    for i in range(0, MESSAGE_NUM):
        msg.append(
            {
                "hail": round(random.uniform(0, 5), 3),
                "snow": round(random.uniform(0, 5), 3),
                "wind": round(random.uniform(0, 5), 3),
            }
        )
    return msg


def td():
    return ThingDescription(
        **{
            "@type": "PhotovoltaicDevice",
            "title": "Photovoltaic Device",
            "id": "urn:uuid:f828f65b-401e-475c-bf97-bd288c4aa145",
            "description": "A PV Panel",
            "properties": {
                "MaxPressureLoad": {
                    "title": "Maximum Pressure",
                    "description": "The maximum mechanical pressure that the panel may endure",
                    "observable": True,
                    "type": "object",
                    "propterties": {
                        "hail": {"type": "number", "minimum": 0},
                        "snow": {"type": "number", "minimum": 0},
                        "wind": {"type": "number", "minimum": 0},
                    },
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "roof/pv_panel/max_pressure_load",
                            "mqv:retain": True,
                            "op": ["observeproperty", "readproperty"],
                            "mock": _mock,
                        }
                    ],
                },
                "NominalPower": {
                    "title": "Power",
                    "description": "Nominal Power of the panel",
                    "observable": True,
                    "type": "number",
                    "minimum": 0,
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "roof/pv_panel/nominal_power",
                            "mqv:retain": True,
                            "op": ["observeproperty", "readproperty"],
                        }
                    ],
                },
                "MaximumSystemVoltage": {
                    "title": "Maximum System Voltage",
                    "description": "Maximum System Voltage for which the module is rated",
                    "observable": True,
                    "type": "number",
                    "minimum": 0,
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "roof/pv_panel/max_system_voltage",
                            "mqv:retain": True,
                            "op": ["observeproperty", "readproperty"],
                        }
                    ],
                },
            },
        }
    )
