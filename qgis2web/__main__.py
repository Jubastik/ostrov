import uvicorn
from uvicorn.config import LOGGING_CONFIG


LOGGING_CONFIG["formatters"]["access"]["fmt"] = '%(asctime)s %(levelprefix)s %(client_addr)s - "%(request_line)s" %(status_code)s'
if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        port=5000,
        reload=True,
    )
