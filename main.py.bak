import grpc
import kafka_pb2, kafka_pb2_grpc

if __name__ == "__main__":
    channel = grpc.insecure_channel('localhost:8085')
    stub = kafka_pb2_grpc.KafkaServiceStub(channel)

    for i in range(10): 
        request = kafka_pb2.ProduceRequest(topic="steam-data", key=f"user{i}", value=f"Message {i}")

        response = stub.ProduceMessage.future(request)
        result = response.result()  

        print(f"Response {i+1} from server: {result}")