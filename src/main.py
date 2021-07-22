import src.Rendezvous.RendezvousNode_pb2 as RN_pb2
import src.Rendezvous.RendezvousNode_pb2_grpc as RN_pb2_grpc

from src.RequestHandler.LoadBalancer import LoadBalancer 
import src.Rendezvous.type_pb2 as type_pb2
import grpc

from collections import defaultdict

lb = LoadBalancer()


# ---------------- show the values in the nodes ---------------------
channel = grpc.insecure_channel('localhost:50251')
node_stub0 = RN_pb2_grpc.RendezvousNodeStub(channel)
channel = grpc.insecure_channel('localhost:50252')
node_stub1 = RN_pb2_grpc.RendezvousNodeStub(channel)
channel = grpc.insecure_channel('localhost:50253')
node_stub2 = RN_pb2_grpc.RendezvousNodeStub(channel)
requestEmpty = RN_pb2.NodeEmpty()
objects_on_node = defaultdict(list)

def show_response(stub=0):
    objects_on_node = defaultdict(list)
    if stub == 0:
        responses = node_stub0.get_objects(requestEmpty)
    elif stub == 1:
        responses = node_stub1.get_objects(requestEmpty)
    elif stub == 2:
        responses = node_stub2.get_objects(requestEmpty)

    for response in responses:
        objects_on_node[response.key].append(response.value)

    print(f"Items on Node {stub}")
    print(objects_on_node)

def show_all_responses():
    show_response(0)
    show_response(1)
    show_response(2)
    print()


# adds a router to the list
# router needs to run already in the docker container
lb.add_router("router0","172.17.0.3","50151")

# adds a node
# node needs to run already in the docker container
print("Add node0. Number of nodes=1") 
lb.add_node("node0","172.17.0.4","50251")

print("Add Nico, Sam and Server. Number of nodes=1") 
lb.request(type=type_pb2.ADD,key="Nico",value="57")
lb.request(type=type_pb2.ADD,key="Sam",value="12")
lb.request(type=type_pb2.ADD,key="bob1",value="42")
show_all_responses()

print("Add node1. Number of nodes=2") 
lb.add_node("node1","172.17.0.5","50252")
show_all_responses()

print("Add node2. Number of nodes=3") 
lb.add_node("node2","172.17.0.6","50253")
show_all_responses()

print("remove node1. Number of nodes=2") 
lb.remove_node("node1","172.17.0.5","50252")
show_all_responses()

print("delete bob1. Number of nodes=2") 
lb.request(type=type_pb2.DELETE,key="bob1",value="42")
show_all_responses()




