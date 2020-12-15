import unittest

from simple_scripts import bobross


class BobRossTests(unittest.TestCase):

    def test_it_should_generate_a_given_number_of_colors(self):
        colors = bobross.generate_colors(4)
        self.assertEqual(4, len(colors))

    def test_it_should_generate_seven_colors_by_default(self):
        colors = bobross.generate_colors()
        self.assertEqual(7, len(colors))

    def test_it_should_ensure_at_least_one_color_is_generated(self):
        colors = bobross.generate_colors(0)
        self.assertEqual(1, len(colors))

    def test_it_should_get_a_given_number_of_tools(self):
        tools = bobross.get_tools(4)
        self.assertEqual(4, len(tools))

    def test_it_should_get_three_tools_by_default(self):
        tools = bobross.get_tools()
        self.assertEqual(3, len(tools))

    def test_it_should_ensure_at_least_one_tool_is_gotten(self):
        tools = bobross.get_tools(0)
        self.assertEqual(1, len(tools))
