package handler

import (
	"api/dataProcessing"
	"api/database/services"
	dataset2 "api/model/dataset"
	"fmt"
	"github.com/gofiber/fiber/v2"
)

func CreateDataset(c *fiber.Ctx) error {
	dataset := &dataset2.Dataset{}
	c.Attachment("Data")
	fileHeader, _ := c.FormFile("Data")
	associatedFile, err := fileHeader.Open()

	if err != nil {
		return c.Status(503).SendString(err.Error())
	}

	file := make([]byte, 104857600)
	n, err := associatedFile.Read(file)
	if err != nil {
		return c.Status(503).SendString(err.Error())
	}

	fmt.Printf(string(n))

	if err := c.BodyParser(dataset); err != nil {
		return c.Status(503).SendString(err.Error())
	}

	dataset.Data = file

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

func ProcessDataset(c *fiber.Ctx) error {
	//id, _ := strconv.ParseInt(c.Params("id"), 10, 32)
	dataset, err := services.GetDatasetByID(c.Params("id"))
	if err != nil {
		return c.Status(503).SendString(err.Error())
	}

	go dataProcessing.Compute(*dataset)

	return c.JSON(fiber.Map{"status": "success", "message": "Dataset founded", "data": nil})
}
