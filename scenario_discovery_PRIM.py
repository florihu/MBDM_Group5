
if __name__ == '__main__':

    import multiprocessing
    multiprocessing.freeze_support()


    from ema_workbench import (
        Model,
        Policy,
        ema_logging,
        SequentialEvaluator,
        MultiprocessingEvaluator,
        perform_experiments,
        Samplers
    )

    import copy


        # Rest of the code
    #Model
    # model
    from dike_model_function import DikeNetwork  # @UnresolvedImport
    from problem_formulation import get_model_for_problem_formulation, sum_over, sum_over_time

    dike_model, planning_steps = get_model_for_problem_formulation(2)

    uncertainties = copy.deepcopy(dike_model.uncertainties)

    levers = copy.deepcopy(dike_model.levers)


    # Experiment: 20 Random policies
    ema_logging.log_to_stderr(ema_logging.INFO)

    # running the model through EMA workbench

    scenarios = 1000
    policies = 20

    with MultiprocessingEvaluator(dike_model) as evaluator:
        results = evaluator.perform_experiments(scenarios, policies)

    experiments, outcomes = results






