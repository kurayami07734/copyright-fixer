"""
Mapping of file type to its comment format

Example:
    "py": '# {comment}'
    "html": '<-- {comment} -->'
"""

comment_formats = {
    "py": "# {comment}",
    "html": "<-- {comment} -->",
    "go": "// {comment}",
    "js": "// {comment}",
    "ts": "// {comment}",
    "cpp": "// {comment}",
    "jsx": "// {comment}",
}
