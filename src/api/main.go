package main

import (
	"api/database"
	"api/router"
	"github.com/gofiber/fiber/v2"
	"github.com/gofiber/fiber/v2/middleware/cors"
	"log"
)

func main() {

	app := fiber.New()
	app.Use(cors.New())

	database.Connect()
	defer database.DBConn.Close()
	database.Migrate()
	router.SetupRoutes(app)
	log.Fatal(app.Listen(":3000"))

	/*conn, err := grpc.Dial("localhost:1111", grpc.WithInsecure())
	if err != nil {
		log.Fatalf("could not connect: %s", err)
	}

	defer conn.Close()

	c := grpcGeneratedCode.NewTestServiceClient(conn)

	request := &grpcGeneratedCode.TestRequest{Number: 15, Text: "abc"}

	response, err := c.TestMethod(context.Background(), request)

	fmt.Println(response)*/

}
