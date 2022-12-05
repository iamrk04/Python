import pytest
from tennis import score_tennis


# wihtout parameterized test
# def test_0_0_love_all():
#     assert score_tennis(0, 0) == "Love-All"

# def test_1_1_fifteen_all():
#     assert score_tennis(1, 1) == "Fifteen-All"

# def test_2_2_thirty_all():
#     assert score_tennis(2, 2) == "Thirty-All"


# with parametrized test
@pytest.mark.parametrize("player1_score, player2_score, expected_score",
                        [
                            (0, 0, "Love-All"),
                            (1, 1, "Fifteen-All"),
                            (2, 2, "Thirty-All")
                        ])
def test_score_tennis(player1_score, player2_score, expected_score):
    assert score_tennis(player1_score, player2_score) == expected_score