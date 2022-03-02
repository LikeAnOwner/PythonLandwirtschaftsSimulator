class feld:
    def __init__(self):
        self.status = 'geerntet'
    def lockern(self):
        self.status = 'gelockert'
    def pflanzen(self):
        self.status = 'bepflanzt'
    def gießen(self):
        self.status = 'begossen'
    def ernten(self):
        self.status = 'geerntet'
