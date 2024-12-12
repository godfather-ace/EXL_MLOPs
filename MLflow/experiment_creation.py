
import mlflow 

if __name__ == "__main__":
    # creating a new mlflow experiment
    experiment_id = mlflow.create_experiment(
        name = "expt_test_mlflow1", 
        artifact_location = "expt_mlflow1_artifacts", 
        tags = {"env": "dev", "version": "1.0.0"}, 
    )
    print(experiment_id)