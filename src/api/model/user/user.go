package user

import (
	"api/model/dataset"
	"github.com/jinzhu/gorm"
)

type User struct {
	gorm.Model
	Username string
	Email    string
	Password string
	Name     string
	Datasets []dataset.Dataset `gorm:"constraint:OnUpdate:CASCADE,OnDelete:CASCADE;"`
}
