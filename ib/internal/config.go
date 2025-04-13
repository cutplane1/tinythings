package internal

import (
	"bytes"
	"encoding/json"
	"fmt"
	"os"
)

type Config struct {
	Url    string
	Port   int
	Boards []string
	Name   string
}

func (c *Config) Load(file string) {
	var bytes []byte
	bytes, _ = os.ReadFile(file)
	json.Unmarshal(bytes, c)
}

func NewConfigFromFile(file string) Config {
	c := &Config{}
	c.Load(file)
	return *c
}

func (c *Config) GetAddress() string {
	b := bytes.Buffer{}
	b.WriteString(c.Url)
	b.WriteString(":")
	b.WriteString(fmt.Sprintf("%v", c.Port))

	return b.String()
}
