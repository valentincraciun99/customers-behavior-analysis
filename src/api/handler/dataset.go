package handler

import (
	"api/database/services"
	dataset2 "api/model/dataset"
	"github.com/gofiber/fiber/v2"
)

func CreateDataset(c *fiber.Ctx) error {
	dataset := &dataset2.Dataset{}

	if err := c.BodyParser(&dataset); err != nil {
		return c.Status(503).SendString(err.Error())
	}

	if err := services.CreateDataset(dataset); err != nil {
		return c.Status(503).SendString(err.Error())
	}

	return c.JSON(fiber.Map{"status": "success", "message": "User created", "data": nil})
}
