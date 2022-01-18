from .base_api import BaseListHandler
from flask import current_app


class ModelHandler(BaseListHandler):
    def __init__(self):
        self.pk_param_name = 'id'
        self.collection = 'models'

    # TODO add GET API for /api/swc/{id}
    def get(self, id=id):
        return self.response_error(200, "Welcome to SWC Project!")

    # TODO this is just a sample code for reference to build upon..
    def post(self):
        # current_app.logger.info('Started POST %s.' % self.collection[:-1])
        # status, data = self.get_data()
        # if not status:
        #     current_app.logger.info("Validation failed. No POST Data.")
        #     return self.response_error(500, "No POST Data specified!")
        # current_app.logger.info("Generating TEXT: ")
        # print(data)
        # if data["modelname"] == "gpt2":
        #
        #     input_ids = current_app.modelgpt2tokenizer.encode(data["seed"], return_tensors='pt')
        #     topk=50
        #     min_length = 30
        #     max_length = 300
        #     top_p = 0.95
        #     temperature = 0.7
        #     num_sentences = 1
        #     if data["top_k"]:
        #         topk = data["top_k"]
        #         print(topk)
        #     if data["min_length"]:
        #         min_length = data["min_length"]
        #         print(min_length)
        #     if data["max_length"]:
        #         max_length = data["max_length"]
        #         print(max_length)
        #     if data["top_p"]:
        #         top_p = data["top_p"]
        #         print(top_p)
        #     if data["temperature"]:
        #         temperature = data["temperature"]
        #         print(temperature)
        #     if data["num_sentences"]:
        #         num_sentences = data["num_sentences"]
        #         print(num_sentences)
        #     sample_outputs = current_app.modelgpt2.generate(input_ids,
        #                                                     do_sample=True,
        #                                                     top_k=topk,
        #                                                     min_length=min_length,
        #                                                     max_length=max_length,
        #                                                     top_p=top_p,
        #                                                     temperature=temperature,
        #                                                     num_return_sequences=num_sentences)
        #     retSentence = []
        #     for i, sample_output in enumerate(sample_outputs):
        #         retSentence.append(current_app.modelgpt2tokenizer.decode(sample_output, skip_special_tokens=True))
        #     # status, retSentences = current_app.modelgpt2.generate(data)
        # if retSentence:
        #     response = {'status': 200, 'messages': retSentence}
        #     return self.response_200(response)
        # else:
        #     self.status_message = "Failed"
        #     return self.response_error(status, self.status_message)
        response = {'status': 200, 'messages': "Hello World"}
        return self.response_200(response)
