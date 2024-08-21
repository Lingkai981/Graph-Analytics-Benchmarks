# LLM-based usability evaluation

1. On line 33 of the config.py file, change it to your Authorization key (registration link: https://api.coze.com).
2. On lines 19 and 21 of the main.py file, modify the platforms ([‘Flash’, ‘Gemini’, ‘Ligra’, ‘Grape’, ‘PowerGraph’, ‘Pregel’, ‘Graphx’]) and algorithms ([‘PageRank’, ‘SSSP’, ‘Louvain’, ‘kCore’, ‘BC’, ‘LPA’, ‘TriangleCounting’, ‘kClique’, ‘CC’]) that you need to test.
3. run: python3 main.py
