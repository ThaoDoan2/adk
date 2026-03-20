from google.adk.agents import Agent
from google.adk.tools import google_search

def get_current_time()-> dict:
    """
    Get the current time in the format of "YYYY-MM-DD HH:MM:SS".
    """
    import datetime
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"current_time": current_time}


root_agent = Agent(
    model='gemini-2.5-flash',
    name='tool_agent',
    description='A helpful assistant for user questions.',
    instruction="""
    You are a helpful assistant that can use the following tools:
    """,
    #tools=[google_search]   
    tools= [get_current_time]
)