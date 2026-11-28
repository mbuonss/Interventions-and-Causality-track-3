class MemoryOptimizer:
    def __init__(self):
        self.history = []

    #registers details of every completed iteration
    def add_record(self, iteration: int, prompt: str, accuracy: float, errors_count: int):
        record = {
            "iteration": iteration,
            "prompt": prompt,
            "accuracy": accuracy,
            "errors_count": errors_count
        }
        self.history.append(record)

    #resume of the last iterations fot the prompt
    def get_history_summary(self) -> str:
        if not self.history:
            return "No previous optimizations available."

        summary = "PREVIOUS OPTIMIZATION HISTORY (do NOT repeat past failed prompts or patterns):\n"

        for rec in self.history:
            summary += (
                f"- Iteration #{rec['iteration']}: Accuracy = {rec['accuracy'] * 100:.1f}% "
                f"- Errors = {rec['errors_count']} - Prompt: '{rec['prompt']}'\n"
            )
        return summary