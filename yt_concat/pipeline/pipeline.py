class Pipeline():

    def __init__(self, steps):
        self.steps = steps

    def run(self, inputs):
        data = []
        for step in self.steps:
            data = step.process(inputs, data)
