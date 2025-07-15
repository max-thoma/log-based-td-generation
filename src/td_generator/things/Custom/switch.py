from td import ThingDescription

def td():
    return ThingDescription(
        **{
            "@type": "Switch",
            "title": "Switch",
            "id": "urn:uuid:4819ac0e-ffa5-4d26-a83f-3dcd605f9d29",
            "description": "A stateful switch",
            "securityDefinitions": {"nosec_sc": {"scheme": "nosec"}},
            "security": ["nosec_sc"],
            "properties": {
                "state": {
                    "title": "Switch State",
                    "description": "Binary state of the switch",
                    "observable": True,
                    "type": "boolean",
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "home/downstairs/kitchen/switch004",
                            "mqv:retain": True,
                            "op": ["observeproperty", "readproperty"],
                        }
                    ],
                }
            },
        }
    )
