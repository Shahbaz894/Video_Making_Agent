from utils.model_loader import ModelLoader
from prompt_library.system_prompt import SYSTEM_PROMPT
from langgraph.graph import StateGraph, MessagesState, END, START
from langgraph.prebuilt import ToolNode, tools_condition

from tools.generate_images_tool import GenerateImagesTool
from tools.generate_video_tool import GenerateVideoTool
from tools.text_to_script_tool import TextToScriptTool
from tools.text_to_speech_tool import TextToSpeechTool
class GraphBuilder():
    def __init__(self):
        pass
    
    def agent_function(self):
        pass

    def build_graph(self):
        pass
    
    def __call__(self):
        pass
