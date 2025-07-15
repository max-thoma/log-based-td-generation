import random
import sys
from enum import Enum
from random import sample
from typing import Optional, List, Any, Callable, Dict

from pydantic import (
    BaseModel,
    Field,
    RootModel,
)
from pydantic.json_schema import SkipJsonSchema

MESSAGE_NUM = 5

# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger(__name__)


def eq_logger(t1, t2):
    # s = ""
    # if t1 == t2:
    #     for val1, val2 in zip(t1, t2):
    #         if val1 != val2:
    #             s = f"{s} | {val1} != {val2}"
    #         # else:
    #         #     s = f"{s} | {val1} == {val2}"
    #     logger.debug(s)
    pass


class AttributeType(str, Enum):
    string = "string"
    boolean = "boolean"
    integer = "integer"
    object = "object"
    null = "null"
    number = "number"

    # def __eq__(self, other):
    #     if self.value in ["integer", "number"]:
    #         return other.value in ["integer", "number"]
    #     else:
    #
    #         return other.value == self.value
    #
    # def __hash__(self):
    #     return hash(str(self))


def default_mock(type=AttributeType.null, min=None, max=None, enum=None, name=None):
    if min is None:
        min = 0
    if max is None:
        max = 250
    if type is AttributeType.null:
        return [""] * MESSAGE_NUM
    elif type == "string":
        if enum is not None:
            return enum
    elif type == "integer":
        return sample(range(min, max), MESSAGE_NUM)
    elif type == "number":
        msg = []
        for i in range(0, MESSAGE_NUM):
            msg.append(round(random.uniform(min, max), 3))
        return msg
    elif type == "boolean":
        return ["true", "false"] * int(MESSAGE_NUM / 2)

    raise NotImplementedError(f"The default mock does not work for {name}: {type}")


class Forms(BaseModel):
    href: str = "broker.emqx.io:1883"
    contentType: Optional[str] = None
    topic: str = Field(
        alias="mqv:topic", description="The MQTT topic of the affordance"
    )
    retain: bool = Field(
        alias="mqv:retain",
        default=False,
        description="Indicates if the topic is retained or not",
    )
    op: List[str] = Field(default_factory=list, description="")
    mock: SkipJsonSchema[Optional[Callable]] = Field(exclude=True, default=default_mock)

    def __eq__(self, other):
        t1 = (self.topic, self.retain)
        t2 = (other.topic, other.retain)
        eq_logger(t1, t2)
        return t1 == t2

    def __str__(self):
        return f"topic='{self.topic}' retain='{self.retain}'"


class BaseProperty(BaseModel):
    title: Optional[str] = Field(default="", description="The title of the property")
    description: Optional[str] = Field(
        default="", description="The description of the property"
    )
    observable: Optional[bool] = None
    type: AttributeType = AttributeType.null
    minimum: Optional[int] = None
    maximum: Optional[int] = None
    enum: Optional[List[str]] | Optional[List[int]] | Optional[List[float]] = Field(
        default=None,
        description="A list of string or number values that the property may have.",
    )
    properties: dict[str, "BaseProperty"] = Field(
        default_factory=dict,
        description="If the property is of type 'object', 'properties' further describes how the 'object' "
        "is structured",
    )

    def __eq__(self, other):
        if other is None:
            # logger.debug("other is None")
            return False

        try:
            s1 = set(self.enum)
        except:
            s1 = set()
        t1 = (
            self.type,
            s1,
            self.properties,
        )

        try:
            s2 = set(other.enum)
        except:
            s2 = set()
        t2 = (
            other.type,
            s2,
            other.properties,
        )
        eq_logger(t1, t2)
        return t1 == t2

    def __str__(self):
        return f"type='{self.type}' enum='{self.enum}' properties='{self.properties}'"


class Property(BaseProperty, BaseModel):
    forms: List[Forms] = Field(default_factory=list)

    def __eq__(self, other):

        if other is None:
            # logger.debug("other is None")
            return False
        try:
            s1 = set(self.enum)
        except:
            s1 = set()
        t1 = (
            self.type,
            s1,
            self.forms,
            self.properties,
        )
        try:
            s2 = set(other.enum)
        except:
            s2 = set()
        t2 = (
            other.type,
            s2,
            other.forms,
            other.properties,
        )
        eq_logger(t1, t2)

        return t1 == t2

    def to_property(self) -> "Property":
        """
        This is the smallest common denominator when comparing affordances
        :return:
        """
        return self

    def __str__(self):
        return f"type='{self.type}' enum='{self.enum}' forms='{self.forms}' properties='{self.properties}'"


class Action(BaseModel):
    title: Optional[str] = Field(
        default="",
        description="The title of the action. An action is an interactive affordance",
    )
    description: Optional[str] = Field(
        default="",
        description="Describes the action",
    )
    input: Optional[BaseProperty] = BaseProperty()
    output: Optional[BaseProperty] = BaseProperty()
    forms: List[Forms]

    def __eq__(self, other):
        if other is None:
            # logger.debug("other is None")
            return False

        t1 = (self.input, self.output, self.forms)
        t2 = (
            other.input,
            other.output,
            other.forms,
        )

        eq_logger(t1, t2)
        return t1 == t2

    def to_property(self) -> Property:
        """
        This is smallest common denominator when comparing affordances
        :return:
        """
        return Property(
            title=self.title + " " + str(self.input.title),
            description=self.description + " " + self.input.description,
            observable=self.input.observable,
            type=self.input.type,
            minimum=self.input.minimum,
            maximum=self.input.maximum,
            enum=self.input.enum,
            forms=self.forms,
            properties=self.input.properties,
        )

    def __str__(self):
        return f"{self.input}"


class Event(BaseModel):
    title: Optional[str] = Field(default="", description="The title of the event")
    description: Optional[str] = Field(default="", description="Describes the event")
    data: BaseProperty = Field(
        default=BaseProperty(), description="The data produced by the event"
    )
    forms: List[Forms]

    def __eq__(self, other):
        t1 = (self.data, self.forms)
        t2 = (other.data, other.forms)

        eq_logger(t1, t2)
        return t1 == t2

    def to_property(self) -> Property:
        """
        This is the smallest common denominator when comparing affordances
        :return:
        """
        return Property(
            title=self.title + " " + str(self.data.title),
            description=self.description + " " + self.data.description,
            observable=self.data.observable,
            type=self.data.type,
            minimum=self.data.minimum,
            maximum=self.data.maximum,
            enum=self.data.enum,
            forms=self.forms,
            properties=self.data.properties,
        )


class ThingDescription(BaseModel):
    context: List[str | Dict[str, str]] = Field(
        alias="@context",
        default=["https://www.w3.org/2022/wot/td/v1.1"],
    )
    type: str = Field(
        alias="@type",
        description="Is the type of the Thing that the Thing Description models",
    )
    title: str = Field(description="A short title that describes the Thing")
    id: str = Field(description="A URN")
    securityDefinitions: Optional[dict[str, Any]] = Field(
        default={"nosec_sc": {"scheme": "nosec"}}
    )
    security: Optional[List[str]] | Optional[str] = Field(default=["nosec_sc"])
    description: str = Field(description="A short description of the Thing")
    properties: dict[str, Property] = Field(
        default_factory=dict,
        description="All affordances of the Thing that can be described as property",
    )
    events: dict[str, Event] = Field(
        default_factory=dict,
        description="All affordances of the Thing that can be described as event",
    )
    actions: dict[str, Action] = Field(
        default_factory=dict,
        description="All affordances of the Thing that can be described as action/command",
    )

    def __eq__(self, other):
        return (self.actions, self.events, self.properties) == (
            other.actions,
            other.events,
            other.properties,
        )

    def to_dict(self) -> dict:
        affordances = []
        affordances.extend(
            [(y.forms[0].topic, (x, y)) for x, y in self.properties.items()]
        )
        affordances.extend([(y.forms[0].topic, (x, y)) for x, y in self.events.items()])
        affordances.extend(
            [(y.forms[0].topic, (x, y)) for x, y in self.actions.items()]
        )
        try:
            assert len(affordances) == len(dict(affordances))
        except AssertionError:
            print("\033[93mWarining: topics are not unique!!!\033[0m")
            for t, _ in affordances:
                print(t)
                # exit(1)
        return dict(affordances)

    def items(self):
        return self.to_dict().items()


class AffordanceType(str, Enum):
    property = "property"
    event = "event"
    action = "action"

    # def __eq__(self, other):
    #     if self.value in ["property", "event"]:
    #         return str(other) in ["property", "event"]
    #     else:
    #         return str(other) == "action"
    #
    # def __hash__(self):
    #     return hash(str(self))


def match_affordance_type(affordance):
    if isinstance(affordance, Property):
        return AffordanceType.property
    if isinstance(affordance, Event):
        return AffordanceType.event
    if isinstance(affordance, Action):
        return AffordanceType.action


class AffordanceComparison(BaseModel):
    same_affordance_type: bool = False
    same_data_type: bool = False
    same_enum: bool = False
    same_properties: bool = False
    weak_equal: bool = False
    strong_equal: bool = False
    src_affordance_type: AffordanceType
    src_attribute_type: AttributeType
    dest_affordance_type: AffordanceType = None
    dest_attribute_type: AttributeType = None


def compare_affordance(
    src: Property | Event | Action, dest: Property | Event | Action | None
) -> AffordanceComparison:
    src_cmp = src.to_property()

    if dest is None:
        # All default values are 'FalseÄ
        return AffordanceComparison(
            src_affordance_type=match_affordance_type(src),
            src_attribute_type=src_cmp.type,
        )

    dest_cmp = dest.to_property()
    same_affordance_type = type(src) == type(dest)
    same_data_type = src_cmp.type == dest_cmp.type
    same_properties = src_cmp.properties == dest_cmp.properties

    src_cmp_enum = set(src_cmp.enum) if src_cmp.enum is not None else set()
    dest_cmp_enum = set(dest_cmp.enum) if dest_cmp.enum is not None else set()
    same_enum = src_cmp_enum == dest_cmp_enum

    weak_equal = same_data_type & same_enum & same_properties
    strong_equal = weak_equal & same_affordance_type

    return AffordanceComparison(
        same_affordance_type=same_affordance_type,
        same_data_type=same_data_type,
        same_enum=same_enum,
        same_properties=same_properties,
        weak_equal=weak_equal,
        strong_equal=strong_equal,
        src_affordance_type=match_affordance_type(src),
        src_attribute_type=src_cmp.type,
        dest_affordance_type=match_affordance_type(dest),
        dest_attribute_type=dest_cmp.type,
    )


def explain_comparison(comp: AffordanceComparison):
    s = ""
    if comp.strong_equal:
        return "Everything is correct"
    if not comp.same_affordance_type:
        s += f"Wrong affordance type {comp.src_affordance_type} =/= {comp.dest_affordance_type}\n"
    if not comp.same_data_type:
        s += f"Wrong data type: {comp.src_attribute_type} =/= {comp.dest_attribute_type}\n"
    if not comp.same_enum:
        s += "Enum values mismatch\n"
    if not comp.same_properties:
        s += "Properties mismatch\n"
    return s
