package dataset

import (
	"api/grpcGeneratedCode"
	"github.com/jinzhu/gorm"
)

type Metadata struct {
	gorm.Model
	*grpcGeneratedCode.Transactions
	DatasetID uint
	UserID    uint
}
