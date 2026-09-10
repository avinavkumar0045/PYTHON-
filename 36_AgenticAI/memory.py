from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.db.sqlite import SqliteDb
from rich.pretty import pprint
#thre are 2 types of memory long ther ans short term memory
load_dotenv()

db = SqliteDb(db_file="agno.db")
db.clear_memories()

def build_agent():
    return Agent(
        db=db,
        model=Groq(id="qwen/qwen3.6-27b"),
        markdown=True,
        add_history_to_context=True,
        update_memory_on_run=True
    )

agent = build_agent()

user_id = "avinavkumar0045@gmail.com"
agent.print_response("I am Avinav & I am a Data Analyst.", user_id=user_id) # phele kuch bola
agent.print_response("who am I?, Response in 5 sentenses", user_id=user_id) # isne usko memory ko store kiya aur jawab diya

memories = agent.get_user_memories(
    user_id=user_id
)

print("MEMORIES: ") # ye end mein hum memories bhi print kara rhe hai
pprint(memories)