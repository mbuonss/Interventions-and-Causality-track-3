class Evaluator:
    @staticmethod
    def clean_text(text: str) -> str:
        return text.strip().lower()

    @staticmethod
    def is_correct(predicted: str, ground_truth: str) -> bool:
        clean_pred = Evaluator.clean_text(predicted)
        clean_gt = Evaluator.clean_text(ground_truth)
        return clean_pred == clean_gt