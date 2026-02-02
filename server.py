import asyncio
from protocol.types import JSONRPCResponse

async def call_tool(method, params):
    if method == "execute_db_migration":
        try:
            return await asyncio.wait_for(run_migration(params), timeout=10.0)
        except asyncio.TimeoutError:
            return {
                "error": {
                    "code": -32000, 
                    "message": "Migration exceeded safety timeout. Transaction rolled back."
                }
            }