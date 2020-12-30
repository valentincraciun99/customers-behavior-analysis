package model

import "github.com/jinzhu/gorm"

type Dataset struct {
	gorm.Model
	UserID uint
	Data   []byte
}
