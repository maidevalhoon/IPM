from typing import List, Optional
from pydantic import BaseModel, Field

class IPMTicketAnalysis(BaseModel):
    """
    Structured Output Schema for the AI-Augmented Triage Layer
    Infrastructure Planning and Management (IPM), IIT Guwahati.
    """
    ipm_validity: bool = Field(
        ...,
        description="False if the issue is IT/Network related (e.g., LAN internet issues, Wi-Fi, ERP portal), True if it is an actual physical infrastructure issue for IPM."
    )
    corrected_department: str = Field(
        ...,
        description="Reclassified department from: 'Electricity', 'Plumbing', 'Carpentry', 'Sanitary', 'Other Civil Works'. If invalid, reclassify as 'Invalid (IT/Network) - Computer Center'."
    )
    technical_summary_english: str = Field(
        ...,
        description="Concise professional translation and technical breakdown of the raw colloquial or multilingual complaint text."
    )
    technician_instructions_assamese: str = Field(
        ...,
        description="Direct Assamese translation (অসমীয়া) of the physical task, required components, and specific room/location directive for frontline campus technicians."
    )
    predicted_tools_parts: List[str] = Field(
        ...,
        description="Specific hardware, parts, and tools required for single-visit resolution (e.g., '2.5uF fan condenser', '5mm screws', 'geyser tap', 'teflon tape')."
    )
    interdependency_flag: Optional[str] = Field(
        None,
        description="Trade interdependency directive if multi-trade work is needed (e.g., 'Civil works required before Carpentry' if wall masonry is crumbling), or None if single trade."
    )
    severity_score: int = Field(
        ...,
        ge=1,
        le=5,
        description="Urgency/hazard level from 1 (minor/cosmetic) to 5 (active flooding leaks, electric short-circuit risk, severe physical hazard)."
    )
    chronic_issue_flag: bool = Field(
        ...,
        description="True if the text indicates repeated failures or historical unresponsiveness (e.g., '4th time', 'complained 3 times', 'comes again and again'), triggering complete asset replacement."
    )
    visual_evidence_detected: Optional[List[str]] = Field(
        default_factory=list,
        description="Physical indicators detected from image evidence (e.g., 'water pooling on floor', 'wobbling downrod', 'missing latch screws', 'exposed brickwork')."
    )
    confidence_score: Optional[float] = Field(
        0.95,
        description="Model confidence score for the classification and tool prediction (0.0 to 1.0)."
    )
    recommended_action: Optional[str] = Field(
        None,
        description="Dispatcher recommendation (e.g., 'Immediate Dispatch', 'Scheduled Repair', 'Route to IT Desk', 'Trigger Asset Replacement')."
    )
