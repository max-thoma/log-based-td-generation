import unittest
from unittest import TestCase

from td_generator.td import (
    Property,
    Event,
    Action,
    compare_affordance,
    explain_comparison,
    AttributeType,
    BaseProperty,
    Forms,
)


class TestTDModel(TestCase):
    def test_property_equality(self):
        prop1 = Property(title="Property 1", type=AttributeType.string)
        prop2 = Property(title="Property 2", type=AttributeType.string)
        self.assertEqual(prop1, prop2)

    def test_property_unequality_topic(self):
        prop1 = Property(
            title="Property 1",
            type=AttributeType.string,
            forms=[Forms(**{"mqv:topic": "/test1"})],
        )
        prop2 = Property(
            title="Property 2",
            type=AttributeType.string,
            forms=[Forms(**{"mqv:topic": "/test2"})],
        )
        self.assertNotEqual(prop1, prop2)

    def test_property_unequality_datatype(self):
        prop1 = Property(
            title="Property 1",
            type=AttributeType.string,
            forms=[Forms(**{"mqv:topic": "/test"})],
        )
        prop2 = Property(
            title="Property 2",
            type=AttributeType.integer,
            forms=[Forms(**{"mqv:topic": "/test"})],
        )
        self.assertNotEqual(prop1, prop2)

    def test_event_equality(self):
        event1 = Event(title="Event 1", forms=[Forms(**{"mqv:topic": "/test"})])
        event2 = Event(title="Event 2", forms=[Forms(**{"mqv:topic": "/test"})])
        self.assertEqual(event1, event2)

    def test_action_equality(self):
        action1 = Action(title="Action 1", forms=[Forms(**{"mqv:topic": "/test"})])
        action2 = Action(title="Action 2", forms=[Forms(**{"mqv:topic": "/test"})])
        self.assertEqual(action1, action2)

    def test_compare_affordance_same_type(self):
        src_prop = Property(type=AttributeType.string)
        dest_prop = Property(type=AttributeType.string)
        comparison = compare_affordance(src_prop, dest_prop)
        self.assertTrue(comparison.same_data_type)
        self.assertTrue(comparison.strong_equal)

    def test_compare_affordance_different_types(self):
        src_event = Event(forms=[Forms(**{"mqv:topic": "/test"})])
        dest_action = Action(forms=[Forms(**{"mqv:topic": "/test"})])
        comparison = compare_affordance(src_event, dest_action)
        self.assertFalse(comparison.same_affordance_type)
        self.assertFalse(comparison.strong_equal)

    def test_explain_comparison_strong_equal(self):
        prop1 = Property(type=AttributeType.string)
        prop2 = Property(type=AttributeType.string)
        comparison = compare_affordance(prop1, prop2)
        explanation = explain_comparison(comparison)
        self.assertEqual(explanation, "Everything is correct")

    def test_explain_comparison_weak_equal(self):
        src_prop = Property(
            type=AttributeType.integer,
            enum=[1, 2],
            forms=[Forms(**{"mqv:topic": "/test"})],
        )
        dest_event = Event(
            data=BaseProperty(type=AttributeType.integer, enum=[1, 2]),
            forms=[Forms(**{"mqv:topic": "/test"})],
        )
        comparison = compare_affordance(src_prop, dest_event)
        explanation = explain_comparison(comparison)
        self.assertIn("Wrong affordance type", explanation)

    def test_property_with_enum(self):
        prop = Property(type=AttributeType.string, enum=["option1", "option2"])
        comparison = compare_affordance(prop, None)
        self.assertFalse(comparison.same_enum)

    def test_to_property_equal(self):
        prop = Property(
            type=AttributeType.string,
            enum=["option1", "option2"],
            forms=[Forms(**{"mqv:topic": "/test"})],
        )
        event = Event(
            title="Event",
            data=BaseProperty(type=AttributeType.string, enum=["option1", "option2"]),
            forms=[Forms(**{"mqv:topic": "/test"})],
        )
        action = Action(
            title="Action",
            forms=[Forms(**{"mqv:topic": "/test"})],
            input=BaseProperty(type=AttributeType.string, enum=["option1", "option2"]),
        )
        self.assertEqual(prop.to_property(), event.to_property())
        self.assertEqual(prop.to_property(), action.to_property())
        self.assertEqual(event.to_property(), action.to_property())

    def test_to_property_unequal(self):
        prop = Property(
            type=AttributeType.string,
            enum=["option A", "option B"],
            forms=[Forms(**{"mqv:topic": "/test"})],
        )
        event = Event(
            title="Event",
            data=BaseProperty(type=AttributeType.string, enum=["option1", "option2"]),
            forms=[Forms(**{"mqv:topic": "/test"})],
        )
        action = Action(
            title="Action",
            forms=[Forms(**{"mqv:topic": "/test"})],
            input=BaseProperty(type=AttributeType.string, enum=["option 1"]),
        )
        self.assertNotEqual(prop.to_property(), event.to_property())
        self.assertNotEqual(prop.to_property(), action.to_property())
        self.assertNotEqual(event.to_property(), action.to_property())


if __name__ == "__main__":
    unittest.main()
