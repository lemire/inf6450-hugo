# rm -r -f content/docs/semaines/*
# uv run --with beautifulsoup4 moodle_to_hugo.py "/Users/dlemire/CVS/github/inf6450-hugo/moodle/sauvegarde-moodle2-course-2798-inf6450_vm2-20251210-1338-nu.moodle" "content/docs/semaines"
import os
import sys
import xml.etree.ElementTree as ET
import unicodedata
import re
import html
import bs4

def slugify(text):
    text = unicodedata.normalize('NFD', text).encode('ascii', 'ignore').decode('ascii')
    text = re.sub(r'[^a-zA-Z0-9\s-]', '', text)
    text = re.sub(r'\s+', '_', text).lower()
    return text

def main(backup_dir, output_dir):
    moodle_backup_path = os.path.join(backup_dir, 'moodle_backup.xml')
    tree = ET.parse(moodle_backup_path)
    root = tree.getroot()

    # Get sections
    sections = {}
    for section_elem in root.findall(".//sections/section"):
        section_id = section_elem.find('sectionid').text
        directory = section_elem.find('directory').text
        section_xml_path = os.path.join(backup_dir, directory, 'section.xml')
        if os.path.exists(section_xml_path):
            section_tree = ET.parse(section_xml_path)
            section_root = section_tree.getroot()
            name = section_root.find('name').text
            summary = html.unescape(section_root.find('summary').text or '')
            if summary:
                soup = bs4.BeautifulSoup(summary, 'html.parser')
                summary = soup.prettify()
            sections[section_id] = {'name': name, 'summary': summary}

    # Get activities
    activities_by_section = {}
    for activity in root.findall(".//activities/activity"):
        modulename = activity.find('modulename').text
        if modulename == 'page':
            sectionid = activity.find('sectionid').text
            title = activity.find('title').text
            directory = activity.find('directory').text
            if sectionid not in activities_by_section:
                activities_by_section[sectionid] = []
            activities_by_section[sectionid].append((title, directory))

    # Process each section
    section_weight = 10
    for section_id, section_data in sections.items():
        section_name = section_data['name']
        summary = section_data['summary']
        activities = activities_by_section.get(section_id, [])
        
        if len(activities) == 1 and not summary.strip():
            # Flatten: single page with no summary
            title, directory = activities[0]
            page_xml_path = os.path.join(backup_dir, directory, 'page.xml')
            if os.path.exists(page_xml_path):
                page_tree = ET.parse(page_xml_path)
                page_root = page_tree.getroot()
                content = page_root.find('.//content').text or ''
                if content:
                    soup = bs4.BeautifulSoup(content, 'html.parser')
                    content = soup.prettify()
                filename = slugify(title) + '.md'
                filepath = os.path.join(output_dir, filename)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(f'---\n')
                    f.write(f'title: "{title}"\n')
                    f.write(f'weight: {section_weight}\n')
                    f.write(f'---\n')
                    f.write(content)
        else:
            # Normal: create subdirectory
            dir_name = slugify(section_name)
            dir_path = os.path.join(output_dir, dir_name)
            os.makedirs(dir_path, exist_ok=True)
            
            # Create _index.md
            index_path = os.path.join(dir_path, '_index.md')
            with open(index_path, 'w', encoding='utf-8') as f:
                f.write('---\n')
                f.write(f'title: "{section_name}"\n')
                f.write(f'weight: {section_weight}\n')
                f.write('bookCollapseSection: true\n')
                f.write('---\n')
                f.write(summary)
            
            # Create pages
            weight = 20
            for title, directory in activities:
                page_xml_path = os.path.join(backup_dir, directory, 'page.xml')
                if os.path.exists(page_xml_path):
                    page_tree = ET.parse(page_xml_path)
                    page_root = page_tree.getroot()
                    content = page_root.find('.//content').text or ''
                    if content:
                        soup = bs4.BeautifulSoup(content, 'html.parser')
                        content = soup.prettify()
                    filename = slugify(title) + '.md'
                    filepath = os.path.join(dir_path, filename)
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(f'---\n')
                        f.write(f'title: "{title}"\n')
                        f.write(f'weight: {weight}\n')
                        f.write(f'---\n')
                        f.write(content)
                    weight += 10
        
        section_weight += 10

    # Create root _index.md
    root_index_path = os.path.join(output_dir, '_index.md')
    with open(root_index_path, 'w', encoding='utf-8') as f:
        pass  # empty

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script.py <backup_dir> <output_dir>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])