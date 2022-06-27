from natural_selection.blackjack import ActionSpace
from copy import deepcopy
from datetime import datetime
import numpy as np
import cv2


class StrategyHandler:
    SIZE = 40
    SPLIT_IMG = cv2.imread("natural_selection/images/split.png", cv2.IMREAD_COLOR)
    HIT_IMG = cv2.imread("natural_selection/images/hit.png", cv2.IMREAD_COLOR)
    STAND_IMG = cv2.imread("natural_selection/images/stand.png", cv2.IMREAD_COLOR)
    EMPTY_IMG = cv2.imread("natural_selection/images/empty.png", cv2.IMREAD_COLOR)

    def __init__(self, strategy):
        self._strategy = deepcopy(strategy)

        self._threshold = None
        self._states = []
        self._decisions = []
        self._split_strategy()

        self.x_labels = []
        self.y_labels = []
        self._create_labels()
        self._reshape_decisions()

    def _split_strategy(self):
        for state, decision in self._strategy.items():
            if state == 'threshold':
                self._threshold = decision
            else:
                self._states.append(state)
                self._decisions.append(decision)

    def _create_labels(self):
        for label in self._states:
            c1_c2 = "_".join(label.split("_")[:-1])
            c3 = label.split("_")[-1]

            if c1_c2 not in self.y_labels:
                self.y_labels.append(c1_c2)
            if c3 not in self.x_labels:
                self.x_labels.append(c3)

    def _reshape_decisions(self):
        self._decisions = np.array(self._decisions).reshape((len(self.y_labels), len(self.x_labels)))

    def _get_image(self, decision):
        if decision == ActionSpace.SPLIT:
            return self.SPLIT_IMG
        elif decision == ActionSpace.HIT:
            return self.HIT_IMG
        elif decision == ActionSpace.STAND:
            return self.STAND_IMG

    def show_image(self, number_of_generation):
        final_image = None
        for r in range(len(self.y_labels) + 1):
            current_row_image = None
            for c in range(len(self.x_labels) + 1):
                if current_row_image is None:
                    current_image = deepcopy(self.EMPTY_IMG)
                    if (r, c) == (0, 0):
                        cv2.putText(img=current_image, text=f"{self._threshold}",
                                    org=(0, current_image.shape[0] // 2),
                                    fontFace=cv2.FONT_HERSHEY_TRIPLEX,
                                    fontScale=1.1, color=(255, 0, 0), thickness=2)
                    elif c == 0:
                        cv2.putText(img=current_image, text=f"{self.y_labels[r-1]}",
                                    org=(0, current_image.shape[0] // 2),
                                    fontFace=cv2.FONT_HERSHEY_TRIPLEX,
                                    fontScale=0.5, color=(0, 0, 255), thickness=2)
                    current_row_image = current_image
                else:
                    if r == 0:
                        current_image = deepcopy(self.EMPTY_IMG)
                        cv2.putText(img=current_image, text=f"{self.x_labels[c-1]}",
                                    org=(0, current_image.shape[0] // 2),
                                    fontFace=cv2.FONT_HERSHEY_TRIPLEX,
                                    fontScale=1, color=(0, 0, 255), thickness=2)
                    else:
                        current_image = self._get_image(self._decisions[r-1][c-1])

                    current_row_image = cv2.hconcat([current_row_image, current_image])

            if final_image is None:
                final_image = current_row_image
            else:
                final_image = cv2.vconcat([final_image, current_row_image])

        new_dimension = (self.SIZE * (len(self.x_labels) + 1), self.SIZE * (len(self.y_labels) + 1))
        final_image = cv2.resize(final_image, new_dimension)
        NOW = datetime.now()
        cv2.imwrite(f"strategies/{datetime.now().strftime('%Y_%b_%d_%H_%M_%S_%f')}_G{number_of_generation}.png", final_image)
        cv2.imshow(f"Generation #{number_of_generation}", final_image)
        cv2.waitKey()


