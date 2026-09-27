"""
Pre-loaded Demo Data and Baseline Historical Tickets from IIT Guwahati
For Granica × IIT Guwahati Hackathon: AI-Augmented Triage Layer (IPM).
"""

from typing import List, Dict, Any

DEMO_TICKETS: List[Dict[str, Any]] = [
    {
        "id": "TICKET-086103",
        "title": "Corridor Water Cooler Burst & Flooding",
        "tag": "Plumbing · High Severity",
        "hostel": "Umiam Hostel",
        "room": "2nd Floor Corridor (Near Rm 274)",
        "original_category": "Plumbing",
        "raw_text": "Room 274 ke paas ke water cooler ki pipe me leakage ho gya he , baar baar kuch beep beep noise ata rehta hai usse... Floor pe paani bhar raha hai jaldi koi bhej do!",
        "image_url": "/static/images/cooler_leak.jpg",
        "expected_output": {
            "ipm_validity": True,
            "corrected_department": "Plumbing",
            "technical_summary_english": "High-pressure potable water inlet PVC pipe ruptured beneath corridor water cooler unit. Active water leakage causing floor flooding with audible electronic filter/float sensor alarm triggered.",
            "technician_instructions_assamese": "ৰুম ২৭৪ ৰ ওচৰৰ ৱাটাৰ কুলাৰৰ তলৰ ফাটি যোৱা PVC পানীৰ পাইপ তৎকালীনভাৱে মেৰামতি কৰক আৰু বিপিং চেন্সৰ পৰীক্ষা কৰক। মজিয়াত পানী জমা হৈছে।",
            "predicted_tools_parts": [
                "1/2-inch Heavy Duty PVC Pipe Coupler",
                "CPVC Solvent Cement (100ml)",
                "Adjustable Pipe Wrench (12-inch)",
                "Water Cooler Float Sensor Probe & Teflon Tape"
            ],
            "interdependency_flag": None,
            "severity_score": 5,
            "chronic_issue_flag": False,
            "visual_evidence_detected": [
                "Transverse fracture in blue PVC water pipe",
                "Active pressurized water stream escaping",
                "Substantial puddle and floor slip hazard",
                "Commercial stainless steel water dispenser unit"
            ],
            "confidence_score": 0.98,
            "recommended_action": "EMERGENCY DISPATCH: Shut off main corridor valve immediately, dispatch plumber with PVC couplers and solvent cement."
        }
    },
    {
        "id": "TICKET-057088",
        "title": "LAN Cable Not Working (Misclassified to Electricity)",
        "tag": "Misclassification · Out of Scope",
        "hostel": "Kapili Hostel",
        "room": "Room 308, B-Block",
        "original_category": "Electricity",
        "raw_text": "Connecting laptop with lan shows no internet. Ethernet port yellow light blinking continuously, tried 3 different patch cables. Pls fix urgently I have online test tomorrow at 9 AM.",
        "image_url": "/static/images/lan_port.jpg",
        "expected_output": {
            "ipm_validity": False,
            "corrected_department": "Invalid (IT/Network) - Computer Center",
            "technical_summary_english": "End-user reports absence of LAN internet connectivity through hostel room RJ45 wall faceplate port. Physical link negotiation indicator active but network unreachable. Issue falls under Computer Center (CC) network infrastructure, not IPM civil/electrical maintenance.",
            "technician_instructions_assamese": "এইটো আই পি এম (IPM) ৰ অধিকাৰক্ষেত্ৰত নপৰে। এই অভিযোগটো আইটি/কম্পিউটাৰ চেণ্টাৰ (Computer Center) ৰ নেটৱৰ্ক বিভাগলৈ প্ৰেৰণ কৰা হৈছে।",
            "predicted_tools_parts": [
                "N/A - Diverted to Computer Center (CC) Network Desk",
                "Cat6 RJ45 Keyston Jack Punchdown (CC Team)",
                "Fluke Cable Continuity Tester (CC Team)"
            ],
            "interdependency_flag": "Route Out of IPM: Forwarded automatically to IIT Guwahati Computer Center (CC) Network Ticketing Portal.",
            "severity_score": 2,
            "chronic_issue_flag": False,
            "visual_evidence_detected": [
                "Laptop screen displaying 'No Internet Connection' alert",
                "Hostel Net Room 304 Port 1 wall faceplate",
                "Yellow Cat5e/Cat6 patch cable plugged into laptop port"
            ],
            "confidence_score": 0.99,
            "recommended_action": "AUTOMATIC RE-ROUTE: IPM rejected; Ticket auto-forwarded to Computer Center Network Ops with priority SLA."
        }
    },
    {
        "id": "TICKET-142046",
        "title": "Violently Shaking Fan (4th Repeated Complaint)",
        "tag": "Electricity · Chronic Hazard",
        "hostel": "Kameng Hostel",
        "room": "Room 119",
        "original_category": "Electricity",
        "raw_text": "My fan is creating very noise like it will come down and this is 4 th time when I am posting complaint! Every time technician comes and adds oil then leaves! It shakes violently on high speed and screws are loose!",
        "image_url": "/static/images/fan_issue.jpg",
        "expected_output": {
            "ipm_validity": True,
            "corrected_department": "Electricity",
            "technical_summary_english": "Severe mechanical instability and motor bearing failure in ceiling fan. Severe structural wobble and vibration posing detachment hazard. Historical record confirms 4th consecutive complaint without permanent remediation.",
            "technician_instructions_assamese": "পুৰণি ফেনখন সম্পূৰ্ণভাৱে খুলি নতুন ১২০০ মিমি চিলিং ফেন আৰু মজবুত ডাউনৰড ক্ল্যাম্প লগাওক (৪ৰ্থ বাৰৰ অভিযোগ, তেল দিয়াৰ সলনি ফেন সলনি কৰক)।",
            "predicted_tools_parts": [
                "Complete New 1200mm Heavy-Duty Ceiling Fan Unit",
                "Reinforced Downrod & Shackle Kit with Split Pin",
                "Insulated Heavy Screwdriver Set",
                "Step Ladder & Safety Harness"
            ],
            "interdependency_flag": None,
            "severity_score": 4,
            "chronic_issue_flag": True,
            "visual_evidence_detected": [
                "Deformed rusted downrod shank",
                "Exposed wiring junction at ceiling hook",
                "Visible paint peeling and motor housing distress",
                "Severe dynamic imbalance during rotation"
            ],
            "confidence_score": 0.97,
            "recommended_action": "ASSET REPLACEMENT PROTOCOL: Disallow temporary patching/lubrication. Dispatch electrician with full new ceiling fan replacement unit."
        }
    },
    {
        "id": "TICKET-141190",
        "title": "Crumbling Wall Cracks (Cross-Trade Dependency)",
        "tag": "Civil Works · Trade Dependency",
        "hostel": "Siang Hostel",
        "room": "Room 205",
        "original_category": "Carpentry",
        "raw_text": "There are some holes and deep cracks in the walls as in attached image. I want to fix my study bookshelf and curtain brackets but the masonry concrete is completely crumbling and falling out.",
        "image_url": "/static/images/wall_damage.jpg",
        "expected_output": {
            "ipm_validity": True,
            "corrected_department": "Other Civil Works",
            "technical_summary_english": "Structural brick masonry damage and plaster delamination around study area. Exposed brickwork and conduit cavity prevent mechanical anchoring for carpentry fixtures until structural mortar repair and curing are complete.",
            "technician_instructions_assamese": "প্ৰথমে চিভিল মিস্ত্ৰীয়ে বেৰৰ ফাট আৰু খহি পৰা ইটাৰ গাঁথনি চিমেণ্ট মৰ্টাৰেৰে মেৰামতি কৰক। শুকোৱাৰ পাছতহে কাঠমিস্ত্ৰীয়ে বুকশ্বেল্ফ আৰু পৰ্দাৰ ব্ৰেকেট লগাব।",
            "predicted_tools_parts": [
                "Quick-setting Portland Cement Mortar (10kg)",
                "Polymer Wall Putty & Bonding Primer",
                "Pointing & Plastering Trowel Set",
                "Wire Brush & Masonry Chisel"
            ],
            "interdependency_flag": "Civil Works Required BEFORE Carpentry: Masonry patching and curing (24h) must precede any bookshelf/curtain drilling by Carpentry team.",
            "severity_score": 3,
            "chronic_issue_flag": False,
            "visual_evidence_detected": [
                "Deep structural fissure exposing underlying red brick course",
                "Dislodged conduit wire casing near switchboard",
                "Loose concrete debris fallen onto floor and desk"
            ],
            "confidence_score": 0.96,
            "recommended_action": "SEQUENTIAL DISPATCH: Phase 1 Civil Masonry repairs today; Schedule Phase 2 Carpentry mounting 48 hours post-curing."
        }
    },
    {
        "id": "TICKET-105873",
        "title": "Broken Window Handle & Jammed Sash",
        "tag": "Carpentry · Weather Risk",
        "hostel": "Manas Hostel",
        "room": "Room 412, Block C",
        "original_category": "Carpentry",
        "raw_text": "Windows are not opening properly, jammed tight in monsoon and also there is no handle in the windows, rain water coming inside my room and wetting bedsheets.",
        "image_url": "/static/images/window_broken.jpg",
        "expected_output": {
            "ipm_validity": True,
            "corrected_department": "Carpentry",
            "technical_summary_english": "Missing window casement latch handle with sheared screw anchors. Wooden sash swollen from monsoon moisture causing frame binding and preventing watertight closure.",
            "technician_instructions_assamese": "খিৰিকীৰ হেণ্ডেল নতুনকৈ লগাওক, ফুলি উঠা কাঠৰ ফ্ৰেম ৰেন্দা মাৰি সমান কৰক যাতে বৰষুণৰ পানী সোমাব নোৱাৰে।",
            "predicted_tools_parts": [
                "Standard Heavy-Duty Aluminum Casement Window Handle",
                "M4.5 × 35mm Stainless Wood Screws & Rawl Plugs",
                "Manual Wood Smoothing Plane",
                "Silicone Waterproof Weatherstrip & Lubricant"
            ],
            "interdependency_flag": None,
            "severity_score": 3,
            "chronic_issue_flag": False,
            "visual_evidence_detected": [
                "Stripped screw socket holes on wooden casement stile",
                "Missing sash fastener/handle hardware",
                "Water ingress marks on window sill and frame"
            ],
            "confidence_score": 0.95,
            "recommended_action": "DISPATCH CARPENTER: Bring standard replacement latch handles, wood plane, and waterproof weatherseal."
        }
    },
    {
        "id": "TICKET-082936",
        "title": "Ceiling Fan Speed Defect (Capacitor Failure)",
        "tag": "Electricity · Single Visit Fix",
        "hostel": "Dihing Hostel",
        "room": "Room 114",
        "original_category": "Electricity",
        "raw_text": "Change Fan Condeser. Room fan is running on very slow speed even when regulator is set to 5. Humming noise coming from the fan motor.",
        "image_url": "/static/images/fan_issue.jpg",
        "expected_output": {
            "ipm_validity": True,
            "corrected_department": "Electricity",
            "technical_summary_english": "Single-phase induction motor run-capacitor degradation causing severe rpm drop and magnetic hum under normal supply voltage.",
            "technician_instructions_assamese": "ফেনৰ ২.৫ মাইক্ৰ'ফাৰাড কণ্ডেনচাৰ (Capacitor) সলনি কৰক আৰু ৰেগুলেটৰ স্পীড পৰীক্ষা কৰক।",
            "predicted_tools_parts": [
                "2.5 uF 440V AC Fan Run Capacitor",
                "Insulated Phillips & Flat Screwdrivers",
                "Wire Stripper & PVC Electrical Insulation Tape",
                "Digital Multimeter / Capacitance Tester"
            ],
            "interdependency_flag": None,
            "severity_score": 2,
            "chronic_issue_flag": False,
            "visual_evidence_detected": [
                "Standard 3-blade ceiling fan assembly",
                "Capacitor canister housing situated above motor shell"
            ],
            "confidence_score": 0.98,
            "recommended_action": "DISPATCH ELECTRICIAN: Carry 2.5uF capacitors directly to avoid return trip to electrical substation."
        }
    },
    {
        "id": "TICKET-088651",
        "title": "Bathroom Shower Tap + Tower Bolt Broken",
        "tag": "Plumbing · Multi-Trade Split",
        "hostel": "Barak Hostel",
        "room": "Wing B, Washroom BT-02 & BS-01",
        "original_category": "Plumbing",
        "raw_text": "Shower tap not working in B.NO-BT-02. Tower bolt lock need to be fixed in B.no- Bs-01. Door doesn't stay closed during bath.",
        "image_url": "/static/images/window_broken.jpg",
        "expected_output": {
            "ipm_validity": True,
            "corrected_department": "Plumbing",
            "technical_summary_english": "Dual-trade maintenance request logged under single ticket: 1) Leaking/stuck shower mixer valve in stall BT-02, and 2) Missing/broken brass tower bolt privacy latch on cubicle door BS-01.",
            "technician_instructions_assamese": "বাথৰুম বিটি-০২ ত শ্বাৱাৰৰ টেপ সলনি কৰক আৰু বিএছ-০১ ত দুৱাৰৰ টাৱাৰ ব'ল্ট তলা মেৰামতি কৰক (প্লাম্বাৰ আৰু কাঠমিস্ত্ৰী দুয়োৰে প্ৰয়োজন)।",
            "predicted_tools_parts": [
                "1/2-inch Heavy Chrome Shower Tap & Spindle",
                "6-inch Brass Tower Bolt with Keeper Plate",
                "1-inch Wood Mounting Screws & Cordless Drill",
                "PTFE Thread Seal Tape & Pipe Wrench"
            ],
            "interdependency_flag": "Split Ticket (Plumbing & Carpentry): Ticket requires dual assignment. Plumbing assigned for shower tap; Carpentry assigned for cubicle door bolt.",
            "severity_score": 3,
            "chronic_issue_flag": False,
            "visual_evidence_detected": [
                "Hostel shared sanitary washroom facilities",
                "Damaged fixture mounts and missing door hardware"
            ],
            "confidence_score": 0.94,
            "recommended_action": "SPLIT TICKET DISPATCH: Route primary ticket to Plumbing section, generate sub-work-order to Carpentry section."
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
