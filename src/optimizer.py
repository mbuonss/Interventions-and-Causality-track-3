from src.model_interface import BaseModel

class PromptOptimizer:
    def __init__(self, optimizer_model: BaseModel):
        self.model = optimizer_model

    def optimize_prompt(self, current_prompt: str, feedback: str, history_summary: str = "") -> str:
        model_prompt = (
            "You are an expert prompt engineer.\n"
            f"{history_summary}\n"
            f"Current system prompt: '{current_prompt}'\n"
            f"Feedback on errors: '{feedback}'\n"
            "Task is: Write and optimized and revised system prompt that fixes the errors. "
            "Analyze past iterations to avoid repeating failed patterns or wording. "
            "Return ONLY the new system prompt text, without extra explanation."
        )

        new_prompt = self.model.generate(
            system_prompt="You are a prompt optimization assistant.",
            input_txt=model_prompt
        )

        return new_prompt