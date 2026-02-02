from typing import Literal, Any, Optional, Union, List
from pydantic import BaseModel, Field

class JSONRPCRequest(BaseModel):
    jsonrpc: Literal["2.0"] = "2.0"
    id: Union[int, str]
    method: str
    params : Optional[dict] = None

class JSONRPCResponse(BaseModel):
    jsonrpc: Literal["2.0"] = "2.0"
    id: Union[int, str]
    result: Optional[Any] = None
    error: Optional[dict] = None

class DatabaseMigrationArgs(BaseModel):
    target_schema: str = Field(..., description="The DB schema name")
    batch_size: int = Field(..., gt=0, le=1000)
    timeout_seconds: int = Field(default=30)