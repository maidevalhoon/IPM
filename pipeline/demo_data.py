"""
Pre-loaded Demo Data and Baseline Historical Tickets from IIT Guwahati
For Granica × IIT Guwahati Hackathon: AI-Augmented Triage Layer (IPM).
Includes multimodal test cases using real physical photographic evidence.
"""

from typing import List, Dict, Any

DEMO_TICKETS: List[Dict[str, Any]] = [
    {
        "id": "TICKET-LOHIT-A233",
        "title": "Unhinged Wall Lamp (Vague 'broken thing.')",
        "tag": "Image-First · Misclassified to Plumbing",
        "hostel": "Lohit Hostel",
        "room": "A233",
        "original_category": "Plumbing",
        "raw_text": "broken thing.",
        "image_url": "/static/images/decon_study_lamp.jpeg",
        "expected_output": {
            "ipm_validity": True,
            "corrected_department": "Electricity",
            "technical_summary_english": "Visual analysis detects wall-mounted adjustable DECON study lamp fixture mechanically unhinged and detached from the circular conduit junction box. Fixture is suspended in mid-air supported solely by exposed electrical conductors (phase, neutral, earth), creating an active risk of electrical short-circuit and conductor shearing in Lohit Hostel, Room A233.",
            "technician_instructions_assamese": "লোহিত হোষ্টেলৰ A233 নম্বৰ ৰুমত: বেৰৰ পৰা ওলমি থকা DECON ষ্টাডি লেম্পটো খুলি নতুন ৱাল প্লাগ (গিট্টি) আৰু স্ক্ৰু লগাই মজবুতকৈ ফিক্স কৰক। ওলমি থকা ওৱাৰিং পৰীক্ষা কৰি টেপিং কৰক যাতে শ্বৰ্ট চাৰ্কিট নহয়।",
            "predicted_tools_parts": [
                "Insulated Screwdriver Set (1000V Rated)",
                "Neon Line Phase Tester",
                "6mm Nylon Wall Anchor Plugs (Gitti)",
                "1.5-inch Self-Tapping Screws (M4)",
                "Cordless Drill with 6mm Masonry Bit",
                "PVC Electrical Insulation Tape"
            ],
            "interdependency_flag": None,
            "severity_score": 4,
            "chronic_issue_flag": False,
            "visual_evidence_detected": [
                "DECON wall-mounted adjustable study spotlight",
                "Mechanically detached circular mounting base",
                "Suspended by 3 exposed electrical wires (Phase/Neutral/Earth)",
                "Stripped screw anchor holes on wall plaster"
            ],
            "confidence_score": 0.98,
            "recommended_action": "PRIORITY ELECTRICAL DISPATCH: Reclassify from Plumbing to Electricity; technician must carry 6mm wall plugs, drill, and insulated toolset."
        }
    },
    {
        "id": "TICKET-LOHIT-ELEC",
        "title": "Hanging on Live Wires (Shock Hazard)",
        "tag": "Electricity · Wire Tension Hazard",
        "hostel": "Lohit Hostel",
        "room": "A233",
        "original_category": "Electricity",
        "raw_text": "Bhai study table ke upar wall lamp pura nikal gaya hai aur taar pe latak raha hai! Sparks aa sakte hain ya current lag sakta hai, please electrician ko jaldi bhejo study table use nahi kar pa raha.",
        "image_url": "/static/images/decon_study_lamp.jpeg",
        "expected_output": {
            "ipm_validity": True,
            "corrected_department": "Electricity",
            "technical_summary_english": "Mechanical dislodgement of wall-mounted task spotlight above student study desk. Tensile stress applied directly onto 230V internal wiring junction with exposed conductor terminations. Immediate risk of arc flash, insulation tearing, or accidental contact shock during room occupancy.",
            "technician_instructions_assamese": "লোহিত হোষ্টেলৰ A233 নম্বৰ ৰুমত: পঢ়া টেবুলৰ ওপৰত বেৰৰ পৰা ওলমি থকা লেম্পটো বিজুলী সংযোগ বন্ধ কৰি নতুনকৈ মজবুতকৈ ফিক্স কৰক। তাঁৰবোৰ পৰীক্ষা কৰি টেপিং কৰক যাতে কাৰেণ্ট নালাগে।",
            "predicted_tools_parts": [
                "Digital Multimeter / Voltage Detector",
                "Insulated Electrician Plier & Screwdrivers",
                "6mm Heavy-Duty Rawl Plugs",
                "Twist-On Wire Connectors / Terminal Block",
                "1.5-inch Steel Mounting Screws"
            ],
            "interdependency_flag": None,
            "severity_score": 4,
            "chronic_issue_flag": False,
            "visual_evidence_detected": [
                "Exposed wiring harness under dynamic tension",
                "Open circular conduit hole in wall",
                "Unfastened mounting baseplate dangling"
            ],
            "confidence_score": 0.97,
            "recommended_action": "EXPEDITED DISPATCH: Isolate room lighting circuit, re-terminate wiring inside junction box, and anchor baseplate."
        }
    },
    {
        "id": "TICKET-LOHIT-CARP",
        "title": "Screws Stripped Out (Logged as Carpentry)",
        "tag": "Misclassification · Carpentry to Electricity",
        "hostel": "Lohit Hostel",
        "room": "A233",
        "original_category": "Carpentry",
        "raw_text": "Wall bracket and lamp came out while adjusting light angle, screws fell down and hole in plaster got bigger. Need carpenter with drill machine to tighten it.",
        "image_url": "/static/images/decon_study_lamp.jpeg",
        "expected_output": {
            "ipm_validity": True,
            "corrected_department": "Electricity",
            "technical_summary_english": "Student misclassified as Carpentry due to stripped wall anchor screws. Visual inspection confirms asset is a mains-powered DECON electrical wall luminaire connected to electrical conduit. Reassigned to Electricity section; technician must carry masonry drill and wall anchor plugs.",
            "technician_instructions_assamese": "লোহিত হোষ্টেলৰ A233 নম্বৰ ৰুমত: কাঠমিস্ত্ৰীৰ পৰিৱৰ্তে বিজুলী মিস্ত্ৰীয়ে ড্ৰিল মেচিন আৰু নতুন গিট্টি লৈ আহি ওলমি থকা লেম্পটো বেৰত মজবুতকৈ লগাই দিয়ক।",
            "predicted_tools_parts": [
                "Impact Drill with 6mm Masonry Drill Bit",
                "6mm Plastic Rawl Plugs (Gitti)",
                "Pan-Head Sheet Metal Screws 1.5-inch",
                "Insulated Phase Tester & Wire Stripper"
            ],
            "interdependency_flag": None,
            "severity_score": 3,
            "chronic_issue_flag": False,
            "visual_evidence_detected": [
                "Stripped screw sockets in concrete wall",
                "Lamp base detached during swivel adjustment",
                "Live electrical wiring exposed"
            ],
            "confidence_score": 0.96,
            "recommended_action": "RECLASSIFY TO ELECTRICITY: Do not dispatch carpenter; send electrician equipped with hammer drill and anchor plugs."
        }
    },
    {
        "id": "TICKET-LOHIT-CHRONIC",
        "title": "Wall Lamp Fell Again (3rd Time / Chronic Failure)",
        "tag": "Chronic Issue · Civil Interdependency",
        "hostel": "Lohit Hostel",
        "room": "A233",
        "original_category": "Electricity",
        "raw_text": "This is 3rd time posting complaint! The study lamp fell off the wall again after technician just tightened it last week. The plaster inside the hole is completely crumbled, loose screws cannot hold it anymore.",
        "image_url": "/static/images/decon_study_lamp.jpeg",
        "expected_output": {
            "ipm_validity": True,
            "corrected_department": "Electricity",
            "technical_summary_english": "Recurrent mechanical detachment of wall study lamp (3rd recorded instance). Concrete masonry substrate around circular electrical box has crumbled, causing screw pull-out. Requires civil epoxy/wall putty anchoring before electrical remounting.",
            "technician_instructions_assamese": "লোহিত হোষ্টেলৰ A233 ত ৩য় বাৰৰ অভিযোগ: বেৰৰ প্লাষ্টাৰ খহি পৰাৰ বাবে লেম্পৰ স্ক্ৰু ঢিলা হৈছে। প্ৰথমে চিমেণ্ট পুট্টিৰে গাঁতটো ভৰাই নতুন হেভী প্লাগ লগাই লেম্পটো স্থায়ীভাৱে ফিক্স কৰক।",
            "predicted_tools_parts": [
                "Heavy-Duty Chemical / Expansion Wall Anchors",
                "Quick-Setting Wall Putty / Plaster Patch Compound",
                "Hammer Drill & 6mm Bit",
                "Replacement DECON Luminaire Baseplate",
                "Line Tester & Insulation Tape"
            ],
            "interdependency_flag": "Civil Works Required BEFORE Electrical Remounting: Crumbling masonry cavity must be reinforced with filler before drilling fresh expansion anchors.",
            "severity_score": 4,
            "chronic_issue_flag": True,
            "visual_evidence_detected": [
                "Severe plaster cavity wear around junction box",
                "Chipped masonry edges with loose debris",
                "Exposed wiring hanging with repeated fatigue"
            ],
            "confidence_score": 0.95,
            "recommended_action": "CHRONIC ANCHOR FAILURE PROTOCOL: Disallow temporary tightening; reinforce wall cavity with epoxy putty and install heavy-duty expansion sleeves."
        }
    },
    {
        "id": "TICKET-086103",
        "title": "Corridor Water Cooler Burst & Flooding",
        "tag": "Plumbing · Active Water Hazard",
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
                "Cat6 RJ45 Keystone Jack Punchdown (CC Team)",
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
                "Visible paint peeling and motor housing distress"
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
    }
]

def get_demo_by_id(ticket_id: str) -> Dict[str, Any]:
    for ticket in DEMO_TICKETS:
        if ticket["id"] == ticket_id:
            return ticket
    return DEMO_TICKETS[0]

def get_all_demos() -> List[Dict[str, Any]]:
    return DEMO_TICKETS
