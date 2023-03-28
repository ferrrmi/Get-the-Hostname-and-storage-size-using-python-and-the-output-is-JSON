# Get the Hostname and storage size using python and the output is JSON

simple python script to get hostname and size of your storage and convert the output into JSON file.

How to run?
--> py df.py

Json example output:
```json
{
    "hostname": "xxxx-client",
    "data": [
        {
            "filesystem": "/dev/xxx",
            "type": "ext4",
            "size": "1007G",
            "used": "4.6G",
            "avail": "952G",
            "use": "1%",
            "mount": "/"
        }
    ]
}