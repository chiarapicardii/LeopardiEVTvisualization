from lxml import etree
import requests
import os

# 1. Path to your TEI XML file
xml_file = "src/assets/data/canti_completi.xml"

# 2. URL of the official TEI All RelaxNG schema
schema_path = "tei_all.rng"

def validate_tei(xml_path, rng_path):
    print(f"--- Starting validation for: {xml_path} ---")
    
    if not os.path.exists(xml_path):
        print(f"Error: File {xml_path} not found!")
        return

    # Load and parse the RelaxNG schema
    print("Loading TEI schema...")
    try:
        schema_root = etree.parse(rng_path)
        relaxng = etree.RelaxNG(schema_root)
    except Exception as e:
        print(f"Error loading schema: {e}")
        return

    # Parse the XML file
    parser = etree.XMLParser(remove_blank_text=True)
    tree = etree.parse(xml_path, parser)

    # Validate
    is_valid = relaxng.validate(tree)
    
    if is_valid:
        print("✅ SUCCESS! The file is valid according to the TEI schema.")
    else:
        print("❌ WARNING: The file is not valid.")
        print("Errors found:")
        for error in relaxng.error_log:
            print(f" - Line {error.line}: {error.message}")

if __name__ == "__main__":
    validate_tei(xml_file, schema_path)