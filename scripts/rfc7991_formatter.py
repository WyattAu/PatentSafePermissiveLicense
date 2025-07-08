import re
import textwrap

def format_rfc7991(content):
    # RFC 7991 core requirements
    formatted = []
    page_lines = []
    wrapper = textwrap.TextWrapper(width=72, break_long_words=False)
    
    for line in content.split('\n'):
        # Remove trailing whitespace
        line = line.rstrip()
        # Split into RFC-compliant segments
        wrapped_lines = wrapper.wrap(line)
        page_lines.extend(wrapped_lines)
        
        # Insert form feed every 58 lines (66-line pages with 8-line header)
        while len(page_lines) >= 58:
            formatted.extend(page_lines[:58])
            formatted.append('\x0C')
            page_lines = page_lines[58:]
    
    return '\n'.join(formatted + page_lines)
