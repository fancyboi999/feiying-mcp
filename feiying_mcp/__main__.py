import asyncio
import typer

from server import run_http, run_sse, parse_args, run_stdio

app = typer.Typer(help="Feiying MCP Server")

@app.command()
def sse():
    """Start Feiying MCP Server in SSE mode"""
    print("Feiying MCP Server - SSE mode")
    print("----------------------")
    print("Press Ctrl+C to exit")
    try:
        asyncio.run(run_sse())
    except KeyboardInterrupt:
        print("\nShutting down server...")
    except Exception as e:
        print(f"\nError: {e}")
        import traceback
        traceback.print_exc()
    finally:
        print("Service stopped.")

@app.command()
def stdio():
    """Start Feiying MCP Server in stdio mode"""
    print("Feiying MCP Server - stdio mode")
    print("----------------------")
    print("Press Ctrl+C to exit")
    run_stdio()
    
@app.command()
def http(
    host: str = typer.Option("127.0.0.1", help="服务器主机地址"),
    port: int = typer.Option(8000, help="服务器端口"),
    path: str = typer.Option("/mcp", help="服务器路径"),
    log_level: str = typer.Option("info", help="日志级别，可选: debug, info, warning, error, critical")
):
    """Start Feiying MCP Server in HTTP mode"""
    try:
        print(f"Feiying MCP Server - HTTP mode")
        print(f"----------------------")
        print(f"Server will be available at: http://{host}:{port}{path}")
        print(f"Log level: {log_level}")
        print(f"Press Ctrl+C to exit")
        run_http(host=host, port=port, path=path, log_level=log_level)
    except KeyboardInterrupt:
        print("\nShutting down server...")
    except Exception as e:
        print(f"\nError: {e}")
        import traceback
        traceback.print_exc()
    finally:
        print("Service stopped.")

if __name__ == "__main__":
    app() 