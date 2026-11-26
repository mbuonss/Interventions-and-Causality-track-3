from pickletools import optimize

from src.data_loader import DatasetLoader
from src.evaluator import Evaluator
from src.model_interface import MockModel
from src.feedback_generator import FeedbackGenerator
from src.optimizer import PromptOptimizer

def main():
    loader = DatasetLoader("data/train_set.json")
    dataset = loader.load()

    model = MockModel()
    s_prompt = "Classify sentiment of text as 'Positive', 'Negative', or 'Neutral'"

    predictions = []
    for sample in dataset:
        pred = model.generate(s_prompt, sample["input_txt"])
        predictions.append(pred)


    results = Evaluator.evaluate_dataset(predictions, dataset)

    print("[Test Evaluation n.1]")
    print(f"Accuracy: {results['accuracy'] * 100:.1f}%")
    print(f"Correct: {results['correct_count']}/{results['total_count']}")
    print(f"Errors: {len(results['errors'])}")

    feedback = FeedbackGenerator.contrastive_feedback(results["errors"])
    print("\n[Contrastive Feedback]\n"
          f"{feedback}")

    optimizer = PromptOptimizer(model)
    new_prompt = optimizer.optimize_prompt(s_prompt, feedback)
    print("[Optimized System Prompt]")
    print(f"'{new_prompt}'")


if __name__ == "__main__":
    main()