class Pipeline():

    def __init__(self, steps):  # 由於steps為pipeline底下的一環，"一定會導入steps"
        self.steps = steps

    def run(self, inputs):
        for step in self.steps:
            step.process(inputs)
