from fastapi import FastAPI
import uvicorn

app = FastAPI() #title="API-Somma", description="with FastAPI by Daniele Grotti", version="1.0")

######################################################################

@app.get("/")
def home():
    return {" ---->          http://localhost:8000/docs     <----------"}


@app.get("/input1/{string}")
def nonasynch(string):
    return {f"questa è la stringa inseritacome parametro...... {string}"}

"""Asynchronous Code
Asynchronous code just means that the language 💬 has a way to tell the computer / program 🤖 
that at some point in the code, it 🤖 will have to wait for something else to finish somewhere else. 
Let's say that something else is called "slow-file" 📝."
"""

@app.get("/input2/{string}")
async def asynch(string):
    return {f"questa è la stringa inseritacome parametro...... {string}"}


#######################################################################

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
