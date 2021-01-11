package database

import (
	"api/model/dataset"
	user2 "api/model/user"
	"fmt"
	"github.com/jinzhu/gorm"
	_ "github.com/jinzhu/gorm/dialects/postgres"
)

// Database settings
const (
	host     = "localhost"
	port     = 5432 // Default port
	user     = "postgres"
	password = "root"
	dbname   = "test"
)

var (
	DBConn *gorm.DB
)

// Connect function
func Connect() {
	db, err := gorm.Open("postgres", fmt.Sprintf("host=%s port=%d user=%s password=%s dbname=%s"+
		" sslmode=disable", host, port, user, password, dbname))
	DBConn = db

	if err != nil {
		panic("Database error: " + err.Error())
	}

	fmt.Println("Connection to postgres database successful!")
}

func Migrate() {

	DBConn.AutoMigrate(&user2.User{}, &dataset.Dataset{})
	db := DBConn.Model(&dataset.Dataset{}).AddForeignKey("user_id", "users(id)", "CASCADE", "CASCADE")
	fmt.Println(db.Error)

	fmt.Println("Database Migrated ")
}
