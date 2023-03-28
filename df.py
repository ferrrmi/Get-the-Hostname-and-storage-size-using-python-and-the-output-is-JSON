import subprocess
import json
import socket

# Get the hostname of the machine
hostname = socket.gethostname()

# Run the df command and capture the output
output = subprocess.check_output(['df', '-hT', '/']).decode('utf-8')

# Split the output into lines and remove the header
lines = output.strip().split('\n')[1:]

# Split each line into fields and convert to dictionary
data = []
for line in lines:
    fields = line.split()
    data.append({
'filesystem': fields[0],
'type': fields[1],
'size': fields[2],
'used': fields[3],
'avail': fields[4],
'use': fields[5],
'mount': fields[6]
    })

# Merge the data with the hostname
result = {
    'hostname': hostname,
    'data': data
}

# Convert the result to JSON format
json_data = json.dumps(result, indent=4)

# Save the JSON data to a file
with open('/tmp/df.json', 'w') as f:
    f.write(json_data)