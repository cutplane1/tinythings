package database

import (
	"database/sql"
	"log"

	_ "github.com/go-sql-driver/mysql"
)

type MySqlDatabase struct {
	DB *sql.DB
}

func (mysql *MySqlDatabase) Connect() {
	var err error
	mysql.DB, err = sql.Open("mysql", "root:@tcp(127.0.0.1:3306)/imageboard") //hardcoded
	if err != nil {
		panic(err)
	}
}

func (mysql *MySqlDatabase) Close() {
	mysql.DB.Close()
}

func (mysql *MySqlDatabase) GetThreads(board string) []Post {
	posts := []Post{}

	rows, err := mysql.DB.Query("SELECT * FROM posts WHERE is_thread = 1 AND board = ?", board)
	if err != nil {
		log.Fatal(err)
	}

	for rows.Next() {
		post := Post{}
		err := rows.Scan(&post.Id, &post.Msg, &post.IsThread, &post.ThreadReatedId, &post.Image, &post.Board)
		if err != nil {
			log.Println(err)
			continue
		}
		posts = append(posts, post)
	}

	return posts

}

func (mysql *MySqlDatabase) GetThreadRelatedPosts(thread int) []Post {

	posts := []Post{}

	rows, err := mysql.DB.Query("SELECT * FROM posts WHERE thread_related_id = ?", thread)
	if err != nil {
		log.Fatal(err)
	}

	for rows.Next() {
		post := Post{}
		err := rows.Scan(&post.Id, &post.Msg, &post.IsThread, &post.ThreadReatedId, &post.Image, &post.Board)
		if err != nil {
			log.Println(err)
			continue
		}
		posts = append(posts, post)
	}

	return posts
}

func (mysql *MySqlDatabase) NewThread(msg string, board string) int {
	res, err := mysql.DB.Exec("INSERT INTO posts (msg, is_thread, board) VALUES (?, 1, ?)", msg, board)
	if err != nil {
		log.Fatal(err)
	}
	id, _ := res.LastInsertId()
	return int(id)
}

func (mysql *MySqlDatabase) NewPost(msg string, thread int, board string) int {
	res, err := mysql.DB.Exec("INSERT INTO posts (msg, thread_related_id, board) VALUES (?, ?, ?)", msg, thread, board)
	if err != nil {
		log.Fatal(err)
	}
	id, _ := res.LastInsertId()
	return int(id)
}
