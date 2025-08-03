"""
i still have no idea what an "AI Agent" is.
"""

"""
call 1: game ideas prompt generation
call 2: technical details
"""

from shared import Game
from litellm import completion

class GameGenAgent:
    def __init__(self, game: Game):
        self.game = game
        self.details = ""
        self.code = ""
        self.language = 'english'
        self.model = "openrouter/moonshotai/kimi-k2:free"
        self.api_token = ""
    
    def step_1_prompt(self, game: Game, loc='english') -> str:
        prompt = f"""think in {loc} language.
    Respond in english.
    You are a game idea generator.
    Think about ideas for the game based on genres, features, and titles.
    Do not overthink, just give a short description of the game.
    Output the answer as a prompt for generating a game for the coding model.\n\n
    Game name: {game.name}\n
    Genres: {', '.join(game.genres)}\n
    Features: {', '.join(game.features)}\n"""

        return prompt

    def step_2_prompt(self, game: Game, step_1_response: str) -> str:
        prompt = f"""You are a game developer.
    The game name is: {game.name}\n
    Genres: {', '.join(game.genres)}\n
    Features: {', '.join(game.features)}\n
    Optimization level: {game.optimization_level}\n
    additional details:
    {step_1_response}\n
    you should make a game with the following details:
    1. you should use three.js for the game engine
    2. you should use javascript for the game code
    3. you should respond in one awnser with the code for the game.
    4. start with <script type="module"> tag and end with </script> tag (!!!!)
    5. do not use any libraries except three.js
    6. give full code without todos or placeholders
    7. only one script tag, no imports or requires by yourself
    8. use modern module syntax, for example: import * as THREE from 'three';
    """
        return prompt
    
    def generate_details(self, loc='english'):
        prompt = self.step_1_prompt(self.game, loc)
        response = completion(
            model=self.model,
            messages = [{ "content": prompt,"role": "user"}],
            temperature=0.7,
            api_key=self.api_token
        )

        self.details = response.choices[0].message.content
    
    def generate_code(self):
        prompt = self.step_2_prompt(self.game, self.details)
        response = completion(
            model=self.model,
            messages = [{ "content": prompt,"role": "user"}],
            api_key=self.api_token
        )

        self.code =  response.choices[0].message.content

    def save(self):
        with open(f"{self.game.folder_to_save}/{self.game.name}.js", "w") as file:
            file.write(self.code)

if __name__ == "__main__":
    game = Game(
        name="My Awesome Game",
        genres=["Action", "Adventure"],
        optimization_level="75%",
        features=["Multiplayer", "Open World"],
        folder_to_save="./games"
    )
    
    agent = GameGenAgent(game)
    agent.api_token = "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"
    agent.generate_details()
    print(agent.details)
    agent.generate_code()
    print(agent.code)