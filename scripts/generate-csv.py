from carga.models import Agent
import csv

def run():
    agents = Agent.objects.all()

    with open('names.csv', 'w', newline='') as csvfile:

        fieldnames = ['parent_id', 'parent_name', 'parent_total_children', 'child_id', 'child_name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for agent in agents:
            if agent.parent_entity is not None:
                parents = Agent.objects.all().filter(agent_identifier=int(agent.parent_entity))
                if len(parents) > 0:
                    parent = parents.first()
                    writer.writerow({'parent_id': parent.agent_identifier, 'parent_name': parent.name, 'parent_total_children': parent.children_number, 'child_id': agent.agent_identifier, 'child_name': agent.name})
                    #print("Agent: {}-{} / Parent: {}-{}".format(agent.agent_identifier, agent.name, parent.agent_identifier, parent.name))
