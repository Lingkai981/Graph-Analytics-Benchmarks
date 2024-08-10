import requests
import json
import config
import time

my_config = config.Config('/Users/milk/PycharmProjects/subjectiveEvaluation')

url = my_config.get_url()

headers = {
    'Authorization': my_config.get_Authorization(),
    'Content-Type': 'application/json',
    'Accept': '*/*',
    'Host': 'api.coze.com',
    'Connection': 'keep-alive'
}

# platforms = ['Flash', 'Gemini', 'Ligra', 'Grape', 'PowerGraph', 'Pregel', 'Graphx']
platforms = ['Pregel']

algorithms = ['CC']
# algorithms = ['PageRank', 'SSSP', 'Louvain', 'kCore', 'BC', 'LPA', 'TriangleCounting', 'kClique', 'CC']

levels = ['1', '2', '3', '4']

for platform in platforms:

    for algorithm in algorithms:
        codes = []
        for level in levels:
            data = {
                "conversation_id": "milk123",
                "bot_id": my_config.get_bot_id()[platform],
                "user": "milk123",
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

            # print(json.loads(response.text))
            #
            # print(code)
            print(platform+' '+algorithm+' '+level)

            codes.append(code)

        CodeEvaluator_i = 0
        while CodeEvaluator_i < 1:
            CodeEvaluatorData = {
                "conversation_id": "milk123",
                "bot_id": my_config.get_bot_id()['CodeEvaluator'],
                "user": "milk123",
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



        # Pretty-print JSON data
        # pretty_json = json.dumps(data, indent=4)
        # print(pretty_json)









