import random
import time
from statistics import mean
import logging


class DynamicAI:
    def __init__(self, list_length_range=(500, 5000), length_step=500, num_episodes=100):
        self.list_length_range = list_length_range
        self.length_step = length_step
        self.num_episodes = num_episodes
        self.best_params = {}
        self.logger = logging.getLogger(__name__)

    @staticmethod
    def random_list(lower_bound=0, upper_bound=100):
        ordered_list = list(range(lower_bound, upper_bound + 1))
        random.shuffle(ordered_list)
        return ordered_list

    def comb_sort(self, s_list_length, power, shrink_factor):
        if not (0.1 <= power <= 1.2 and
                1.0 <= shrink_factor <= 1.6 and
                20 <= s_list_length <= 5000):
            raise ValueError("Input values are outside the specified bounds.")

        temp_list = list(range(list_length + 1))

        times_list = []
        for _ in range(250):
            unsorted_list = self.random_list(0, s_list_length)
            pointer_two = int(len(unsorted_list) // pow(shrink_factor, power))
            start_time = time.time()
            swapped = True

            while swapped:
                swapped = False
                pointer_one = 0
                pointer_two = max(1, int(pointer_two // pow(shrink_factor, power)))

                for i in range(pointer_two, len(unsorted_list)):
                    if unsorted_list[pointer_one] > unsorted_list[i]:
                        unsorted_list[pointer_one], unsorted_list[i] = (
                            unsorted_list[i], unsorted_list[pointer_one])
                        swapped = True
                    pointer_one += 1

            times_list.append(time.time() - start_time)

            if _ == 1 and unsorted_list != temp_list:
                self.logger.error(
                    f"Test failed for list_length={s_list_length}, power={power}, shrink_factor={shrink_factor}")
                self.logger.error(f"Expected: {temp_list}")
                self.logger.error(f"Actual: {unsorted_list}")
                raise Exception

        return mean(times_list)

    def evaluate_params(self, e_list_length, power, shrink_factor):
        try:
            avg_time = self.comb_sort(e_list_length, power, shrink_factor)
            return avg_time
        except Exception as e:
            self.logger.error(f"An error occurred: {e}")
            return float('inf')

    def train(self):
        for _ in range(self.num_episodes):
            current_list_length = random.randint(self.list_length_range[0], self.list_length_range[1])
            power = random.uniform(0.1, 1.2)
            shrink_factor = random.uniform(1.0, 1.5)

            current_params = self.best_params.get(current_list_length, (0.6, 1.3))

            current_performance = self.evaluate_params(current_list_length, *current_params)
            random_performance = self.evaluate_params(current_list_length, power, shrink_factor)

            if random_performance < current_performance:
                self.best_params[current_list_length] = (power, shrink_factor)

    def get_best_params(self):
        return self.best_params


# Example usage:
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    dynamic_ai = DynamicAI()
    dynamic_ai.train()
    best_params_by_length = dynamic_ai.get_best_params()

    print("Best Parameters for Different List Lengths:")
    for list_length, params in best_params_by_length.items():
        print(f"List Length: {list_length}, Best Parameters: {params}")
