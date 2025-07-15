# Introduction

This repository holds the prototypical implementation of the proposed methodology for the paper “Utilizing Large Language Models for Log-Based Automated Thing Description Generation” submitted to the SEMANTICS 2025.

# Basic Usage

It is recommended to us [poetry](https://python-poetry.org) and the `pyproject.toml` file to install the dependencies of this project.

```bash
cd src/
poetry install
```

The main implementation can be found in `classification.py`. To run call:

```bash
poetry run python classification.py -m MODEL_NAME -t TEMPERATURE -i ITERATIONS -r RETRIES [-b BASE_URL] [--think]
```

## Arguments

- `-m` or `--model`: Required. The name of the model to use. Available options:
  
  - gpt-4o
  - cogito:70b
  - And more (see code for full list)

- `-t` or `--temperature`: Required. Float value for temperature setting

- `-i` or `--iterations_per_td`: Required. Integer value for iterations per test data point

- `-r` or `--number_of_retries`: Required. Integer value for the number of retries in case the LLM fails

- `-b` or `--base_url`: Optional. Base URL for the experiment (defaults to None)

- `--think`: Optional. Boolean flag for thinking mode (defaults to False)

## Examples

```bash
# Run experiment with gpt-4o
poetry run python classification.py -m GPT-4o -t 0.7 -i 5 -r 10

# Run experiment with cogito:70b and local ollama instance
poetry run python classification.py -m cogito:70b -t 0.5 -i 5 -r 3 -b http://localhost:11434/v1/
```

# Result Analysis

The script `functional_equivalence.py` generates the report of the functional accuracy metrics, and the script `manual_desriptive_equivalence.py` generates the tables for the descriptive accuracy metrics.

For both scripts, set the path to the output file of the `classification.py.` Per default, it is set to analyze our results. For the `manual_desriptive_equivalence.py` script, you may also have to set the `api_key` if you want to use the text embedding analysis.

Our results used in the paper can be found in the `data` directory.

| Directory                 | Description                                   |
| ------------------------- | --------------------------------------------- |
| data/automatic_evaluation | The cosine-similarity and correlation results |
| data/llm_results          | The raw output of the LLM experiment          |
| data/manual_evaluation    | The manually scored dataset                   |
| data/devices              | A list of all device types                    |
| data/percent_affordances  | The distribution of affordances               |

# Custom Dataset

The `things` module holds all our reference TD.

For General inspiration, we consulted the following sources.

| Project                        | Link                                                                           |
| ------------------------------ | ------------------------------------------------------------------------------ |
| HomeAssistant Integration      | https://www.home-assistant.io/integrations/                                    |
| EVCC documentation             | https://evcc.io                                                                |
| SmartDataModels                | https://smartdatamodels.org                                                    |
| WoT TD Specification           | https://www.w3.org/TR/wot-thing-description11/                                 |
| WoT MQTT Binding Specification | https://w3c.github.io/wot-binding-templates/bindings/protocols/mqtt/index.html |
| Eclipse ThingWeb               | https://thingweb.io                                                            |
| Wikipedia SAE J1772 Article    | https://en.wikipedia.org/wiki/SAE_J1772                                        |
| WebThings                      | https://webthings.io                                                           |
| Tasmota                        | https://github.com/arendst/Tasmota                                             |

See the table below to see what was the primary source of inspiration for each TD.

| Thing Description        | Main source of inspiration                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Alarm Control Panel      | https://www.home-assistant.io/integrations/alarm_control_panel.mqtt/                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Alarm Siren              | https://www.home-assistant.io/integrations/siren.mqtt/                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Binary Window Contact    | https://www.home-assistant.io/integrations/binary_sensor.mqtt/                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Button                   | https://www.home-assistant.io/integrations/button.mqtt/                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Ceiling Fan              | https://www.home-assistant.io/integrations/fan.mqtt/                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Door Lock                | https://www.home-assistant.io/integrations/lock.mqtt/                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Doorbell                 | N/A                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Electric Vehicle         | https://docs.evcc.io/docs/devices/vehicles                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Electric Vehicle Charger | https://docs.evcc.io/docs/devices/chargers                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Humidifier               | https://www.home-assistant.io/integrations/humidifier.mqtt/                                                                                                                                                                                                                                                                                                                                                                                                                           |
| HVAC Unit                | https://www.home-assistant.io/integrations/climate.mqtt/                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Illuminance Sensor       | https://w3c.github.io/wot-binding-templates/bindings/protocols/mqtt/index.html#conformance,  <br/>https://www.w3.org/TR/wot-thing-description11/#example-69                                                                                                                                                                                                                                                                                                                           |
| Lawn Mower               | https://www.home-assistant.io/integrations/lawn_mower.mqtt/                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Lightbulb (RGB)          | https://www.home-assistant.io/integrations/light.mqtt/, <br/>https://www.w3.org/TR/wot-thing-description11/                                                                                                                                                                                                                                                                                                                                                                           |
| Lightbulb (Single Color) | https://www.home-assistant.io/integrations/light.mqtt/, <br/>https://www.w3.org/TR/wot-thing-description11/                                                                                                                                                                                                                                                                                                                                                                           |
| Location Tracker (GPS)   | https://www.home-assistant.io/integrations/device_tracker.mqtt/                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Photovoltaic Inverter    | https://github.com/smart-data-models/dataModel.GreenEnergy/tree/master/PhotovoltaicMeasurement,  <br/>https://swagger.lab.fiware.org/?url=https://smart-data-models.github.io/dataModel.GreenEnergy/PhotovoltaicDevice/swagger.yaml,  <br/>https://swagger.lab.fiware.org/?url=https://smart-data-models.github.io/dataModel.S4BLDG/SolarDevice/swagger.yaml,  <br/>https://swagger.lab.fiware.org/?url=https://smart-data-models.github.io/dataModel.Energy/SolarEnergy/swagger.yaml |
| Photovoltaic Panel       | https://github.com/smart-data-models/dataModel.GreenEnergy/tree/master/PhotovoltaicMeasurement,  <br/>https://swagger.lab.fiware.org/?url=https://smart-data-models.github.io/dataModel.GreenEnergy/PhotovoltaicDevice/swagger.yaml,  <br/>https://swagger.lab.fiware.org/?url=https://smart-data-models.github.io/dataModel.S4BLDG/SolarDevice/swagger.yaml,  <br/>https://swagger.lab.fiware.org/?url=https://smart-data-models.github.io/dataModel.Energy/SolarEnergy/swagger.yaml |
| Smart Meter              | https://docs.evcc.io/docs/devices/meters                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Switch                   | https://www.home-assistant.io/integrations/switch.mqtt/                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Vacuum Cleaner           | https://www.home-assistant.io/integrations/vacuum.mqtt/                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Window Cover             | https://www.home-assistant.io/integrations/cover.mqtt/                                                                                                                                                                                                                                                                                                                                                                                                                                |

See the table down below to see which licenses these projects use.

| Project                        | License                                                       |
| ------------------------------ | ------------------------------------------------------------- |
| HomeAssistant Integration      | Attribution-NonCommercial-ShareAlike 4.0 International        |
| EVCC documentation             | MIT License                                                   |
| SmartDataModels                | Creative Commons Attribution 4.0 International Public License |
| WoT TD Specification           | Software and Document license - 2023 version                  |
| WoT MQTT Binding Specification | Software and Document license - 2015 version                  |

# W3C WebThings Dataset

[Source](https://github.com/w3c/wot-testing/tree/037c8d686ad8c145dd4fe01c2123ad26eca0e185/data/input_2022/TD/WebThings)

Changes:

- Removed non-devices and demo TD
- Changed the `href` to `mqv:topic`
- Added enum values to some string attributes
- Added missing descriptions
- Removed any reference to being a virtual device
- Deleted double entries (smart plug) etc

License: Unspecified, presumably Software and Document license - 2023 version

# Kinder et. al Dataset

[Source](https://gitlab.kit.edu/lukas.kinder/plannning_with_thing_descriptions_akr3/-/tree/main/WoT-TD?ref_type=heads)

Changes:

- Converted to MQTT topics
- Added some missing descriptions
- Removed Automated Warehouse as not in our domain
- Removed Chiller no forms data
- Naturally extended topics and made them unique
  - i.e., boolean properties with `is_` or `_enabled`, `_full`, `has_`
  - Boolean and non-boolean: extended by affordance name
- Added missing titles
- Removed redDotImage from counter-
- Unified affordance titles (e.g., Smart Display)

License: Lukas Kinder