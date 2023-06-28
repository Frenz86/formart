from fastapi import FastAPI,Depends,HTTPException,status
from pydantic import BaseModel
import joblib
import uvicorn

app = FastAPI(title="API Company", description="with FastAPI by Daniele Grotti", version="1.0")

## Basemodel
class CompanyData(BaseModel):
    tv: float =147
    radio: float =23
    newspaper: float =30

## blocco per la cache del mio modello
@app.on_event("startup")
def startup_event():
    "modello *.pkl di ML"
    global model # la varibile dovrà essere globale
    model = joblib.load("company.pkl")
    print(" MODEL LOADED!!")
    return model

##########################################################################################################
################################# CHIAMATE DIRETTE GET POST ##############################################

@app.get("/")
def home():
    return {" ---->          http://localhost:8000/docs     <----------"}

## secca GET per streamlit o chiamate esterne
@app.get("/predict")
async def predictget(data:CompanyData=Depends()):
    try:
        X = [[data.tv, data.radio, data.newspaper]]
        y_pred = model.predict(X)[0]
        res = round(y_pred,2)
        return {'prediction':res}
    except:
        raise HTTPException(status_code=404, detail="error")

## secca POST per streamlit o chiamate esterne
@app.post("/predict")
async def predictpost(data:CompanyData):
    try:
        X = [[data.tv, data.radio, data.newspaper]]
        y_pred = model.predict(X)[0]
        res = round(y_pred,2)
        return {'prediction':res}
    except:
        raise HTTPException(status_code=404, detail="error")

###############################################################################################

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
