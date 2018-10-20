from unittest import TestCase

from gameplay.services.reducing_cycle import ReducingCycle


class ReducingCycleTest(TestCase):

    def test_when_instantiate_ReducingCycle_without_starting_index_then_first_position_is_active(
            self):
        char_list = ['a', 'b', 'c', 'd']

        reducing_cycle = ReducingCycle(players=char_list)

        self.assertEqual('a', reducing_cycle.active_player)
        self.assertEqual(4, len(reducing_cycle.remaining_players))
        self.assertEqual(0, reducing_cycle.active_position)

    def test_when_instantiate_ReducingCycle_with_starting_index_of_2_then_third_position_is_active(
            self):
        start_index = 2
        char_list = ['a', 'b', 'c', 'd']

        reducing_cycle = ReducingCycle(players=char_list,
                                       start_index=start_index)

        self.assertEqual('c', reducing_cycle.active_player)
        self.assertEqual(4, len(reducing_cycle.remaining_players))
        self.assertEqual(2, reducing_cycle.active_position)

    def test_when_instantiate_ReducingCycle_with_starting_index_larger_then_list_then_throw_exception(
            self):
        start_index = 4
        char_list = ['a', 'b', 'c', 'd']

        with self.assertRaises(Exception) as context:
            ReducingCycle(players=char_list,start_index=start_index)

        expected_error = 'Cannot set start index to 4 when Cycle has 4 players.'
        self.assertEquals(expected_error, str(context.exception))

    def test_when_next_on_new_ReducingCycle_without_starting_index_then_return_second_element(
            self):
        char_list = ['a', 'b', 'c', 'd']

        reducing_cycle = ReducingCycle(players=char_list)
        result = next(reducing_cycle)

        self.assertEqual('b', result)
        self.assertEqual('b', reducing_cycle.active_player)
        self.assertEqual(1, reducing_cycle.active_position)

    def test_when_next_on_new_ReducingCycle_with_starting_index_of_2_then_return_fourth_element(
            self):
        start_index = 2
        char_list = ['a', 'b', 'c', 'd']

        reducing_cycle = ReducingCycle(players=char_list,
                                       start_index=start_index)

        result = next(reducing_cycle)

        self.assertEqual('d', result)
        self.assertEqual('d', reducing_cycle.active_player)
        self.assertEqual(3, reducing_cycle.active_position)

    def test_when_next_at_end_of_cycle_then_return_first_element(self):
        start_index = 3
        char_list = ['a', 'b', 'c', 'd']

        reducing_cycle = ReducingCycle(players=char_list,
                                       start_index=start_index)

        result = next(reducing_cycle)

        self.assertEqual('a', result)
        self.assertEqual('a', reducing_cycle.active_player)
        self.assertEqual(0, reducing_cycle.active_position)

    def test_when_next_on_new_ReducingCycle_with_starting_index_of_2_then_return_fourth_element(
            self):
        start_index = 2
        char_list = ['a', 'b', 'c', 'd']

        reducing_cycle = ReducingCycle(players=char_list,
                                       start_index=start_index)

        result = next(reducing_cycle)

        self.assertEqual('d', result)
        self.assertEqual('d', reducing_cycle.active_player)
        self.assertEqual(3, reducing_cycle.active_position)

    def test_when_remove_active_player_then_remaining_players_do_not_include_active_player(
            self):
        char_list = ['a', 'b', 'c', 'd']

        reducing_cycle = ReducingCycle(players=char_list)

        reducing_cycle.remove_active_player()

        self.assertEqual(3, len(reducing_cycle.remaining_players))
        self.assertNotIn('a', reducing_cycle.remaining_players)

    def test_when_active_player_is_first_and_remove_active_player_then_new_active_player_is_last_player(
            self):
        start_index = 2
        char_list = ['a', 'b', 'c', 'd']

        reducing_cycle = ReducingCycle(players=char_list,
                                       start_index=start_index)

        self.assertEqual('c', reducing_cycle.active_player)
        self.assertEqual(2, reducing_cycle.active_position)

        reducing_cycle.remove_active_player()

        self.assertEqual('b', reducing_cycle.active_player)
        self.assertEqual(1, reducing_cycle.active_position)

    def test_when_active_player_is_first_and_remove_active_player_then_new_active_player_is_last_player(
            self):
        char_list = ['a', 'b', 'c', 'd']

        reducing_cycle = ReducingCycle(players=char_list)

        self.assertEqual('a', reducing_cycle.active_player)
        self.assertEqual(0, reducing_cycle.active_position)

        reducing_cycle.remove_active_player()

        self.assertEqual('d', reducing_cycle.active_player)
        self.assertEqual(2, reducing_cycle.active_position)
