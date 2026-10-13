from typing import Literal
from pydantic import BaseModel, Field, ConfigDict, field_validator

intent=Literal[
    "greeting",
    "goodbye",
    "thanks",
    "affirmation",
    "negation",
    "farewell",
    "suggestion",
    "other",
]

RiskProfile=Literal["low", "medium", "high","unknown"]
priority=Literal["low", "medium", "high"]

class IngestionRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    message: str = Field(
        min_length=1,
        max_length=1000,
        description="The user original message.",
        example=["Where is my order?"]
    )

    @field_validator("message")
    @classmethod
    def validate_message(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Message cannot be empty or whitespace.")
        return value

class TokenMetaData(BaseModel):
    estimate_input_tokens: int = Field(default=0, ge=0)
    note: str = "Estimated number of input tokens for the message."

class IngestionResult(BaseModel):
    model_config = ConfigDict(extra="forbid")

    intent: intent
    risk_profile: RiskProfile
    priority: priority
    required_action: bool
    summary: str = Field(
        min_length=1,max_length=1000)
    token_metadata: TokenMetaData = Field(
        default_factory=TokenMetaData)
    
