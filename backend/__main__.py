import uvicorn
from uvicorn.config import LOGGING_CONFIG


LOGGING_CONFIG["formatters"]["access"]["fmt"] = '%(asctime)s %(levelprefix)s %(client_addr)s - "%(request_line)s" %(status_code)s'
if __name__ == "__main__":
    uvicorn.run(
        "backend.wsgi:application",
        host="0.0.0.0",
        port=5000,
        reload=True,
    )
