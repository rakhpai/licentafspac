# Ghid Setup Zotero pentru Lucrarea de Licență

## 📦 Instalare

### Pasul 1: Instalare Zotero Desktop
1. Descarcă de la: https://www.zotero.org/download/
2. Instalează versiunea pentru sistemul tău (Windows/Mac/Linux)
3. Creează cont Zotero (pentru sync cloud - optional dar recomandat)

### Pasul 2: Instalare Browser Connector
1. După ce instalezi Zotero desktop, instalează extensia pentru browser
2. Chrome/Firefox/Edge: https://www.zotero.org/download/connectors
3. Această extensie permite salvarea articolelor direct din browser într-un click

### Pasul 3: Instalare Word Plugin
1. În Zotero desktop: Edit → Preferences → Cite → Word Processors
2. Click "Install Microsoft Word Plugin"
3. Restart Word
4. Ar trebui să apară tab "Zotero" în ribbon-ul Word

## 📚 Organizarea Bibliotecii

### Structură Colecții Recomandată:

```
My Library
├── Licenta_AI_Agentii (ROOT)
│   ├── 01_AI_General (general AI în advertising/PR)
│   ├── 02_Technology_Adoption (TAM, TOE, Rogers, etc.)
│   ├── 03_Skills_Competencies (future of work, reskilling)
│   ├── 04_ROI_Performance (metrici, măsurare impact)
│   ├── 05_Romania_EasternEurope (context specific)
│   ├── 06_Methodology (design cercetare, analiza date)
│   │
│   ├── TEMA1_Transformare_Procese
│   ├── TEMA2_Competente_Viitor
│   ├── TEMA3_ROI_Metrici
│   │
│   ├── High_Priority (citire urgentă)
│   ├── Cited_In_Thesis (folosite efectiv)
│   └── Background_Reading (context general)
```

### Cum să creezi colecții:
1. Click dreapta în panoul stâng "My Library"
2. "New Collection..."
3. Numește colecția
4. Drag & drop articole între colecții (același articol poate fi în multiple colecții)

## 🏷️ Taguri Recomandate

### Tags Tematice:
- `tema1`, `tema2`, `tema3`
- `comparative_study`, `romania`, `western_europe`
- `ai_adoption`, `barriers`, `benefits`
- `skills`, `reskilling`, `upskilling`
- `roi`, `efficiency`, `effectiveness`, `metrics`

### Tags Tip Document:
- `theoretical_framework`
- `empirical_study`
- `case_study`
- `methodology_guide`
- `meta_analysis`
- `book_chapter`

### Tags Status:
- `to_read`
- `read_partial`
- `read_complete`
- `cited_intro`
- `cited_litreview`
- `cited_methodology`

### Cum să adaugi tags:
1. Selectează articolul în Zotero
2. În panoul dreapta, secțiunea "Tags"
3. Click "Add" și scrie tag-ul
4. SAU: drag articolul peste tag-ul existent din tag selector (panoul jos-stânga)

## 💾 Import Articole

### Metoda 1: Browser Connector (CEL MAI RAPID)
1. Când ești pe pagina unui articol (Google Scholar, ResearchGate, journal website)
2. Click icon-ul Zotero din browser (sus-dreapta)
3. Alege colecția
4. Salvare automată cu metadate complete

### Metoda 2: DOI/ISBN Direct
1. În Zotero: Click icon-ul bagheta magică (toolbar)
2. Introduce DOI sau ISBN
3. Enter
4. Zotero descarcă automat metadata

### Metoda 3: PDF Drag & Drop
1. Drag PDF-ul direct în Zotero (în colecția dorită)
2. Click dreapta pe PDF → "Retrieve Metadata for PDF"
3. Zotero găsește automat informațiile articolului

### Metoda 4: Manual
1. Click "New Item" (icon +) → alege tipul (Article, Book, etc.)
2. Completează manual câmpurile în panoul dreapta

## 📄 Atașarea PDF-urilor

- Când salvezi cu Browser Connector, PDF-ul se atașează automat (dacă ai acces)
- Pentru articole fără acces direct:
  - Găsește PDF-ul pe Sci-Hub
  - Drag & drop peste item-ul din Zotero
  - SAU: Click dreapta pe item → "Add Attachment" → "Attach Stored Copy of File..."

## 📖 Citire și Notițe în Zotero

### Built-in PDF Reader (Zotero 6+):
1. Double-click pe PDF în Zotero
2. Se deschide reader-ul integrat
3. Poți face highlight, adăuga notes, tag-uri
4. Notes-urile se salvează automat cu item-ul

### Note-taking Workflow:
1. Selectează textul important în PDF
2. Click dreapta → "Add Note from Annotation"
3. SAU: Click "Add Note" (icon sticky note) și scrie manual
4. Notițele sunt searchable și apar în item

### Export Notes pentru Git:
- Notițele din Zotero rămân în Zotero
- Pentru notes mai detaliate (integrate cu git): creează markdown files în `bibliography/reading_notes/`
- Format: `Autor_An_TitluScurt.md`

## 📝 Citarea în Word

### Inserare Citări:
1. Poziționează cursorul unde vrei citarea
2. În Word: Tab Zotero → "Add/Edit Citation"
3. La prima utilizare: alege stilul de citare:
   - **APA 7th Edition** (recomandat pentru științe sociale)
   - **Chicago Manual of Style 17th**
4. Caută autorul/titlul în dialog
5. Enter
6. Citarea apare automat formatată

### Inserare Bibliografie:
1. Poziționează cursorul la sfârșitul documentului
2. Tab Zotero → "Add/Edit Bibliography"
3. Bibliografia se generează automat din toate citările

### Update Bibliografie:
- La fiecare citare nouă, bibliografia se update automat
- Dacă editezi ceva în Zotero (fix typo), click "Refresh" în Word

### Preferred Citation Styles:
- **APA 7th** - standard pentru științe sociale, comunicare
- **Chicago Author-Date** - alternativă validă

## 🔄 Backup și Sync

### Sync Cloud (Recomandat):
1. Preferences → Sync → Login cu contul Zotero
2. Check "Sync automatically"
3. Free: 300 MB storage (suficient pentru metadata + câteva PDF-uri)
4. Articolele se sincronizează între devices

### Backup Local:
1. Export regulat biblioteca: File → Export Library...
2. Format: **Zotero RDF** (include notițe, tags, etc.)
3. SAU: **BibTeX** (pentru compatibilitate git)
4. Salvează în `bibliography/zotero_library.bib`

### Backup în Git:
```bash
# Periodic export pentru tracking
cd bibliography
# Exportă din Zotero în BibTeX format
# File → Export Library → Better BibTeX → zotero_library.bib
git add zotero_library.bib
git commit -m "Update bibliography export"
```

## 🎯 Best Practices

### 1. Organizare Consistentă:
- Adaugă ÎNTOTDEAUNA tag-uri când salvezi un articol
- Plasează în colecția corectă
- Atașează PDF-ul dacă îl ai

### 2. Completitudine Metadata:
- Verifică că toate câmpurile sunt completate corect
- Fix typos în nume autori (Zotero e case-sensitive)
- Verifică anul, volumul, paginile

### 3. Reading Workflow:
- To Read → Mark cu tag `to_read`
- După citire → Remove `to_read`, add `read_complete`
- Dacă citat în thesis → Add tag `cited_intro` / `cited_litreview` etc.

### 4. Prevent Duplicates:
- Înainte de import, search în biblioteca ta
- Zotero detectează duplicates → Merge-uiește-le

### 5. Regular Export:
- Săptămânal: exportă în BibTeX pentru backup git
- Lunar: exportă backup complet RDF

## 🚨 Troubleshooting

### Problema: Word plugin nu apare
- Restart Word
- Reinstalează plugin din Zotero Preferences

### Problema: "Item not found" în Word
- Click "Refresh" în tab Zotero din Word
- Verifică că item-ul există în Zotero

### Problema: Bibliografie format greșit
- Edit → Preferences → Export → Default Format: schimbă în APA/Chicago
- În Word: click "Document Preferences" și schimbă stilul

### Problema: PDF-ul nu se deschide
- Verifică că PDF-ul e atașat (icon clip în Zotero)
- Click dreapta → Show File → verifică că există

## 📌 Resurse Suplimentare

- **Zotero Documentation**: https://www.zotero.org/support/
- **Zotero Forums**: https://forums.zotero.org/
- **Video Tutorials**: https://www.youtube.com/zotero
- **Better BibTeX Plugin** (advanced): https://retorque.re/zotero-better-bibtex/ (optional, pentru LaTeX users)

## ✅ Setup Checklist

- [ ] Zotero Desktop instalat
- [ ] Browser Connector instalat
- [ ] Word Plugin instalat și functional
- [ ] Cont Zotero creat (pentru sync)
- [ ] Structură de colecții creată (vezi mai sus)
- [ ] Tag-uri favorite adăugate în Tag Selector
- [ ] Citation style setat la APA 7th
- [ ] Primul articol adăugat (test)
- [ ] Prima citare în Word (test)
- [ ] Export backup în .bib (test)

---

**Data setup**: 2024-10-22
**Next review**: După primele 10 articole adăugate

