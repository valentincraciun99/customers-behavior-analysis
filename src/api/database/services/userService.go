package services

import (
	"api/database"
	"api/model"
)

func GetUser(id string) (*model.User, error) {
	var user model.User
	err := database.DBConn.Find(&user, id)

	return &user, err.Error
}

func GetUserWithDatasets(id string) (*model.User, error) {
	var user model.User
	err := database.DBConn.Find(&user, id).Association("Datasets").Find(&user.Datasets)

	return &user, err.Error
}

func CreateUser(user *model.User) error {
	err := database.DBConn.Create(&user)
	return err.Error
}

func DeleteUser(id string) error {

	db := database.DBConn.Delete(model.User{}, id)

	return db.Error
}
