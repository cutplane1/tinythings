package database

type Database interface {
	Connect()
	Close()
	GetThreads(board string) []Post
	GetThreadRelatedPosts(thread int) []Post
	NewThread(msg string, board string) int
	NewPost(msg string, thread int, board string) int
}
