# PLAN DE CERCETARE DETALIAT - TEMA 3

## ROI și metrici de performanță: Evaluarea impactului implementării AI asupra eficienței și eficacității campaniilor în agențiile românești

**Data creării**: 2024-10-22
**Status**: Planning Phase

---

## 📋 REZUMAT EXECUTIV

### Titlu
**ROI și metrici de performanță: Evaluarea impactului implementării AI asupra eficienței și eficacității campaniilor în agențiile românești**

### Problema de Cercetare
Majoritatea cercetărilor despre AI în advertising se concentrează pe adopție și intențfurther (intent to use). Există un gap major în măsurarea impactului real al AI asupra performanței. Literatura abundă în date despre **eficiență** ("AI reduce timpul cu X%") dar e rară în **eficacitate** ("campaniile AI sunt mai performante?").

**Întrebarea centrală**: Care este impactul măsurabil al implementării AI asupra eficienței operaționale și eficacității campaniilor în agențiile românești?

### Obiective
1. Măsurarea impactului AI asupra eficienței (timp economisit, costuri, volum producție)
2. Măsurarea impactului asupra eficacității (performanța campaniilor: engagement, conversion, ROI client)
3. Compararea campaniilor AI-enhanced vs tradiționale
4. Calcularea ROI efectiv al investițiilor în AI tools
5. Identificarea condițiilor în care AI adaugă valoare măsurabilă

### Metodologie
**Design mixt paralel** (QUANT + QUAL simultaneous):
- **Analiza secundară date performanță**: 30-50 campanii (15-25 AI-enhanced vs 15-25 tradiționale) - metrici eficiență + eficacitate
- **Interviuri** cu 10-15 account managers + clienți (perceived value, satisfacție, ROI subiectiv)
- **Cost-Benefit Analysis**: Calculare ROI investiții AI (licențe, training, timp vs beneficii)

### Provocări Anticipate
- ⚠️ Acces la date proprietare (confidențialitate, competitivitate)
- ⚠️ Variabilitate metrici între agenții
- ⚠️ Multi confounding variables (buget campanie, brand strength, industrie, timing)

### Soluții
- NDA-uri cu agenții partenere
- Focus pe tendințe relative (nu valori absolute)
- Control statistic pentru confounders
- Case study approach dacă acces date limitat

---

## 🎯 ÎNTREBĂRI DE CERCETARE

### RQ1: Impactul asupra Eficienței Operaționale
Cum afectează AI eficiența proceselor de lucru în agenții?
- **RQ1a**: Timp economisit per campanie/task?
- **RQ1b**: Costuri reduse (sau crescute)?
- **RQ1c**: Volum producție crescut (# assets, variații)?

### RQ2: Impactul asupra Eficacității Campaniilor
Performează campaniile AI-enhanced mai bine decât cele tradiționale?
- **RQ2a**: Metrici engagement (CTR, engagement rate, shares, comments)
- **RQ2b**: Metrici conversion (leads, sales, ROI client)
- **RQ2c**: Metrici brand (awareness, sentiment, brand lift - dacă disponibile)

### RQ3: ROI Investiții în AI
Care este return-ul efectiv pe investiția în AI tools și training?
- **RQ3a**: Costuri totale (licențe, training, timp implementare)
- **RQ3b**: Beneficii cuantificabile (eficiență + eficacitate)
- **RQ3c**: Break-even point?

### RQ4: Condiții de Succes
În ce condiții AI adaugă cel mai mult valoare?
- **RQ4a**: Tipuri de campanii (awareness vs performance, B2B vs B2C)?
- **RQ4b**: Tipuri de task-uri (copywriting vs design vs analytics)?
- **RQ4c**: Mărimea agenției/buget?

### RQ5: Perceived Value
Cum percep account managers și clienții valoarea adusă de AI?
- Satisfacție, confidence în rezultate, willingness to pay premium

---

## 📚 CADRU TEORETIC

### Concepte Cheie

#### 1. Eficiență vs Eficacitate (Drucker)
- **Eficiență**: "Doing things right" - optimizare resurse, reduce waste, speed
- **Eficacitate**: "Doing the right things" - achieving objectives, rezultate dorite
- **AI Impact**: Poate crește eficiența (faster, cheaper) fără să crească eficacitatea (dacă output-ul e mediocru)

#### 2. ROI (Return on Investment)
**Formula**: ROI = (Beneficii - Costuri) / Costuri × 100%

**Pentru AI**:
- **Costuri**: Licențe tools (ChatGPT Plus, Midjourney, Jasper), training (ore × salariu), timp implementare, infrastructure
- **Beneficii**: Timp economisit (ore × cost/oră), creștere revenue (dacă campaigns perform better), client retention, competitive advantage

**Challenge**: Multe beneficii sunt intangibile/hard to quantify

#### 3. Marketing Performance Metrics
**Framework AIDA** (Awareness, Interest, Desire, Action):
- **Top-funnel (Awareness)**: Impressions, Reach, Brand awareness
- **Mid-funnel (Interest/Desire)**: Engagement rate, CTR, time spent, shares
- **Bottom-funnel (Action)**: Conversions, leads, sales, ROI client

**AI poate impacta diferit pe fiecare nivel**

#### 4. Attribution & Causality
**Challenge**: How do we attribute performance la AI vs alte factori?
- Campaign buget
- Brand strength
- Message quality (strategy, insights)
- Media placement
- Market conditions
- Timing

**Solution**: Comparative approach cu control pentru confounders

---

## 🔬 METODOLOGIE

### COMPONENTA 1: ANALIZA SECUNDARĂ DATE PERFORMANȚĂ

#### Corpus Campanii
**Target**: 30-50 campanii din ultimii 2 ani (2023-2024) din 3-5 agenții românești

**Categorizare**:
- **AI-Enhanced** (15-25): Campanii unde AI a fost folosit substanțial (ex: copy generat/rafinat cu ChatGPT, vizuale cu Midjourney/DALL-E, research cu AI tools)
- **Tradiționale** (15-25): Campanii făcute integral de oameni, fără AI

**Diversitate dorită**:
- Tipuri campanii: Awareness, Performance (lead gen, sales)
- Canale: Social media, Display, Search, Video, PR
- Industrii: FMCG, Auto, Tech, Finance, Retail
- Bugete: Mix (small <10k EUR, medium 10-50k, large 50k+)

#### Acces la Date - Strategie de Negociere

**Agenții țintă**:
- 2-3 agenții mari (rețele internaționale) cu date robuste
- 1-2 independente RO

**Pitch către agenții**:
1. **Value proposition**: Insights gratuite despre eficacitatea AI în propriile campanii (benchmark)
2. **Confidențialitate**: NDA semnat, anonimizare clienți/branduri (doar "Client A", "Industrie: Auto")
3. **Agregare**: Nu vom publica date individual-level, doar aggregate
4. **Acces coordinator**: Dacă coordonatorul are conexiuni, poate facilita introduceri

**Fall-back**: Dacă < 3 agenții colaborează → Pivot la **case study aprofundat** (1-2 agenții, 10-15 campanii, analiza calitativă detailed)

#### Metrici Colectate

**Metrici EFICIENȚĂ (operaționale)**:
| Metric | Definiție | Măsurare |
|--------|-----------|----------|
| **Timp producție** | Ore lucrate pe campanie | Timesheet data (dacă disponibil) SAU estimated by PM |
| **Cost producție** | Buget alocat intern (salariate ore) | Ore × avg hourly rate |
| **# Assets create** | Volum output (# vizuale, # copy variations, etc.) | Count |
| **Time-to-market** | Zile de la brief la launch | Date milestones |

**Metrici EFICACITATE (performanță campanie)**:
| Metric | Definiție | Măsurare |
|--------|-----------|----------|
| **Reach** | Unique users reached | Platform analytics |
| **Impressions** | Total views | Platform analytics |
| **Engagement Rate** | (Likes + Comments + Shares) / Reach × 100 | Calculated |
| **CTR** (Click-Through Rate) | Clicks / Impressions × 100 | Platform analytics (pentru ads) |
| **Conversion Rate** | Conversions / Clicks × 100 | Google Analytics sau platform |
| **Cost per Click (CPC)** | Total spent / Clicks | Platform analytics |
| **Cost per Acquisition (CPA)** | Total spent / Conversions | Calculated |
| **ROI Client** | (Revenue - Cost) / Cost × 100 | Dacă disponibil (rareori) |

**Metrici CALITATE (subjective - dacă date available)**:
- Awards/industry recognition?
- Client satisfaction score (dacă agenția măsoară)

#### Procedură Colectare

1. **Meeting cu agenții**: Prezentare proiect, NDA signing, alignment pe metrici
2. **Template Excel**: Creez template uniform pentru toate agențiile
3. **Data extraction**: Agenția populează template SAU dă acces direct la dashboards (preferabil)
4. **Verificare calitate date**: Missing values? Outliers? Consistency check
5. **Anonimizare**: Replace brand names cu codes (Client_A, Client_B)

#### Analiza Statistică

**Software**: SPSS, Excel (pentru basics), Python/R (dacă metrici complexe)

**Analize**:

1. **Descriptive Statistics**:
   - Mean, SD pentru toate metricile (AI vs Tradițional)
   - Visualizare: Box plots, bar charts comparații

2. **T-Tests (Independent Samples)**:
   - H0: Nu e diferență între AI-enhanced și tradiționale
   - H1: Există diferență semnificativă
   - Pentru fiecare metric: Engagement rate AI vs Tradițional, CPA AI vs Tradițional, etc.

3. **Control pentru Confounders (ANCOVA sau Regression)**:
   - **Problema**: Dacă AI campaigns au bugete mai mari → performance better, dar nu datorită AI, ci buget!
   - **Soluție**: Control statistic
   - **Model**: Performance = β0 + β1(AI_use) + β2(Budget) + β3(Industry) + β4(Channel) + ε
   - Check dacă AI_use coefficient e semnificativ după control

4. **Subgroup Analysis**:
   - Performance AI în awareness campaigns vs performance campaigns?
   - Social media vs Display vs Search?
   - FMCG vs Tech vs Finance?

5. **Effect Size** (Cohen's d):
   - Not just p < .05 (statistical significance), but practical significance
   - Cât de mare e diferența? (small, medium, large effect)

**Limitări Recognized**:
- Sample size probabil mic (N=30-50 campanii, nu 300+) → limited statistical power
- Multi confounders hard to control complet
- Selection bias (agențiile care colaborează poate folosesc AI mai bine)
- Data quality variability

**Soluție transparență**: Recognize limitations explicit, interpret findings cautiously, frame ca exploratory

---

### COMPONENTA 2: INTERVIURI ACCOUNT MANAGERS & CLIENȚI

#### Țintă
**Account Managers / Project Managers** (10-12) + **Clienți** (3-5 dacă posibil)

**Diversitate**:
- AM din agenții care au furnizat date (knowledge of specific campaigns)
- Mix: Lucrează pe AI campaigns vs tradiționale

#### Ghid Interviu Account Managers (12-14 Q, 35-40 min)

##### PARTE 1: Experiență cu AI în Campanii
**Q1**: Povestește-mi despre o campanie recentă unde ați folosit AI. Ce rol a jucat AI?

**Q2**: Cum compari procesul de lucru (workflow) pe campaniile AI vs tradiționale?
- *Probe*: Mai rapid? Mai ușor? Mai complicat?

**Q3**: Concret, cât timp estimezi că AI a economisit (sau a adăugat) în acea campanie?
- *Probe*: Ore/zile? Pe ce task-uri specific?

##### PARTE 2: Performanță & Rezultate
**Q4**: Cum au performat campaniile AI comparativ cu așteptările?
- *Probe*: Metrici konkrete (engagement, conversions)? Better, same, worse vs baseline?

**Q5**: Ai observat diferențe în calitatea output-ului (copy, vizuale) generat cu AI vs uman?
- *Probe*: Clienții pot distinge? Audience-ul?

**Q6**: Cum au reacționat clienții când ați folosit AI în campaniile lor?
- *Probe*: Enthusiasm, skepticism, neutralitate? Disclosure (ai spus că e AI)?

##### PARTE 3: Costuri & ROI
**Q7**: Din punctul tău de vedere, investiția în AI tools (licențe, training) se justifică prin rezultate?
- *Probe*: Break-even? Cât a durat să vezi ROI?

**Q8**: Care sunt costurile "ascunse" ale folosirii AI pe care nu le anticipați inițial?
- *Probe*: Timp de learning, prompt iterations, quality control?

##### PARTE 4: Condiții de Succes
**Q9**: Pentru ce tipuri de campanii/task-uri AI adaugă cel mai mult valoare?

**Q10**: În ce situații AI nu e potrivit sau chiar dăunează?

**Q11**: Ce factori determină dacă o campanie AI e success sau fail?
- *Probe*: Skillurile echipei? Quality of brief? Tipul de client?

##### PARTE 5: Viitor & Recomandări
**Q12**: Cum vezi evoluând metrici de performanță când AI devine standard?
- *Probe*: Bar-ul se ridică (because everyone uses AI)? New metrics needed?

**Q13**: Ce sfaturi ai pentru alte agenții care vor să măsoare ROI-ul AI?

##### Clienți (dacă acces) - Ghid Adaptat (8-10 Q, 25-30 min)

**Q1**: Știi că agenția ta folosește AI tools în campaniile tale? Cum te simți în legătură cu asta?

**Q2**: Ai observat diferențe în calitatea livrabilelor sau performanța campaniilor recent?

**Q3**: Cât de important e pentru tine ca agenția să folosească AI vs metode tradiționale?
- *Probe*: Value for money? Innovation perception?

**Q4**: Ai fi dispus să plătești un premium pentru campanii care folosesc AI avansat? (dacă da rezultate better)

**Q5**: Ce îți inspiră încredere (sau îngrijorare) când vine vorba de AI în advertising?

#### Analiza Interviuri
**Metoda**: Analiza tematică (nu Gioia rigid)
- Teme: Perceived efficiency gains, perceived quality, client reactions, ROI justification, conditions for success
- Triangulare cu datele cantitative: Perceived time saved (interview) vs actual time saved (data)
- Quote-uri reprezentative pentru findings

---

### COMPONENTA 3: COST-BENEFIT ANALYSIS (ROI Calculation)

#### Framework

**STEP 1: Identificare TOATE Costurile AI**

**Costuri Directe (one-time)**:
- Training inițial (ore angajați × cost/oră)
- Setup time (experimentation, learning curve)

**Costuri Recurente (monthly/annual)**:
- Licențe AI tools:
  - ChatGPT Plus: $20/user/month
  - Midjourney: $30-60/month
  - Jasper (copywriting): $49-125/month
  - Canva Pro (design cu AI): $13/user/month
  - Alte tools specific
- **Total licențe** pentru echipă: estimate pentru diverse mărimi agenții

**Costuri Indirecte (opportunity costs)**:
- Timp spending pe prompt iterations, quality control (ore × cost)
- Training continuu (staying updated)

**STEP 2: Identificare TOATE Beneficiile**

**Beneficii Eficiență** (time/cost savings):
- Timp economisit per campanie: Avg X ore (din date) × cost/oră
- Example: Dacă AI economisește 10 ore/campanie, și agenția face 50 campanii/an, și cost/oră = 50 EUR → 10×50×50 = 25,000 EUR/an saved

**Beneficii Eficacitate** (performance improvement):
- Dacă AI campaigns perform Y% better (ex: +15% engagement rate) → potential revenue increase
- Client retention: Dacă clienții sunt mai satisfăcuți → less churn (value of retained clients)
- Competitive advantage: Win new business (hard to quantify, but mention)

**Beneficii Intangibile**:
- Brand perception (innovative agency)
- Employee satisfaction (less boring tasks)

**STEP 3: Calculare ROI**

**Simplified Formula**:
ROI = [(Total Annual Benefits - Total Annual Costs) / Total Annual Costs] × 100%

**Example Calculation** (Agenție medie, 30 angajați):

**Costuri Anuale**:
- Licențe: 30 users × $30/month avg × 12 = $10,800 (≈ 10,000 EUR)
- Training inițial: 30 ore × 50 EUR = 1,500 EUR (one-time, amortizat year 1)
- **Total Year 1**: 11,500 EUR

**Beneficii Anuale**:
- Time saved: 50 campanii × 10 ore × 50 EUR/oră = 25,000 EUR
- Performance lift: +10% avg campaign ROI → estimate +5,000 EUR revenue increase
- **Total**: 30,000 EUR

**ROI** = (30,000 - 11,500) / 11,500 × 100% = **161% ROI**

**Breakeven**: Aproximativ 5 luni (11,500 / 2,500 per month)

**Sensitivity Analysis**:
- Best case (AI saves 15 ore/camp, +15% performance): ROI = 250%
- Worst case (AI saves 5 ore/camp, no performance lift): ROI = 62%
- Conservative estimate: 100-150% ROI

**Output**: Tabel ROI scenarios pentru diverse mărimi agenții (boutique, medie, large)

---

### INTEGRARE REZULTATE

**Triangulare**:
1. **Date cantitative** (campanii): "AI campaigns had 12% higher engagement rate (p<.05)"
2. **Interviuri (calitativ)**: "Account managers percep că AI campaigns sunt 'more engaging' dar nu dramatic different"
3. **Cost-benefit**: "Despite 12% performance lift, ROI is 150% datorită mainly time savings, not performance"

**Meta-Inference**:
- **Finding integrat**: "AI's primary value în agențiile RO e eficiență (time/cost savings) mai mult decât eficacitate (better campaign results). Performance lift e modest dar consistent."

---

## ✍️ STRUCTURA LUCRĂRII

### Introducere (3-5 pag)
- Gap: Lots of adoption research, little performance research
- Obiective: Măsurare impact real AI
- RQ1-RQ5

### Cap 1: Fundamentare Teoretică (12-15 pag)
**1.1. Eficiență vs Eficacitate în Advertising** (2 pag)
**1.2. Măsurarea Performanței Campaniilor** (3 pag)
- Marketing metrics frameworks (AIDA, etc.)
- Digital metrics (engagement, CTR, conversion)
**1.3. ROI & Cost-Benefit Analysis** (2 pag)
**1.4. AI Impact pe Creative Work & Advertising** (3 pag)
- Ce zice literatura despre AI impact (mostly anecdotal, not empirical)
**1.5. Lacune & Justificare** (2 pag)

### Cap 2: Metodologie (10-12 pag)
**2.1. Design paralel mixt** (2 pag)
**2.2. Analiza date campanii** (4 pag): Corpus, metrici, acces, procedură, analiza statistică (t-tests, ANCOVA)
**2.3. Interviuri AM/clienți** (3 pag): Eșantion, ghid, procedură, analiza tematică
**2.4. Cost-benefit analysis** (2 pag): Framework, calculare ROI
**2.5. Etică & limite** (1 pag)

### Cap 3: Rezultate (15-18 pag)

**3.1. Analiza Campanii - Eficiență** (3-4 pag)
- Descriptive stats: Timpul, costuri, volum
- Comparații AI vs Tradițional (t-tests)
- **Finding**: "AI reduced production time by avg 23% (p<.01)"

**3.2. Analiza Campanii - Eficacitate** (4-5 pag)
- Descriptive stats: Engagement, CTR, conversions, ROI client
- Comparații AI vs Tradițional (t-tests)
- Control pentru confounders (ANCOVA/regression)
- Subgroup analysis (tip campanie, canal, industrie)
- **Finding**: "AI campaigns showed 8-15% higher engagement, but conversion rates similar"

**3.3. Rezultate Interviuri** (3-4 pag)
- Perceived efficiency gains (confirm quant findings)
- Perceived quality & client reactions
- Conditions of success (teme)
- Quote-uri

**3.4. Cost-Benefit Analysis & ROI** (2-3 pag)
- Detailed calculation
- Scenarios (best, worst, realistic)
- Breakeven point
- **Finding**: "ROI ranges 100-200% primarily due to efficiency, not efficacy"

**3.5. Integrare (Triangulare)** (2 pag)
- Synthesis: Where quant + qual agree/diverge
- Holistic picture

### Cap 4: Discuție (6-8 pag)

**4.1. Răspunsuri la RQ** (3 pag)
- RQ1 (Efficiency): Clear gains
- RQ2 (Efficacy): Modest gains, nuanțe
- RQ3 (ROI): Positive, driven by efficiency
- RQ4 (Conditions): Task-dependent
- RQ5 (Perceived value): Generaly positive

**4.2. Implicații Teoretice** (1 pag)
- Efficiency vs efficacy distinction e crucial
- AI as productivity tool, not (yet) creative genius

**4.3. Implicații Practice** (2 pag)
- **Pentru agenții**: Justify AI investment based on time savings, not magic performance boost
- Focus AI pe task-uri high-volume, repetitive (where efficiency matters)
- Quality control remains critical (AI doesn't guarantee better results)

**4.4. Limite** (1 pag)
- Sample size, data access, confounders, selection bias

### Concluzii (5-6 pag)
- Rezumat findings
- Recomandări:
  - Track metrici eficiență AND eficacitate separate
  - Realistic expectations (AI e tool, not magic)
  - Continuous measurement & optimization
- Future research: Longitudinal tracking, experimental designs

### Bibliografie (25-30 surse)

### Anexe
- Tabel campanii analizate (anonymizat)
- Ghid interviuri AM & clienți
- Cost-benefit calculation template
- Consent forms, NDA template

---

## ⏱️ TIMELINE TEMA 3

**Noiembrie**: Contactare agenții pentru parteneriate date + Draft interviuri guide + Literatura ROI/metrics
**Decembrie**: Negociere NDA + Start colectare date campanii + Draft introducere
**Ianuarie**: Finalizare colectare date + Analiza preliminară + Recrutare interviuri
**Februarie**: Interviuri AM/clienți + Analiza statistică campanii (t-tests, ANCOVA)
**Martie**: Cost-benefit analysis + Integrare rezultate
**Aprilie**: Writing (rezultate + discuție + metodologie)
**Mai**: Finalizare

---

## 🎯 SUCCESS CRITERIA

**Minimum**:
- ✓ N >= 20 campanii analyzed (10 AI, 10 trad) - permite comparații basic
- ✓ Metrici eficiență pentru toate (time, cost)
- ✓ Metrici eficacitate pentru most (engagement, CTR - mai accesibile)
- ✓ N >= 8 interviuri AM
- ✓ Cost-benefit calculation realistic
- ✓ Findings moderate (recognize limitations)

**Excellent**:
- ✓ N >= 40 campanii (robust pentru ANCOVA cu confounders control)
- ✓ Metrici comprehensive (efficiency + full funnel efficacy)
- ✓ N = 12+ interviuri (AM + 3-5 clienți)
- ✓ ROI calculation pentru multiple scenarios (agenție sizes)
- ✓ Subgroup analysis revealing (ex: "AI works better pentru awareness than performance")
- ✓ Triangulare solidă quant + qual
- ✓ Practical tool: ROI calculator Excel template pentru alte agenții

---

## 📊 PROVOCĂRI SPECIFICE & STRATEGII

### Provocare 1: Acces la Date (HIGH RISK)
**Bariere**: Confidențialitate, competitivitate, data privacy

**Strategii Mitigation**:
1. **Strong NDA**: Legal protection pentru both parties
2. **Anonimizare riguroasă**: Nu public brand names, client names
3. **Value exchange**: Oferă insights gratuite (benchmark report) pentru agenții
4. **Coordinator leverage**: Request introduceri oficiale
5. **Start early**: Nov-Dec outreach (build trust takes time)
6. **Backup plan**: Dacă < 2 agenții → Pivot la case study deep-dive (1 agenție, multe campanii, rich qualitative)

### Provocare 2: Multi Confounders
**Problem**: Hard to attribute performance la AI când multi factori influențează (buget, brand, message, etc.)

**Strategies**:
1. **Statistical control**: ANCOVA/regression control pentru obvii confounders (buget, industrie)
2. **Matching**: Pair AI campaigns cu similar tradiționale (same brand, similar buget) - matched-pair design
3. **Transparență**: Recognize limitation, interpret cautiously, use language "associated with" not "caused by"
4. **Triangulate**: Use qual să understand nuances (interviews reveal contextual factors)

### Provocare 3: Data Quality & Availability
**Problem**: Not all metrics available pentru all campaigns

**Strategies**:
1. **Tier metrics**: Must-have (time, engagement) vs nice-to-have (ROI client - rareori disponibil)
2. **Flexible analysis**: Analyze ce e available, mention limitations pentru missing
3. **Estimated data**: Dacă hard data lipsă, use AM estimates (mark clearly as "estimated")

---

**Last Updated**: 2024-10-22
**Status**: Ready to Execute (HIGHEST risk due to data access, but highest potential impact if successful)

