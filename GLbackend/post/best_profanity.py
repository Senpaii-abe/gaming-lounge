# contains the predict function
# profcheck
from best_profanity import predict


def has_profanity(text):
    probability = predict([text])
    return probability == 1
