# Nordex-Shift-Performance-Optimization

NorDex Manufacturing AS runs three shifts around the clock across three production plants in Bergen, Norway. Morning shift consistently hits its targets. Evening and Night shifts keep falling behind — despite using the same machines, the same processes, and similar headcounts.
This project digs into 296,334 operational records across Q1 2024 to find out exactly why, and builds a predictive model that helps managers get ahead of the problem before it costs production time.

 About NorDex

NorDex Manufacturing AS is a Bergen-based precision parts manufacturer founded in 1998, employing approximately 1,000 people across three automated production plants and generating over €120 million in annual revenue serving the automotive and industrial equipment sectors across Northern Europe.

Despite running the same machines, processes, and staffing levels across all three shifts, Morning shift consistently outperforms Evening and Night, producing 847 units per hour at 90.87% efficiency while Night shift manages just 485 units at 61.16% efficiency with 98.9% of its machines flagged with issues. OEE dropped from 75% in January to 69% in February and never recovered across Q1 2024.

 What I Found
Three root causes explain almost everything:
1. Operator experience is concentrated on the Morning shift
88% of Senior and Expert operators work Morning shift. Night shift runs with zero Senior or Expert coverage and is 53% Junior staff. The correlation between experience level and shift efficiency is 0.69 — moderate to strong and very consistent.
2. Machines degrade across the day with no intervention
Morning shift starts with 96.5% of machines operational. By Night shift, 98.9% of machines have flagged issues. Average downtime jumps from 29 minutes on Morning to 68 minutes on Night — a 2.3x difference that directly suppresses Night shift output. Downtime correlates with efficiency at -0.85, the strongest single predictor in the dataset.
3. Maintenance is reactive, not predictive
All 1,897 maintenance events are logged on the Morning shift, meaning issues discovered overnight are only addressed the next morning. The Night shift absorbs the full cost of machine degradation with no intra-day intervention.

OEE Analysis
OEE = Availability × Performance × Quality
ComponentMorningNightAvailability0.9640.882Performance1.0000.652 – 0.740Quality0.9780.955 – 0.962OEE0.9430.549 – 0.628
Quality is consistently high across both shifts at 0.96+. The OEE loss on Night shift is driven entirely by availability and performance — not defects. This points directly to operator experience and machine health as the root causes.


Features used for modelling:
experience_level, maintenance_flag, shift_duration, defect_rate, downtime_ratio, day_of_week, hour_of_day, shift_name, skill_category, machine_status, issue_type, defect_type, severity
Features removed (leakage or redundant):
units_produced (r = 0.93 with target), inspection_result, defect_count, downtime_minutes, runtime_hours, temperature, humidity, cycle_time_avg, and all raw identifiers

Dataset
Source: ShiftData.db — SQLite database integrating 7 operational domains
DomainKey FeaturesShift Mastershift_id, shift_name, supervisor_idOperator Assignmentexperience_level, skill_categoryMachine Logruntime_hours, downtime_minutes, machine_statusProduction Logunits_produced, defect_count, shift_efficiency_scoreMaintenance Recordsissue_type, maintenance_downtimeQuality Controldefect_type, severity, inspection_resultEnvironmental Datatemperature, humidity

Raw table: 296,334 rows (inflated by 1:many QC join)
Analytical grain: 13,650 unique production events
Date range: Q1 2024 — 1 January to 31 March


Getting Started
bash# Clone the repository
git clone https://github.com/ogunlademodupeola/Nordex-Shift-Performance-Optimization.git
cd Nordex-Shift-Performance-Optimization

# Install dependencies
pip install -r requirements.txt

# Launch the notebook
jupyter notebook notebooks/EDA.ipynb

# View MLflow experiment logs
mlflow ui

📁 Project Structure
Nordex-Shift-Performance-Optimization/
│
├── notebooks/
│   └── EDA.ipynb              ← Full analysis, EDA, OEE, and modelling
│
├── ShiftData.db               ← Source SQLite database (gitignored)
├── requirements.txt           ← Python dependencies
├── .gitignore
└── README.md

💡 Key Recommendations

Rebalance operator experience across shifts — move some Senior and Expert operators to Evening and Night shifts. This is the single highest-leverage action available.
Introduce intra-day predictive maintenance — a machine health check at every shift handover would interrupt the degradation cycle before Night shift absorbs it.
Replace weekly reports with shift-level dashboards — by the time a weekly report shows a problem, it has been compounding for days.

