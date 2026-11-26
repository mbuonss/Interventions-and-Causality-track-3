class Evaluator:

    #clening text for lower, upper case and spaces
    @staticmethod
    def clean_text(text: str) -> str:
        return text.strip().lower()


    @staticmethod
    def is_correct(predicted: str, ground_truth: str) -> bool:
        clean_pred = Evaluator.clean_text(predicted)
        clean_gt = Evaluator.clean_text(ground_truth)
        return clean_pred == clean_gt


    # taking llms generated responses and confronting them with the real dataset
    @staticmethod
    def evaluate_dataset(predictions: list, dataset: list)-> dict:
        correct_count = 0
        total_count = len(dataset)
        errors = []

        for pred, sample in zip(predictions, dataset):
            gt = sample["ground_truth"]
            input = sample["input_txt"]

            if Evaluator.is_correct(pred, gt):
                correct_count += 1

            else:
                errors.append({
                    "input_txt": input,
                    "predicted": pred,
                    "ground_truth": gt
                })

        accuracy = correct_count/total_count if total_count > 0 else 0.0

        return {
            "accuracy": accuracy,
            "correct_count": correct_count,
            "total_count": total_count,
            "errors": errors
        }