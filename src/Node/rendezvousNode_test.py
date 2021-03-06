import unittest
from collections import defaultdict

import grpc
import src.grpc_enums.type_pb2 as type_pb2
import src.Node.RendezvousNode_pb2 as RN_pb2
import src.Node.RendezvousNode_pb2_grpc as RN_pb2_grpc


class TestRendezvousNodeMethods(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestRendezvousNodeMethods, self).__init__(*args, **kwargs)
        channel = grpc.insecure_channel('localhost:50251')
        self.stub = RN_pb2_grpc.RendezvousNodeStub(channel)
        channel = grpc.insecure_channel('localhost:50252')
        self.stub2 = RN_pb2_grpc.RendezvousNodeStub(channel)

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
        # delete all previous entries to ensure a clean slate for the test
        request = RN_pb2.NodeGetRequest(
            type=type_pb2.DELETE, key="Sam", values=[])
        self.stub.get_request(request)

        request = RN_pb2.NodeGetRequest(
            type=type_pb2.DELETE, key="Shan", values=[])
        self.stub.get_request(request)

        request = RN_pb2.NodeGetRequest(
            type=type_pb2.DELETE, key="Nico", values=[])
        self.stub.get_request(request)

        request = RN_pb2.NodeGetRequest(
            type=type_pb2.DELETE, key="Serwar", values=[])
        self.stub.get_request(request)



        # add entries to the dict
        request = RN_pb2.NodeGetRequest(
            type=type_pb2.ADD, key="Sam", values=["24"])
        self.stub.get_request(request)
        self.tst_value_for_key("Sam", ["24"])

        request = RN_pb2.NodeGetRequest(
            type=type_pb2.ADD, key="Sam", values=["14", "42"])
        self.stub.get_request(request)
        self.tst_value_for_key("Sam", ["24", "14", "42"])

        request = RN_pb2.NodeGetRequest(
            type=type_pb2.ADD, key="Shan", values=["18"])
        self.stub.get_request(request)
        self.tst_value_for_key("Shan", ["18"])

    def test3_get_objects(self):
        objects_on_node = defaultdict(list)
        request = RN_pb2.NodeEmpty()
        responses = self.stub.get_objects(request)

        for response in responses:
            objects_on_node[response.key].extend(response.values)

        self.assertEqual(len(objects_on_node["Sam"]), len(
            ["24", "14", "42"]), "len(values) != len(responses)")
        self.assertListEqual(objects_on_node["Sam"], ["24", "14", "42"])

        self.assertEqual(len(objects_on_node["Shan"]), len(
            ["18"]), "len(values) != len(responses)")
        self.assertListEqual(objects_on_node["Shan"], ["18"])

    def test4_delete(self):
        # delete a key that exists
        request = RN_pb2.NodeGetRequest(
            type=type_pb2.DELETE, key="Sam", values=["24"])
        self.stub.get_request(request)
        self.tst_value_for_key("Sam", ["14", "42"])

        # delete all with values left
        request = RN_pb2.NodeGetRequest(type=type_pb2.DELETE, key="Sam")
        self.stub.get_request(request)
        self.tst_value_for_key("Sam", [])

        # delete all with values left
        request = RN_pb2.NodeGetRequest(type=type_pb2.DELETE, key="Shan")
        self.stub.get_request(request)
        self.tst_value_for_key("Shan", [])

        # delete all with no values left
        request = RN_pb2.NodeGetRequest(type=type_pb2.DELETE, key="Shan")
        self.stub.get_request(request)
        self.tst_value_for_key("Shan", [])

        # add two times the same element
        request = RN_pb2.NodeGetRequest(
            type=type_pb2.ADD, key="Sam", values=["24"])
        self.stub.get_request(request)
        request = RN_pb2.NodeGetRequest(
            type=type_pb2.ADD, key="Sam", values=["24"])
        self.stub.get_request(request)
        self.tst_value_for_key("Sam", ["24", "24"])

        # TODO: should it just delete the first occurance or all occurances???
        # delete element if it is 2 times in the list
        request = RN_pb2.NodeGetRequest(
            type=type_pb2.DELETE, key="Sam", values=["24"])
        self.stub.get_request(request)
        self.tst_value_for_key("Sam", ["24"])

        # delete value what is not in the list
        request = RN_pb2.NodeGetRequest(
            type=type_pb2.DELETE, key="Sam", values=["32"])
        self.stub.get_request(request)
        self.tst_value_for_key("Sam", ["24"])

        # delete value where key is not in list
        request = RN_pb2.NodeGetRequest(
            type=type_pb2.DELETE, key="Test", values=["24"])
        self.stub.get_request(request)
        self.tst_value_for_key("Test", [])

        # delete all where key is not in list
        request = RN_pb2.NodeGetRequest(type=type_pb2.DELETE, key="Test")
        self.stub.get_request(request)
        self.tst_value_for_key("Test", [])

        # delete all for sam
        request = RN_pb2.NodeGetRequest(type=type_pb2.DELETE, key="Sam")
        self.stub.get_request(request)
        self.tst_value_for_key("Sam", [])

    def test5_send_item_to_new_node(self):
        # adds iteams
        request = RN_pb2.NodeGetRequest(
            type=type_pb2.ADD, key="Sam", values=["14"])
        self.stub.get_request(request)

        request = RN_pb2.NodeGetRequest(
            type=type_pb2.ADD, key="Shan", values=["34"])
        self.stub.get_request(request)

        request = RN_pb2.NodeGetRequest(
            type=type_pb2.ADD, key="Nico", values=["54", "612"])
        self.stub.get_request(request)

        request = RN_pb2.NodeGetRequest(
            type=type_pb2.ADD, key="Serwar", values=["54"])
        self.stub.get_request(request)

        request = RN_pb2.NodeSendItemToNewNodeRequest(
            ip_address="172.17.0.5:50252")
        self.stub.send_item_to_new_node(request)

        self.tst_value_for_key("Sam", ["14"])
        self.tst_value_for_key("Shan", ["34"])
        self.tst_value_for_key("Nico", [])
        self.tst_value_for_key("Serwar", [])

        self.tst_value_for_key("Sam", [], 1)
        self.tst_value_for_key("Shan", [], 1)
        self.tst_value_for_key("Nico", ["54", "612"], 1)
        self.tst_value_for_key("Serwar", ["54"], 1)

    def test6_delete_all(self):
        # delete all for sam
        request = RN_pb2.NodeGetRequest(type=type_pb2.DELETE, key="Sam")
        self.stub.get_request(request)
        self.tst_value_for_key("Sam", [])

        # delete all for Shan
        request = RN_pb2.NodeGetRequest(type=type_pb2.DELETE, key="Shan")
        self.stub.get_request(request)
        self.tst_value_for_key("Shan", [])

        # delete all for nico
        request = RN_pb2.NodeGetRequest(type=type_pb2.DELETE, key="Nico")
        self.stub2.get_request(request)
        self.tst_value_for_key("Nico", [])

        # delete all for Serwar
        request = RN_pb2.NodeGetRequest(type=type_pb2.DELETE, key="Serwar")
        self.stub2.get_request(request)
        self.tst_value_for_key("Serwar", [])

    def tst_value_for_key(self, key, values, stub=0):

        request = RN_pb2.NodeGetRequest(type=type_pb2.GET, key=key)
        if stub == 0:
            response = self.stub.get_request(request)
        else:
            response = self.stub2.get_request(request)

        x = list(response.values)
        self.assertEqual(len(values), len(x), "len(values) != len(responses)")
        self.assertListEqual(values, x)

if __name__ == '__main__':
    unittest.main()
