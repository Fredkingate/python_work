from survey import AnonymousSurvey

def test_store_single_response():
    """Test that a signle response is stored properly"""
    question = "What language did you learn to speak?"
    language_survey = AnonymousSurvey(question)
    language_survey.store_response('English')
    assert 'English' in language_survey.responses