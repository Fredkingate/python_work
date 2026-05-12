class AnonymousSurvey:
    """Collect anonymous answers to survey questions."""

    def __init__(self,question):
        """Stores a question and prepares to store responses."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Shows the survey question"""
        print(self.question)

    def store_response(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response)
        
    def show_results(self):
        """Show all responses that have been given thus far."""
        print("Survey results:")
        for response in self.responses:
            print(f"= {response}")