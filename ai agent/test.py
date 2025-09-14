import webbrowser
def open_web(web_name): #瑞克搖網站開啟
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=RDdQw4w9WgXcQ&start_radio=1")
    print("開啟瑞克搖")









from pydantic_ai.models.gemini import GeminiModel
from dotenv import load_dotenv
from pydantic_ai import Agent

print("開始程式")
load_dotenv()
model= GeminiModel("gemini-2.5-flash")
agent = Agent(model,
              system_prompt="你是一隻說中文的暴躁哥吉拉，但不能說髒話 ",
              tools=[open_web]
              )

def main():
    history:list[any] = []
    while True:
        user_input: str =input()
        resp: AgentRunResult[str]=agent.run_sync(user_input,message_history=history)
        history = list(resp.all_messages())
        print(resp.output)

main()
