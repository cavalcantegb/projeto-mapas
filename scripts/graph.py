from carga.models import Agent
import networkx as nx
import matplotlib.pyplot as plt
import plotly.offline as py
import plotly.graph_objects as go

def run():
    agents = Agent.objects.all()
    G = nx.Graph()
    for agent in agents:
        G.add_node(agent.agent_identifier)
        if agent.parent_entity is not None:
            G.add_edge(agent.agent_identifier, int(agent.parent_entity))

    pos_ = nx.spring_layout(G)

    layout = go.Layout(
        paper_bgcolor='rgba(0,0,0,0)', # transparent background
        plot_bgcolor='rgba(0,0,0,0)', # transparent 2nd background
        xaxis =  {'showgrid': False, 'zeroline': False}, # no gridlines
        yaxis = {'showgrid': False, 'zeroline': False}, # no gridlines
    )
    # Create figure
    fig = go.Figure(layout = layout)

    # Add all edge traces
    for trace in edge_trace:
        fig.add_trace(trace)

    # Add node trace
    fig.add_trace(node_trace)
    # Remove legend
    fig.update_layout(showlegend = False)
    # Remove tick labels
    fig.update_xaxes(showticklabels = False)
    fig.update_yaxes(showticklabels = False)
    # Show figure
    fig.show()

    # nx.draw(G, with_labels=True, font_weight='bold')
    # plt.figure(figsize=(100, 100))
    # plt.savefig("grafo.png")

    # plt.figure(figsize=(1000, 1000))

    # # pos_random = nx.random_layout(G)
    # # nx.draw_networkx_nodes(G, node_positions, node_size=20, node_color="red")
    # # nx.draw_networkx_edges(G, node_positions, alpha=0.1)
    # # plt.axis('off')
    # # plt.title('Complete Graph of Odd-degree Nodes')
    # # plt.show()
