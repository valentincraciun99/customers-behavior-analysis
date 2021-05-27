package services

import (
	"api/database"
	"api/model/dataset"
)

func CreateMetadata(metadata *dataset.Metadata) error {
	err := database.DBConn.Create(&metadata)
	return err.Error
}
