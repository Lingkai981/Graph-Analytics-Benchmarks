
class Config:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_bot_id(self):
        return {
            'Flash': '7368468233818521605',
            'Gemini': '7374034815957368849',
            'CodeEvaluator': '7365418502205325318',
            'Ligra': '7384457424637296648',
            'Grape': '7384752282170523654',
            'PowerGraph': '7388857314184839186',
            'Pregel': '7389832072153939976',
            'Graphx': '7389855404106530834'
        }


    def get_algorithm_name(self):
        return {
            'PageRank': 'PageRank',
            'SSSP': 'Single-Source Shortest Path',
            'Louvain': 'Louvain',
            'kCore': 'k-Core',
            'BC': 'Betweenness Centrality',
            'TriangleCounting': 'Triangle Counting',
            'kClique': 'k Clique',
            'LPA': 'Label Propagation',
            'CC': 'Connected Component'
        }

    def get_Authorization(self):
        return 'your Authorization key'

    def get_url(self):
        return 'https://api.coze.com/open_api/v2/chat'

    def tip_level(self, platform, algorithm, level):
        with open(self.file_path + '/tips/' + platform + '/' + algorithm + '/' + level, 'r') as file:
            file_contents = file.read()
            return str(file_contents)

    def get_algoritm(self, platform, algorithm):
        return 'Refer to the above tips to help me generate the ' + self.get_algorithm_name()[algorithm] + ' algorithm completed code.'
    def get_standard_code(self, platform, algorithm):
        with open(self.file_path + '/code/' + platform + '/' + algorithm, 'r') as file:
            file_contents = file.read()
            return str(file_contents)

    def get_code_evaluator_str(self, platform, algorithm, codes):
        str_ = 'This is the standard reference code:\n' + self.get_standard_code(platform, algorithm) + '\n' + 'Next, a few codes to be evaluated.\n'
        code_i = 1
        for code in codes:
            str_+= 'The code ' + str(code_i) + ':\n' + code + '\n'
            code_i+=1

        return str_


    def getCode(self, s):
        start_index = s.find("```")
        if start_index != -1:
            
            end_index = s.find("```", start_index + 3)  
            if end_index != -1:
                
                code = s[start_index + 6:end_index]
                return code
            else:
                print("error \"```\"")
                return -1
        else:
            print("error \"```\"")
            return -1
