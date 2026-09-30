import re

with open('frontend/insights-icon-active.b64', 'r', encoding='utf-8') as f:
    new_b64 = f.read().strip()

new_src = f'data:image/png;base64,{new_b64}'

for filename in ['frontend/index.html', 'frontend/user.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace insights-icon-active src
    content_new = re.sub(
        r'(<img\s+src=")[^"]+("\s+alt="Insights Active"\s+class="insights-icon-active"\s*\/?>)',
        r'\g<1>' + new_src + r'\2',
        content
    )
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content_new)
    print('Updated', filename)
