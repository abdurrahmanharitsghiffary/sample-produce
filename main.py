import grpc
import kafka_pb2, kafka_pb2_grpc

def consume(data, type):
    channel = grpc.insecure_channel('localhost:8085')
    stub = kafka_pb2_grpc.KafkaServiceStub(channel)

    request = kafka_pb2.ConsumeRequest(consumer_group="sample-group", partition=1, topic="steam-data")

    for response in stub.ConsumeMessages.future(request):
        result = response.result()  
        print(f"Response from server: {result}")

# if __name__ == "__main__":
#     consume()
