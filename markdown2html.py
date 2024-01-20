#!/usr/bin/python3
"""
Markdown to HTML script.

Usage:
    ./markdown2html.py <input_file> <output_file>

Arguments:
    <input_file>: The name of the Markdown file.
    <output_file>: The name of the HTML output file.
"""
import sys
import os
import markdown

def convert_markdown_to_html(input_file, output_file):
    """
    Convert Markdown to HTML.

    Args:
        input_file (str): The name of the Markdown file.
        output_file (str): The name of the HTML output file.
    """
    if not os.path.isfile(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    with open(input_file, 'r') as md_file, open(output_file, 'w') as html_file:
        html_content = markdown.markdown(md_file.read())
        html_file.write(html_content)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py <input_file> <output_file>", file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    convert_markdown_to_html(input_file, output_file)
    sys.exit(0)
