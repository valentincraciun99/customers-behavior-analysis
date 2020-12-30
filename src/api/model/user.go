package model

import "github.com/jinzhu/gorm"

type User struct {
	gorm.Model
	Username string
	Email    string
	Password string
	Name     string
	Datasets []Dataset `gorm:"constraint:OnUpdate:CASCADE,OnDelete:CASCADE;"`
}
