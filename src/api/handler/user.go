package handler

import (
	"api/model"
	"fmt"
	"github.com/gofiber/fiber/v2"
)

func GetUser(c *fiber.Ctx) error {
	id := c.Params("id")
	fmt.Println(c.IP())
	user:= &model.User{Username: id,Password:"password", Email: "sanky@yahoo.eu",Name: "Zon"}

	if user.Username == "" {
		return c.Status(404).JSON(fiber.Map{"status": "error", "message": "No user found with ID", "data": nil})
	}
	return c.JSON(fiber.Map{"status": "success", "message": "User found", "data": user})
}