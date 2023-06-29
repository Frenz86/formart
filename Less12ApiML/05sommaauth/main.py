import uvicorn
from fastapi import FastAPI, HTTPException, Depends,status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel

app = FastAPI(title="API-Somma con security", description="with FastAPI by Daniele Grotti", version="1.0")

# Model for input data
class Numbers(BaseModel):
    num1: int =4
    num2: int =5

from fastapi.middleware.cors import CORSMiddleware
# Allow CORS (Cross-Origin Resource Sharing) for javascipt response
"""Is a mechanism that allows restricted resources on a web page to be requested 
from another domain outside the domain from which the first resource was served. """
app.add_middleware(
                    CORSMiddleware,
                    allow_origins=["*"],
                    allow_methods=["*"],
                    allow_headers=["*"],
                    )

## SIMPLE AUTH ##########################################################
USERS = {
        "user1": {"password": "password1","roles": ["root"]},
        "user2": {"password": "password2","roles": []}
        }

# HTTPBasic for handling authentication
security = HTTPBasic()

# Function to authenticate user based on credentials
def authenticate_user(credentials: HTTPBasicCredentials):
    # Mocked authentication logic
    # Replace this with your actual authentication logic
    if credentials:
        for username, password in USERS.items():
            if credentials.username == username and credentials.password == password['password']:
                return {"username": username, "roles": USERS[username]['roles']}
    return None


###########################################################################

@app.get("/", status_code=status.HTTP_200_OK)
def home():
    return {" ---->          http://localhost:8000/docs     <----------"}


# Endpoint for summing two integers
@app.post("/sum")
async def sum_numbers(number: Numbers, credentials: HTTPBasicCredentials = Depends(security)):
    # Authenticate user based on credentials
    user = authenticate_user(credentials)
    if not user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    # Check if user has 'root' role
    if 'root' not in user['roles']:
        raise HTTPException(status_code=403, detail="Forbidden")
    # Perform sum operation
    result = number.num1 + number.num2
    return {"result": result}


######################################################################################à

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)