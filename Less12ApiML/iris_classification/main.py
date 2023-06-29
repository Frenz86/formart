from fastapi import FastAPI, Request,Form,Depends,HTTPException
from pydantic import BaseModel
from typing import List
from fastapi.templating import Jinja2Templates
from starlette.responses import JSONResponse
import joblib
import uvicorn

app = FastAPI(title="API IRIS", description="with FastAPI by Daniele Grotti", version="1.0")

## Basemodel
class IrisData(BaseModel):
    sepal_length: float =3
    sepal_width: float =3
    petal_length: float =3
    petal_width: float =3

class Prediction(BaseModel):
    target: int
    target_names: List[str]

# JINJA2
templates = Jinja2Templates(directory="templates")

@app.on_event("startup")
def startup_event():
    "modello *.pkl di ML"
    global model # la varibile dovrà essere globale
    #     iris = load_iris()
    #     X, y = iris.data, iris.target
    #     model.fit(X, y)
    model = joblib.load("model_iris.pkl")
    print(" MODEL LOADED!!")
    return model

##########################################################################################################
################################# SERVER JINJA2 + INFERENCE ##############################################

@app.get("/",status_code=200)
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.post("/predict")
async def predict(request: Request,sepal_len: float = Form(...), #<input name ="sepal_len">
                             sepal_wid: float = Form(...), #<input name ="sepal_wid">
                             petal_len: float = Form(...), #<input name ="petal_len">
                             petal_wid: float = Form(...)  #<input name ="petal_wid">
                            ):
    #target_names = load_iris().target_names.tolist()
    target_names = ['setosa', 'versicolor', 'virginica']
    data = IrisData(sepal_length=sepal_len, sepal_width=sepal_wid, petal_length=petal_len, petal_width=petal_wid)
    X = [[data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]]
    y_pred = model.predict(X)
    prediction = Prediction(target=y_pred[0], target_names=target_names)
    return templates.TemplateResponse("home.html", {"request": request,"prediction": prediction})

##########################################################################################################
################################# CHIAMATE DIRETTE GET POST ##############################################

## secca GET per streamlit o chiamate esterne
@app.get("/predict2")
async def predict2get(data:IrisData=Depends()):
    try:
        target_names = ['setosa', 'versicolor', 'virginica']
        X = [[data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]]
        y_pred = model.predict(X)
        res = target_names[y_pred[0]]
        return JSONResponse(res)
    except:
        raise HTTPException(status_code=404, detail="error")


## secca POST per streamlit o chiamate esterne
@app.post("/predict2")
async def predict2post(data:IrisData):
    try:
        target_names = ['setosa', 'versicolor', 'virginica']
        X = [[data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]]
        y_pred = model.predict(X)
        res = target_names[y_pred[0]]
        return JSONResponse(res)
    except:
        raise HTTPException(status_code=404, detail="error")

###############################################################################################

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
