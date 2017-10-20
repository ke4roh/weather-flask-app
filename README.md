# Weather radio UI

# Running
run.sh

Submit a message to the server: 

   curl -X POST http://localhost:5000/alert --header "Content-type: application/json" --data-binary '{"alert":"Bananas are expensive."}'

