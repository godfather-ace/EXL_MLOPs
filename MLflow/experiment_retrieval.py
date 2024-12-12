import mlflow


if __name__ == "__main__":
    experiment = mlflow.get_experiment(experiment_id = "981105499811704220")
    
    print("Name : {}".format(experiment.name))
    print("Experiment_id: {}".format(experiment.experiment_id))
    print("Artifact Location: {}".format(experiment.artifact_location))
    print("Tags: {}".format(experiment.tags))
    print("Lifecycle_stage: {}".format(experiment.lifecycle_stage))
    print("Creation Timestamp: {}".format(experiment.creation_time))