package main

import (
	"encoding/json"
	"net/http"
	"os/exec"
	"strings"
)

func getData (writer http.ResponseWriter, request *http.Request){
	ip, _ := exec.Command("hostname", "-i").Output()
	processes, _ := exec.Command("ps", "-ax").Output()
	disk, _ := exec.Command("df", "-h", "/").Output()
	uptime, _ := exec.Command("uptime", "-p").Output()
	
	// creating a map with data 
	info := map[string]interface{}{
		"ip":         strings.TrimSpace(string(ip)),
		"processes":  string(processes),
		"disk space": string(disk),
		"uptime":     strings.TrimSpace(string(uptime)),
	}
	
	writer.Header().Set("Content-Type", "application/json")
	// coverting the map
	json.NewEncoder(writer).Encode(info)
}

func main () {
	// creating /data endpoint and listening on port 8500
	http.HandleFunc("/data", getData)
	http.ListenAndServe(":8500", nil)
}
