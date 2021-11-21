def get_cohort_from_request(request):
    """ Returns the cohort from the query params of a request """
    cohort = request.query_params.get('cohort', None)

    if not cohort:
        raise ValueError('Required parameter cohort not provided')

    return cohort
