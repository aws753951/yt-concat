class Pipeline():

    def __init__(self, steps):
        self.steps = steps

    def run(self, inputs, utils):
        data = None
        for step in self.steps:
            data = step.process(inputs, data, utils)
