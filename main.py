from src.data_loader import DatasetLoader
from src.evaluator import Evaluator
from src.model_interface import MockModel
from src.feedback_generator import FeedbackGenerator
from src.optimizer import PromptOptimizer

def main():
    loader = DatasetLoader("data/train_set.json")
    dataset = loader.load()

    model = MockModel()
    optimizer = PromptOptimizer(model)

    current_prompt = "Classify sentiment of text as 'Positive', 'Negative', or 'Neutral'"

    max_iterations = 3
    iteration = 1
    target_accuracy = 1.0

    print("-- Automatic prompt optimization STARTING LOOP --")

    while iteration <= max_iterations:
        print(f"Iteration number {iteration}")
        print(f"Current Prompt: '{current_prompt}'")

        results = run_eval(current_prompt, model, dataset)
        acc = results['accuracy']
        # print("[Test Evaluation n.1]")

        print(f"Accuracy: {results['accuracy'] * 100:.1f}%")

        if acc >= target_accuracy:
            print("\nAccuracy reached, optimization stopped.")
            break

        print(f"Errors: {len(results['errors'])}")

        # print(f"Correct: {results['correct_count']}/{results['total_count']}")
        feedback = FeedbackGenerator.contrastive_feedback(results["errors"])

        # print("\n[Contrastive Feedback]\n"
        #       f"{feedback}")
        current_prompt = optimizer.optimize_prompt(current_prompt, feedback)
        print(f"Updated system prompt for new iteration: '{current_prompt}'\n")

        iteration += 1

        # print("[Optimized System Prompt]")
        # print(f"'{new_prompt}'")

        #evaluation of second optimized prompt
        # results_2 = run_eval(new_prompt, model, dataset)
        # print("[Test Evaluation n.2 - Post Optimization]")
        # print(f"Accuracy: {results_2['accuracy'] * 100:.1f}%")
        # print(f"Correct: {results_2['correct_count']}/{results_2['total_count']}")
        # print(f"Errors: {len(results_2['errors'])}")

    print("-- Automatic prompt optimization ENDING LOOP --")
    print(f"Final Prompt: '{current_prompt}'")


def run_eval(s_prompt: str, model: MockModel, dataset: list) -> dict:
    predictions = []
    for sample in dataset:
        pred = model.generate(s_prompt, sample["input_txt"])
        predictions.append(pred)

    return Evaluator.evaluate_dataset(predictions, dataset)


if __name__ == "__main__":
    main()