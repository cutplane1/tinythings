package template

import (
	_ "embed"
	"fmt"
	"html/template"
	"io"
)

//go:embed index.html
var IndexTemplate string

//go:embed thread.html
var ThreadTemplate string

//go:embed threads.html
var ThreadsTemplate string

func Exec(w io.Writer, name string, t string, data any) {
	tmpl, err := template.New(name).Parse(t)
	if err != nil {
		fmt.Println(err)
	}
	if err := tmpl.Execute(w, data); err != nil {
		fmt.Println(err)
	}
}
