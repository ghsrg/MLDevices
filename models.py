class BaseModel:
    def train(self, data):
        raise NotImplementedError

    def get_weights(self):
        raise NotImplementedError

    def set_weights(self, weights):
        raise NotImplementedError

class DeviceModel(BaseModel):
    def __init__(self, device_id):
        self.device_id = device_id
        self.weights = None

    def train(self, data):
        # Навчання моделі на портативному пристрої
        pass

    def get_weights(self):
        return self.weights

    def set_weights(self, weights):
        self.weights = weights

class DeviceModelFactory:
    def __init__(self):
        self.device_models = {}

    def get_device_model(self, device_id):
        if device_id not in self.device_models:
            self.device_models[device_id] = DeviceModel(device_id)
        return self.device_models[device_id]