class TextClassifier:
    def __init__(self, property, output_type):
        self.property = property
        self.output_type = output_type
    
    def build_prompt(self, e) -> str:
        prompt = "classify the message by {}; given a comment: '{}'; respond with ONLY {} type".format(self.property, e, self.output_type.__name__)
        return prompt


c = TextClassifier("toxicity", float)
print(c.build_prompt("you're a fag"))

