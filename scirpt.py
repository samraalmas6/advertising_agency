import json

postman_collection = {
    "info": {
        "name": "Advertising Agency API",
        "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
    },
    "item": [
        {
            "name": "Get All Advertising Locations",
            "request": {
                "method": "GET",
                "header": [
                    {
                        "key": "Content-Type",
                        "value": "application/json"
                    },
                    {
                        "key": "Authorization",
                        "value": "Token YOUR_API_TOKEN"
                    }
                ],
                "url": {
                    "raw": "http://127.0.0.1:8000/api/advertising-locations/",
                    "protocol": "http",
                    "host": ["127.0.0.1"],
                    "port": "8000",
                    "path": ["api", "advertising-locations"]
                }
            }
        },
        {
            "name": "Create a New Advertising Location",
            "request": {
                "method": "POST",
                "header": [
                    {
                        "key": "Content-Type",
                        "value": "application/json"
                    },
                    {
                        "key": "Authorization",
                        "value": "Token YOUR_API_TOKEN"
                    }
                ],
                "body": {
                    "mode": "raw",
                    "raw": json.dumps({
                        "name": "Location 3",
                        "description": "New location description",
                        "location_coordinates": "13.0827,80.2707"
                    })
                },
                "url": {
                    "raw": "http://127.0.0.1:8000/api/advertising-locations/",
                    "protocol": "http",
                    "host": ["127.0.0.1"],
                    "port": "8000",
                    "path": ["api", "advertising-locations"]
                }
            }
        },
        {
            "name": "Get All Advertisers",
            "request": {
                "method": "GET",
                "header": [
                    {
                        "key": "Content-Type",
                        "value": "application/json"
                    },
                    {
                        "key": "Authorization",
                        "value": "Token YOUR_API_TOKEN"
                    }
                ],
                "url": {
                    "raw": "http://127.0.0.1:8000/api/advertisers/",
                    "protocol": "http",
                    "host": ["127.0.0.1"],
                    "port": "8000",
                    "path": ["api", "advertisers"]
                }
            }
        },
        {
            "name": "Create a New Ad Spend",
            "request": {
                "method": "POST",
                "header": [
                    {
                        "key": "Content-Type",
                        "value": "application/json"
                    },
                    {
                        "key": "Authorization",
                        "value": "Token YOUR_API_TOKEN"
                    }
                ],
                "body": {
                    "mode": "raw",
                    "raw": json.dumps({
                        "advertisement": 1,
                        "amount": "200.00",
                        "date": "2023-06-06"
                    })
                },
                "url": {
                    "raw": "http://127.0.0.1:8000/api/adspends/",
                    "protocol": "http",
                    "host": ["127.0.0.1"],
                    "port": "8000",
                    "path": ["api", "adspends"]
                }
            }
        }
    ]
}

# Save to a JSON file
with open('postman_collection.json', 'w') as file:
    json.dump(postman_collection, file, indent=4)

print("Postman collection JSON created successfully.")