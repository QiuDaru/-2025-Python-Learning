
from pydantic_ai.models.gemini import GeminiModel
from dotenv import load_dotenv
from pydantic_ai import Agent
import tools
print("開始程式")
load_dotenv()

model= GeminiModel("gemini-2.5-flash")
agent = Agent(model,
              system_prompt="你是一隻說中文的奇怪貓咪 ",
              tools=[tools.play_rps,tools.find_stock,tools.open_web,tools.guess_number]
              )

def main():
    history:list[any] = []
    while True:
        user_input: str =input()
        resp=agent.run_sync(user_input,message_history=history)
        history = list(resp.all_messages())
        print(resp.output)

main()
