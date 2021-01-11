package dataset

import "github.com/jinzhu/gorm"

type Dataset struct {
	gorm.Model
	UserID uint
	Name   string
	Data   []byte
}
