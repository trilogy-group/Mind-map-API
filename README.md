# Mind Map Generator API

This project provides a FastAPI-based API for generating mind maps based on course details. The API is hosted on Render and can be easily integrated into various applications.

## API Details

- **Hosted URL**: https://mind-map-api-yn7x.onrender.com
- **Endpoint**: `/generate-mindmap/` (POST request)

## API Parameters

The API accepts a JSON payload with the following parameters:

1. `course_title` (string): The title of the course.
2. `key_concepts` (string): A comma-separated list of key concepts, themes, and central ideas.
3. `granularity_level` (string): The desired level of detail (e.g., "Overview", "Detailed Overview", "Comprehensive Breakdown", "In-Depth Analysis", "Exhaustive Detail").
4. `course_duration` (string): The duration of the course (e.g., "1 week", "1 month", "3 months", "6 months", "1 year").
5. `target_audience` (string): The intended audience for the course (e.g., "Beginners", "Intermediate", "Advanced").
6. `learning_objectives` (string): A comma-separated list of main learning objectives for the course.

## Example Usage

Here's an example of how to use the API using Python's `requests` library:

```python
import requests

url = "https://mind-map-api-yn7x.onrender.com/generate-mindmap/"

payload = {
    "course_title": "Introduction to Python Programming",
    "key_concepts": "Variables, Data Types, Control Structures, Functions, Object-Oriented Programming",
    "granularity_level": "Detailed Overview",
    "course_duration": "1 month",
    "target_audience": "Beginners",
    "learning_objectives": "Understand basic Python syntax, Write simple Python programs, Implement basic algorithms"
}

response = requests.post(url, json=payload)

if response.status_code == 200:
    mind_map = response.json()['markdown']
    print(mind_map)
else:
    print(f"Error: {response.status_code}")
    print(response.text)
```

## HTML Demo

This repository includes an HTML file (`index.html`) that demonstrates how to use the API with JavaScript. To use the demo:

1. Clone this repository.
2. Open `index.html` in a web browser.
3. Click the "Generate Mind Map" button to send a request to the API with hardcoded data.
4. The generated mind map will be displayed on the page in Markdown format.

## API Response

The API returns a JSON object with a single key `markdown`, containing the generated mind map in Markdown format.

## Error Handling

If an error occurs, the API will return an appropriate HTTP status code along with an error message in the response body.

Happy mind mapping!
