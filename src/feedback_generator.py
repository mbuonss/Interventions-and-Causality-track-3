class FeedbackGenerator:
    @staticmethod
    def contrastive_feedback(errors: list)-> str:
        #se la lista degli errori è vuota
        if not errors:
            return "No errors, good performance of the prompt."

        feedback_txt = "The current prompt generated the following errors: \n"

        #enumerate gives me index + element of the list "errors"
        for i, err in enumerate(errors, start = 1):
            feedback_txt += f"Error #{i}:\n"
            feedback_txt += f" - Input: {err['input_txt']}\n"
            feedback_txt += f" - Predicted: {err['predicted']}\n"
            feedback_txt += f" - Ground Truth: {err['ground_truth']}\n\n"

        return feedback_txt