from random import choices
import matplotlib.pyplot as plt
class ProbsAlgo:
    def __init__(self, data_path: str, probs, n: int) -> None:
        self.true_labels = self.read_file(data_path)
        self.probs = probs
        self.n = n

        self.preds = self.make_predictions()
        self.metrics = self.get_final_metrics()

    def read_file(self, data_path):
        with open(data_path, newline='') as csvfile:
            labels = [int(i) for i in csvfile]
        return labels

    def make_predictions(self):
        predictions = []

        for _ in range(self.n):
            pred = choices([0, 1, 2], weights=self.probs, k=len(self.true_labels))
            predictions.append(pred)
        return predictions

    @staticmethod

    def accuracy(true_labels, preds) ->float:
        count = 0
        for A, B in zip(true_labels, preds):
            if A == B:
                count += 1
        return count/len(true_labels)

    @staticmethod

    def precision(self, m, k) -> float:
        pred = self.preds[m]
        count = 0
        count_class_k = 0
        for A in pred:
            if A == k:
                count_class_k += 1
        for A, B in zip(self.preds, self.true_labels):
            if (A == k) and (B == k):
                count += 1
        return count/count_class_k

    @staticmethod

    def recall(self, m, k) -> float:
        pred = self.preds[m]
        count_class_k = 0
        count = 0
        for i in range(len(self.true_labels)):
            if self.true_labels[i] == k:
                count_class_k += 1
        for i in range(len(self.preds)):
            if (pred[i] == k) and (self.true_labels[i] == k):
                count += 1
        return count/count_class_k

    @staticmethod
    def cumulative_average(lst) -> list[float]:
        cum_avg = [lst[0]]
        for i in range(1, len(lst)):
            cum_avg.append((cum_avg[i - 1] * i + lst[i]) / (i + 1))
        return cum_avg
    def get_final_metrics(self):
        metrics = dict.fromkeys(['accuracy',
                                 'precision_0', 'precision_1', 'precision_2',
                                 'recall_0', 'recall_1', 'recall_2'])
        pres = ['precision_0', 'precision_1', 'precision_2']
        rec = ['recall_0', 'recall_1', 'recall_2']
        temp = []
        for pr in self.preds:
            temp.append(self.accuracy(self.true_labels, pr))
        metrics['accuracy'] = self.cumulative_average(temp)
        for k, p in zip(range(3), pres):
            temp = []
            for i in range(self.n):
                temp.append(self.precision(i, k))
            metrics[p] = self.cumulative_average(temp)
        for k, p in zip(range(3), rec):
            temp = []
            for i in range(self.n):
                temp.append(self.recall(i, k))
            metrics[p] = self.cumulative_average(temp)

    def plot_and_save_result(self, output_path: str) -> None:
        fig, axs = plt.subplots(7)
        fig.suptitle('Metrics')
        x = []
        for i in range(self.n):
            x.append(i)
        met = self.metrics.keys()
        for i in range(7):
            axs[i].set_title(f'{self.metrics[met[i]]}')
            axs[i] = plt.plot(x, self.metrics[met[i]])
        plt.savefig(output_path)
        pass
