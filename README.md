# Week 03 - Python Assessment
### PG Diploma · AI-ML & Agentic AI Engineering · IIT Gandhinagar

## Structure

```
week03-assessment/
├── section1_mcqs/
│   └── mcq_answers.py        # All 33 MCQ answers with reasoning
└── section2_coding/
    ├── q1_ola_rides.py        # Ride duration stats - loops, bubble sort, IQR
    ├── q2_byjus_passrate.py   # Pass/fail rate calculator
    ├── q3_zepto_categories.py # Category order counter - manual unique list + sort
    ├── q4_nykaa_deviation.py  # Mean and absolute deviation without abs()
    ├── q5_meesho_stats.py     # Mean, median, mode from scratch
    └── q6_flipkart_qc.py      # Batch QC with z-score flagging, Newton-Raphson sqrt
```

## How to Run

Each coding file reads from standard input. Example:

```bash
python q1_ola_rides.py
# then type inputs as prompted
```

Or pipe directly:
```bash
echo "5
32 18 45 27 38" | python q1_ola_rides.py
```

## Key Constraints Followed
- No built-in functions like sum(), min(), max(), sorted(), abs() where restricted
- Bubble Sort used wherever sorting was needed
- Newton-Raphson method used for square root in Q6
- No NumPy, Pandas, statistics, or math imports (except where explicitly allowed)
