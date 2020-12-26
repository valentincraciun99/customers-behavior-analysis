package main

import (
	"api/grpcGeneratedCode"
	"context"
	"fmt"
	"google.golang.org/grpc"
	"log"
)


func main(){


	conn, err := grpc.Dial(":1111",grpc.WithInsecure())
	if err != nil {
		log.Fatalf("could not connect: %s",err)
	}

	defer conn.Close()

	c := grpcGeneratedCode.NewTestServiceClient(conn)

	request:= &grpcGeneratedCode.TestRequest{Number: 15,Text: "abc"}

	response,err := c.TestMethod(context.Background(),request)

	fmt.Println(response)



}