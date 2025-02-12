import requests
import json
import config
import time

my_config = config.Config('subjectiveEvaluation')

url = my_config.get_url()

headers = {
    'Authorization': my_config.get_Authorization(),
    'Content-Type': 'application/json',
    'Accept': '*/*',
    'Host': 'api.coze.com',
    'Connection': 'keep-alive'
}

platforms = ['Flash', 'Gemini', 'Ligra', 'Grape', 'PowerGraph', 'Pregel', 'Graphx', 'Gthinker']
# platforms = ['Gthinker']

# algorithms = ['kClique']
algorithms = ['PageRank', 'SSSP', 'kCore', 'BC', 'LPA', 'TriangleCounting', 'kClique', 'CC']

levels = ['1', '2', '3', '4']

def Evaluation(platform, algorithm):

        codes = []
        for level in levels:
            data = {
                "conversation_id": my_config.get_conversation_id(),
                "bot_id": my_config.get_bot_id()[platform],
                "user": my_config.get_conversation_id(),
                "query": my_config.tip_level(platform, algorithm, level) + '\n' + my_config.get_algoritm(platform, algorithm),
                "stream": False
            }
            code = ''
            judge = 1
            while judge:
                response = requests.post(url, headers=headers, json=data)
                print(response.text)
                res = json.loads(response.text)['messages']
                for res_ in res:
                    if res_['type'] == 'answer':
                        code = my_config.getCode(res_['content'])
                        # print(code)
                        if code != -1:
                            judge = 0
                        break

            codes.append(code)

        CodeEvaluator_i = 0
        while CodeEvaluator_i < 1:
            CodeEvaluatorData = {
                "conversation_id": "your conversation id",
                "bot_id": my_config.get_bot_id()['CodeEvaluator'],
                "user": "your conversation id",
                "query": my_config.get_code_evaluator_str(platform, algorithm, codes),
                "stream": False
            }

            print(my_config.get_code_evaluator_str(platform, algorithm, codes))
            # exit(1)

            response = requests.post(url, headers=headers, json=CodeEvaluatorData)
            data = json.loads(response.text)['messages']

            for data_ in data:
                if data_['type'] == 'answer':
                    print(data_['content'])
            CodeEvaluator_i+=1


def main():
    
    platform = input("Enter platform (Pregel, Grape, GraphX, GThinker, Flash, PowerGraph, Ligra): ")
    algorithm = input("Enter algorithm (PageRank, SSSP, kCore, BC, LPA, TriangleCounting, kClique, CC): ")
    
    if platform not in platforms or algorithm not in algorithms:
        print("Please choose the correct platform and algorithm.")
        ruturn

    Evaluation(platform, algorithm)
    





