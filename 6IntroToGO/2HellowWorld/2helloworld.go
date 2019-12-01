package main

import (
	"fmt"
	"net/http"
)

func main() {
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintf(w, "Hello, you've requested: %s\n", r.URL.Path)
	})

	http.ListenAndServe(":5431", nil)
}

// to run this program, go to the correct folder, then type in go run 2helloworld.go
// Then in your web broswer, got to the local port plus want you want to be printed http://127.0.0.1:5431/HelloWorld
