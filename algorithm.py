from random import choices
import matplotlib.pyplot as plt

class ProbsAlgo:

    def __init__(self, data_path: str, probs: list, n: int) -> None:
        self.true_labels = self.read_file(data_path)
        self.probs = probs
        self.n = n

        self.preds = self.make_predictions()
        self.metrics = self.get_final_metrics()

    def read_file(self, data_path:str) -> list:
        with open(data_path, newline='') as csvfile:
            labels = [int(i) for i in csvfile]
        return labels

    def make_predictions(self) -> list:
        predictions = []

        for _ in range(self.n):
            pred = choices([0, 1, 2], weights=self.probs, k=len(self.true_labels))
            predictions.append(pred)
        return predictions

    @staticmethod
    def accuracy(true_labels: list, preds: list) -> float:
        count = 0
        for A, B in zip(true_labels, preds):
            if A == B:
                count += 1
        return count/len(true_labels)

    @staticmethod
    def precision(predictions: list, true_values: list, k: int) -> float:
        count = 0
        count_class_k = 0
        for A in predictions:
            if A == k:
                count_class_k += 1
        for A, B in zip(predictions, true_values):
            if (A == k) and (B == k):
                count += 1
        return count/count_class_k

    @staticmethod
    def recall(predictions: list, true_values: list, k: int) -> float:
        count_class_k = 0
        count = 0
        for tr in true_values:
            if tr == k:
                count_class_k += 1
        for tr, pr in zip(true_values, predictions):
            if (tr == k) and (pr == k):
                count += 1
        return count/count_class_k

    @staticmethod
    def cumulative_average(lst) -> list:
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
                temp.append(self.precision(self.preds[i], self.true_labels, k))
            metrics[p] = self.cumulative_average(temp)
        for k, p in zip(range(3), rec):
            temp = []
            for i in range(self.n):
                temp.append(self.recall(self.preds[i], self.true_labels, k))
            metrics[p] = self.cumulative_average(temp)
        return metrics

    def plot_and_save_result(self, output_path: str) -> None:
        fig, axs = plt.subplots(7)
        fig.suptitle('Metrics')
        x = []
        for i in range(self.n):
            x.append(i)
        met = self.metrics.keys()
        for i, tatle in zip(range(7), met):
            axs[i].set_title(f'{self.metrics[tatle]}')
            axs[i] = plt.plot(x, self.metrics[tatle])
        plt.savefig(output_path)
        pass
