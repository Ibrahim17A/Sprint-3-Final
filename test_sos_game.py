import unittest
from unittest.mock import MagicMock
from UserInterface import UserInterface

class TestCheckGameEnd(unittest.TestCase):
    # CHATGPT GENERATED
    def test_check_game_end_simple_win(self):
        """Test that the game ends correctly when an SOS sequence is created in Simple Game mode."""
        ui = UserInterface(board_size=3, game_mode="Simple Game")
        
        # Set up the board for a winning condition in the Simple Game
        ui.board = [['S', '', ''], 
                    ['O', '', ''], 
                    ['S', '', '']]
        
        # Mock the button objects
        buttons = [[MagicMock() for _ in range(3)] for _ in range(3)]
        
        # Set the current player and letter to create the winning sequence
        ui.current_player = 'blue'
        ui.check_game_end(0, 0, 'S', buttons)

        # Assert that the game ended with a win
        self.assertTrue(ui.simple_game_ended, "The game should end when an SOS sequence is created.")
        buttons[0][0].config.assert_any_call(bg="blue", fg="black")  # Winning sequence coloring
    # CHATGPT GENERATED
    def test_check_game_end_general_mode_scores(self):
        """Test that the score is updated correctly when an SOS sequence is created in General Game mode."""
        ui = UserInterface(board_size=3, game_mode="General Game")
        
        # Set up the board for a scoring condition in the General Game
        ui.board = [['S', '', ''], 
                    ['O', '', ''], 
                    ['S', '', '']]
        
        # Mock the button objects
        buttons = [[MagicMock() for _ in range(3)] for _ in range(3)]
        
        # Set the current player and make the move that completes an SOS sequence
        ui.current_player = 'blue'
        ui.check_game_end(0, 0, 'S', buttons)
        
        # Assert that the blue player's score increased
        self.assertEqual(ui.blue_player_win_count, 1, "The blue player's score should increment by 1 after completing an SOS.")

    # personally created
    def test_check_game_end_general_mode_scores_fail(self):
        """Test that the score is updated correctly when an SOS sequence is created in General Game mode."""
        ui = UserInterface(board_size=3, game_mode="General Game")
        # Mock the button objects
        buttons = [[MagicMock() for _ in range(3)] for _ in range(3)]
        # Set the current player and make the move that completes an SOS sequence
        ui.current_player = 'blue'
        ui.check_game_end(0, 0, 'S', buttons)
        # Assert that the blue player's score increased
        self.assertNotEqual(ui.blue_player_win_count, 2, "If blue scores one point, his score should not be two.")

    # personally created
    def test_simple_game_draw(self):
        ui = UserInterface(board_size=3, game_mode="Simple Game")
        # Mock the button objects
        buttons = [[MagicMock() for _ in range(3)] for _ in range(3)]
        # Set the current player and letter to create the winning sequence
        ui.current_player = 'blue'
        ui.turn_count = 9
        ui.check_game_end(0, 0, 'S', buttons)
        # Assert that the game ended with a win
        self.assertEqual(ui.turn_count , ui.tile_count, "This game should end in a draw")

    # personally created
    def test_general_game_mode(self):
        ui = UserInterface(board_size=3, game_mode="General Game")
        # Mock the button objects
        buttons = [[MagicMock() for _ in range(3)] for _ in range(3)]
        # Set the current player and letter to create the winning sequence
        ui.current_player = 'blue'
        ui.blue_player_win_count = 5
        ui.red_player_win_count = 0
        ui.turn_count = ui.tile_count
        ui.check_game_end(0, 0, 'S', buttons)
        # Assert that the game ended with a win
        self.assertTrue(ui.blue_player_win_count > ui.red_player_win_count, "Blue should win this game")
    # personally created
    def test_draw_general_game_mode(self):
        ui = UserInterface(board_size=3, game_mode="General Game")
        # Mock the button objects
        buttons = [[MagicMock() for _ in range(3)] for _ in range(3)]
        # Set the current player and letter to create the winning sequence
        ui.current_player = 'blue'
        ui.blue_player_win_count = 0
        ui.red_player_win_count = 0
        ui.turn_count = ui.tile_count
        ui.check_game_end(0, 0, 'S', buttons)
        # Assert that the game ended with a win
        self.assertTrue(ui.blue_player_win_count == ui.red_player_win_count, "This game should end in a draw")


# Running the tests
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestCheckGameEnd))

