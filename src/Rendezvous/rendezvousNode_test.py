import grpc
import time

import src.Rendezvous.RendezvousNode_pb2 as RN_pb2
import src.Rendezvous.RendezvousNode_pb2_grpc as RN_pb2_grpc
import time
import unittest

class TestRendezvousNodeMethods(unittest.TestCase):
    def __init__(self, *args, **kwargs):
            super(TestRendezvousNodeMethods, self).__init__(*args, **kwargs)
            channel = grpc.insecure_channel('localhost:50251')
            self.stub = RN_pb2_grpc.RendezvousNodeStub(channel)

    def test1_hash(self):
        # Get Hash values for diffrent keys
        request = RN_pb2.NodeHashValueForRequest(key="Sam")
        response = self.stub.hash_value_for_key(request)
        self.assertEqual(response.hashValue, 3.1905721063649946e+38)

        request = RN_pb2.NodeHashValueForRequest(key="Nico")
        response = self.stub.hash_value_for_key(request)
        self.assertEqual(response.hashValue, 3.9998298548157744e+37)
        
        request = RN_pb2.NodeHashValueForRequest(key="Serwar")
        response = self.stub.hash_value_for_key(request)
        self.assertEqual(response.hashValue, 3.2634492126070555e+36)

        request = RN_pb2.NodeHashValueForRequest(key="Shan")
        response = self.stub.hash_value_for_key(request)
        self.assertEqual(response.hashValue, 3.0317865978285987e+38)

        request = RN_pb2.NodeHashValueForRequest(key="Zhanglei")
        response = self.stub.hash_value_for_key(request)
        self.assertEqual(response.hashValue, 2.725641473381928e+38)

    # TODO: adding does only work when we loop over the responses. if we don't nothing is done
    # TODO: look into why this is the case
    def test2_add(self):
        # add entries to the dict
        request = RN_pb2.NodeGetRequest(type=RN_pb2.ADD,key="Sam",value="24")
        responses = self.stub.get_request(request)
        for i in responses:
            pass
        self.tst_value_for_key("Sam", ["24"])

        request = RN_pb2.NodeGetRequest(type=RN_pb2.ADD,key="Sam",value="14")
        responses = self.stub.get_request(request)
        for i in responses:
            pass
        self.tst_value_for_key("Sam", ["24", "14"])

        request = RN_pb2.NodeGetRequest(type=RN_pb2.ADD,key="Sam",value="42")
        responses = self.stub.get_request(request)
        for i in responses:
            pass
        self.tst_value_for_key("Sam", ["24", "14", "42"])

        request = RN_pb2.NodeGetRequest(type=RN_pb2.ADD,key="Sand",value="18")
        responses = self.stub.get_request(request)
        for i in responses:
            pass
        self.tst_value_for_key("Sand", ["18"])

    def test3_delete(self):
        # delete a key that exists
        request = RN_pb2.NodeGetRequest(type=RN_pb2.DELETE,key="Sam",value="24")
        responses = self.stub.get_request(request)
        for i in responses:
            pass
        self.tst_value_for_key("Sam", ["14", "42"])
        
        # delete all with values left
        request = RN_pb2.NodeGetRequest(type=RN_pb2.DELETE,key="Sam")
        responses = self.stub.get_request(request)
        for i in responses:
            pass
        self.tst_value_for_key("Sam", [])

        # delete all with values left
        request = RN_pb2.NodeGetRequest(type=RN_pb2.DELETE,key="Sand")
        responses = self.stub.get_request(request)
        for i in responses:
            pass
        self.tst_value_for_key("Sand", [])

        # delete all with no values left
        request = RN_pb2.NodeGetRequest(type=RN_pb2.DELETE,key="Sand")
        responses = self.stub.get_request(request)
        for i in responses:
            pass
        self.tst_value_for_key("Sand", [])

        # add two times the same element
        request = RN_pb2.NodeGetRequest(type=RN_pb2.ADD,key="Sam",value="24")
        responses = self.stub.get_request(request)
        for i in responses:
            pass
        request = RN_pb2.NodeGetRequest(type=RN_pb2.ADD,key="Sam",value="24")
        responses = self.stub.get_request(request)
        for i in responses:
            pass
        
        # TODO: should it just delete the first occurance or all occurances???
        # delete element if it is 2 times in the list
        request = RN_pb2.NodeGetRequest(type=RN_pb2.DELETE,key="Sam", value="24")
        responses = self.stub.get_request(request)
        for i in responses:
            pass
        self.tst_value_for_key("Sam", ["24"])

        # delete value what is not in the list
        request = RN_pb2.NodeGetRequest(type=RN_pb2.DELETE,key="Sam", value="32")
        responses = self.stub.get_request(request)
        for i in responses:
            pass
        self.tst_value_for_key("Sam", ["24"])

        # delete value where key is not in list
        request = RN_pb2.NodeGetRequest(type=RN_pb2.DELETE,key="Test", value="24")
        responses = self.stub.get_request(request)
        for i in responses:
            pass
        self.tst_value_for_key("Test", [])

        # delete all where key is not in list
        request = RN_pb2.NodeGetRequest(type=RN_pb2.DELETE,key="Test")
        responses = self.stub.get_request(request)
        for i in responses:
            pass
        self.tst_value_for_key("Test", [])

    def tst_value_for_key(self, key, values):

        request = RN_pb2.NodeGetRequest(type=RN_pb2.GET,key=key)
        responses = self.stub.get_request(request)
        
        x = []
        for response in responses:
            x.append(response.value)
        
        self.assertEqual(len(values), len(x), "len(values) != len(responses)")
        self.assertListEqual(values, x)    
        
if __name__ == '__main__':
    unittest.main()