package main

import (
	"github.com/wailsapp/wails"
)

func basicEditor() string {
	return "This is a basic text editor."
}

func main() {
	app := wails.CreateApp(&wails.AppConfig{
		Width:  800,
		Height: 600,
		Title:  "Text Editor",
		JS:     "frontend/dist/app.js",
		CSS:    "frontend/dist/app.css",
		Colour: "#131313",
	})
	app.Bind(basicEditor)
	app.Run()
}
