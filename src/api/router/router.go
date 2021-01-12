package router

import (
	"api/handler"
	"github.com/gofiber/fiber/v2"
	"github.com/gofiber/fiber/v2/middleware/logger"
)

func SetupRoutes(app *fiber.App) {
	// Middleware
	api := app.Group("/api", logger.New())
	api.Get("/", handler.Hello)
	api.Get("/data", handler.AddDataset)

	// Auth

	// User
	user := api.Group("/user")
	user.Get("/:id", handler.GetUser)
	user.Post("/create", handler.CreateUser)
	user.Post("/delete", handler.DeleteUser)
	user.Post("/update", handler.UpdateUser)

	// Dataset
	dataset := api.Group("/dataset")
	dataset.Post("/create", handler.CreateDataset)
	dataset.Post("/delete", handler.DeleteDataset)

}
