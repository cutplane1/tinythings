package internal

import (
	"fmt"
	"net/http"
	"strconv"

	"github.com/cutplane1/imageboard/internal/database"
	"github.com/cutplane1/imageboard/internal/template"
)

type Imageboard struct {
	db     database.Database
	mux    *http.ServeMux
	config Config
}

func New(config Config, db database.Database) *Imageboard {
	ib := &Imageboard{}
	ib.DefineRoutes()
	ib.db = db
	ib.config = config
	return ib
}

func (i *Imageboard) Server() *http.Server {
	return &http.Server{Handler: i.mux, Addr: i.config.GetAddress()}
}

func (i *Imageboard) DefineRoutes() {
	i.mux = http.NewServeMux()

	i.mux.HandleFunc("GET /", i.Index)
	i.mux.HandleFunc("GET /{board}", i.Threads)
	i.mux.HandleFunc("POST /{board}", i.NewThread)
	i.mux.HandleFunc("GET /{board}/{thread}", i.ThreadDetail)
	i.mux.HandleFunc("POST /{board}/{thread}", i.NewPost)
}

func (i *Imageboard) Index(w http.ResponseWriter, r *http.Request) {
	template.Exec(w, "index", template.IndexTemplate, i.config)
}

func (i *Imageboard) Threads(w http.ResponseWriter, r *http.Request) {
	board := r.PathValue("board")

	template.Exec(w, "threads", template.ThreadsTemplate, i.db.GetThreads(board))
}

func (i *Imageboard) ThreadDetail(w http.ResponseWriter, r *http.Request) {
	thread, _ := strconv.Atoi(r.PathValue("thread"))
	template.Exec(w, "thread", template.ThreadTemplate, i.db.GetThreadRelatedPosts(thread))
}

func (i *Imageboard) NewThread(w http.ResponseWriter, r *http.Request) {
	r.ParseForm()
	msg := r.Form["msg"][0]
	board := r.PathValue("board")

	id := i.db.NewThread(msg, board)
	http.Redirect(w, r, fmt.Sprintf("/%v/%d", board, id), http.StatusFound)
}

func (i *Imageboard) NewPost(w http.ResponseWriter, r *http.Request) {
	r.ParseForm()
	msg := r.Form["msg"][0]
	board := r.PathValue("board")
	thread, _ := strconv.Atoi(r.PathValue("thread"))

	i.db.NewPost(msg, thread, board)
	http.Redirect(w, r, fmt.Sprintf("/%v/%d", board, thread), http.StatusFound)
}
