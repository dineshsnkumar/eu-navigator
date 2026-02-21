import json
import os
from datetime import datetime

def add_document():
    """Convert documents to JSONL"""
    print("Adding documents")

    doc = {}
    doc['doc_id'] = input("\n What is the doc_id? ").strip()
    doc['title'] = input("\n Title: ").strip()
    doc['url'] = input("\n URL: ").strip()
    doc['country'] = input("\n Country code (DE/FR/ES): ").strip().upper()
    doc['service_type'] = input("\n Service type (health_insurance/tax_id/residence_permit): ").strip()
    doc['language'] = input("\n Language (en/de/fr/es/hi): ").strip().lower()
    doc['source_type'] = input("\n Source type (official_government/community_verified) ").strip()
    doc['collected_date'] = datetime.now().strftime("%Y-%m-%d")

    print("Paste content from the website. After entreing press Ctrl+D \n")
    
    # Adding content
    lines = []
    try:
        while True:
            lines.append(input())
    except EOFError:
        pass
    doc['content'] = '\n'.join(lines)
    doc['word_count'] = len(doc['content'].split())

    #Preview the content
    print(f"doc_id: {doc['doc_id']}")
    print(f"Title: {doc['title']}")
    print(f"Words: {doc['word_count']}")
    print(f"Content preview: {doc['content'][:200]}...")

    # Confirm if you want to add document?
    confirm = input("Add this document? (y/n)").strip().lower()

    if confirm == 'y':
        output_file = '../data/tier1_documents.jsonl'

        with open(output_file, 'a', encoding='utf-8') as f:
            f.write(json.dumps(doc, ensure_ascii=True) + '\n')

        print("Document successfully added")
    else: 
        print("Document not added")

if __name__ == "__main__":
    os.makedirs('data', exist_ok=True)
    add_document()

    while input("Add another document: y/n ").strip().lower() == 'y':
        add_document()

    
