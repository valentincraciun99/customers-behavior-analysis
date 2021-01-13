package services

import (
	"api/database"
	"api/model/dataset"
)

func CreateDataset(dataset *dataset.Dataset) error {
	err := database.DBConn.Create(&dataset)
	return err.Error
}

func DeleteDataset(dataset *dataset.Dataset) error {
	err := database.DBConn.Delete(&dataset)
	return err.Error
}

func GetDatasetByID(ID string) (*dataset.Dataset, error) {
	var data dataset.Dataset
	err := database.DBConn.Find(&data, ID)

	return &data, err.Error
}
