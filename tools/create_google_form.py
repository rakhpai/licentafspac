#!/usr/bin/env python3
"""
Create Google Forms for Thesis Questionnaires

This script helps create structured questionnaires for the thesis research.
Supports all three thesis themes with pre-configured question templates.

Usage:
    python create_google_form.py --theme 1  # Transformarea proceselor
    python create_google_form.py --theme 2  # Competențe și skills gap
    python create_google_form.py --theme 3  # ROI și metrici

Author: Robert Eduard Antal
Date: 2024-10-22
"""

import os
import sys
import argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from dotenv import load_dotenv
from google.oauth2 import service_account
from googleapiclient.discovery import build

load_dotenv()

# Questionnaire templates for each theme
QUESTIONNAIRE_TEMPLATES = {
    1: {
        "title": "Transformarea Proceselor prin AI în Agențiile de Publicitate",
        "description": """
Bună ziua!

Sunt Robert Eduard Antal, student la Facultatea de Științe Politice, Administrative și ale Comunicării, și desfășor un studiu despre adoptarea și impactul inteligenței artificiale în agențiile de publicitate și comunicare din România.

Chestionarul durează aproximativ 10-12 minute și răspunsurile dvs. sunt complet anonime și confidențiale. Datele vor fi utilizate exclusiv în scop academic, pentru lucrarea mea de licență.

Vă mulțumesc pentru timpul acordat!
""",
        "sections": [
            {
                "title": "A. Date Demografice și Profesionale",
                "questions": [
                    {"type": "MULTIPLE_CHOICE", "question": "Vârstă", "options": ["18-25", "26-35", "36-45", "46-55", "56+"]},
                    {"type": "MULTIPLE_CHOICE", "question": "Gen", "options": ["Masculin", "Feminin", "Prefer să nu răspund"]},
                    {"type": "MULTIPLE_CHOICE", "question": "Poziție în agenție", "options": ["Junior", "Mid-level", "Senior", "Manager/Director", "C-level"]},
                    {"type": "TEXT", "question": "Departament (ex: Creative, Strategy, Media, etc.)"},
                    {"type": "MULTIPLE_CHOICE", "question": "Vechime în industria publicitară", "options": ["0-2 ani", "3-5 ani", "6-10 ani", "11-15 ani", "15+ ani"]},
                    {"type": "MULTIPLE_CHOICE", "question": "Mărime agenție", "options": ["Micro (1-10 angajați)", "Mică (11-50)", "Medie (51-200)", "Mare (200+)"]},
                    {"type": "MULTIPLE_CHOICE", "question": "Tip agenție", "options": ["Independentă românească", "Network internațional", "Boutique/specialized"]},
                ]
            },
            {
                "title": "B. Adoptarea AI în Muncă",
                "questions": [
                    {"type": "MULTIPLE_CHOICE", "question": "Folosești instrumente AI în munca ta?", "options": ["Da, zilnic", "Da, săptămânal", "Da, ocazional", "Nu, dar planific să încep", "Nu și nu planific"]},
                    {"type": "CHECKBOX", "question": "Ce instrumente AI folosești? (Selectează toate opțiunile aplicabile)", "options": ["ChatGPT/GPT-4", "Midjourney/DALL-E", "Jasper/Copy.ai", "Claude/Anthropic", "Runway ML", "Synthesia", "Canva AI", "Adobe Firefly", "Altele (specificați)"]},
                    {"type": "MULTIPLE_CHOICE", "question": "De cât timp folosești AI în muncă?", "options": ["Sub 3 luni", "3-6 luni", "6-12 luni", "1-2 ani", "Peste 2 ani"]},
                    {"type": "CHECKBOX", "question": "În ce procese folosești AI?", "options": ["Generare conținut scris", "Generare imagini/video", "Research și insights", "Planificare media", "Analiza datelor", "Brainstorming/ideație", "Personalizare campanii", "Altele (specificați)"]},
                ]
            },
            {
                "title": "C. Impact asupra Muncii",
                "questions": [
                    {"type": "SCALE", "question": "Cât timp economisești lunar prin folosirea AI? (estimare)", "scale": {"low": "0%", "high": "50%+"}},
                    {"type": "SCALE", "question": "Cu cât AI a crescut calitatea muncii tale?", "scale": {"low": "Deloc", "high": "Semnificativ"}},
                    {"type": "CHECKBOX", "question": "Ce taskuri ai automatizat/delegat la AI?", "options": ["Writing copy", "Visual creation", "Data analysis", "Research", "Reporting", "Social media content", "Altele"]},
                ]
            }
        ]
    },
    2: {
        "title": "Viitorul Competențelor: Skills Gap și Reskilling în Era AI",
        "description": """
Bună ziua!

Acest chestionar investighează nevoile de competențe și training în contextul adoptării AI în agențiile de comunicare.

Completarea durează aproximativ 10 minute. Răspunsurile sunt anonime și confidențiale.

Mulțumesc!
Robert Eduard Antal, Student FSPAC
""",
        "sections": [
            {
                "title": "A. Skills Actuale vs. Necesare",
                "questions": [
                    {"type": "GRID", "question": "Evaluează-ți competențele actuale și importanța lor viitoare", "rows": ["Prompt engineering", "Data analysis", "AI tools literacy", "Creative thinking", "Strategic planning", "Storytelling", "Technical skills"], "columns": ["Nivel actual (1-7)", "Importanță viitor (1-7)"]},
                ]
            },
            {
                "title": "B. Training și Reskilling",
                "questions": [
                    {"type": "MULTIPLE_CHOICE", "question": "Agenția oferă training pe AI?", "options": ["Da, formal și structurat", "Da, dar informal", "Nu, dar planifică", "Nu"]},
                    {"type": "CHECKBOX", "question": "Ce tipuri de training ai urmat?", "options": ["Workshop-uri interne", "Cursuri online", "Certificări", "Self-learning", "Conferences", "Niciunul"]},
                ]
            }
        ]
    },
    3: {
        "title": "ROI și Metrici de Performanță AI în Campanii",
        "description": """
Bună ziua!

Acest chestionar analizează impactul măsurabil al AI asupra performanței campaniilor.

Completarea durează 8-10 minute. Confidențial și anonim.

Mulțumesc!
Robert Eduard Antal, Student FSPAC
""",
        "sections": [
            {
                "title": "A. Utilizare AI în Campanii",
                "questions": [
                    {"type": "MULTIPLE_CHOICE", "question": "Cât de des folosești AI în campanii?", "options": ["În toate", "În majoritatea", "În unele", "Rar", "Niciodată"]},
                    {"type": "CHECKBOX", "question": "Pentru ce folosești AI în campanii?", "options": ["Targeting", "Content creation", "Optimization", "Reporting", "Predictive analytics", "Personalization"]},
                ]
            },
            {
                "title": "B. Impact Măsurabil",
                "questions": [
                    {"type": "SCALE", "question": "ROI campanii cu AI vs. fără AI", "scale": {"low": "Similar", "high": "Mult mai mare"}},
                    {"type": "TEXT", "question": "Cu cât (%) au crescut performanțele campaniilor cu AI? (estimare)"},
                ]
            }
        ]
    }
}

def create_form(theme_id: int):
    """
    Create a Google Form based on theme template.

    Args:
        theme_id: Theme number (1, 2, or 3)
    """
    if theme_id not in QUESTIONNAIRE_TEMPLATES:
        print(f"❌ Invalid theme ID: {theme_id}. Use 1, 2, or 3.")
        return

    template = QUESTIONNAIRE_TEMPLATES[theme_id]

    print(f"\n📝 Creating Google Form: {template['title']}")
    print("=" * 60)

    # Load credentials
    credentials_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
    if not credentials_path:
        print("❌ ERROR: GOOGLE_APPLICATION_CREDENTIALS not set in .env")
        return

    creds_file = Path(__file__).parent.parent / credentials_path
    if not creds_file.exists():
        print(f"❌ ERROR: Credentials file not found at {creds_file}")
        return

    try:
        credentials = service_account.Credentials.from_service_account_file(
            str(creds_file),
            scopes=['https://www.googleapis.com/auth/forms.body']
        )

        forms_service = build('forms', 'v1', credentials=credentials)

        # Create form
        form = {
            "info": {
                "title": template['title'],
                "documentTitle": template['title'],
            }
        }

        result = forms_service.forms().create(body=form).execute()
        form_id = result['formId']

        print(f"✓ Form created with ID: {form_id}")
        print(f"✓ Form URL: https://docs.google.com/forms/d/{form_id}/edit")

        print("\n📋 Note: Questions need to be added manually or via additional API calls")
        print("   Use the URL above to add questions from the template below:")
        print("\n" + "=" * 60)
        print(template['description'])

        for section in template['sections']:
            print(f"\n{section['title']}")
            print("-" * 40)
            for i, q in enumerate(section['questions'], 1):
                print(f"{i}. {q['question']} ({q['type']})")
                if 'options' in q:
                    for opt in q['options']:
                        print(f"   - {opt}")

        return form_id

    except Exception as e:
        print(f"❌ ERROR: {str(e)}")
        return None

def main():
    parser = argparse.ArgumentParser(description="Create Google Forms for thesis questionnaires")
    parser.add_argument('--theme', type=int, choices=[1, 2, 3], required=True,
                        help="Theme number: 1=Transformarea proceselor, 2=Competențe, 3=ROI")

    args = parser.parse_args()
    create_form(args.theme)

if __name__ == "__main__":
    main()
