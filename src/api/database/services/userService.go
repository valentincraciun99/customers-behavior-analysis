package services

import (
	"api/database"
	"api/model/user"
)

func GetUser(id string) (*user.User, error) {
	var user user.User
	err := database.DBConn.Find(&user, id)

	return &user, err.Error
}

func GetUserWithDatasets(id string) (*user.User, error) {
	var user user.User
	err := database.DBConn.Find(&user, id).Association("Datasets").Find(&user.Datasets)

	return &user, err.Error
}

func CreateUser(user *user.User) error {
	err := database.DBConn.Create(&user)
	return err.Error
}

func DeleteUser(id string) error {

	db := database.DBConn.Delete(user.User{}, id)

	return db.Error
}

func UpdateUser(user *user.User) error {

	db := database.DBConn.Save(&user)
	return db.Error
}
