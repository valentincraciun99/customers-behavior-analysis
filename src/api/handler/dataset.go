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

	return c.JSON(fiber.Map{"status": "success", "message": "Dataset created", "data": nil})
}

func DeleteDataset(c *fiber.Ctx) error {
	dataset := &dataset2.Dataset{}

	if err := c.BodyParser(&dataset); err != nil {
		return c.Status(503).SendString(err.Error())
	}

	if err := services.DeleteDataset(dataset); err != nil {
		return c.Status(503).SendString(err.Error())
	}

	return c.JSON(fiber.Map{"status": "success", "message": "Dataset deleted", "data": nil})
}

func GetDatasetByID(c *fiber.Ctx) error {
	id := c.Params("id")
	dataset, err := services.GetDatasetByID(id)

	if err != nil {
		return c.Status(503).SendString(err.Error())
	}

	return c.JSON(fiber.Map{"status": "success", "message": "Data found", "data": dataset})
}

func GetDatasetsByUserId(c *fiber.Ctx) error {
	dataset := &dataset2.Dataset{}

	if err := c.BodyParser(&dataset); err != nil {
		return c.Status(503).SendString(err.Error())
	}

	data, err := services.GetDatasetsByUserID(dataset.UserID)

	if err != nil {
		return c.Status(503).SendString(err.Error())
	}

	if len(data) == 0 {
		return c.Status(204).SendString("data not found")
	}

	return c.JSON(fiber.Map{"status": "success", "message": "Dataset founded", "data": data})
}
