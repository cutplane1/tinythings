package database

type Post struct {
	Id             int64
	Msg            string
	IsThread       bool
	ThreadReatedId int64
	Image          string
	Board          string
}
