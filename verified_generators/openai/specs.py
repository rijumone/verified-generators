# generated by datamodel-codegen:
#   filename:  specs.yml
#   timestamp: 2024-05-16T09:52:11+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field
from dat_core.pydantic_models import ConnectionSpecification


class ConnectionSpecificationModel(ConnectionSpecification):
    openai_api_key: str = Field(..., description='OpenAI key', title='OpenAI key')
    openai_model: Optional[str] = Field(
        'text-embedding-ada-002', description='OpenAI model', title='OpenAI model'
    )


class OpenAISpecification(BaseModel):
    class Config:
        extra = 'allow'

    connection_specification: ConnectionSpecificationModel = Field(
        ...,
        description='ConnectorDefinition specific blob. Must be a valid JSON string.',
    )
