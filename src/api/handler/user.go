package handler

import (
	"api/database"
	"api/database/services"
	"api/model"
	"fmt"
	"github.com/gofiber/fiber/v2"
)

func GetUser(c *fiber.Ctx) error {
	id := c.Params("id")

	user, err := services.GetUser(id)

	if err != nil {
		return c.Status(503).SendString(err.Error())
	}

	return c.JSON(fiber.Map{"status": "success", "message": "Data found", "data": user})
}

func CreateUser(c *fiber.Ctx) error {
	user := &model.User{}

	if err := c.BodyParser(&user); err != nil {
		return c.Status(503).SendString(err.Error())
	}

	if err := services.CreateUser(user); err != nil {
		return c.Status(503).SendString(err.Error())
	}

	return c.JSON(fiber.Map{"status": "success", "message": "User created", "data": user})
}

func DeleteUser(c *fiber.Ctx) error {
	user := &model.User{}

	if err := c.BodyParser(&user); err != nil {
		return c.Status(503).SendString(err.Error())
	}

	var err = services.DeleteUser(fmt.Sprint(user.ID))
	if err != nil {
		return c.Status(503).SendString(err.Error())
	}

	return c.JSON(fiber.Map{"status": "success", "message": "User deleted!", "data": nil})
}

func UpdateUser(c *fiber.Ctx) error {
	user := &model.User{}

	if err := c.BodyParser(&user); err != nil {
		return c.Status(503).SendString(err.Error())
	}

	if err := services.UpdateUser(user); err != nil {
		return c.Status(503).SendString(err.Error())
	}

	return c.JSON(fiber.Map{"status": "success", "message": "User updated!", "data": nil})

}

func AddDataset(c *fiber.Ctx) error {
	user, _ := services.GetUserWithDatasets("11")

	//user.Datasets = append(user.Datasets, model.Dataset{Data: []byte{1,2,3,4,5,1,1,1,2,3,2,1,2}})

	database.DBConn.Model(&user).Association("Datasets").Append(model.Dataset{Data: []byte{1, 24, 5, 5, 5, 52, 2, 1}})

	return c.JSON(fiber.Map{"status": "success", "message": "User created", "data": user})
}
