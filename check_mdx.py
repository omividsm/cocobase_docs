#!/usr/bin/env python3
import sys
import re
from pathlib import Path

def check_mdx_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    issues = []

    # Check for unclosed tags
    tags = ['Tabs', 'Tab', 'Card', 'CardGroup', 'Accordion', 'AccordionGroup', 'Note', 'Warning']

    for tag in tags:
        open_pattern = f'<{tag}[\\s>]'
        close_pattern = f'</{tag}>'

        open_count = len(re.findall(open_pattern, content))
        close_count = len(re.findall(close_pattern, content))

        if open_count != close_count:
            issues.append(f'{tag}: {open_count} open, {close_count} close')

    return issues

def main():
    mdx_files = list(Path('.').rglob('*.mdx'))

    has_issues = False
    for filepath in sorted(mdx_files):
        issues = check_mdx_file(filepath)
        if issues:
            has_issues = True
            print(f'\n❌ {filepath}:')
            for issue in issues:
                print(f'   {issue}')

    if not has_issues:
        print('✅ All MDX files are valid!')
    else:
        sys.exit(1)

if __name__ == '__main__':
    main()
