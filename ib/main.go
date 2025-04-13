package main

import (
	"context"
	"log"
	"os"
	"os/signal"
	"syscall"

	"github.com/cutplane1/imageboard/internal"
	"github.com/cutplane1/imageboard/internal/database"
)

func main() {
	done := make(chan os.Signal, 1)
	signal.Notify(done, os.Interrupt, syscall.SIGINT, syscall.SIGTERM)

	c := internal.NewConfigFromFile("config.json")

	logger := log.Default()
	logger.Printf("running at %v", c.GetAddress())

	mysql := &database.MySqlDatabase{}
	mysql.Connect()
	defer mysql.Close()

	ib := internal.New(c, mysql)
	server := ib.Server()

	go func() {
		server.ListenAndServe()
	}()

	shutdownSignal := make(chan os.Signal, 1)
	signal.Notify(shutdownSignal, syscall.SIGINT, syscall.SIGTERM)

	<-shutdownSignal
	server.Shutdown(context.TODO())
	mysql.Close()
	logger.Print("stopped")
}
