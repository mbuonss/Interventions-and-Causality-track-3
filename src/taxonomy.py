class ErrorTaxonomy

    #initial test to categories
    @staticmethod
    def categorize_error(error: dict) -> str:

    #groups the list of errors in categories and returns a structured report
    @classmethod
    def taxonomic_report(cls, errors: list) -> str:
        if not errors:
            return "No errors to categorize."

        categorized = []

        for err in errors:
            cat = cls.categorize_error(err)
            if cat not in categorized:
                categorized[cat] = []