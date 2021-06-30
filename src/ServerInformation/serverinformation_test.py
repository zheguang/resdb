import grpc

import unittest

import src.ServerInformation.ServerInformation_pb2 as SI_pb2
import src.ServerInformation.ServerInformation_pb2_grpc as SI_pb2_grpc

unittest.TestLoader.sortTestMethodsUsing = None

class TestServerInformationMethods(unittest.TestCase):
    
    def __init__(self, *args, **kwargs):
        super(TestServerInformationMethods, self).__init__(*args, **kwargs)
        channel = grpc.insecure_channel('localhost:50050')
        self.stub = SI_pb2_grpc.ServerInformationStub(channel)

    def test1_delete_all(self):
        # Delete all entries from the dicts
        request = SI_pb2.DeleteAllRequest(type=SI_pb2.LOADBALANCER)
        response = self.stub.delete_all_(request)
        self.assertEqual(response.message, "Delete was successfull")
        
        request = SI_pb2.DeleteAllRequest(type=SI_pb2.ROUTER)
        response = self.stub.delete_all_(request)
        self.assertEqual(response.message, "Delete was successfull")
        
        request = SI_pb2.DeleteAllRequest(type=SI_pb2.NODE)
        response = self.stub.delete_all_(request)
        self.assertEqual(response.message, "Delete was successfull")

        # try to delete all from an none existing server type
        request = SI_pb2.DeleteAllRequest(type=-1)
        response = self.stub.delete_all_(request)
        self.assertEqual(response.message, "Delete was not successfull")

    def test2_add(self):
        # Add new servers
        request = SI_pb2.AddRequest(type=SI_pb2.LOADBALANCER, name="LB1", ip_address = "192.168.0.1:55003")
        response = self.stub.add_(request)
        self.assertEqual(response.message, "Add was successfull")

        request = SI_pb2.AddRequest(type=SI_pb2.ROUTER, name="Router1", ip_address = "192.168.0.1:55004")
        response = self.stub.add_(request)
        self.assertEqual(response.message, "Add was successfull")

        request = SI_pb2.AddRequest(type=SI_pb2.NODE, name="Node1", ip_address = "192.168.0.1:55005")
        response = self.stub.add_(request)
        self.assertEqual(response.message, "Add was successfull")

        # Try to add the same servers again
        request = SI_pb2.AddRequest(type=SI_pb2.LOADBALANCER, name="LB1", ip_address = "192.168.0.1:55003")
        response = self.stub.add_(request)
        self.assertEqual(response.message, "Add was not successfull")
        
        request = SI_pb2.AddRequest(type=SI_pb2.ROUTER, name="Router1", ip_address = "192.168.0.1:55004")
        response = self.stub.add_(request)
        self.assertEqual(response.message, "Add was not successfull")
        
        request = SI_pb2.AddRequest(type=SI_pb2.NODE, name="Node1", ip_address = "192.168.0.1:55005")
        response = self.stub.add_(request)
        self.assertEqual(response.message, "Add was not successfull")

        # Try to add on none existing server types
        request = SI_pb2.AddRequest(type=4, name="Node1", ip_address = "192.168.0.1:55005")
        response = self.stub.add_(request)
        self.assertEqual(response.message, "Add was not successfull")

        request = SI_pb2.AddRequest(type=-1, name="Node1", ip_address = "192.168.0.1:55005")
        response = self.stub.add_(request)
        self.assertEqual(response.message, "Add was not successfull")

    def test3_get(self):
        
        # Tries to get the ips from existing names
        request = SI_pb2.GetRequest(type=SI_pb2.LOADBALANCER, name="LB1")
        response = self.stub.get_(request)
        self.assertEqual(response.ip_address, "192.168.0.1:55003")

        request = SI_pb2.GetRequest(type=SI_pb2.ROUTER, name="Router1")
        response = self.stub.get_(request)
        self.assertEqual(response.ip_address, "192.168.0.1:55004")

        request = SI_pb2.GetRequest(type=SI_pb2.NODE, name="Node1")
        response = self.stub.get_(request)
        self.assertEqual(response.ip_address, "192.168.0.1:55005")

        # Tries to get the ips from non existing names
        request = SI_pb2.GetRequest(type=SI_pb2.LOADBALANCER, name="LB2")
        response = self.stub.get_(request)
        self.assertEqual(response.message, "No IP-Address for this Name found")
        
        request = SI_pb2.GetRequest(type=SI_pb2.ROUTER, name="Router2")
        response = self.stub.get_(request)
        self.assertEqual(response.message, "No IP-Address for this Name found")
        
        request = SI_pb2.GetRequest(type=SI_pb2.NODE, name="Node2")
        response = self.stub.get_(request)
        self.assertEqual(response.message, "No IP-Address for this Name found")

    # Tries to get the ips from existing names on wrong servers
        request = SI_pb2.GetRequest(type=4, name="Node1")
        response = self.stub.get_(request)
        self.assertEqual(response.message, "No IP-Address for this Name found")

        request = SI_pb2.GetRequest(type=-1, name="Node1")
        response = self.stub.get_(request)
        self.assertEqual(response.message, "No IP-Address for this Name found")

    def test4_get_random(self):
        # Tries to get the a random server with one dict entry
        request = SI_pb2.GetRandomRequest(type=SI_pb2.LOADBALANCER)
        response = self.stub.get_random_(request)
        self.assertEqual(response.name, "LB1") 
        self.assertEqual(response.ip_address, "192.168.0.1:55003")

        request = SI_pb2.GetRandomRequest(type=SI_pb2.ROUTER)
        response = self.stub.get_random_(request)
        self.assertEqual(response.name, "Router1") 
        self.assertEqual(response.ip_address, "192.168.0.1:55004")

        request = SI_pb2.GetRandomRequest(type=SI_pb2.NODE)
        response = self.stub.get_random_(request)
        self.assertEqual(response.name, "Node1")
        self.assertEqual(response.ip_address, "192.168.0.1:55005")

        # Tries to get the a random server with multiple dict entries
        request = SI_pb2.AddRequest(type=SI_pb2.LOADBALANCER, name="LB2", ip_address="192.168.0.1:55004")
        response = self.stub.add_(request)
        request = SI_pb2.AddRequest(type=SI_pb2.LOADBALANCER, name="LB3", ip_address="192.168.0.1:55005")
        response = self.stub.add_(request)

        request = SI_pb2.GetRandomRequest(type=SI_pb2.LOADBALANCER)
        response = self.stub.get_random_(request)
        ip_addresses = ["192.168.0.1:55003", "192.168.0.1:55004", "192.168.0.1:55005"]
        self.assertIn(response.name, ["LB1", "LB2", "LB3"])
        self.assertIn(response.ip_address, ip_addresses)
        response = self.stub.get_random_(request)
        self.assertIn(response.name, ["LB1", "LB2", "LB3"])
        self.assertIn(response.ip_address, ip_addresses)
        response = self.stub.get_random_(request)
        self.assertIn(response.name, ["LB1", "LB2", "LB3"]) 
        self.assertIn(response.ip_address, ip_addresses)

        # Tries to get the a random server with multiple on wrong type
        request = SI_pb2.GetRandomRequest(type=4)
        response = self.stub.get_random_(request)
        self.assertEqual(response.message, "No IP-Addresses are saved")

        request = SI_pb2.GetRandomRequest(type=-1)
        response = self.stub.get_random_(request)
        self.assertEqual(response.message, "No IP-Addresses are saved")

    def test5_get_all(self):
        # Tries to get the a random server with one dict entry
        request = SI_pb2.GetAllRequest(type=SI_pb2.LOADBALANCER)
        responses = self.stub.get_all_(request)
        for i, response in enumerate(responses):
            if i == 0:
                self.assertEqual(response.ip_address, "192.168.0.1:55003")
                self.assertEqual(response.name, "LB1")
            elif i == 1:
                self.assertEqual(response.ip_address, "192.168.0.1:55004") 
                self.assertEqual(response.name, "LB2")
            elif i == 2:
                self.assertEqual(response.ip_address, "192.168.0.1:55005") 
                self.assertEqual(response.name, "LB3")

    def test6_delete(self):
        
        # trie to delete servers
        request = SI_pb2.DeleteRequest(type=SI_pb2.LOADBALANCER, name="LB1")
        response = self.stub.delete_(request)
        self.assertEqual(response.message, "Delete was successfull")

        request = SI_pb2.DeleteRequest(type=SI_pb2.ROUTER, name="Router1")
        response = self.stub.delete_(request)
        self.assertEqual(response.message, "Delete was successfull")

        request = SI_pb2.DeleteRequest(type=SI_pb2.NODE, name="Node1")
        response = self.stub.delete_(request)
        self.assertEqual(response.message, "Delete was successfull")

        # Try to delete the same servers again
        request = SI_pb2.DeleteRequest(type=SI_pb2.LOADBALANCER, name="LB1")
        response = self.stub.delete_(request)
        self.assertEqual(response.message, "Delete was not successfull")
        
        request = SI_pb2.DeleteRequest(type=SI_pb2.ROUTER, name="Router1")
        response = self.stub.delete_(request)
        self.assertEqual(response.message, "Delete was not successfull")
        
        request = SI_pb2.DeleteRequest(type=SI_pb2.NODE, name="Node1")
        response = self.stub.delete_(request)
        self.assertEqual(response.message, "Delete was not successfull")

        # Try to delete on none existing server types
        request = SI_pb2.DeleteRequest(type=4, name="Node1")
        response = self.stub.delete_(request)
        self.assertEqual(response.message, "Delete was not successfull")

        request = SI_pb2.DeleteRequest(type=-1, name="Node1")
        response = self.stub.delete_(request)
        self.assertEqual(response.message, "Delete was not successfull")

if __name__ == '__main__':
    unittest.main()