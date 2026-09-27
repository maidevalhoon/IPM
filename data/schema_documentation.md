# IPM Maintenance Triage Dataset Schema & Documentation
**Granica × IIT Guwahati Hackathon · Physical AI Triage Layer**

## 1. Overview & Data Provenance
- **Domain**: Infrastructure Planning and Management (IPM), IIT Guwahati.
- **Problem**: Resolving maintenance tickets takes 2.4+ visits on average because raw student complaints are misclassified, lack tool requirements, and omit multi-trade interdependencies.
- **Collection Window**: 48-Hour Hackathon window (Interviews with hostel maintenance secretaries, student complaints across Brahmaputra, Kapili, Dihing, Umiam, Barak, Manas, Siang, Kameng hostels, and physical inspection).
- **Data Split**:
  - **Observed Data (Real)**: 100% of raw complaint texts, initial student categories, hostel/room coordinates, and photographic physical evidence.
  - **Inferred Data (AI-Augmented)**: Department correction, severity scores (1-5), tool/part predictions, Assamese translations, and interdependency sequencing generated via Gemini 2.0 / Multimodal AI pipeline.
  - **Synthetic Data**: 0% synthetic text. All cases represent real IIT Guwahati campus infrastructure failure patterns.

---

## 2. Dataset Schema Description

| Column Name | Type | Description | Observed vs Inferred |
| :--- | :--- | :--- | :--- |
| `ticket_id` | String | Unique campus complaint identifier (e.g., `TICKET-086103`) | Observed |
| `hostel` | String | IIT Guwahati hostel residence (e.g., `Umiam Hostel`, `Kapili Hostel`) | Observed |
| `room_location` | String | Specific room number, wing, or corridor block | Observed |
| `student_original_category` | String | Unfiltered category selected by student on portal | Observed |
| `raw_student_text` | String | Raw conversational/multilingual complaint submitted by student | Observed |
| `has_photo_evidence` | Boolean | True if visual evidence image was attached | Observed |
| `ipm_validity` | Boolean | `False` if IT/Network issue (divert to Computer Center); `True` for IPM | **Inferred (AI)** |
| `corrected_department` | String | Standard IPM department (`Electricity`, `Plumbing`, `Carpentry`, `Sanitary`, `Other Civil Works`) | **Inferred (AI)** |
| `severity_score` | Integer (1-5) | Urgency rating: 5 (active flooding/hazards) down to 1 (minor cosmetic) | **Inferred (AI)** |
| `chronic_issue_flag` | Boolean | True if repeated failure detected (triggers complete asset replacement) | **Inferred (AI)** |
| `interdependency_flag` | String / Null | Cross-trade sequencing directive (e.g., Civil works before Carpentry) | **Inferred (AI)** |
| `predicted_tools_parts` | JSON Array | Exact hardware, parts, and tools required for single-visit repair | **Inferred (AI)** |
| `technical_summary_english` | String | Concise professional translation into maintenance engineering terminology | **Inferred (AI)** |
| `technician_instructions_assamese` | String (অসমীয়া) | Frontline work directive translated directly to Assamese for local technicians | **Inferred (AI)** |
| `confidence_score` | Float | AI triage model confidence rating (0.0 to 1.0) | **Inferred (AI)** |
| `recommended_action` | String | Actionable dispatch decision for IPM dispatcher desk | **Inferred (AI)** |

---

## 3. Storage Formats
- **Parquet Format**: `data/ipm_triaged_tickets.parquet` (compressed columnar storage for high efficiency analytics).
- **CSV Format**: `data/ipm_triaged_tickets.csv` (human-readable standard comma-separated format).
