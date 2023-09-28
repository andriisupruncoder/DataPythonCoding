import xml.etree.ElementTree as ET

def json_to_xml(json_data, root_name="data"):
    root = ET.Element(root_name)
    return _json_to_xml_rec(json_data, root)

def _json_to_xml_rec(json_data, xml_element):
    if isinstance(json_data, dict):
        for key, value in json_data.items():
            sub_element = ET.SubElement(xml_element, key)
            _json_to_xml_rec(value, sub_element)
    elif isinstance(json_data, list):
        for item in json_data:
            _json_to_xml_rec(item, xml_element)
    else:
        xml_element.text = str(json_data)
    return xml_element

# Read the provided JSON data (this is just a representation; in a real-world scenario, you would read from the file)
json_data = {
    "course_id": "CS101",
    "title": "Introduction to Computer Science",
    "instructor": {
        "name": "Dr. Alice",
        "email": "alice@example.edu"
    },
    "modules": [
        {
            "module_id": "M01",
            "title": "Basics of Programming",
            "content": [
                {"type": "video", "url": "/videos/1.mp4"},
                {"type": "quiz", "questions": 10},
                {"type": "reading", "url": "/readings/1.pdf"},
                {"type": "discussion", "topic": "Getting Started with Programming"}
            ]
        },
        {
            "module_id": "M02",
            "title": "Data Structures",
            "content": [
                {"type": "video", "url": "/videos/2.mp4"},
                {"type": "assignment", "topic": "Implementing a list"},
                {"type": "reading", "url": "/readings/2.pdf"},
                {"type": "quiz", "questions": 12}
            ]
        },
        {
            "module_id": "M03",
            "title": "Algorithms",
            "content": [
                {"type": "video", "url": "/videos/3.mp4"},
                {"type": "assignment", "topic": "Implementing a basic sorting algorithm"},
                {"type": "reading", "url": "/readings/3.pdf"},
                {"type": "discussion", "topic": "Efficiency and Time Complexity"}
            ]
        },
        {
            "module_id": "M04",
            "title": "Computer Organization",
            "content": [
                {"type": "video", "url": "/videos/4.mp4"},
                {"type": "quiz", "questions": 8},
                {"type": "reading", "url": "/readings/4.pdf"},
                {"type": "assignment", "topic": "Basic operations of a computer"}
            ]
        }
    ]
}

# Convert the JSON data to XML and print the result
xml_root = json_to_xml(json_data, root_name="course")
tree = ET.ElementTree(xml_root)
tree.write("education_course_content.xml")

# To view the generated XML, you can print it using:
# print(ET.tostring(xml_root, encoding='utf-8', method='xml').decode())
