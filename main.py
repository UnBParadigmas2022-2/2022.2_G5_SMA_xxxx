from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from src.ShoalAgent import ShoalAgent
from src.PinkDolphinAgent import PinkDolphinAgent
from src.WaterAgent import WaterAgent
from src.Model import Model
import mesa

def portrayal_method(agent):
    portrayal = {
        "Filled": "true", 
        "Layer": 0, 
        "w": 1, 
        "h": 1,
    }

    if type(agent) is ShoalAgent:
        if not agent.eated:
            portrayal["Shape"] = "assets/cardume.png"

    elif type(agent) is PinkDolphinAgent:
        portrayal["Shape"] = "assets/pink_dolphin.jpg"

    elif type(agent) is WaterAgent:
        if agent.qualidade == 5:
            portrayal["Shape"] = "rect"
            portrayal["Color"] = "blue"
        else:
            portrayal["Shape"] = "rect"
            portrayal["Color"] = "green"

    return portrayal

model_params = {
    "num_agents": mesa.visualization.Slider(
        "População Inicial de cardumes", 10, 10, 30
    ),
}

grid = CanvasGrid(portrayal_method, 15, 15, 600, 600)

server = ModularServer(
    Model, [grid], "Pink Dolphin", model_params
)
server.port = 8001
server.launch()
