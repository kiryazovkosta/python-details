from typing import Optional

from project.formula_teams.mercedes_team import MercedesTeam
from project.formula_teams.red_bull_team import RedBullTeam

class F1SeasonApp:
    VALID_TEAMS = ["Red Bull", "Mercedes"]

    def __init__(self):
        self.red_bull_team: Optional[RedBullTeam] = None
        self.mercedes_team: Optional[MercedesTeam] = None

    def register_team_for_season(self, team_name: str, budget: int) -> str:
        if team_name == self.VALID_TEAMS[0]:
            self.red_bull_team = RedBullTeam(budget)
        elif team_name == self.VALID_TEAMS[1]:
            self.mercedes_team = MercedesTeam(budget)
        else:
            raise ValueError("Invalid team name!")

        return f"{team_name} has joined the new F1 season."

    def new_race_results(self, race_name: str, red_bull_pos: int, mercedes_pos: int):
        if self.red_bull_team is None or self.mercedes_team is None:
            raise Exception("Not all teams have registered for the season.")

        return (f"Red Bull: {self.red_bull_team.calculate_revenue_after_race(red_bull_pos)}. "
                f"Mercedes: {self.mercedes_team.calculate_revenue_after_race(mercedes_pos)}. "
                f"{self.VALID_TEAMS[0] if red_bull_pos < mercedes_pos else self.VALID_TEAMS[1]} is ahead at the {race_name} race.")