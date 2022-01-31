import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
class ProbsAlgo:
    def __init__(self, data_path: str, probs, n: int) -> None:
        self.true_labels = self.read_file_please(data_path)
        self.probs = probs
        self.n = n

        self.preds = self.make_predictions()
        self.metrics = self.get_final_metrics()

    def read_file_please(self, data_path):
        true = []
        data = pd.read_csv(data_path)
        true = list(data.values())
        return true

    def make_predictions(self):
        predictions = []
        pred = []
        pr = self.probs
        for k in range(self.n):
            for i in range(len(self.true_labels)):
                a = np.random.uniform(0, 1, 1)
                for j in range(len(pr)-1):
                    if (a > pr[-1]):
                        a = len(pr)
                        break
                    if (a > pr[j]) and (a < pr[j+1]):
                        a = j
                        break
                pred.append(a)
            predictions.append(pred)
        assert len(predictions) == self.n
        for pred in predictions:
            assert len(pred) == len(self.true_labels)
        return predictions




def accuracy(self) -> float:
    true = self.true_labels
    pred = self.preds
    count=0
    for i in range(len(self.true_labels)):
        if(true[i]==pred[i]):
            count+=1
    return count/len(self.true_labels)




def precision(self,m, k) -> float:
    pred = self.preds[m]
    count = 0
    count_class_k=0
    for i in range(len(pred)):
        if(pred[i]==k):
            count_class_k+=1
    for i in range(len(self.preds)):
        if (pred[i] == k) and (self.true_labels[i] == k):
            count += 1
    return count/count_class_k




def recall(self, m, k) -> float:
    pred = self.preds[m]
    count_class_k = 0
    count = 0
    for i in range(len(self.true_labels)):
        if(self.true_labels[i]==k):
            count_class_k+=1
    for i in range(len(self.preds)):
        if (pred[i] == k) and (self.true_labels[i] == k):
            count += 1
    return count/count_class_k



def get_final_metrics(self):
    metrics = dict.fromkeys(['accuracy',
                             'precision_0', 'precision_1', 'precision_2',
                             'recall_0', 'recall_1', 'recall_2'])
    #assert len(metrics) == 7
    metrics['accuracy'] = []
    for i in range(self.n):
        metrics['accuracy'].append(accuracy(self.preds[i]))
    metrics['precision_0'] = []
    metrics['precision_1'] = []
    metrics['precision_2'] = []
    list_of_met=['precision_0', 'precision_1', 'precision_2']
    for k in range(2):
        for i in range(self.n):
            metrics[list_of_met[k]].append(precision(i, k))
    metrics['recall_0'] = []
    metrics['recall_1'] = []
    metrics['recall_2'] = []
    list_of_met = ['recall_0', 'recall_1', 'recall_2']
    for k in range(2):
        for i in range(self.n):
            metrics[list_of_met[k]].append(recall(i, k))
    for metric in metrics.values():
        assert len(metric) == self.n
    return metrics


def plot_and_save_result(self, output_path: str) -> None:
    fig, axs = plt.subplots(7)
    fig.suptitle('Metrics')
    x=[]
    for i in range(self.n):
        x.append(i)
    met = self.metrics.keys()
    for i in range(7):
        axs[i].set_title(f'{self.metrics[met[i]]}')
        axs[i] = plt.plot(x, self.metrics[met[i]])
    plt.savefig(output_path)
    pass
