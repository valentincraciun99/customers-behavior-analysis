package interop

import (
	"api/grpcGeneratedCode"
	"context"
	"google.golang.org/grpc"
	"log"
)

func SendRequest(dataset []byte, target string, ch chan *grpcGeneratedCode.DatasetResponse) error {
	conn, err := grpc.Dial(target, grpc.WithInsecure())
	if err != nil {
		log.Fatalf("could not connect: %s", err)
	}

	defer conn.Close()

	co := grpcGeneratedCode.NewDataServiceClient(conn)

	request := &grpcGeneratedCode.DatasetRequest{UserId: 7, Name: "abc", Data: dataset}

	response, err := co.ProcessesData(context.Background(), request)

	ch <- response

	return err
}
