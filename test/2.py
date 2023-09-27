import json
import xml.etree.ElementTree as ET

# Load the JSON data
with open("music_streaming_data.json", "r") as file:
    data = json.load(file)

def json_to_xml(json_data, root_tag):
    root = ET.Element(root_tag)

    def build_element(parent, key, value):
        if isinstance(value, dict):
            sub_elem = ET.SubElement(parent, key)
            for sub_key, sub_value in value.items():
                build_element(sub_elem, sub_key, sub_value)
        elif isinstance(value, list):
            sub_elem = ET.SubElement(parent, key)
            for item in value:
                item_elem = ET.SubElement(sub_elem, "item")
                for sub_key, sub_value in item.items():
                    build_element(item_elem, sub_key, sub_value)
        else:
            sub_elem = ET.SubElement(parent, key)
            sub_elem.text = str(value)

    for key, value in json_data.items():
        build_element(root, key, value)

    return ET.ElementTree(root)

# Convert the JSON data to XML
xml_data = json_to_xml(data, "user_data")

# Save the XML data to a file
with open("music_streaming_data.xml", "wb") as file:
    xml_data.write(file)

