"""
Independent Gemini-Augmented Examples and Demo Scenarios
Granica × IIT Guwahati Hackathon: AI-Augmented Triage Layer (IPM).
Strictly monochrome, Gemini multimodal outputs, and reduced to 2 wall, 2 lamp, and 2 non-IPM scenarios.
"""

from typing import List, Dict, Any

DEMO_TICKETS: List[Dict[str, Any]] = [
    # ----------------------------------------------------
    # IMAGE 1: static/images/image.png (Wall Graffiti / Peeling Plaster) - 2 SCENARIOS
    # ----------------------------------------------------
    {
        "id": "TICKET-WALL-01",
        "title": "Wall: 'paint the wall' (Misclassified to Carpentry)",
        "tag": "Wall Image · Carpentry -> Other Civil Works",
        "hostel": "Umiam Hostel",
        "room": "Room 102",
        "original_category": "Carpentry",
        "raw_text": "paint the wall",
        "image_url": "/static/images/image.png",
        "expected_output": {
            "ipm_validity": True,
            "corrected_department": "Other Civil Works",
            "technical_summary_english": "The student requested wall painting. Visual evidence shows ink graffiti on the wall along with a small hole/damaged plaster in the center. The wall requires plaster patching/putty filling followed by a fresh coat of paint to cover the graffiti and repair the surface damage.",
            "technician_instructions_assamese": "উমিয়াম হোষ্টেলৰ ১০২ নম্বৰ কোঠাৰ দেৱালখনত চিয়াঁহীৰ দাগ আৰু এটা সৰু ফুটা আছে। প্ৰথমে ফুটাটো পুটি (putty) বা প্লাষ্টাৰেৰে বন্ধ কৰক আৰু তাৰ পিছত দেৱালখনত নতুনকৈ ৰং কৰক। প্ৰয়োজনীয় সামগ্ৰী: দেৱালৰ পুটি, ৰং, ব্ৰাছ, আৰু চেণ্ডপেপাৰ।",
            "predicted_tools_parts": [
                "Wall putty",
                "White paint",
                "Paint brush",
                "Sandpaper",
                "Putty knife"
            ],
            "interdependency_flag": None,
            "severity_score": 1,
            "chronic_issue_flag": False,
            "visual_evidence_detected": [
                "ink graffiti on wall",
                "small hole in plaster",
                "scratched wall surface"
            ],
            "confidence_score": 0.95,
            "recommended_action": "Scheduled Repair"
        }
    },
    {
        "id": "TICKET-WALL-02",
        "title": "Wall: 'plaster chipping off and graffiti on wall'",
        "tag": "Wall Image · Plaster & Surface Prep",
        "hostel": "Umiam Hostel",
        "room": "Room 102",
        "original_category": "Other Civil Works",
        "raw_text": "plaster chipping off and graffiti on wall",
        "image_url": "/static/images/image.png",
        "expected_output": {
            "ipm_validity": True,
            "corrected_department": "Other Civil Works",
            "technical_summary_english": "The wall plaster is chipped, creating a small hole/indentation, and there is ink graffiti on the wall surface. Requires plaster patching, sanding, and repainting to restore the wall finish.",
            "technician_instructions_assamese": "উমিয়াম হোষ্টেলৰ ১০২ নম্বৰ কোঠাৰ দেৱালৰ প্লাষ্টাৰ খহি যোৱা অংশটো পুটি আৰু চিমেণ্টেৰে মেৰামতি কৰক। দেৱালত থকা চিয়াহীৰ দাগবোৰ আঁতৰাই নতুনকৈ ৰং কৰিব লাগিব। প্ৰয়োজনীয় সামগ্ৰী: ৱাল পুটি, বগা চিমেণ্ট, ৰং, ব্ৰাছ আৰু ছেণ্ডপেপাৰ।",
            "predicted_tools_parts": [
                "Wall putty",
                "White cement",
                "Sandpaper",
                "Paint brush",
                "Wall paint",
                "Scraper"
            ],
            "interdependency_flag": None,
            "severity_score": 2,
            "chronic_issue_flag": False,
            "visual_evidence_detected": [
                "chipped wall plaster hole",
                "ink graffiti markings",
                "damaged wall surface"
            ],
            "confidence_score": 0.96,
            "recommended_action": "Scheduled Repair"
        }
    },

    # ----------------------------------------------------
    # IMAGE 2: static/images/decon_study_lamp.jpeg - 1 SCENARIO
    # ----------------------------------------------------
    {
        "id": "TICKET-LAMP-01",
        "title": "Lamp: 'broken thing.' (Misclassified to Plumbing)",
        "tag": "Lamp Image · 2-Phase Breakdown (Civil Gap Fill -> Electrical)",
        "hostel": "Lohit Hostel",
        "room": "A233",
        "original_category": "Plumbing",
        "raw_text": "broken thing.",
        "image_url": "/static/images/decon_study_lamp.jpeg",
        "expected_output": {
            "ipm_validity": True,
            "corrected_department": "Electricity",
            "technical_summary_english": "Visual analysis confirms wall-mounted study lamp detached from electrical junction box in Lohit Hostel, Room A233, and suspended precariously on live electrical wiring. The wall mounting cavity is stripped and fractured. Requires 2-Phase Sequential Repair: Phase 1 Civil Works to fill and patch the crumbling wall gap/hole with polymer putty/mortar and allow to set, followed by Phase 2 Electrical Works to drill fresh anchor holes, secure the baseplate with wall plugs and screws, and verify circuit integrity.",
            "technician_instructions_assamese": "লোহিত হোষ্টেলৰ A233 নম্বৰ কোঠাত ২টা পৰ্যায়ৰ কাম (2-Phase Work): প্ৰথম পৰ্যায়ত চিভিল মিস্ত্ৰীয়ে দেৱালৰ খহি পৰা ফাঁক আৰু ফুটাটো ৱাল পুটি/চিমেণ্টেৰে ভৰাই সমান কৰক। শুকোৱাৰ পাছত দ্বিতীয় পৰ্যায়ত বিজুলী মিস্ত্ৰীয়ে নতুন ৱাল প্লাগ (গিট্টি) আৰু স্ক্ৰু লগাই লেম্পটো মজবুতকৈ স্থাপন কৰক আৰু টেষ্টাৰেৰে বিজুলী পৰীক্ষা কৰক।",
            "predicted_tools_parts": [
                "Phase 1 (Civil): Quick-Setting Wall Putty & White Cement (2kg)",
                "Phase 1 (Civil): Steel Putty Knife & Surface Scraper",
                "Phase 2 (Electrical): 6mm Nylon Wall Anchor Plugs (Gitti)",
                "Phase 2 (Electrical): 1.5-inch Self-Tapping Screws (M4)",
                "Phase 2 (Electrical): Insulated Line Phase Tester & Screwdriver Set",
                "Phase 2 (Electrical): Cordless Drill with 6mm Masonry Bit",
                "Phase 2 (Electrical): PVC Electrical Insulation Tape"
            ],
            "interdependency_flag": "2-Phase Trade Interdependency: Phase 1 Civil Works required to fill and patch the crumbling wall gap before Phase 2 Electrical remounting and wiring termination.",
            "severity_score": 4,
            "chronic_issue_flag": False,
            "visual_evidence_detected": [
                "detached wall study lamp",
                "hanging exposed electrical wiring",
                "damaged crumbling plaster cavity around mounting hole"
            ],
            "confidence_score": 0.98,
            "recommended_action": "2-PHASE DISPATCH: Phase 1 Civil gap filling and plaster patching first; Phase 2 Electrical remounting post-setting."
        }
    },

    # ----------------------------------------------------
    # NON-IPM COMPLAINTS (NO IMAGE) - 2 SCENARIOS
    # ----------------------------------------------------
    {
        "id": "TICKET-NON-IPM-LAN",
        "title": "LAN Outage: 'Connecting laptop with lan shows no internet'",
        "tag": "Non-IPM · CCC Portal Redirect",
        "hostel": "Kapili Hostel",
        "room": "Room 308",
        "original_category": "Electricity",
        "raw_text": "Connecting laptop with lan shows no internet",
        "image_url": None,
        "expected_output": {
            "ipm_validity": False,
            "corrected_department": "Invalid (IT/Network) - Computer & Communication Centre (CCC)",
            "technical_summary_english": "Not IPM section part. The user is reporting a network connectivity issue where connecting a laptop via LAN does not provide internet access. This is an IT/Network infrastructure issue, not a physical infrastructure (IPM) issue. Submit in CCC complaint portal.",
            "technician_instructions_assamese": "এইটো আই.পি.এম. (IPM) বিভাগৰ কাম নহয়। অনুগ্ৰহ কৰি এই অভিযোগটো চি.চি.চি. (CCC) পৰ্টেলত দাখিল কৰক।",
            "predicted_tools_parts": [
                "N/A - Submit in CCC complaint portal"
            ],
            "interdependency_flag": "Out of IPM Scope: Submit in CCC complaint portal (Computer & Communication Centre).",
            "severity_score": 1,
            "chronic_issue_flag": False,
            "visual_evidence_detected": [],
            "confidence_score": 0.99,
            "recommended_action": "Not IPM section part. Submit in CCC complaint portal."
        }
    },
    {
        "id": "TICKET-NON-IPM-FURN",
        "title": "Missing Furniture: 'no table and chair in my hostel room'",
        "tag": "Non-IPM · Hostel Office Redirect",
        "hostel": "Disang Hostel",
        "room": "Room 105",
        "original_category": "Carpentry",
        "raw_text": "no table and chair in my hostel room",
        "image_url": None,
        "expected_output": {
            "ipm_validity": False,
            "corrected_department": "Invalid (Hostel Administration) - Hostel Office",
            "technical_summary_english": "Not IPM section part. The student is reporting missing room furniture (table and chair) in Disang Hostel, Room 105. This is an administrative/hostel inventory issue, not a physical maintenance or carpentry repair task under IPM. Submit in hostel office.",
            "technician_instructions_assamese": "এইটো আই.পি.এম. (IPM) বিভাগৰ কাম নহয়। অনুগ্ৰহ কৰি হোষ্টেল কাৰ্যালয়ত যোগাযোগ কৰক।",
            "predicted_tools_parts": [
                "N/A - Submit in hostel office"
            ],
            "interdependency_flag": "Out of IPM Scope: Submit in hostel office (Caretaker / Warden / HAB Office).",
            "severity_score": 1,
            "chronic_issue_flag": False,
            "visual_evidence_detected": [],
            "confidence_score": 0.99,
            "recommended_action": "Not IPM section part. Submit in hostel office."
        }
    }
]

def get_demo_by_id(ticket_id: str) -> Dict[str, Any]:
    for ticket in DEMO_TICKETS:
        if ticket["id"] == ticket_id:
            return ticket
    return DEMO_TICKETS[0]

def get_all_demos() -> List[Dict[str, Any]]:
    return DEMO_TICKETS
