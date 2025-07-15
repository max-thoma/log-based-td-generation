from td import ThingDescription

def td():
    return ThingDescription(
        **{
            "@type": "SmartLock",
            "title": "Lock Back Door",
            "id": "urn:uuid:c21c77f6-5549-4196-923a-b3ffd78e14e6",
            "description": "The lock at the back door",
            "securityDefinitions": {"nosec_sc": {"scheme": "nosec"}},
            "security": ["nosec_sc"],
            "properties": {
                "state": {
                    "title": "Lock State",
                    "description": "The current state of the lock",
                    "observable": True,
                    "type": "string",
                    "enum": ["unknown", "locked", "unlocked", "jammed"],
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "backdoor/lock/state",
                            "mqv:retain": True,
                            "op": ["observeproperty", "readproperty"],
                        }
                    ],
                },
                "batteryEstimate": {
                    "title": "Battery Estimate",
                    "description": "Estimate when the battery has to be changed in days",
                    "observable": True,
                    "type": "number",
                    "minimum": 3,
                    "maximum": 9999,
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "backdoor/lock/remaining_time",
                            "mqv:retain": True,
                            "op": ["observeproperty", "readproperty"],
                        }
                    ],
                },
            },
            "events": {
                "manualOverwrite": {
                    "title": "Manual Overwrite",
                    "description": "The manual overwrite was activated",
                    "data": {"observable": False, "type": "null"},
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "backdoor/lock/manualoverwrite",
                            "mqv:retain": False,
                            "op": ["subscribeevent", "unsubscribeevent"],
                        }
                    ],
                },
            },
            "actions": {
                "lock": {
                    "title": "Lock",
                    "description": "Lock the backdoor",
                    "input": {
                        "observable": True,
                        "type": "string",
                        "enum": ["LOCK"],
                    },
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "backdoor/lock/lock",
                            "mqv:retain": False,
                            "op": ["invokeaction"],
                        }
                    ],
                },
                "unlock": {
                    "title": "unlock",
                    "description": "Unlock the backdoor via a six-digit code",
                    "input": {
                        "observable": True,
                        "type": "number",
                        "minimum": 100000,
                        "maximum": 999999,
                    },
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "backdoor/lock/unlock",
                            "mqv:retain": False,
                            "op": ["invokeaction"],
                        }
                    ],
                },
            },
        }
    )
