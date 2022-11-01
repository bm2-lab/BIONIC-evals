import typer
from pathlib import Path
from typing import Optional, List
from resolvers import resolve_config_path, resolve_tasks
from process_config import process_config
from file_utils import import_datasets
from coannotation import coannotation_eval
from module_detection import module_detection_eval
from function_prediction import function_prediction_eval


app = typer.Typer()


@app.command("bioniceval")
def evaluate(
    config_path: Path,
    baseline_path: Optional[Path] = Path(""),
    exclude_tasks: Optional[List[str]] = [],
    exclude_standards: Optional[List[str]] = [],
):
    resolve_config_path(config_path)
    process_config(exclude_tasks, exclude_standards, baseline_path)
    import_datasets()
    tasks = resolve_tasks()
    for task in tasks:
        print(task)
        evaluate_task(task)


def evaluate_task(task: str):
    if task == "coannotation":
        coannotation_eval()
    elif task == "module_detection":
        module_detection_eval()
    elif task == "function_prediction":
        function_prediction_eval()
    else:
        raise NotImplementedError(f"Task '{task}' has not been implemented.")


def main():
    app()
