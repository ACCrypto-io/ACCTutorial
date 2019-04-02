import logging
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


logger = logging.getLogger(__name__)


class RF:

    @staticmethod
    def __get_model():
        return RandomForestClassifier(n_estimators=10, n_jobs=-1, random_state=1)

    def create_model(self, np_features, np_target, test_size=0.33):
        # x_train, x_test, y_train, y_test = train_test_split(np_features, np_target, test_size=test_size, random_state=1)

        index_split_train = int(np_features.shape[0] * (1 - test_size))
        x_train, x_test, y_train, y_test = np_features[:index_split_train, :], np_features[index_split_train:, :], \
                                           np_target[:index_split_train], np_target[index_split_train:]

        clf = self.__get_model()
        clf.fit(x_train, y_train)

        score = clf.score(x_test, y_test)

        logger.info("RF score {}".format(score))
