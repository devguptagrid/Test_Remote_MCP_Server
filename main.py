from fastmcp import FastMCP
import random
import json

mcp=FastMCP('Remote server')

@mcp.tool
def add(a:int,b:int)->int:
    """Add two numbers"""
    return a+b

@mcp.tool
def random_number(min_value:int=1,max_value:int=100)->int:
    """Generate a random number"""
    return random.randint(min_value,max_value)

@mcp.resource("info://server")
def srver_info()->str:
    """Get info about server"""
    info={
        "name":"Simple remote server",
        "verison":"1.0.0",
        "description":"A basic MCP server with math tools",
        "tools":['add','random_number'],
        "author":"Your Name"
    }
    return json.dumps(info,indent=2)
    
if __name__=="__main__":
    mcp.run(transport="http",host="0.0.0.0",port=8000)
    
