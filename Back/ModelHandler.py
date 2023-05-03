from Model.test_binary_model import load_model, test_model
import threading
import asyncio
import keras
class ModelHandler:
    
    def __init__(self):
        self.path = "Model/Models/iau_phrase 99/model.h5"
        self.audioPath = "Audio/105-iau.wav"
        self.isModelLoaded = asyncio.Event()
        self.model = None
        
    async def loadModel(self):
        print("Start loading model ")
        print(f"Model Path : {self.path}")
        
        # load model in a separate thread
        t = threading.Thread(target=self._loadModelThread)
        t.start()
        
        # wait for model to be loaded
        await self.isModelLoaded.wait()

    def _loadModelThread(self):
        self.model = keras.models.load_model(self.path)
        self.isModelLoaded.set()
        
    async def modelPredict(self, sessionID):     
        
        await self.isModelLoaded.wait()
        result = None
        if self.model is not None:
            print(f"Start prediction session ID : {sessionID}")
            print(self.model)
            result = test_model(self.model, self.audioPath)
            print(f"Result is: {result}")
        return result
