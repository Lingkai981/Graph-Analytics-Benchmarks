### Ligra

#### Platform Source Code

[Ligra](https://github.com/jshun/ligra)

#### Algorithms

1. add the `.C` file to ligra/apps (some are already existed)
2. update the file name in ligra/apps/Makefile
```shell
ALL= <file name>
```
3. update the number of threads in the algorithm file
```shell
setWorkers(Number_of_Threads);
```
4. compile and run by the platform guidance

PageRank: [[Code]](Performance%20Evaluation/Ligra/PageRank.C) [[Command]](Performance%20Evaluation/Ligra/PageRank.sh)

SSSP: [[Code]](Performance%20Evaluation/Ligra/SSSP.C) [[Command]](Performance%20Evaluation/Ligra/SSSP.sh)

Triangle Counting: [[Code]](Performance%20Evaluation/Ligra/TriangleCounting.C) [[Command]](Performance%20Evaluation/Ligra/TriangleCounting.sh)

Connected Component: [[Code]](Performance%20Evaluation/Ligra/ConnectedComponent.C) [[Command]](Performance%20Evaluation/Ligra/ConnectedComponent.sh)

Betweenness: [[Code]](Performance%20Evaluation/Ligra/Betweenness.C) [[Command]](Performance%20Evaluation/Ligra/Betweenness.sh)

LPA: [[Code]](Performance%20Evaluation/Ligra/LPA.C) [[Command]](Performance%20Evaluation/Ligra/LPA.sh)

K-Core: [[Code]](Performance%20Evaluation/Ligra/K-Core.C)
[[Command]](Performance%20Evaluation/Ligra/K-Core.sh)

K-Clique: [[Code]](Performance%20Evaluation/Ligra/K-Clique.C) [[Command]](Performance%20Evaluation/Ligra/K-Clique.sh)
