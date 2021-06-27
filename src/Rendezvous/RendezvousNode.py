from src.Node.node_abstract import AbstractNodeClass
from typing import DefaultDict, Union
from collections import defaultdict
import hashlib
import socket

import src.Rendezvous.RendezvousNode_pb2 as RN_pb2
import src.Rendezvous.RendezvousNode_pb2_grpc as RN_pb2_grpc
import src.ServerInformation.ServerInformation_pb2 as SI_pb2
import src.ServerInformation.ServerInformation_pb2_grpc as SI_pb2_grpc

import grpc
from concurrent import futures

# TODO: look how to import from AbstractNodeClass since it is our abstract class. Maybe like this: RendezvousNode(AbstractNodeClass(RN_pb2_grpc.RendezvousNodeServicer))
class RendezvousNode(RN_pb2_grpc.RendezvousNodeServicer):

    def __init__(self, name, ip_address, port, weight):
        self._host_name = name
        self._host_ip = ip_address
        self._http_port = port
        self._node_weight = weight
        self._hashing = hashlib.md5()
        # TODO: Check if ip_address is a adequate seed for the node
        self._node_seed = str(ip_address)+str(name)
        # TODO: Check if a list is a good representation for values
        self._objects_dict = defaultdict(list)

    def hash_value_for_key(self, request, context) -> float:
        """
        GRPC

        returns the hash for a given key. Uses sha256 for creating the hash value. In the
        hash function the seed is appended to key. The hash is then converted to int and then 
        multplied by the node weight
        """
        hash = self._hashing.update((request.key+self._host_ip).encode('utf-8')).hexdigest()
        return RN_pb2.NodeHashValueForReply(float.fromhex(hash) * self._node_weight)

    # TODO: implement as a GRPC function. Since it needs to connect to the other node. Add_object is not a grpc function so use get_request()
    def send_item_to_new_node(self, node):
        for k,v in self._objects_dict.items():
            if node.hash_value_for_key(k) >= self.hash_value_for_key(k):
                node.add_object(k,v)
                # TODO: maybe store hash values of the keys?

    def add_object(self, key, value):
        """
        not GRPC

        adds a new object to the dict
        key = the key from the object
        value = value of the key

        TODO: extend to working with dicts as values
        """
        # using default dicts to ensure the possibility of adding multiple values
        self._objects_dict[key] = self._objects_dict[key].append(value)

    def remove_object(self, key, value=None):
        """
        not GRPC

        removes a object from the dict, 
        if a value is given it just removes the value/s for the key
        
        key = the key from the object
        value = optional parameter, if a specific value/s should be deleted
        """
        if key in self._objects_dict:
            if value:
                self._objects_dict[key] = self._objects_dict[key].remove(value)
            else:
                del self._objects_dict[key]

    def update_object(self, key, value):
        """
        not GRPC

        updates a object in the dict, 
        if a dict, list or tuple is used we append the value/s to the key
        key = the key from the object
        value = value of the key

        TODO: Check if necessary if we keep using lists as values in the defaultdict
        """
        self._objects_dict[key] = self._objects_dict[key].append(value)
    
    def get_object(self, key) -> Union[int,str,list,bool,tuple,dict]:
        """
        not GRPC

        returns the values for a given key
        key = the key from the object
        """
        return self._objects_dict[key]

    # TODO: implement as GRPC
    def get_objects(self) -> dict:
        """
        not GRPC

        returns all objects in node
        """
        return self._objects_dict
    
    # TODO: use enum for request.type in protobuffer 
    def get_request(self, request, context):
        """
        GRPC

        Node gets a request, checks the type of the request and calls the responsible function
        
        type = can be (get, add, remove or update)
        key = the key for the item that should be stored
        value = only necessary for add and update
        """

        if request.type == "add":
            self.add_object(request.key,request.value)
        elif request.type == "remove":
            self.remove_object(request.key,request.value)
        elif request.type == "get":
            self.get_object(request.key)
            # TODO: return value
        elif request.type == "update":
            self.update_object(request.key,request.value)

def serve(name, ip_address, port, weight):
    channel = grpc.insecure_channel('172.17.0.2:50050')
    server_information_stub = SI_pb2_grpc.ServerInformationStub(channel)
    request = SI_pb2.AddRequest(type=SI_pb2.NODE,name=name,ip_address=f'{ip_address}:{port}')
    _ = server_information_stub.add_(request)


    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    RN_pb2_grpc.add_RendezvousNodeServicer_to_server(RendezvousNode(name, ip_address, port, weight), server)
    server.add_insecure_port(f'{ip_address}:{port}')
    server.start()
    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    name = "node1"
    port = 50250
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    weight = 1
    print(f"starting Node '{name}': {ip_address}:{port} with {weight}.")
    serve(name, ip_address, port, weight)
